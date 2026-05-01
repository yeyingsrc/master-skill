<div align="center">

# 大师.skill

### *你不再需要学习和寻找任何 skill。*
### *只需要大师.skill — 任何行业，它都为你蒸馏出一套最先进、最适合你的 skill。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/voidborne-d/master-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/voidborne-d/master-skill)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://github.com/voidborne-d/master-skill)
[![Status](https://img.shields.io/badge/status-v0.1--draft-orange)]()

[**English**](#english) · 中文

</div>

---

## 一句话

[同事.skill](https://github.com/titanwings/colleague-skill) 把**一个人**蒸馏成 skill。
[女娲.skill](https://github.com/alchaincyf/nuwa-skill) 把**任何人**的思维方式蒸馏成 skill。
**大师.skill** 把**一整个行业的认知操作系统**蒸馏成 skill。

每一层都是 10 倍跃迁：一个你认识的人 → 任何活着或死去的人 → 一整个领域的人类知识。

> **你不再需要去 awesome-skills 列表里挑。不需要去 Reddit 问哪个 framework 选型。不需要订阅 12 个 newsletter 怕错过行业动态。
> 告诉大师.skill 你做哪一行，它把这一行的资深人脑子里的东西，浓缩成一个你能装载的 skill。**

---

## 效果示例

> 这不是搜索引擎。这是「这一行的资深人此刻在你旁边」。

#### 场景 1 · LLM agent 基础设施

```
你    ❯ 该不该把这个 RAG 系统迁到 Vespa？

大师  ❯ 这是一个「framework 临时性 vs 基建沉降」的判断。

       先看 retrieval 阶段的瓶颈到底在 Vespa 解决，还是
       在 embedding 模型本身。如果是后者，迁移就是把
       脚手架换成混凝土 — 6 个月模型迭代会让你又想换。

       如果真的卡在 retrieval：Vespa 比 Pinecone 多了
       hybrid search 原生支持，但你的运维栈是不是已经
       吃下了它的 ZooKeeper / Tensor 复杂度？这一行的
       资深判断 — Filtering speed × Index size × Team
       Op overhead 三选二，你的瓶颈在哪边？

       Production case：[3-4 个真实迁移案例摘要 + 链接]
```

#### 场景 2 · 跨境电商运营

```
你    ❯ 亚马逊德国站要上一个新品类，从哪儿开始？

大师  ❯ 德国站有三件事跟美国站完全不同 — 你必须先回答：

       1) VAT 一站式申报你走 OSS 还是各国注册？
          这决定了你能不能用 Pan-EU FBA。
       2) 包装法 (VerpackG) 和 WEEE/电池法注册了吗？
          没注册 listing 第一天就会被举报下架。
       3) GS 认证 vs CE — 你品类是不是 GS 强制？
          这决定能不能上 Idealo / 比价导购流量池。

       这三个不是合规 checklist — 是你「能不能开卖」的硬门槛。
       搞定后，关键词调研用 Helium 10 的德语包，不要从
       美国词库直翻 — 德国搜索习惯长尾密度高得多。
```

#### 场景 3 · 短视频投流

```
你    ❯ 投流 ROAS 总是上不去，是不是出价策略有问题？

大师  ❯ 出价是后果，不是原因。先回答创意层：

       你的素材在 cold audience 上的 3s 完播率是多少？
       低于 35% 时调出价没用 — 巨量引擎的探索预算
       不会给你跑出量。

       创意没问题再看人群定向。这一行的资深判断 —
       「优质素材 × 合理定向 × 出价」，三角顺序错了，
       后两个调出花。你近 7 天创意素材曲线给我看一眼。
```

**这不是把行业百科塞进 prompt。** 大师.skill 蒸馏的是**这一行的资深人怎么想**：

| 层 | 说明 |
|---|---|
| **怎么判断** | 心智模型 — 这一行的资深人看问题的镜片 |
| **怎么决策** | 标准 playbook — 「如果 X，则 Y」的快速规则 |
| **用什么工具** | 工具栈 + 选型决策树 |
| **怎么干活** | 工作流 / SOP，标注「2026-04 起这一步换成 Y」的时效 |
| **怎么沟通** | 行业表达 DNA — 黑话 / register / 外行破绽 |
| **不做什么** | 反模式 — 外行才会犯的错 |
| **知道局限** | 诚实边界 — 信息截止时间，衰减最快的模块 |

每个 skill 还自带 **Agentic Protocol** — 拿到行业新问题时，先按这一行人的研究维度去搜事实，再用上面这套 OS 输出判断。**不是说得像，是做得像**。

---

## 安装

```bash
# Claude Code
git clone https://github.com/voidborne-d/master-skill.git ~/.claude/skills/master-skill
```

```bash
# OpenClaw / Codex / Hermes — clone 到对应 skills 目录即可
```

---

## 用法

```
> 造大师 LLM agent infra
> 做个跨境电商运营的 master skill
> 我做的是足踝外科，给我蒸一个

> update 大师 LLM-agent-infra    # 6 个月后增量刷新
```

大师.skill 会跟你确认 6 件事（行业 / 子方向 / 地域 / 你的角色 / 有没有一手素材 / 是新建还是更新），然后启动 6 路并行调研：行业大佬 / 工具地图 / 工作流 / 知识正典 / 信息源 / 术语标准。30-60 分钟后你会拿到一个 `{industry}-master.skill` 目录，装到任意 Claude Code / OpenClaw / Codex / Hermes agent，立即让它进入「这一行的资深人」模式。

---

## 工作原理

5 phase + 3 质量关卡，全程可被拦截：

```
Phase 0   行业澄清          ← 用户给坏粒度时主动收窄
Phase 0.5 创建目录          ← 自包含，所有产物都在 skill 内部
Phase 1   六轨并行调研      ← Agent swarm，每轨独立 subagent
Phase 1.5 调研 review 关卡  ← 用户确认调研质量再继续
Phase 2   框架提炼          ← 三重验证挡住行业八股
Phase 2.5 提炼 review 关卡  ← 用户确认 OS 框架再生成
Phase 3   skill 写出        ← 调用 skill_writer 生成完整目录
Phase 4   三测验证          ← 已知 / 边界 / 风格盲测
Phase 5   双 agent 精炼     ← 优化 skill 的「激活即执行」程度
```

详情看 [SKILL.md](SKILL.md) — 524 行 agent 可加载的工作流规约。
方法论看 [references/extraction-framework.md](references/extraction-framework.md) — 三重验证、工具栈三层提炼、流派分歧处理、衰减速度表。

---

## 路线图

| 版本 | 内容 | 状态 |
|------|------|------|
| v0.1 | SKILL.md + README + ROADMAP | ✅ |
| v0.2 | 模板 + prompts (intake / research × 6 / synthesis / quality-check) | 🔨 进行中 |
| v0.3 | 工具：merge_research / quality_check / yt-dlp 字幕管线 / skill_writer / 各宿主 installers | 🔲 |
| v0.4 | 跨 skill 调用：调用女娲.skill 蒸 top 3 figures 当 sub-skill | 🔲 |
| v0.5 | 增量刷新：`update 大师 X` 按衰减表只刷工具/工作流 | 🔲 |
| v1.0 | repo 公开 + ≥ 3 个真实行业 sample skill 开源 | 🔲 |

详细看 [ROADMAP.md](ROADMAP.md)。

---

## 致谢与谱系

大师.skill 站在两个前作的肩膀上：

- **[同事.skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — 证明「蒸馏一个人」是可行的。提供了 intake → multi-source collect → analyze → write 的元 skill 模式。
- **[女娲.skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — 证明「蒸馏思维方式」比「蒸馏话语」更有价值。提供了 6-agent 并行 swarm + 三重质量关卡 + Agentic Protocol。**大师.skill 在 Phase 3 调用女娲.skill 蒸馏 top 3 figures，作为生成 skill 的 sub-skill**。

三者同源，逐层放大：

```
同事.skill         蒸馏一个具体的人        范围: 1 人
女娲.skill         蒸馏一种思维方式        范围: 任何活人 / 历史人物
大师.skill         蒸馏一个行业的 OS       范围: 一整个细分领域
```

---

## License

MIT

---

<div align="center">

<a name="english"></a>

# 大师.skill (English)

### *Stop hunting for the right skill.*
### *Tell us your industry — we hand you the only skill you'll need.*

</div>

[colleague-skill](https://github.com/titanwings/colleague-skill) distilled **a person** into a skill.
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) distilled **anyone's mind** into a skill.
**master-skill** distills **an entire industry's operating system** into a skill.

Each is a 10× leap — one person you know → anyone alive or dead → an entire field of human knowledge.

Tell master-skill which sub-niche you work in. 30-60 minutes later you get an installable `{industry}-master` skill that loads into any Claude Code / OpenClaw / Codex / Hermes agent and turns it into "the senior practitioner sitting next to you."

Not a Wikipedia stuffed into a prompt. **The mental models, decision heuristics, tool selection trees, current workflows, jargon, anti-patterns, and honest boundaries** of that industry — distilled from public material + your local files into a runnable cognitive OS. Every generated skill ships with an **Agentic Protocol** — when faced with a new problem in this field, the agent researches it the way a senior practitioner would, then applies the OS to deliver judgment. **Not just sounding like a pro. Acting like one.**

```
> master-skill: LLM agent infrastructure
> master-skill: cross-border e-commerce operations
> master-skill: foot-and-ankle surgery
```

See above (Chinese) for full demos and architecture. Roadmap to v1.0 in [ROADMAP.md](ROADMAP.md).
