# Roadmap

## v0.1 — Draft ✅

- [x] `SKILL.md` v0.1：agent-facing 工作流规约，5 phases + 3 质量关卡
- [x] `README.md`：项目意图 + 触发词 + 安装方式
- [x] `.gitignore`：secrets / 生成产物

## v0.2 — Templates & Prompts ✅

- [x] `references/skill-template.md`：生成产物的 SKILL.md 标准结构
- [x] `references/extraction-framework.md`：提炼方法论
- [x] `prompts/intake.md`：Phase 0 行业澄清问卷
- [x] `prompts/research/01-figures.md` 至 `06-glossary.md`：6 个 subagent 的 task 模板
- [x] `prompts/synthesis.md`：Phase 2 提炼指引
- [x] `prompts/quality_check.md`：Phase 4 验证 rubric

## v0.3 — Tooling ✅

- [x] `tools/skill_writer.py`：从临时 meta + content 文件生成完整 skill 目录
- [x] `tools/research/merge_research.py`：合并 6 轨调研 → Phase 1.5 摘要
- [x] `tools/research/quality_check.py`：Phase 4 机械 rubric runner
- [x] `tools/transcribe/youtube.sh`：yt-dlp 多语言字幕优先级
- [x] `tools/transcribe/srt_to_transcript.py`：SRT/VTT → 干净文本
- [x] `tools/install.py`：装到 Claude Code / OpenClaw / Codex / Hermes (含 `--host all`)

## v0.4 — Polish & Self-correction ✅

- [x] skill_writer 注入 synthesis body 到 SKILL.md（self-contained 输出）
- [x] skill_writer 自动从 research/ 计算 primary_source_ratio
- [x] Time-decay Registry 显式标记 (`last_updated` + `decay_risk`)
- [x] Adaptive cold floor (industry-type 多项式)
- [x] Cross-track contradiction detection (heuristic)
- [x] Voice-check 部分机械 surrogate (Tier-1 jargon counting)
- [x] Tool-tier 02-tools.md fallback parsing
- [x] VTT NOTE multi-line block 正确过滤
- [x] install --host all 多宿主一键 install
- [x] 版本 drift 警告

## v1.0 — End-to-end Validated ✅

- [x] LLM agent infra prototype 真实跑通 Phase 0 → 4
- [x] Phase 4 mechanical rubric verdict: PASS (10 pass / 1 partial / 0 fail)
- [x] Repo 公开
- [x] 至少 1 个真实行业的 sample skill 进入 prototypes/

## v0.6 — CLI tool stream (用户方向 2026-05-02) ✅

生成的 `{industry}-master.skill` 不只是 markdown，还包含可被 bash 调用的 CLI scripts：

- [x] `references/cli-spec.md`：完整 spec (目录布局 + 三类脚本 + 标准接口)
- [x] `tools/cli_writer.py`：从 synthesis 解析 + emit cli/ subtree
- [x] Section 9 Agentic Protocol → `cli/protocol/agentic.sh`
- [x] Section 2 Playbook 聚类 → `cli/decision/{cluster}.sh` (含 general-playbook 兜底)
- [x] research/03-workflows.md SOP → `cli/workflow/{slug}.sh`
- [x] 标准接口 `--help` / `--explain` / `--dry-run` / `--json` 全部实现
- [x] skill_writer create 默认调 cli_writer (新增 `--no-cli` 旁路)
- [x] 模板 + prompts 同步, 引导 synthesis 输出 CLI-friendly 格式
- [x] 验证 prototype 1 (LLM agent infra): 11 scripts emitted, all bash -n pass
- [x] 验证 prototype 2 (跨境电商, zh-CN): 5 scripts emitted, general-playbook 兜底成功

## v1.1 — Cross-skill composition + Increment ✅

- [x] Phase 3 Step 3 详 spec：调 [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 蒸馏 top 3 figures → 嵌入 sub-skills/
- [x] `prompts/sub-skill-figures.md`：subagent 调女娲的 prompt template
- [x] `tools/update_skill.py`：plan / archive / mark-in-progress / finalize 四 action
- [x] 衰减速度按 track 自动检测 (per-track refresh_at_months 表)
- [x] update 流程支持 changelog 追加

## v1.2 — Cluster 自动学 + cron + 5 个行业样本 ✅

- [x] cli_writer cluster keywords 自动从 synthesis 学习 (mental models + playbook + protocol 加权抽词频)
- [x] 中英 stopword 过滤, 中文 character n-gram, 英文 word-level
- [x] cluster anchor 保留原文 (中文 anchor 显示中文 topic_title, 文件名走 topic-N 兜底)
- [x] tools/update_skill.py schedule action — 生成 macOS launchd plist + Linux cron 一行
- [x] 检查频率按 skill 最高 decay 模块自动决定 (high → 周, medium → 月, low → 季)
- [x] 小红书运营 prototype (内容运营行业)
- [x] SEO 专家 prototype (半技术行业)
- [x] 恋爱高手 prototype (软技能 / 非工作类行业)

## v1.3 — 8 个行业样本横切覆盖 ✅

- [x] 短视频投流 master skill (商业 + 算法投放)
- [x] 足踝外科 master skill (医疗强监管)
- [x] 法律 master skill / 中国法 (法律强监管)

8 个 prototype 横切覆盖技术 / 商业 / 内容运营 / 软技能 / 医疗 / 法律。

## v1.x — 计划中

- [ ] Phase 1 子 agent 主动用 brave-search / agent-reach
- [ ] 调 web-article-reader 精读关键文章
- [ ] cli_writer 生成的 cluster 中文 anchor 加 transliteration (eg 「合规」→ "compliance")

## v2.x — Distribution

- [ ] 多语言 README (中英日韩)
- [ ] 与 dot-skill / nuwa-skill 互相引用
- [ ] PyPI 打包 `master-skill` 命令
- [ ] GitHub Action: 自动 update 已 fork 的 industry skill repos

---

## 非目标（明确不做）

- **不做行业实操工具**：master skill 是「认知操作系统」，不是 RPA。比如蒸馏「跨境电商」不会包含「自动登录 Amazon Seller Central」
- **不做版权侵权**：不存全本书 / 完整字幕 / 长段原文。只保留结构化摘要 + 来源元数据 + 极短引用
- **不做行业新闻聚合**：master skill 不是 newsfeed。最新动态以「指向哪些信息源」的形式存在，不直接搬内容
