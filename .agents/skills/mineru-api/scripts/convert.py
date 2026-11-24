#!/usr/bin/env python3
"""统一入口：短 PDF 直接提交，超过 200 页自动分段，输出后校验全文与图片。"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import zipfile

import mineru_to_md as client


def validate_output(markdown: Path, expected_pages: int, source: Path) -> dict:
    """验证交付完整性；不把页数、图片与 ZIP 检查当成公式准确率。"""
    assets = markdown.with_suffix("")
    archive = markdown.with_suffix(".zip")
    text = markdown.read_text(encoding="utf-8")
    layouts = sorted(assets.rglob("layout.json"))
    actual_pages = 0
    backends = []
    for path in layouts:
        data = json.loads(path.read_text(encoding="utf-8"))
        actual_pages += len(data.get("pdf_info", []))
        backends.append({key: data.get(key) for key in
                         ("_backend", "_effort", "_ocr_enable", "_version_name")})
    if actual_pages != expected_pages:
        raise client.MinerUError(f"结果页数 {actual_pages} 与源文件 {expected_pages} 不一致。")
    refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
    missing = []
    for ref in refs:
        target = urlsplit(ref.strip("<>"))
        if target.scheme or target.netloc:
            missing.append(ref)
        elif not (markdown.parent / unquote(target.path)).is_file():
            missing.append(ref)
    if missing:
        raise client.MinerUError(f"发现 {len(missing)} 处未本地化或不存在的图片：{missing[:3]}")
    with zipfile.ZipFile(archive) as package:
        bad = package.testzip()
        names = set(package.namelist())
        expected = {markdown.name} | {
            (markdown.parent / unquote(urlsplit(ref.strip('<>')).path)).relative_to(markdown.parent).as_posix()
            for ref in refs
        }
        if bad or not expected.issubset(names):
            raise client.MinerUError("ZIP 完整性或包内图片路径校验失败。")
    return {"state": "done", "source": str(source),
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "source_pages": expected_pages, "returned_pages": actual_pages,
            "markdown": str(markdown), "archive": str(archive),
            "image_references": len(refs), "missing_images": missing,
            "zip_valid": True, "backends": backends,
            "quality_scope": "仅校验完整性；未验证公式识别准确率或目标编辑器渲染。"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--project-root", type=Path, default=client.project_root())
    parser.add_argument("--output-dir", type=Path, help="输出根目录，默认项目 mds/，沿用 raw/ 分类。")
    parser.add_argument("--work-dir", type=Path, help="长文档分段工作目录。")
    parser.add_argument("--env-file", type=Path)
    parser.add_argument("--language", default="ch")
    parser.add_argument("--model-version", choices=("vlm", "pipeline"), default="vlm")
    parser.add_argument("--ocr", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--poll-interval", type=float, default=15)
    parser.add_argument("--timeout", type=float, default=7200)
    parser.add_argument("--dry-run", action="store_true", help="检查输入与计划，不提交任务、不写输出。")
    args = parser.parse_args()
    try:
        from pypdf import PdfReader
    except ImportError:
        parser.error("缺少 pypdf，请用选定的 Python 安装本技能 requirements.txt。")
    source = args.input.expanduser().resolve()
    root = args.project_root.expanduser().resolve()
    raw = root / "raw"
    try:
        relative = source.relative_to(raw)
    except ValueError:
        parser.error("源 PDF 必须位于指定项目的 raw/ 下。")
    if not source.is_file() or source.suffix.lower() != ".pdf":
        parser.error("请输入存在的 PDF 文件。")
    if args.poll_interval <= 0 or args.timeout <= 0:
        parser.error("轮询间隔与超时时间必须大于 0。")
    try:
        pages = len(PdfReader(source).pages)
        if pages == 0:
            raise client.MinerUError("源 PDF 没有页面。")
        output_root = (args.output_dir or root / "mds").expanduser().resolve()
        output = output_root / relative.parent
        markdown = output / f"{source.stem}.md"
        validation = output / f"{source.stem}.validation.json"
        if any(path.exists() for path in (markdown, markdown.with_suffix(""), markdown.with_suffix(".zip"), validation)):
            raise client.MinerUError("输出已存在，请选择新的 --output-dir，避免覆盖或重复调用。")
        route = "直接提交" if pages <= 200 else f"分为 {(pages + 199) // 200} 段后合并"
        print(f"计划：{pages} 页；{route}；输出 {markdown}", flush=True)
        if args.dry_run:
            return 0
        scripts = Path(__file__).resolve().parent
        common = ["--model-version", args.model_version, "--language", args.language,
                  "--ocr" if args.ocr else "--no-ocr", "--env-file", str(args.env_file or root / ".env.local"),
                  "--poll-interval", str(args.poll_interval), "--timeout", str(args.timeout)]
        if pages <= 200:
            command = [sys.executable, "-u", str(scripts / "mineru_to_md.py"), str(source),
                       "--raw-dir", str(raw), "--output-dir", str(output_root), *common]
        else:
            work = args.work_dir or root / "output/mineru-full" / source.stem
            command = [sys.executable, "-u", str(scripts / "mineru_full_pdf.py"), str(source),
                       "--work-dir", str(work), "--output-dir", str(output), *common]
        result = subprocess.run(command, check=False)
        if result.returncode:
            return result.returncode
        report = validate_output(markdown, pages, source)
        validation.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"校验通过：{pages} 页，{report['image_references']} 处图片，ZIP 完整。\n记录：{validation}", flush=True)
        return 0
    except (client.MinerUError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
