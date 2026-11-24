---
name: mineru-api
description: "使用 MinerU 官网 API 将 raw/ 中指定 PDF 转为 Markdown、图片和 ZIP，支持超过 200 页的全文分段合并。Use for MinerU cloud PDF conversion and packaged Markdown export; excludes Colab and local model deployment."
---

# MinerU 官网 PDF 转写 / Cloud PDF conversion

使用本技能的 `scripts/convert.py` 处理用户指定的 PDF。它复用
`scripts/mineru_to_md.py`（上传、轮询与下载）和 `scripts/mineru_full_pdf.py`
（长文档分段合并）；两份实现均位于本技能内。

Use `scripts/convert.py` for the requested PDF. The upload/download client and
long-document splitter are bundled in this skill; no root-level scripts are needed.

## 执行 / Run

1. 定位用户指定的 `raw/` 文件。准备 Python 3.10+ 与 `requirements.txt` 中的依赖；
   优先复用已有 Python 环境，缺少依赖时在项目虚拟环境安装。
   Resolve the requested file under `raw/`; use Python 3.10+ with this skill's requirements.
2. 使用项目 `.env.local` 的 `MINERU_API_KEY` 或同名环境变量。
   密钥只由脚本读取，保持本地凭据不进入终端输出、技能、日志或结果包。
   Read the token through the script's environment/file support; keep credentials out of outputs.
3. 先运行 `--dry-run` 核实输入、页数和目标。正文型 PDF 使用默认非强制 OCR；
   扫描件或用户明确要求时加 `--ocr`；语言按源文件设置。默认 `vlm`，开启公式和表格。
   Check the plan first; select OCR and language for the source. Formula and table extraction stay enabled.
4. 用户请求转换即按指定范围上传到官网；继续等待至完成并下载。
   短 PDF 直接提交，超过 200 页自动按原顺序分段并合并，所有页面都要保留。
   Submit only the requested scope, wait for completion, and download. Long PDFs are split and merged in order.
5. 查看生成的 `.validation.json`：源页数与返回页数一致、图片链接存在、ZIP 通过校验，
   才报告交付成功。返回 Markdown、ZIP 和校验记录的路径。
   Report success after page, image-path, and ZIP checks pass; link all deliverables.

以下命令在项目根目录执行；从其他目录调用时，使用技能脚本绝对路径并指定
`--project-root` 与源文件绝对路径。
Run these commands from the project root; elsewhere use absolute script/input paths and `--project-root`.

```bash
python3 .agents/skills/mineru-api/scripts/convert.py \
  "raw/OFFSHORE/example.pdf" --language en --dry-run

python3 .agents/skills/mineru-api/scripts/convert.py \
  "raw/OFFSHORE/example.pdf" --language en
```

依赖安装 / Dependencies（仅在选定环境缺少 `pypdf` 时 / only if missing）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r .agents/skills/mineru-api/requirements.txt
```

## 路径与恢复 / Paths and recovery

- 输出默认为 `mds/<raw 相对分类>/<源文件名>.md`、同名资源目录、`.zip` 与
  `.validation.json`；`--output-dir` 替换输出根目录。已有结果会阻止覆盖。
  Outputs preserve the `raw/` category under `mds/`; choose another output root to retain existing results.
- 长文档工作目录默认 `output/mineru-full/<源文件名>/`，包含分段 PDF、分段结果与
  `manifest.json`。保留它可跳过已有分段结果；恢复前核实此前云端任务是否仍在运行。
  Retain the work directory for partial-result recovery; check the previous cloud task before resubmitting.
- 凭据错误、额度不足、任务失败或超时应报告服务返回原因和批次 ID。
  上传后失败不能直接认为任务未创建；先查已有批次，避免反复创建同一任务。
  On auth/quota/failure/timeout, report the cause and batch ID; inspect an existing batch before retrying submission.
- 脚本保留 HTTPS 证书验证。遇到证书问题使用有效 CA 或修复 Python 信任链。
  Keep TLS verification enabled and use a valid CA trust store.

## 结果边界 / Result boundaries

`vlm` 是官网请求选项，实际后端、版本和强度以返回 `layout.json` 元数据为准；
它不提供本地 `hybrid-auto-engine`、`effort=high` 或 “hyper” 的承诺。
页数、图片与 ZIP 校验代表交付完整性，不代表公式识别正确率。用户要求公式验收时，
另对照原页核查上下标、运算符、分段条件和分式结构，并区分原 PDF 的错误与识别错误。

The cloud model option does not guarantee a specific backend or effort. Delivery checks do not
prove formula accuracy; compare original pages when the user requests content review.

## 发现与调用 / Discovery and invocation

本目录为 `.agents/skills/mineru-api/`，提供标准 `SKILL.md` 元数据。
Codex 可用 `$mineru-api`；OpenCode 可通过技能 ID `mineru-api` 加载（新版本支持 `@mineru-api`）。
创建后启动新会话或刷新技能目录以发现它；其他 harness 依其 Agent Skills 路径设置加载。

This directory uses standard Agent Skills metadata. Start a fresh session or refresh discovery.
Codex and OpenCode both support project `.agents/skills/`; other harnesses may need their own discovery configuration.

来源 / Sources：[Codex skills](https://developers.openai.com/codex/skills/)、
[OpenCode skills](https://opencode.ai/docs/skills/)、
[MinerU API](https://mineru.net/apiManage/docs)。
