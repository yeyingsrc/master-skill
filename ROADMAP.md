# Roadmap

## v0.1 — Draft (current)

- [x] `SKILL.md` v0.1：agent-facing 工作流规约，5 phases + 3 质量关卡
- [x] `README.md`：项目意图 + 触发词 + 安装方式
- [x] `.gitignore`：secrets / 生成产物
- [ ] 在真实行业上跑通一次（候选：cross-border e-commerce / LLM agent infra / podiatry）

## v0.2 — Templates & Prompts

- [ ] `references/skill-template.md`：生成产物的 SKILL.md 标准结构（行业 OS + 6 个知识模块）
- [ ] `references/extraction-framework.md`：提炼方法论（如何从 6 轨调研中抽出行业 OS）
- [ ] `prompts/intake.md`：Phase 0 行业澄清问卷
- [ ] `prompts/research/`：6 个 subagent 的 task 模板
- [ ] `prompts/synthesis.md`：Phase 2 提炼指引
- [ ] `prompts/quality_check.md`：Phase 4 验证 rubric

## v0.3 — Tooling

- [ ] `tools/research/merge_research.py`：合并 6 轨调研 → Phase 1.5 摘要
- [ ] `tools/research/quality_check.py`：Phase 4 自检
- [ ] `tools/transcribe/youtube.sh`：yt-dlp 字幕优先 + whisper.cpp fallback
- [ ] `tools/transcribe/podcast.sh`：rss → audio → transcript
- [ ] `tools/skill_writer.py`：从临时 meta + content 文件生成完整 skill 目录
- [ ] `tools/install_*.py`：装到 Claude Code / OpenClaw / Codex / Hermes

## v0.4 — Cross-skill composition

- [ ] 调用 [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 蒸馏 top 3 figures → 嵌入 sub-skill
- [ ] 调用 brave-search / agent-reach 增强信息获取
- [ ] 调用 web-article-reader 精读关键文章

## v0.5 — Increment & decay

- [ ] `update master X` 增量刷新工作流
- [ ] 时效性标注：哪些信息会衰减、衰减速度
- [ ] 定期自动 refresh hook

## v0.6 — CLI output (新方向 2026-05-02)

生成的 `{industry}-master.skill` 不只是 markdown，还要包含可被 bash 调用的 CLI scripts：

- [ ] `cli/` 目录结构 spec：每个核心 workflow / tool 一个 bash script
- [ ] Track 02 tools 的「典型使用场景」字段 → CLI script 模板
- [ ] Track 03 workflows 的入门 SOP 步骤 → 多步 CLI 编排
- [ ] skill_writer.py 增加 emit-cli 模式
- [ ] 给生成的 CLI 配 `--help` / `--dry-run` / `--explain` 三个标准接口
- [ ] 让 master skill 不只是「思维顾问」，是「思维顾问 + 实操 CLI 套件」

## v1.0 — Public release

- [ ] Repo 转 public
- [ ] 至少 3 个真实行业的样例 master skill 已开源
- [ ] 多语言 README（中英日韩）
- [ ] 与 dot-skill / nuwa-skill 互相引用

---

## 非目标（明确不做）

- **不做行业实操工具**：master skill 是「认知操作系统」，不是 RPA。比如蒸馏「跨境电商」不会包含「自动登录 Amazon Seller Central」
- **不做版权侵权**：不存全本书 / 完整字幕 / 长段原文。只保留结构化摘要 + 来源元数据 + 极短引用
- **不做行业新闻聚合**：master skill 不是 newsfeed。最新动态以「指向哪些信息源」的形式存在，不直接搬内容
