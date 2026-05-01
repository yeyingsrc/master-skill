<div align="center">

# 大师.skill

### *你不再需要学习和寻找任何 skill。*
### *只需要大师.skill — 任何行业，它都为你蒸馏出一套最先进、最适合你的 skill。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/voidborne-d/master-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/voidborne-d/master-skill)
[![Status](https://img.shields.io/badge/status-v0.1--draft-orange)]()

</div>

> 你想蒸馏的下一个员工，何必是同事，何必是名人。蒸馏一个**行业**。

输入一个行业，自动完成：

1. **行业大佬调研**：top 10-15 思想领袖，文字 / 长访谈 / 视频 / 播客全部转成可读文本
2. **工具地图**：canonical 工具 + 新兴工具 + 选型决策树
3. **工作流提炼**：当前 SOP、方法论、最新 pipeline（每年都在变的那部分）
4. **知识正典**：必读书 / 论文 / 课程 / 核心概念
5. **信息源**：newsletter / podcast / 会议 / 社区 / dataset
6. **术语 + 标准**：黑话、缩写、合规、认证

输出：一个自包含的 `{industry}.master.skill` 目录，所有 hermit agent / Claude Code agent / OpenClaw / Codex 都能安装，让 AI 立刻进入「这行的资深人」模式。

## 灵感来源

- [同事.skill](https://github.com/titanwings/colleague-skill) 证明蒸馏一个人是可行的
- [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 证明蒸馏「思维方式」比蒸馏「话」更有用

大师.skill 把这套方法论从「一个人」推向「一整个行业」。底层共享同一个核心：**多源并行调研 → 三重质量关卡 → 框架提炼 → Agentic Protocol 让 skill 用起来不只是说得像，是做得像**。

## 状态

**v0.1 — Draft**。`SKILL.md` 已可被 Claude Code / OpenClaw / Codex 等 agent 加载并跑通完整 5-phase 工作流，但 `references/`、`prompts/`、`tools/` 中的脚本与模板还在补齐。看 [ROADMAP.md](ROADMAP.md)。

## 触发词

- `造大师 X` / `做个 X 的 master skill` / `我是 X 行业，给我蒸一个`
- `update 大师 X`（增量刷新已有 master skill）

## 安装

```bash
# Claude Code
mkdir -p ~/.claude/skills/master-skill
git clone https://github.com/voidborne-d/master-skill.git ~/.claude/skills/master-skill
```

其他宿主（OpenClaw / Codex / Hermes）按各自 skill 目录约定 clone 即可。

## License

MIT
