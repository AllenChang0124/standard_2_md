#!/usr/bin/env python3
"""使用 MinerU 精准解析 API，将 raw/ 中指定文件导出为 Markdown 与图片包。

默认使用官方推荐的 ``vlm`` 模型，并同时开启公式、表格和 OCR 识别。每份
文档会写入 ``mds/<原相对目录>/``：一个 Markdown 文件、一个同名资源目录，
以及一个包含二者的 ZIP 包。ZIP 中的 Markdown 链接已改为指向包内资源。

示例：
    python3 .agents/skills/mineru-api/scripts/mineru_to_md.py \
      "raw/GB/GB 50017-2017 钢结构设计标准（含条文说明）.pdf"

    python3 .agents/skills/mineru-api/scripts/mineru_to_md.py --all --overwrite
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import shutil
import ssl
import sys
import tempfile
import time
from dataclasses import dataclass
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen
import zipfile


API_BASE = "https://mineru.net/api/v4"
MAX_FILES_PER_BATCH = 50
MAX_FILE_SIZE = 200 * 1024 * 1024
SUPPORTED_SUFFIXES = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".webp",
    ".gif",
    ".bmp",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
}
ACTIVE_STATES = {"waiting-file", "pending", "running", "converting"}
MARKDOWN_LINK_RE = re.compile(
    r"(?P<prefix>!?\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)(?P<suffix>(?:\s+[^)]*)?\))"
)
HTML_IMAGE_RE = re.compile(
    r"(?P<prefix><img\b[^>]*?\bsrc\s*=\s*)(?P<quote>['\"])(?P<target>.*?)(?P=quote)",
    re.IGNORECASE,
)


class MinerUError(RuntimeError):
    """MinerU 请求或结果处理失败。"""


def project_root() -> Path:
    """从工作目录或技能所在项目定位 raw/，支持不同 harness 的工作目录。"""
    for base in (Path.cwd(), Path(__file__).resolve().parent):
        for candidate in (base, *base.parents):
            if (candidate / "raw").is_dir():
                return candidate
    return Path.cwd()


def make_ssl_context() -> ssl.SSLContext:
    """保留证书校验；补足部分 macOS Python 安装缺失的默认 CA 路径。"""
    context = ssl.create_default_context()
    paths = ssl.get_default_verify_paths()
    if not paths.cafile and not paths.capath and not os.getenv("SSL_CERT_FILE"):
        system_ca = Path("/etc/ssl/cert.pem")
        if system_ca.is_file():
            context.load_verify_locations(cafile=str(system_ca))
        else:
            try:
                import certifi
            except ImportError:
                pass
            else:
                context.load_verify_locations(cafile=certifi.where())
    return context


@dataclass(frozen=True)
class SourceDocument:
    """本地源文件及其稳定的 MinerU data_id。"""

    path: Path
    relative_to_raw: Path
    data_id: str


@dataclass(frozen=True)
class OutputPaths:
    """一份源文件对应的 Markdown、资源目录与归档包路径。"""

    markdown: Path
    assets: Path
    archive: Path


def parse_arguments(project_root: Path) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="调用 MinerU 精准解析 API，导出 Markdown、图片目录和 ZIP 包。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        metavar="PATH",
        help="raw/ 下的文件或目录；目录会递归查找支持的文件。",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="解析 raw/ 下全部支持的文件。",
    )
    parser.add_argument(
        "--api-key",
        help="MinerU API Token；优先级高于环境变量，避免写入命令历史。",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=project_root / ".env.local",
        help="读取 MINERU_API_KEY 的环境文件。",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=project_root / "raw",
        help="源文件根目录。",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "mds",
        help="Markdown 输出根目录。",
    )
    parser.add_argument(
        "--model-version",
        choices=("vlm", "pipeline"),
        default="vlm",
        help="MinerU 模型版本；vlm 是官方推荐的高精度模型。",
    )
    parser.add_argument(
        "--language",
        default="ch",
        help="文档语言代码，例如 ch、en、auto。",
    )
    parser.add_argument(
        "--ocr",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="启用 OCR；扫描件通常需要它。可用 --no-ocr 关闭。",
    )
    parser.add_argument(
        "--page-ranges",
        help="所有输入文件共用的页码范围，例如 1-20 或 2,4-6。",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=10.0,
        help="轮询解析结果的间隔（秒）。",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=7200.0,
        help="从上传完成到全部任务结束的最长等待时间（秒）。",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="覆盖已有的 Markdown、资源目录和 ZIP 包。",
    )
    parser.add_argument(
        "--no-package",
        dest="package",
        action="store_false",
        help="不生成便于携带的 ZIP 包。",
    )
    parser.set_defaults(package=True)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅列出将要解析的文件和输出路径，不调用 API。",
    )
    args = parser.parse_args()

    if not args.inputs and not args.all:
        parser.error("请提供至少一个 PATH，或使用 --all。")
    if args.inputs and args.all:
        parser.error("PATH 与 --all 不能同时使用，以免误提交不需要的文件。")
    if args.poll_interval <= 0:
        parser.error("--poll-interval 必须大于 0。")
    if args.timeout <= 0:
        parser.error("--timeout 必须大于 0。")
    return args


def read_dotenv(path: Path) -> dict[str, str]:
    """读取足够覆盖 API Key 的 .env 格式；不会打印其中的值。"""
    if not path.is_file():
        return {}

    result: dict[str, str] = {}
    assignment = re.compile(
        r"^\s*(?:export\s+)?(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<value>.*)$"
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        match = assignment.match(line)
        if not match:
            continue
        value = match.group("value").strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        else:
            value = value.split(" #", 1)[0].rstrip()
        result[match.group("key")] = value
    return result


def resolve_api_key(args: argparse.Namespace) -> str:
    if args.api_key:
        return args.api_key.strip()
    environment = read_dotenv(args.env_file)
    return (os.getenv("MINERU_API_KEY") or environment.get("MINERU_API_KEY") or "").strip()


def normalized_path(value: Path) -> Path:
    return value.expanduser().resolve()


def iter_candidates(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
    elif input_path.is_dir():
        yield from (path for path in input_path.rglob("*") if path.is_file())
    else:
        raise MinerUError(f"找不到输入路径：{input_path}")


def collect_sources(args: argparse.Namespace) -> list[SourceDocument]:
    raw_dir = normalized_path(args.raw_dir)
    if not raw_dir.is_dir():
        raise MinerUError(f"raw 根目录不存在：{raw_dir}")

    roots = [raw_dir] if args.all else [normalized_path(Path(item)) for item in args.inputs]
    files: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        for path in iter_candidates(root):
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            if path.suffix.lower() in SUPPORTED_SUFFIXES:
                files.append(resolved)
            else:
                print(f"跳过不支持的文件：{path}", file=sys.stderr)

    if not files:
        raise MinerUError("没有找到 MinerU 支持的文件。")

    documents: list[SourceDocument] = []
    for path in sorted(files, key=lambda item: str(item)):
        size = path.stat().st_size
        if size == 0:
            raise MinerUError(f"文件为空：{path}")
        if size > MAX_FILE_SIZE:
            raise MinerUError(f"文件超过 MinerU 的 200 MB 限制：{path}")
        try:
            relative_to_raw = path.relative_to(raw_dir)
        except ValueError as error:
            raise MinerUError(f"输入文件必须位于 raw/ 下：{path}") from error
        digest = hashlib.sha256(relative_to_raw.as_posix().encode("utf-8")).hexdigest()[:32]
        documents.append(SourceDocument(path, relative_to_raw, f"mineru-{digest}"))
    return documents


def output_paths(document: SourceDocument, output_dir: Path) -> OutputPaths:
    relative_without_suffix = document.relative_to_raw.with_suffix("")
    directory = output_dir / relative_without_suffix.parent
    name = relative_without_suffix.name
    return OutputPaths(
        markdown=directory / f"{name}.md",
        assets=directory / name,
        archive=directory / f"{name}.zip",
    )


def assert_outputs_available(
    documents: Iterable[SourceDocument], output_dir: Path, overwrite: bool, package: bool
) -> None:
    conflicts: list[Path] = []
    for document in documents:
        paths = output_paths(document, output_dir)
        candidates = (paths.markdown, paths.assets, paths.archive) if package else (paths.markdown, paths.assets)
        conflicts.extend(path for path in candidates if path.exists())
    if conflicts and not overwrite:
        rendered = "\n  ".join(str(path) for path in conflicts[:10])
        remaining = "" if len(conflicts) <= 10 else f"\n  …以及另外 {len(conflicts) - 10} 项"
        raise MinerUError(
            "输出已存在；为防止覆盖，脚本没有提交任务。请改用 --overwrite，或指定 --output-dir：\n  "
            f"{rendered}{remaining}"
        )


def api_json(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    request = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=60, context=make_ssl_context()) as response:
            response_body = response.read()
    except HTTPError as error:
        detail = error.read(4096).decode("utf-8", errors="replace")
        raise MinerUError(f"MinerU API 返回 HTTP {error.code}：{detail}") from error
    except URLError as error:
        raise MinerUError(f"无法连接 MinerU API：{error.reason}") from error

    try:
        decoded = json.loads(response_body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MinerUError("MinerU API 返回了非 JSON 响应。") from error
    if decoded.get("code") != 0:
        raise MinerUError(
            f"MinerU API 请求失败（code={decoded.get('code')}）：{decoded.get('msg', '未知错误')}"
        )
    data = decoded.get("data")
    if not isinstance(data, dict):
        raise MinerUError("MinerU API 成功响应中缺少 data 对象。")
    return data


def request_upload_urls(documents: list[SourceDocument], args: argparse.Namespace, token: str) -> tuple[str, list[str]]:
    files: list[dict[str, Any]] = []
    for document in documents:
        item: dict[str, Any] = {
            "name": document.path.name,
            "data_id": document.data_id,
            "is_ocr": args.ocr,
        }
        if args.page_ranges:
            item["page_ranges"] = args.page_ranges
        files.append(item)

    payload: dict[str, Any] = {
        "files": files,
        "model_version": args.model_version,
        "language": args.language,
        "enable_formula": True,
        "enable_table": True,
    }
    data = api_json("POST", f"{API_BASE}/file-urls/batch", token, payload)
    batch_id = data.get("batch_id")
    urls = data.get("file_urls")
    if not isinstance(batch_id, str) or not isinstance(urls, list) or not all(isinstance(url, str) for url in urls):
        raise MinerUError("MinerU 返回的上传链接格式异常。")
    if len(urls) != len(documents):
        raise MinerUError(
            f"MinerU 返回 {len(urls)} 个上传链接，但本批次包含 {len(documents)} 个文件。"
        )
    return batch_id, urls


def upload_file(url: str, path: Path) -> None:
    """流式 PUT 至预签名 URL，避免将最大 200 MB 文件整体读入内存。"""
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise MinerUError("MinerU 返回了无效的上传链接。")
    connection_type = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection
    connection = connection_type(
        parsed.hostname,
        parsed.port,
        timeout=120,
        **({"context": make_ssl_context()} if parsed.scheme == "https" else {}),
    )
    target = parsed.path or "/"
    if parsed.query:
        target = f"{target}?{parsed.query}"
    try:
        connection.putrequest("PUT", target)
        connection.putheader("Content-Length", str(path.stat().st_size))
        connection.putheader("User-Agent", "standard-2-md-mineru-client/1.0")
        connection.endheaders()
        with path.open("rb") as source:
            while chunk := source.read(1024 * 1024):
                connection.send(chunk)
        response = connection.getresponse()
        response_body = response.read(4096).decode("utf-8", errors="replace")
        if not 200 <= response.status < 300:
            raise MinerUError(f"上传失败（HTTP {response.status}）：{response_body}")
    except OSError as error:
        raise MinerUError(f"上传文件失败：{path}（{error}）") from error
    finally:
        connection.close()


def iter_batches(items: list[SourceDocument], size: int = MAX_FILES_PER_BATCH) -> Iterable[list[SourceDocument]]:
    for index in range(0, len(items), size):
        yield items[index : index + size]


def download_file(url: str, destination: Path) -> None:
    request = Request(url, headers={"User-Agent": "standard-2-md-mineru-client/1.0"})
    try:
        with urlopen(request, timeout=120, context=make_ssl_context()) as response, destination.open("wb") as target:
            while chunk := response.read(1024 * 1024):
                target.write(chunk)
    except (HTTPError, URLError, OSError) as error:
        raise MinerUError(f"下载 MinerU 结果包失败：{error}") from error


def safe_extract(zip_path: Path, destination: Path) -> None:
    """提取可信结果包前仍防护 Zip Slip 与符号链接。"""
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            name = Path(info.filename)
            is_symlink = (info.external_attr >> 16) & 0o170000 == 0o120000
            if name.is_absolute() or ".." in name.parts or is_symlink:
                raise MinerUError(f"结果 ZIP 含不安全条目：{info.filename}")
        archive.extractall(destination)


def local_target_exists(target: str, markdown_parent: Path) -> bool:
    candidate = target.strip()
    if candidate.startswith("<") and candidate.endswith(">"):
        candidate = candidate[1:-1]
    parsed = urlsplit(candidate)
    if parsed.scheme or parsed.netloc or candidate.startswith("#"):
        return False
    resource = (markdown_parent / unquote(parsed.path)).resolve()
    try:
        resource.relative_to(markdown_parent.resolve())
    except ValueError:
        return False
    return resource.is_file()


def rewrite_local_references(markdown: str, markdown_parent: Path, assets_name: str) -> str:
    """将 full.md 中已有的本地图片/资源链接改为同级资源目录。"""
    escaped_assets_name = quote(assets_name, safe="-_.~")

    def prefixed_target(target: str) -> str:
        if not local_target_exists(target, markdown_parent):
            return target
        if target.startswith("<") and target.endswith(">"):
            return f"<{escaped_assets_name}/{target[1:-1]}>"
        return f"{escaped_assets_name}/{target}"

    def replace_markdown(match: re.Match[str]) -> str:
        return f"{match.group('prefix')}{prefixed_target(match.group('target'))}{match.group('suffix')}"

    def replace_html_image(match: re.Match[str]) -> str:
        quote_char = match.group("quote")
        return f"{match.group('prefix')}{quote_char}{prefixed_target(match.group('target'))}{quote_char}"

    markdown = MARKDOWN_LINK_RE.sub(replace_markdown, markdown)
    return HTML_IMAGE_RE.sub(replace_html_image, markdown)


def find_full_markdown(extracted: Path) -> Path:
    candidates = sorted(extracted.rglob("full.md"), key=lambda item: (len(item.parts), str(item)))
    if not candidates:
        candidates = sorted(extracted.rglob("*.md"), key=lambda item: (len(item.parts), str(item)))
    if not candidates:
        raise MinerUError("MinerU 结果包中未找到 Markdown 文件。")
    return candidates[0]


def remove_output(paths: OutputPaths, package: bool) -> None:
    if paths.markdown.exists():
        paths.markdown.unlink()
    if paths.assets.exists():
        shutil.rmtree(paths.assets)
    if package and paths.archive.exists():
        paths.archive.unlink()


def write_package(paths: OutputPaths) -> None:
    with zipfile.ZipFile(paths.archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.write(paths.markdown, paths.markdown.name)
        for path in sorted(paths.assets.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(paths.markdown.parent))


def export_result(
    document: SourceDocument,
    result_zip_url: str,
    output_dir: Path,
    overwrite: bool,
    package: bool,
) -> OutputPaths:
    paths = output_paths(document, output_dir)
    paths.markdown.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="mineru-") as temporary:
        working = Path(temporary)
        downloaded_zip = working / "mineru-result.zip"
        extracted = working / "extracted"
        extracted.mkdir()
        download_file(result_zip_url, downloaded_zip)
        safe_extract(downloaded_zip, extracted)
        source_markdown = find_full_markdown(extracted)

        if overwrite:
            remove_output(paths, package)
        elif paths.markdown.exists() or paths.assets.exists() or (package and paths.archive.exists()):
            raise MinerUError(f"下载过程中发现输出已存在：{paths.markdown}")

        # 复制 full.md 同级的所有资源；通常包含 images/，并保留 MinerU 的相对路径。
        paths.assets.mkdir(parents=True)
        for source in source_markdown.parent.rglob("*"):
            if source.is_file() and source != source_markdown:
                destination = paths.assets / source.relative_to(source_markdown.parent)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)

        markdown_text = source_markdown.read_text(encoding="utf-8")
        markdown_text = rewrite_local_references(markdown_text, source_markdown.parent, paths.assets.name)
        paths.markdown.write_text(markdown_text, encoding="utf-8", newline="\n")
        if package:
            write_package(paths)
    return paths


def describe_state(result: dict[str, Any]) -> str:
    state = str(result.get("state", "unknown"))
    progress = result.get("extract_progress")
    if isinstance(progress, dict):
        current = progress.get("extracted_pages", "?")
        total = progress.get("total_pages", "?")
        return f"{state}（{current}/{total} 页）"
    return state


def process_batch(
    documents: list[SourceDocument], args: argparse.Namespace, token: str
) -> tuple[list[OutputPaths], list[str]]:
    batch_id, urls = request_upload_urls(documents, args, token)
    print(f"已创建批次 {batch_id}，开始上传 {len(documents)} 个文件。")
    for document, url in zip(documents, urls, strict=True):
        print(f"上传：{document.relative_to_raw}")
        upload_file(url, document.path)

    pending = {document.data_id: document for document in documents}
    exported: list[OutputPaths] = []
    errors: list[str] = []
    last_states: dict[str, str] = {}
    started = time.monotonic()
    while pending:
        if time.monotonic() - started > args.timeout:
            errors.extend(f"{document.relative_to_raw}：等待解析超时" for document in pending.values())
            break

        data = api_json("GET", f"{API_BASE}/extract-results/batch/{batch_id}", token)
        results = data.get("extract_result")
        if not isinstance(results, list):
            raise MinerUError("MinerU 批量查询响应缺少 extract_result 列表。")

        seen: set[str] = set()
        for result in results:
            if not isinstance(result, dict):
                continue
            data_id = result.get("data_id")
            if not isinstance(data_id, str) or data_id not in pending:
                continue
            seen.add(data_id)
            state = str(result.get("state", "unknown"))
            state_description = describe_state(result)
            if last_states.get(data_id) != state_description:
                print(f"{pending[data_id].relative_to_raw}：{state_description}")
                last_states[data_id] = state_description

            if state == "failed":
                errors.append(f"{pending[data_id].relative_to_raw}：{result.get('err_msg') or 'MinerU 解析失败'}")
                del pending[data_id]
            elif state == "done":
                zip_url = result.get("full_zip_url")
                if not isinstance(zip_url, str) or not zip_url:
                    errors.append(f"{pending[data_id].relative_to_raw}：任务完成但未返回结果 ZIP 下载链接")
                    del pending[data_id]
                    continue
                document = pending.pop(data_id)
                try:
                    paths = export_result(document, zip_url, normalized_path(args.output_dir), args.overwrite, args.package)
                    exported.append(paths)
                    print(f"已导出：{paths.markdown}")
                except MinerUError as error:
                    errors.append(f"{document.relative_to_raw}：导出结果失败（{error}）")
            elif state not in ACTIVE_STATES:
                errors.append(f"{pending[data_id].relative_to_raw}：收到未知任务状态 {state!r}")
                del pending[data_id]

        if pending:
            not_reported = set(pending) - seen
            if not_reported:
                print(f"MinerU 尚未返回 {len(not_reported)} 个任务的状态，继续等待。")
            time.sleep(args.poll_interval)
    return exported, errors


def main() -> int:
    args = parse_arguments(project_root())
    try:
        documents = collect_sources(args)
        output_dir = normalized_path(args.output_dir)
        assert_outputs_available(documents, output_dir, args.overwrite, args.package)
        print(f"将以 {args.model_version} 模型解析 {len(documents)} 个文件；公式、表格识别均已开启。")
        for document in documents:
            paths = output_paths(document, output_dir)
            print(f"  {document.relative_to_raw} -> {paths.markdown}")
        if args.dry_run:
            print("Dry run 完成：未调用 MinerU API。")
            return 0

        token = resolve_api_key(args)
        if not token:
            raise MinerUError(
                f"未找到 MINERU_API_KEY。请在 {args.env_file} 中设置它，或通过环境变量提供。"
            )

        all_exports: list[OutputPaths] = []
        all_errors: list[str] = []
        batches = list(iter_batches(documents))
        for number, batch in enumerate(batches, start=1):
            print(f"处理第 {number}/{len(batches)} 批（{len(batch)} 个文件）。")
            exports, errors = process_batch(batch, args, token)
            all_exports.extend(exports)
            all_errors.extend(errors)

        print(f"完成：成功导出 {len(all_exports)} 份文档。")
        for paths in all_exports:
            package_text = f"；打包 {paths.archive}" if args.package else ""
            print(f"  Markdown：{paths.markdown}；资源：{paths.assets}{package_text}")
        if all_errors:
            print("以下文件未完成：", file=sys.stderr)
            for error in all_errors:
                print(f"  - {error}", file=sys.stderr)
            return 1
        return 0
    except MinerUError as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
