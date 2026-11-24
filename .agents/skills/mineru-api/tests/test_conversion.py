"""离线检查路由、图片打包与 Unicode 路径；测试不调用官网。"""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import ssl
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import quote
import zipfile

from pypdf import PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import convert
import mineru_to_md as client


def make_pdf(path: Path, pages: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=100, height=100)
    with path.open("wb") as stream:
        writer.write(stream)


class ConversionTests(unittest.TestCase):
    def test_long_dry_run_has_no_output_or_submission(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "raw/book.pdf"
            make_pdf(source, 201)
            stdout = io.StringIO()
            with patch.object(sys, "argv", ["convert.py", str(source), "--project-root", str(root), "--dry-run"]), \
                    patch.object(subprocess, "run", side_effect=AssertionError("dry-run 不得提交")), \
                    redirect_stdout(stdout):
                self.assertEqual(convert.main(), 0)
            self.assertIn("分为 2 段", stdout.getvalue())
            self.assertFalse((root / "mds").exists())

    def test_long_route_preserves_language_and_ocr(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "raw/book.pdf"
            make_pdf(source, 201)
            with patch.object(sys, "argv", ["convert.py", str(source), "--project-root", str(root),
                                            "--language", "ch", "--ocr"]), \
                    patch.object(subprocess, "run", return_value=subprocess.CompletedProcess([], 7)) as run, \
                    redirect_stdout(io.StringIO()):
                self.assertEqual(convert.main(), 7)
            command = run.call_args.args[0]
            self.assertEqual(Path(command[2]).name, "mineru_full_pdf.py")
            self.assertEqual(command[command.index("--language") + 1], "ch")
            self.assertIn("--ocr", command)

    def make_delivery(self, root: Path):
        source = root / "source.pdf"
        make_pdf(source, 1)
        markdown = root / "含空格 文档—示例.md"
        assets = markdown.with_suffix("")
        (assets / "images").mkdir(parents=True)
        (assets / "images/example.png").write_bytes(b"test-image")
        (assets / "layout.json").write_text(json.dumps({"pdf_info": [{}], "_backend": "hybrid"}))
        ref = quote(assets.name) + "/images/example.png"
        markdown.write_text(f"![]({ref})\n", encoding="utf-8")
        client.write_package(client.OutputPaths(markdown, assets, markdown.with_suffix(".zip")))
        return source, markdown

    def test_unicode_delivery_and_zip_are_validated(self):
        with tempfile.TemporaryDirectory() as directory:
            source, markdown = self.make_delivery(Path(directory))
            result = convert.validate_output(markdown, 1, source)
            self.assertEqual(result["image_references"], 1)
            self.assertEqual(result["returned_pages"], 1)
            self.assertTrue(result["zip_valid"])

    def test_missing_local_image_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            source, markdown = self.make_delivery(Path(directory))
            (markdown.with_suffix("") / "images/example.png").unlink()
            with self.assertRaisesRegex(client.MinerUError, "图片"):
                convert.validate_output(markdown, 1, source)

    def test_missing_packaged_image_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            source, markdown = self.make_delivery(Path(directory))
            with zipfile.ZipFile(markdown.with_suffix(".zip"), "w") as package:
                package.write(markdown, markdown.name)
            with self.assertRaisesRegex(client.MinerUError, "ZIP"):
                convert.validate_output(markdown, 1, source)

    def test_tls_verification_remains_required(self):
        self.assertEqual(client.make_ssl_context().verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(client.make_ssl_context().check_hostname)


if __name__ == "__main__":
    unittest.main()
