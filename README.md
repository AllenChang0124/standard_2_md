# standard_2_md

> An open, OCR-derived Markdown vault of public Chinese / European / AISI
> steel- and concrete-design standards — shareable, diff-able, and easy to
> search.
>
> 基于公开规范 OCR 导出的中 / 欧 / 美钢结构和混凝土设计规范 Markdown 文档库,
> 开放分享、可版本管理、可全文检索。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Docs: mds/](https://img.shields.io/badge/docs-mds%2F-blue)](./mds)
[![Skill: validate-md-headings](https://img.shields.io/badge/skill-validate--md--headings-lightgrey)](./.claude/skills/validate-md-headings/SKILL.md)

---

## English

### What this repo is

A community-maintained vault of OCR-extracted Markdown copies of public design
standards, plus the source PDFs that produced them. There is no build step, no
test runner, and no package manager — it is **data + one custom validation
skill**. Every `.md` is paired with a sibling directory of page images so you
can audit the OCR character by character.

The standards covered here are **public documents**: Chinese national standards
(GB / GB-T / JGJ), Eurocodes (EN 1993), and (eventually) AISI North American
specifications. The Markdown is provided for **reading, searching, citing, and
diffing across revisions** — it is not a substitute for the official published
standard.

### Layout

```
standard_2_md/
├── mds/
│   ├── AISI/                  # (planned) AISI North American specs
│   ├── EN/                    # EN 1993 (Eurocode 3) — steel design
│   │   ├── EN1993-1-1-2005钢结构设计1-1.md
│   │   ├── EN1993-1-1-2005钢结构设计1-1/   # page images extracted by OCR
│   │   └── …
│   └── GB/                    # Chinese GB / GB-T / JGJ standards
│       ├── GB50017-2017.md
│       ├── GB50017-2017/      # page images extracted by OCR
│       └── …
├── raw/
│   ├── EN/                    # source PDFs (one per .md)
│   └── GB/
├── .claude/skills/
│   └── validate-md-headings/  # the only custom tool (see below)
├── .obsidian/                 # Obsidian vault config — do not edit by hand
├── CLAUDE.md
├── LICENSE
└── README.md
```

Each `<name>.md` under `mds/<jurisdiction>/` is paired with a sibling
`<name>/` directory that holds the OCR-extracted page images, so you can
cross-check every character against the source PDF in `raw/<jurisdiction>/`.

### Current contents

| Jurisdiction | Standard                                    | File                                                                |
| ------------ | ------------------------------------------- | ------------------------------------------------------------------- |
| EN           | EN 1993-1-1:2005 Eurocode 3 — Part 1-1       | `mds/EN/EN1993-1-1-2005钢结构设计1-1.md`                              |
| EN           | EN 1993-1-3:2006 Eurocode 3 — Part 1-3       | `mds/EN/EN1993-1-1-3-2006钢结构设计1-3.md`                             |
| EN           | EN 1993-1-5:2006 Eurocode 3 — Part 1-5       | `mds/EN/EN1993-1-1-5-2006钢结构设计1-5.md`                             |
| GB           | GB 50010-2010 (2015 ed.) 混凝土结构设计规范     | `mds/GB/GB50010-2010_v2015.md`                                       |
| GB           | GB 50017-2017 钢结构设计标准                   | `mds/GB/GB50017-2017.md`                                             |
| GB           | GB 50018-2002 冷弯薄壁型钢结构技术规范           | `mds/GB/GB50018-2002.md`                                             |
| GB           | GB/T 50018-2025 冷弯型钢结构技术规范 (新版)      | `mds/GB/GBT50018-2025.md`                                            |
| GB           | JGJ 94-2008 建筑桩基技术规范                    | `mds/GB/JGJ_94-2008.md`                                              |
| GB           | JGJ 106-2014 建筑基桩检测技术规范               | `mds/GB/JGJ_106-2014.md`                                             |
| AISI         | —                                           | _(folder reserved; no entries yet)_                                  |

### Contributing

Issues and pull requests are the supported way to participate.

- **🐛 Report a bug / OCR defect.** Open an issue and paste:
  - the file path under `mds/` and the offending line range;
  - the expected text from the source PDF (cite a page number);
  - ideally a screenshot of the page in `mds/<file>/`.
- **📄 Provide a new raw document.** Open a PR that adds:
  1. the source PDF in `raw/<jurisdiction>/` named exactly as the standard's
     official title;
  2. the OCR'd `.md` in `mds/<jurisdiction>/` with the same base name;
  3. the page-image directory `mds/<jurisdiction>/<base name>/`;
  4. a row in the **Current contents** table above.

  Before opening the PR,  confirm it
  reports only `MD025` issues (the standards-doc chapter-H1 convention). Any
  other class of issue should be fixed first.
- **🔧 Heading fixes.** The validator never edits the file — only reports.
  Fixes must be applied manually using the Edit tool, **changing only the
  leading `#` marker run on heading lines**. Body text, math, tables, and
  image refs must never be touched. After editing, run `scope_check.py`
  against your pre-edit snapshot to byte-verify that only `#` markers changed.

### Licence

This repository is released under the [MIT License](./LICENSE). The Markdown
files are derivative works of **public standards documents** — please cite
the original issuing body (SAC, CEN, AISI, …) when reusing them.

---

## 中文

### 项目简介

这是一个**社区维护的公开规范 Markdown 文档库**,内容来自 OCR 提取的 PDF
转写结果,以及对应的源 PDF 文件本身。本仓库**不构建、不打包、不测试**,
只有 **数据 + 一个自定义校验脚本**。每个 `.md` 都附带同级目录的页图像,
方便逐字核对 OCR 质量。

收录的规范均为 **公开发布的工程技术标准**:中国国家标准(GB / GB-T / JGJ)、
欧洲规范(EN 1993 系列)、以及(计划中的)AISI 北美规范。Markdown 版本仅供
**阅读、检索、引用、版本对比**之用,**不替代官方正式发布的纸质或电子版
**。

### 目录结构

```
standard_2_md/
├── mds/
│   ├── AISI/                  # (预留) AISI 北美规范
│   ├── EN/                    # EN 1993(欧洲规范 3)—— 钢结构设计
│   │   ├── EN1993-1-1-2005钢结构设计1-1.md
│   │   ├── EN1993-1-1-2005钢结构设计1-1/   # OCR 提取的页图像
│   │   └── …
│   └── GB/                    # 中国 GB / GB-T / JGJ 标准
│       ├── GB50017-2017.md
│       ├── GB50017-2017/      # OCR 提取的页图像
│       └── …
├── raw/
│   ├── EN/                    # 源 PDF(与 .md 一一对应)
│   └── GB/
├── .claude/skills/
│   └── validate-md-headings/  # 唯一的自定义工具(见下文)
├── .obsidian/                 # Obsidian 库配置 —— 请勿手动修改
├── CLAUDE.md
├── LICENSE
└── README.md
```

`mds/<目录>/<name>.md` 与同级 `<name>/` 页图像目录、`raw/<目录>/<name>.pdf`
一一对应,任何字符都可以从 PDF 反查。

### 当前收录

| 体系 | 规范名称                                  | 文件                                                                 |
| ---- | ----------------------------------------- | -------------------------------------------------------------------- |
| EN   | EN 1993-1-1:2005 欧洲规范 3 第 1-1 部分     | `mds/EN/EN1993-1-1-2005钢结构设计1-1.md`                              |
| EN   | EN 1993-1-3:2006 欧洲规范 3 第 1-3 部分     | `mds/EN/EN1993-1-1-3-2006钢结构设计1-3.md`                             |
| EN   | EN 1993-1-5:2006 欧洲规范 3 第 1-5 部分     | `mds/EN/EN1993-1-1-5-2006钢结构设计1-5.md`                             |
| GB   | GB 50010-2010(2015 版)混凝土结构设计规范     | `mds/GB/GB50010-2010_v2015.md`                                       |
| GB   | GB 50017-2017 钢结构设计标准                 | `mds/GB/GB50017-2017.md`                                             |
| GB   | GB 50018-2002 冷弯薄壁型钢结构技术规范       | `mds/GB/GB50018-2002.md`                                             |
| GB   | GB/T 50018-2025 冷弯型钢结构技术规范(新版)   | `mds/GB/GBT50018-2025.md`                                            |
| GB   | JGJ 94-2008 建筑桩基技术规范                  | `mds/GB/JGJ_94-2008.md`                                              |
| GB   | JGJ 106-2014 建筑基桩检测技术规范             | `mds/GB/JGJ_106-2014.md`                                             |
| AISI | —                                         | _(目录已预留,暂无内容)_                                              |


### 如何参与

推荐通过 **Issue 和 Pull Request** 参与协作。

- **🐛 报告 OCR 缺陷。** 请在 Issue 中提供:`mds/` 下文件路径与出错行号、
  源 PDF 中的正确文字(标注页码)、最好附上 `mds/<file>/` 中对应页图像的
  截图。
- **📄 提供新的原始规范。** 请提交 PR,内容包括:
  1. 源 PDF 放入 `raw/<目录>/`,文件名沿用规范的官方名称;
  2. OCR 转写的 `.md` 放入 `mds/<目录>/`,与 PDF 同名;
  3. OCR 提取的页图像目录 `mds/<目录>/<文件名>/`;
  4. 在上方 **当前收录** 表格中新增一行。

  提交 PR 前,请对新文件,确认仅剩 `MD025` 报告(章节
  采用 H1 是规范文档的惯例)。其他任何类型的报告都应先修复。
- **🔧 修复标题层级。** 校验脚本只读不改。所有标题修复必须**人工使用
  Edit 工具逐行完成**,**只能改动标题行开头的 `#` 标记**,正文、数学公式、
  表格、图片引用一律不得改动。改完后,用 `scope_check.py` 对照改动前的
  快照做字节级验证,确认只有 `#` 标记发生了变化。

### 许可证

本仓库使用 [MIT 许可证](./LICENSE)。Markdown 文件均为 **公开发布规范的
衍生作品**,引用时请标注原规范发布机构(SAC、CEN、AISI 等)。

---

## Badges / 徽章

The MIT badge at the top of this file is auto-generated by
[shields.io](https://shields.io) and links to [`LICENSE`](./LICENSE).

顶部 MIT 徽章由 [shields.io](https://shields.io) 自动生成,链接到
[`LICENSE`](./LICENSE)。