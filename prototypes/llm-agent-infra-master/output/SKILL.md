---
name: llm-agent-infra-master
description: |
  LLM agent 基础设施 (LLM agent infra) Master OS — automated mastery of LLM agent infra: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on LLM agent infra problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「agent framework」「LLM agent」「agent infra」「multi-agent orchestration」「agent runtime」
triggers:
  - "agent framework"
  - "LLM agent"
  - "agent infra"
  - "multi-agent orchestration"
  - "agent runtime"
  - "tool use"
  - "RAG"
  - "agent observability"
industry: "LLM agent infra"
industry-cn: "LLM agent 基础设施"
locale: "global"
last_research_date: "2026-05-02"
source_count: 0
profile: "practitioner"
generator: "master-skill v0.3"
---

# LLM agent 基础设施 · Master OS

> This skill makes the agent operate as a senior LLM agent infra practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 LLM agent infra 相关的问题时（关键词：agent framework, LLM agent, agent infra, multi-agent orchestration, agent runtime, tool use, RAG, agent observability），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 LLM agent infra 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：LLM agent infra 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: LLM agent infra 式研究维度

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

{{# Phase 2.9 推导出来的 5-8 个研究维度，每个含具体搜索动作。例如：

#### 维度 1: {{name}}
- 看什么：{{what to inspect}}
- 在哪看：{{specific sources, not generic "search the web"}}
- 输出：{{1-2 line factual summary}}

#### 维度 2: ...
}}

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: LLM agent infra 式回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型（0 个）

{{# Phase 2.1 输出。每个 3-7 个之间。}}

### {{1. 模型名称}}

**一句话**：{{summary}}

**它说的是**：{{2-4 句具体阐述}}

**证据来源**：
- {{source 1, with type marker — primary / secondary / inference}}
- {{source 2}}

**应用方式**：{{when to invoke this model in real work}}

**局限**：{{when this model fails — must be filled, not skipped}}

### {{2. ...}}

[repeat 3-7 times total]

---

## 标准 Playbook（0 条决策启发式）

{{# Phase 2.2 输出。5-10 条。每条形如「如果 X，则 Y」。}}

1. **如果 {{scenario 1}}**，则 {{decision/action 1}}。
   - 案例：{{1-2 specific examples from research notes}}

2. **如果 {{scenario 2}}**，则 ...

[5-10 条]

---

## 工具栈与选型决策树

{{# Phase 2.3 输出。}}

### 必备工具（≥ 80% 从业者用）

| 工具 | 场景 | 上手难度 | 替代品 |
|------|------|---------|-------|
| {{tool}} | {{when to use}} | low/med/high | {{alt}} |

### 场景特化

{{# 列出 2-4 个常见场景，每个推荐对应工具。}}

#### 场景 A: {{name}}
推荐：{{tool}}（理由：{{why}}）
不推荐：{{tool}}（理由：{{why not}}）

### 新兴 / 实验阶段

{{# 近 12 个月出现的工具，未必稳定。明确标注「{{date}} 后才出现」。}}

### 避坑清单

- 不要用 {{X}} 做 {{Y}}：{{为什么}}
- ...

---

## 工作流 / Pipeline

{{# Phase 2.4 输出。}}

### 入门 SOP（最小完整任务）

{{Step-by-step. 给 3-7 步走完。}}

### 资深路径

{{资深人会跳过 / 优化哪些步骤，为什么。}}

### 近期工作流变化（{{YYYY-MM}} 起）

{{AI / 新工具 / 法规变化 带来的工作流改写。具体到哪一步换成什么。}}

---

## 表达 DNA

{{# Phase 2.5 输出。}}

| 维度 | LLM agent infra 风格 |
|------|----------|
| 高频用语 | {{words/phrases}} |
| 黑话 / 缩写 | {{jargon, top 5-10}} |
| 严肃 register | {{how this field talks in serious discussion}} |
| 内 vs 外沟通 | {{difference}} |
| 外行破绽 | {{things outsiders say that immediately mark them}} |

---

## 质量基准 + 反模式

{{# Phase 2.6 输出。}}

### 什么算「好」

- {{criterion 1, verifiable}}
- {{criterion 2}}
- ...

### 反模式（外行 / 入门常犯）

- {{anti-pattern 1}} — 为什么错：{{reason}}
- ...

---

## 智识谱系

{{# Phase 2.7 输出。}}

主要流派 / 思想分支：

### {{流派 A}}
- 奠基：{{founders}}
- 当前代表：{{current voices}}
- 核心主张：{{1-2 lines}}

### {{流派 B}}
- ...

### 流派间分歧

{{What's the field actually arguing about right now?}}

---

## 诚实边界

{{# Phase 2.8 输出。≥ 3 条具体局限。}}

- 信息截止 `2026-05-02`。工具 / 工作流模块衰减最快（建议每 3-6 月 update 大师 {{slug}}）。
- {{specific gap from Phase 1.5 — e.g. "Track 4 (canon) 收集到的英文资料显著多于中文，对中文圈实践的描述偏弱"}}
- {{specific bias from public material — e.g. "成功案例的比例远高于失败案例，幸存者偏差明显"}}
- master skill 不能替代真实从业经验。涉及具体雇佣 / 投资 / 法律决策时，必须找真人确认。

---

## 知识模块（详细）

### 1. Figures — 行业大佬

{{# Phase 1 Track 01 整理。Top 10-15 人。每人 2-3 行。}}

| 人物 | 一句话 | 代表作品 | 值得读/听/看的 3 件事 | 最近 12 个月动态 |
|------|--------|---------|--------------------|-----------------|
| {{name}} | {{tagline}} | {{key work}} | {{3 items}} | {{recent}} |

{{# 如果 Phase 3 调用了 nuwa.skill 蒸 top 3：}}
深度蒸馏的 sub-skill：
- `sub-skills/{{figure-1-slug}}/` — 调用方式：在对话中提「按 {{name}} 的视角看这个问题」
- ...

### 2. Tools — 工具地图

参见上方 [工具栈与选型决策树](#工具栈与选型决策树)，详细数据：`references/research/02-tools.md`

### 3. Workflows — 工作流详解

参见上方 [工作流 / Pipeline](#工作流--pipeline)，原始素材：`references/research/03-workflows.md`

### 4. Canon — 知识正典

{{# Phase 1 Track 04 整理。每条标 [Primary] / [Secondary]。}}

#### 必读书 / 论文 / 课
- [Primary] {{title}} — {{author}}, {{year}}: {{what it teaches}}
- [Secondary] {{title}}: {{1-line value}}
- ...

#### 核心 20-30 个概念

{{Concept 1}} · {{Concept 2}} · ... （详细定义见 `references/research/06-glossary.md`）

### 5. Sources — 信息源

{{# Phase 1 Track 05 整理。每个标更新频率。}}

#### Newsletter / Substack
- {{name}} ({{url}}) — {{cadence}} — {{why follow}}

#### Podcast
- ...

#### 会议 / Conference
- ...

#### 社区
- ...

#### Dataset / Benchmark（如适用）
- ...

### 6. Glossary — 术语 + 标准

详见 `references/research/06-glossary.md`。高频 top 20 摘到这里：

| 术语 | 含义 | 易混淆于 |
|------|------|---------|
| {{term}} | {{def}} | {{near-but-different}} |

---

## 调研来源

本 skill 基于 0 条来源生成，一手 / 二手比例 {{a}}:{{b}}。详见 `references/research/`。

主要 primary sources（按权重）：
1. {{source}} — {{type}}
2. ...

---

## Changelog

| Version | Date | What changed |
|---------|------|-------------|
| 0.3 | 2026-05-02 | Initial generation, {{source_count}} sources |

更新本 skill：`update 大师 llm-agent-infra`，会按 master-skill 的 Phase 0C 路径增量刷新。

---

## 致谢

本 skill 由 [大师.skill](https://github.com/voidborne-d/master-skill) 自动生成。
> 蒸馏一个细分行业，让 agent 立刻进入「这行的资深人」模式。

底层方法论参考：
- [同事.skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill) — 蒸馏个体的元 skill 引擎
- [女娲.skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill) — 蒸馏思维框架（master-skill Phase 3 可调它生成 top 3 figures sub-skill）

---

## Synthesized Content

See `references/synthesis.md` for the full Phase 2 output. Counts:
- Mental models: 5
- Playbook rules: 7
- Agentic Protocol dimensions: 5
