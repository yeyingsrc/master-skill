---
name: xiaohongshu-ops-master
description: |
  小红书运营 (xiaohongshu operations) Master OS — automated mastery of xiaohongshu operations: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on xiaohongshu operations problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「小红书」「种草」「薯条」「信息流」「笔记」
triggers:
  - "小红书"
  - "种草"
  - "薯条"
  - "信息流"
  - "笔记"
  - "笔记测评"
industry: "xiaohongshu operations"
industry-cn: "小红书运营"
locale: "zh-CN"
last_research_date: "2026-05-02"
source_count: 25
profile: "practitioner"
generator: "master-skill v1.3"
---

# 小红书运营 · Master OS

> 装上这个 skill, agent 立刻进入「小红书运营」资深人模式 — 用这一行的心智模型 + 决策规则 + 工作流 + 说话方式 给判断。

## 激活规则

收到与 小红书运营 相关的问题时（关键词：小红书, 种草, 薯条, 信息流, 笔记, 笔记测评），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 小红书运营 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：小红书运营 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 内容差距评估
- 看什么: 当前账号 / 笔记跟头部对标差距在哪 — 选题 / 封面 / 文案 / 视频质感
- 在哪看: 千瓜 / 蝉小红 / 灰豚的对标账号分析
- 输出: 差距 score (1-10) + 1 句最大瓶颈

#### 维度 2: 流量池判断
- 看什么: 笔记当前在哪个流量层 — 初始流量池 / 中等流量池 / 大流量池
- 在哪看: 笔记后台数据 + 实时刷新次数
- 输出: 当前层级 + 突破到下一层的关键动作

#### 维度 3: 投流性价比
- 看什么: 类目当前 CPC / CPM, 自家笔记达标率
- 在哪看: 信息流后台 + 行业 benchmark (蝉小红等)
- 输出: ROI 区间 + 是否值得投

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 内容是种草, 不是销售

**一句话**: 小红书的内容逻辑是「让用户自己想买」, 不是「告诉用户来买」。硬广直发必死。

**它说的是**: 平台算法 + 用户心智都偏向「真实分享 / 测评 / 经验」, 不接受「品牌官方说我好」。一切爆文必须**伪素人化**, 至少有真实使用场景 / 真人感。

**证据来源**:
- [Primary] 多家头部 MCN 创始人长访谈 2024-2025
- [Primary] 小红书官方算法解读公告
- [Reference] 平台内容生态白皮书

**应用方式**:
- 品牌账号也要按素人逻辑写 — 有日常 / 有情绪 / 有场景
- 商单 / 报备笔记必须先把内容写好, 再藏品牌信息

**局限**:
- 美妆 / 服饰 / 母婴 类目种草逻辑最强
- 工具类 / B2B 类目转化路径不一样

### 1.2 数据反馈驱动迭代

**一句话**: 小红书运营是**测试驱动的**, 不是经验驱动的 — 每篇笔记都是 A/B 测试。

**它说的是**: 单条爆文不重要, 重要的是建立「测试 → 数据 → 优化」的循环。点击率 < 8% 的笔记直接放弃, 不要硬撑流量。

**证据来源**:
- [Primary] 头部 MCN 内部数据复盘
- [Primary] 千瓜 / 灰豚等数据工具方法论

**应用方式**:
- 前 20 篇笔记按矩阵投放, 不押单点
- 数据异常笔记 (突然爆) 立刻分析爆点 + 复刻

**局限**:
- 适合做矩阵账号; 单 IP 路径不太用得上

### 1.3 信息流投放 ≠ 自然流推荐

**一句话**: 小红书的薯条 / 信息流投流, 跟自然流量是两套逻辑, 笔记表现也不同。

**它说的是**: 自然流爆的笔记不一定能投流跑出量; 反过来投流跑量的笔记自然流可能死。两个流量池要分开养。

**证据来源**:
- [Primary] 信息流投放案例长篇拆解
- [Primary] 千瓜 / 蝉小红等工具数据

**应用方式**:
- 笔记上线后先看 24 小时自然流, 表现不好再决定投流
- 投流的笔记和自然流的笔记内容要分开写

**局限**:
- 中小品牌可能没预算两套都做, 先押自然流再投流

---



## 标准 Playbook

1. **如果发笔记**, 则封面图必须 3 秒内传达核心卖点, 否则点击率必死。
   - 案例: 头部账号封面 A/B 测试数据反复证明

2. **如果点击率 < 8%**, 则放弃这条笔记, 不要硬投流救。
   - 案例: 千瓜 benchmark 数据

3. **如果做品牌号**, 则必须养至少 3-5 个账号矩阵, 单点风险太大。
   - 案例: 头部 MCN 标准做法

4. **如果发商单**, 则必须先做内容质量, 再谈品牌信息植入比例。
   - 案例: 平台对纯硬广限流案例

5. **如果数据突然爆**, 则立刻分析爆点并在 48 小时内复刻 2-3 条同主题笔记。
   - 案例: 多家品牌爆款复刻 SOP

---



## 工具栈与选型决策树

详见 `references/research/02-tools.md`. 三层结构:
- **必备**: 千瓜 / 灰豚 / 小红书蒲公英 (官方报备平台)
- **场景特化**: 蝉小红 (投流) / 新红 (热点)
- **新兴**: AI 笔记生成器 (谨慎用)



## 工作流 / Pipeline

详见 `references/research/03-workflows.md`. 2 个 workflows:
- 品牌新号冷启动 (high decay — 平台规则每年改)
- 商单笔记生产 (medium decay)

---



## 表达 DNA

**高频黑话**: 笔记 / 薯条 / 蒲公英 / 信息流 / 报备 / 私信 / 收藏率 / 完读率 / IPpip / 矩阵号 / 品牌专业号 / KOC / KOL / 站内 / 站外 / 抢流量

**严肃 register**: 数据导向 / 强调真实分享 / 对硬广敏感 / 对刷量保持距离

**外行破绽**: 把 "笔记" 叫 "帖子" / 不知道蒲公英是报备平台 / 把投流叫 "投广告"

---



## 质量基准 + 反模式

### 什么算「好」:

1. 笔记互动率 ≥ 类目平均 1.5 倍
2. 收藏率 > 点赞率 (说明内容有用)
3. 矩阵号 30 天内能产出 2-3 篇爆文 (≥ 1k 互动)

### 反模式:

1. 不报备发商单 (限流风险)
2. 单点账号押宝, 不做矩阵
3. 数据差还硬投流救
4. 内容硬广不做种草化

---



## 智识谱系

略 (mini scope).

---



## 诚实边界

1. 信息截止 2026-05. 平台规则 / 投流策略每 3-6 月需 update.
2. 平台政策变化极快 (商业内容 / 黑科技限制 / KOC 标准都在动).
3. 本 prototype 是 mini scope, 仅验证 zh-CN 内容运营行业的 CLI 生成.

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-02 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-02 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-02 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-02 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-02 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-02 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-02 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-02 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-02 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
