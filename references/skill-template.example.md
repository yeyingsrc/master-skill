# Example: `llm-agent-infra-master` (partial)

A **fragmentary** populated example of `skill-template.md` for the prototype industry "LLM agent infra". Not a full skill — covers frontmatter + Agentic Protocol (2 dims) + 1 mental model + 1 playbook rule. Used to stress-test the template structure during master-skill v0.x development.

To regenerate this example after the master-skill workflow goes end-to-end, delete this file and run the actual Phase 0-5 against "LLM agent infra".

---

```markdown
---
name: llm-agent-infra-master
description: |
  LLM Agent Infrastructure Master OS — automated mastery of the agent-framework / orchestration / runtime tooling space: top builders' mental models, current tool stack (frameworks / runtimes / observability / eval harnesses), workflows for building reliable agents, jargon, and where to keep up.
  Trigger this skill when the user works on agent framework problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「写 agent」「agent framework 选哪个」「LangGraph vs CrewAI」「agent 上线」「multi-agent orchestration」「agent observability」
industry: "LLM agent infrastructure"
industry-cn: "LLM agent 基础设施"
locale: "global"
last_research_date: "2026-05-01"
source_count: 0
profile: "practitioner"
generator: "master-skill v0.1"
---

# LLM Agent 基础设施 · Master OS

> 「The bitter lesson is that frameworks lose to model capability. Pick a framework that can be ripped out in a weekend.」 — paraphrased from Harrison Chase, 2025.

## 激活规则

收到与 LLM agent infrastructure 相关的问题时（关键词：agent framework / orchestration / multi-agent / tool use / agent runtime / agent eval），先按下方 Agentic Protocol 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 agent infra 无关 — 不激活。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：LLM agent infra 不靠训练语料硬答 — 这个领域 6 个月就大变样。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体框架版本 / 公司选型 / benchmark 数字 / 价格 / API 行为 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 |
| **混合** | 用具体框架讨论抽象架构问题 | → 先取事实，再用框架分析 |

### Step 2: LLM agent infra 式研究维度

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）。

#### 维度 1: Framework 当前态
- 看什么：当前 GitHub stars / 最近 30 天 commit 频率 / breaking change 历史
- 在哪看：GitHub 仓库本身（不是排行榜聚合站）；`langchain-ai/langgraph`、`microsoft/autogen`、`crewAIInc/crewAI`、`pydantic/pydantic-ai` 的 releases
- 输出：each candidate 的「活跃度 / 稳定度」二维标记

#### 维度 2: 真实生产案例
- 看什么：有没有公司在用这个框架跑生产，规模如何，遇到什么 pain point
- 在哪看：a) 框架官方的 case studies — 但要打折扣（自营销）；b) Twitter/X 上工程师吐槽（搜「framework + production」+「sucks/painful/broken」）；c) Hacker News 评论（搜框架名）
- 输出：production-ready 等级（toy / pilot / scaled）

[Phase 2.9 还会推出 3-6 个其他维度，本示例不展开]

### Step 3: LLM agent infra 式回答

基于 Step 2 的事实 + 心智模型回答。注意：不要隐瞒「这个领域的标准答案 6 个月前是 X，现在是 Y」。版本敏感性是这个领域的核心特征。

---

## 心智模型（1 个示例 — 实际 skill 应有 3-7 个）

### 1. 框架是临时的，能力是永恒的

**一句话**：你今天选的 agent framework 6 个月后大概率不再合适，因为模型能力升级会让上层抽象失效。

**它说的是**：很多 agent framework 存在的理由是「弥补模型能力不足」（例如 manually 编排 retry / chain-of-thought / 工具调用 fallback）。当模型本身把这些能力 native 化后，framework 的价值反而成为障碍。这跟 Sutton 的 "Bitter Lesson" 一脉相承 — 不要把临时性的脚手架硬编码进系统。

**证据来源**：
- [Primary] Harrison Chase 在 2025 LangChain Interrupt 主题演讲：「我们 LangChain 团队自己已经从 chains 全面转向 graphs，因为 chain 这个抽象本身随着模型能力增强失效了」
- [Primary] Anthropic 的 Tool Use 文档迭代史：从 "function calling beta" 到 "extended thinking" 到 "computer use"，每次都把 framework 层的能力下沉到模型本身
- [Secondary] Hacker News 反复出现的 thread：「framework rotation cost」估算

**应用方式**：
- 选 framework 的标准之一：「我能在一个周末把这层框架剥掉换成原生 SDK 调用吗？」如果不能，太重了
- 不要把框架特定的概念（chain / agent / executor）作为系统的核心抽象 — 它们是脚手架不是承重墙

**局限**：
- 对 multi-agent orchestration 这一层不那么适用 — 多 agent 协作的 routing / state management / human-in-the-loop 短期内不会被模型 native 化
- 在 2025-2026 的快速变化期适用，模型能力曲线趋平后这个模型会失效

---

## 标准 Playbook（1 条示例 — 实际 skill 应有 5-10 条）

1. **如果选 agent framework 是为「快速 ship 一个 demo」**，则用 LangGraph 或 PydanticAI 一类 graph-first / type-first 的薄框架，不用 CrewAI / AutoGen 一类提供完整 multi-agent 抽象的厚框架。
   - 案例：Vercel 在 v0 chat 上用 ai-sdk 直接调原生 tool calling，没用 LangChain — 6 个月后他们的工程师在 podcast 里说这是省下技术债最关键的决策
   - 案例：某 YC W25 公司一开始用 CrewAI 上线，3 个月后因为 framework breaking change + production debug 困难，rewrite 到原生 SDK

---

[此处省略：工具栈、工作流、表达 DNA、质量基准、智识谱系、诚实边界、6 个知识模块、调研来源、changelog、致谢]
```

---

## Findings — 模板结构问题（v0.1 dry run）

测试方法：手动用 LLM agent infra 知识填充 frontmatter + Agentic Protocol Step 2 头 2 维 + 1 个心智模型 + 1 条 playbook 规则。

### Pass

- frontmatter 字段够用，`industry-cn` / `industry` 双语字段对中英混用很必要
- Agentic Protocol 的「维度 → 看什么 / 在哪看 / 输出」三段结构能强制具体化，避免「搜索相关信息」这种空话
- 心智模型卡片的「证据 / 应用 / 局限」三段是关键 — 没有「局限」段就会变成口号
- 「证据来源」用 `[Primary]` / `[Secondary]` 标记一手 / 二手，简洁有效

### Issues found

1. **缺 `triggers` 字段的机器可读形式** — 现在触发词只在 description 里，agent 路由判断时不好提取。建议 frontmatter 加一个 `triggers: ["agent framework", "agent runtime", ...]` 列表。
2. **「最近 12 个月动态」** 在 figures 表的 cadence 不明确 — 是更新 skill 时刷新这一列？还是初版就要写？需要在 SKILL.md 的 Phase 0C（更新路径）里说明。
3. **Agentic Protocol 维度数量** 现在是「5-8 个」— 但对一个简单细分（如「短视频投流」）5 个可能就饱和了，对一个复杂细分（如「LLM agent infra」）可能要 10+。改成「3-10，按领域复杂度」更准。
4. **缺 sub-skills 段的引用规则** — 现在只说「调用方式：在对话中提『按 X 视角看这个问题』」，但 host 不一定支持 sub-skill 自动发现。要补充：sub-skills 需手动 install，路径示意。
5. **「调研来源」段** 没规定格式。需要明确：每条至少含 `(URL, title, type[primary|secondary], collected_date)`。

### Action items for next iteration

- [ ] 修 SKILL.md：Agentic Protocol 维度数改为「3-10，按领域复杂度」
- [ ] 修 SKILL.md：Phase 0C 增加 figures 「最近动态」列的更新规则
- [ ] 修模板 frontmatter：加 `triggers` 列表字段
- [ ] 修模板「调研来源」段：明确每条引用格式
- [ ] 修模板「sub-skills」段：增加 install 路径说明
- [ ] 写 `references/extraction-framework.md`（v0.2 next item）
