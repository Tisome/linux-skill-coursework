# Linux 内核原理与分析 · Skill 课程实档版

以课程仓库中第二周至第八周的七套 Skill 快照为核心，保存原始字节与每版引用的演进记录。以第二周预习原稿为基线，附实际题面和终端截图。

[最终 PDF](report/final-analysis.pdf) · [报告源稿](report/final-analysis.md) · [历史演进记录](archive/course-evolution.md) · [快照来源及 SHA-256](archive/skill-manifest.json)

## 再跑一轮

1. 取 `skill/vN/skill.md` 及该版 `references` 中的课程演进记录。
2. 把它们与 `cases/` 中对应周次的材料发给 AI，要求仅按材料写预习稿。做首尾对照时，两版都使用 `cases/07-elf.md`。
3. 对照版本目录下的 `generated.md` 和 `human-edited.md`。后者为本次 AI 审阅和批注稿。历史改动和本次审阅分别记在 `feedback/`。
4. 在 Python 3 环境运行 `python checks/verify.py`，核对快照、引用文件哈希、七轮稿件与课程截图。

本次回放在同一 AI 会话内生成。九月源仓库的现存 Git 记录中，选用的七份 Skill 最后均由同一个提交归档。本仓库按周次整理和打标签，提交使用当前实际时间。

## 目录和标签

`archive/` 保留原稿、截图、课程演进和来源信息。 `handmade/` 记录归档基线与回顾。 `skill/`、`output/`、`feedback/` 对应七轮整理与回放。 `phase1-handmade` 标记基线归档，`skill-v1` 到 `skill-v7` 标记周次回放，`final-report` 标记报告。

查看首尾差异可执行 `git diff --ignore-space-at-eol skill-v1:skill/v1/skill.md skill-v7:skill/v7/skill.md`。
