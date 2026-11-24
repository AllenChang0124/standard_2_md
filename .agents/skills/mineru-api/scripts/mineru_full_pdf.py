#!/usr/bin/env python3
"""将超出官网页数上限的 PDF 分段，复用 mineru_to_md.py，并合并全文结果。

需要 pypdf。输入原文件不变；所有分段和任务记录保留在 --work-dir 中，便于复核。
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

from pypdf import PdfReader, PdfWriter

import mineru_to_md as client


def save_manifest(path: Path, manifest: dict) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--language", default="en")
    parser.add_argument("--model-version", choices=("vlm", "pipeline"), default="vlm")
    parser.add_argument("--ocr", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--env-file", type=Path, default=client.project_root() / ".env.local")
    parser.add_argument("--poll-interval", type=float, default=15)
    parser.add_argument("--timeout", type=float, default=7200)
    args = parser.parse_args()
    source = args.input.resolve()
    work = args.work_dir.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    final_md = output_dir / f"{source.stem}.md"
    final_assets = output_dir / source.stem
    final_zip = output_dir / f"{source.stem}.zip"
    if any(path.exists() for path in (final_md, final_assets, final_zip)):
        parser.error("最终输出已存在，请先核实，避免覆盖。")

    reader = PdfReader(source)
    page_count = len(reader.pages)
    work.mkdir(parents=True, exist_ok=True)
    parts_dir = work / "inputs"
    parts_dir.mkdir(exist_ok=True)
    part_output = work / "results"
    manifest_path = work / "manifest.json"
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    manifest = {
        "source": str(source),
        "source_sha256": source_hash,
        "total_pages": page_count,
        "request": {"model_version": args.model_version, "language": args.language, "is_ocr": args.ocr,
                    "enable_formula": True, "enable_table": True},
        "state": "preparing",
        "parts": [],
    }
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding="utf-8"))
        if previous.get("source_sha256") != source_hash:
            parser.error("工作目录对应其他源文件，请使用新的 --work-dir。")
        if previous.get("request") != manifest["request"]:
            parser.error("工作目录的解析参数与本次不同，请使用新的 --work-dir。")
        manifest = previous

    parts = []
    for start in range(0, page_count, 200):
        end = min(start + 200, page_count)
        name = f"part-{start + 1:04d}-{end:04d}"
        path = parts_dir / f"{name}.pdf"
        if not path.exists():
            writer = PdfWriter()
            for index in range(start, end):
                writer.add_page(reader.pages[index])
            with path.open("wb") as stream:
                writer.write(stream)
        parts.append({"name": name, "first_page": start + 1, "last_page": end,
                      "pages": end - start, "input": str(path)})
    manifest["parts"] = parts
    manifest["state"] = "submitting"
    save_manifest(manifest_path, manifest)

    pending = [part for part in parts if not (part_output / f"{part['name']}.md").exists()]
    if pending:
        command = [sys.executable, "-u", str(Path(__file__).with_name("mineru_to_md.py")),
                   *(part["input"] for part in pending),
                   "--raw-dir", str(parts_dir), "--output-dir", str(part_output),
                   "--model-version", args.model_version, "--language", args.language,
                   "--ocr" if args.ocr else "--no-ocr", "--env-file", str(args.env_file),
                   "--no-package", "--poll-interval", str(args.poll_interval), "--timeout", str(args.timeout)]
        completed = subprocess.run(command, check=False)
        if completed.returncode:
            manifest["state"] = "incomplete"
            save_manifest(manifest_path, manifest)
            return completed.returncode

    manifest["state"] = "merging"
    save_manifest(manifest_path, manifest)
    stage = work / "merged"
    stage.mkdir(exist_ok=True)
    stage_assets = stage / source.stem
    stage_assets.mkdir(exist_ok=True)
    texts = []
    for part in parts:
        name = part["name"]
        markdown = part_output / f"{name}.md"
        assets = part_output / name
        content = markdown.read_text(encoding="utf-8")
        destination = stage_assets / name
        shutil.copytree(assets, destination, dirs_exist_ok=True)
        # 分段 Markdown 的链接含 part-xxxx-xxxx/，在此统一加上全文资源目录。
        content = client.rewrite_local_references(content, markdown.parent, source.stem)
        texts.append(f"<!-- 原 PDF 第 {part['first_page']}–{part['last_page']} 页 -->\n\n{content}")
        layouts = list(assets.rglob("layout.json"))
        if layouts:
            layout = json.loads(layouts[0].read_text(encoding="utf-8"))
            actual_pages = len(layout.get("pdf_info", []))
            if actual_pages != part["pages"]:
                raise RuntimeError(f"{name} 返回 {actual_pages} 页，预期 {part['pages']} 页。")
            part["returned_pages"] = actual_pages
            part["backend"] = {key: value for key, value in layout.items() if key != "pdf_info"}

    merged = "\n\n".join(texts)
    stage_md = stage / final_md.name
    stage_md.write_text(merged, encoding="utf-8")
    # 逐一验证所有 Markdown 直接图片引用均指向本地文件。
    import re
    from urllib.parse import unquote, urlsplit
    refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", merged)
    missing = [ref for ref in refs if not (stage / unquote(urlsplit(ref).path)).is_file()]
    if missing:
        raise RuntimeError(f"合并后存在 {len(missing)} 个失效图片链接：{missing[:3]}")
    stage_zip = stage / final_zip.name
    paths = client.OutputPaths(stage_md, stage_assets, stage_zip)
    client.write_package(paths)
    with zipfile.ZipFile(stage_zip) as archive:
        corrupt = archive.testzip()
        if corrupt:
            raise RuntimeError(f"ZIP 校验失败：{corrupt}")

    shutil.move(stage_assets, final_assets)
    shutil.move(stage_md, final_md)
    shutil.move(stage_zip, final_zip)
    manifest.update({"state": "done", "markdown": str(final_md), "archive": str(final_zip),
                     "image_references": len(refs), "missing_images": missing,
                     "markdown_characters": len(merged)})
    save_manifest(manifest_path, manifest)
    print(f"全文处理完成：{page_count} 页，{len(parts)} 段，{len(refs)} 处图片引用。", flush=True)
    print(f"Markdown：{final_md}\nZIP：{final_zip}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
