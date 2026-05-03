<div align="center">

# 🎓 大师.skill

> *「下一步，不只蒸馏一个人，蒸馏一整个行业。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

[同事.skill](https://github.com/titanwings/colleague-skill) 把**一个人**蒸馏成 AI。<br>
[女娲.skill](https://github.com/alchaincyf/nuwa-skill) 把**任何人的思维方式**蒸馏成 AI。<br>

但有些东西比一个人更大——<br>
**一整个行业的资深判断、工作流、工具栈。**

<br>

大师.skill 不蒸馏单个人，<br>
它蒸馏**整个行业的认知操作系统**。

<br>

告诉它你做哪个细分行业，<br>
30-60 分钟自动跑完调研、蒸馏、生成 skill 加上一套 bash 命令套件。<br>

装到任何 AI agent，从那一刻起，<br>
**它就是这一行最资深的人。**

<br>

> **有了大师.skill，你不再需要安装其他 skill ——**<br>
> **它会为你的行业，自动蒸馏出最适合的那一个。**

<br>

[🚀 安装](#-安装) · [✨ 效果示例](#-效果示例) · [🛠️ 自动蒸馏 bash 工具](#️-自动蒸馏出-bash-命令套件) · [🧬 三代谱系](#-三代谱系) · [⭐ 已蒸馏的行业](#-已蒸馏的行业)

[**English README →**](README_en.md)

</div>

---

> 📢 &nbsp;**2026.05.02 发布** — 生成的 skill 不只能对话，还自带一套 bash 命令工具帮你执行。[Release notes →](https://github.com/voidborne-d/master-skill/releases/tag/v1.1)
>
> 🔥 &nbsp;**2026.05.02 公开** — 第一个完整行业（LLM agent 基础设施）端到端跑通验证。

---

## ✨ 效果示例

> 这不是搜索引擎。这是「这一行的资深人此刻在你旁边」。

#### 🤖 场景 1 · LLM agent 基础设施

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

#### 🛒 场景 2 · 跨境电商运营

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

#### 🎬 场景 3 · 短视频投流

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

**不是把行业百科塞进 prompt**，是用**这一行的心智模型 + 决策规则**给你判断。

每个 skill 都自带一套「研究协议」(Agentic Protocol) — 拿到一个行业新问题，它先按这行资深人的研究维度去搜事实，再用心智模型输出判断。**不是说得像，是做得像。**

---

## 🛠️ 自动蒸馏出 bash 命令套件

> 这是大师.skill 跟同事 / 女娲最大的区别 — 蒸馏出来的不只是「会说」，还是「会做」。

每个生成的 skill **都自动配一个 `cli/` 子目录** —— 把这个行业的认知操作系统直接物化成可执行的命令行工具：

```
{industry}-master/
└── cli/
    ├── protocol/agentic.sh         # 拿到新问题 → 按几个研究维度做功课 → 出报告
    ├── decision/{主题}.sh           # 决策树（按主题聚类的几条决策规则）
    └── workflow/{流程}.sh           # 走查工作流 + 失败模式自检
```

每个脚本都支持四个标准开关：`--help`（帮助）/ `--explain`（解释背后的心智模型）/ `--dry-run`（试跑）/ `--json`（机器可读输出）。

```bash
# 拿到新问题：「该不该把 RAG 系统迁到 Vespa」
$ ./cli/protocol/agentic.sh
# → 引导你按 5 个研究维度收集信息 → 生成报告

# 选型决策
$ ./cli/decision/framework-select.sh

# 走完一个完整工作流 + 失败模式自检
$ ./cli/workflow/build-rag-agent.sh

# 解释背后的心智模型（不交互，直接打印）
$ ./cli/decision/framework-select.sh --explain
```

**纯 bash + 系统命令，零外部依赖**（不需要 jq、不需要 Python）。由 [`tools/cli_writer.py`](tools/cli_writer.py) 自动从蒸馏结果生成 —— 你不用写一行代码，工具是从行业的工作流和决策规则里**直接长出来的**。

设计细节看 [`references/cli-spec.md`](references/cli-spec.md)。

---

## 🌐 自动调女娲，蒸馏行业 top 人物

> 大师不重新发明轮子。蒸馏行业 top 人物的活儿，自动外包给女娲.skill 做，结果直接嵌进 `sub-skills/`。

```
{industry}-master/
├── SKILL.md
└── sub-skills/                       ← 女娲蒸馏的人物 sub-skill
    ├── {人物-1}/SKILL.md             ← 比如 Karpathy
    ├── {人物-2}/SKILL.md             ← 比如 Hamel Husain
    └── {人物-3}/SKILL.md             ← 比如 Eugene Yan
```

大师同时启动 3 个子 agent，每个走完女娲.skill 完整流程，蒸馏出一个人物 sub-skill。

之后用户问到某位人物的视角时，agent 自动加载对应 sub-skill — 不用重跑大师。

详见 [SKILL.md Phase 3.3-3.5](SKILL.md) + [`prompts/sub-skill-figures.md`](prompts/sub-skill-figures.md)。

---

## 📦 它蒸馏了什么

行业的认知操作系统，不是行业的百科全书。一个 skill 装下四件事：

- 🧠 &nbsp;**资深人怎么想** — 心智模型 + 决策规则
- ⚙️ &nbsp;**工作流怎么走** — 当前最先进的 SOP，每一步标注衰减时点
- 🛠️ &nbsp;**工具怎么选** — 选型决策树 + 避坑清单 + **自动生成的 bash 命令套件**
- 💬 &nbsp;**黑话怎么讲** — 行业表达方式 + 外行破绽

具体提取的 7 层：

| 层 | 说明 |
|---|---|
| **怎么判断** | 心智模型 — 这行的资深人看问题用的镜片 |
| **怎么决策** | 标准决策规则 — 「如果 X，则 Y」的快速判断 |
| **用什么工具** | 工具栈 + 选型决策树 + 避坑清单 |
| **怎么干活** | 工作流，每一步标注「2026-04 起这一步换成 Y」的时效 |
| **怎么沟通** | 行业表达方式 — 黑话、说话节奏、外行破绽 |
| **不做什么** | 反模式 — 外行才会犯的错 |
| **知道局限** | 诚实边界 — 信息截止时间，哪些模块衰减最快 |

### 诚实边界

每个 skill 都明确标注它做不到什么：

- 工具和工作流的模块**衰减最快**，建议每 3-6 个月刷新一次
- 法规和标准的模块**衰减更快**，12 个月内一定要更新
- 大师不能替代真实的实战经验 — 给的是认知框架，不是事故处理手册

**一个不告诉你局限在哪的 skill，不值得信任。**

---

## ⚡ 安装

```bash
# Claude Code
git clone https://github.com/voidborne-d/master-skill.git ~/.claude/skills/master-skill
```

<details>
<summary><b>🛠️ 其他 host 安装路径</b></summary>

<br>

```bash
git clone https://github.com/voidborne-d/master-skill.git <TARGET>
```

| Host | `<TARGET>` 路径 |
|------|-----------------|
| 🟣 Claude Code | `~/.claude/skills/master-skill` |
| 🔵 OpenClaw | `~/.openclaw/skills/master-skill` |
| ⚫ Codex | `~/.codex/skills/master-skill` |
| 🟠 Hermes | clone 后 `python3 tools/install.py install --host hermes` |

一键装到所有宿主：`python3 tools/install.py install --host all`

</details>

---

## 🚀 用法

在装好大师.skill 的 agent 里，直接说：

```
> 造大师 LLM agent 基础设施
> 做个跨境电商运营的大师 skill
> 我做的是足踝外科，给我蒸一个

> update 大师 LLM-agent-infra      # 6 个月后增量刷新
```

大师跟你确认 6 件事（行业、子方向、地域、你的角色、有没有一手素材、是新建还是更新），然后启动**六路并行调研**：行业大佬 / 工具地图 / 工作流 / 知识正典 / 信息源 / 术语标准。

30-60 分钟后你拿到一个 `{行业}-master` 目录。装到任意 agent，立刻进入「这一行的资深人」模式。

### 🎛️ 调用生成出来的 skill

```
> 用 llm-agent-infra-master 帮我评估这个框架选型
> 用 跨境电商-master 看一下我这个亚马逊 listing
> 让 llm-agent-infra-master 跑 framework-select 决策树
```

### 💻 命令行直接跑

```bash
# 5 步端到端流程
python3 tools/research/merge_research.py merge --skill-dir ./prototype/   # 调研评审
python3 tools/skill_writer.py create --skill-dir ./output ...             # 生成 skill
python3 tools/research/quality_check.py check --skill-dir ./output        # 质量检查
python3 tools/install.py install --host claude --source ./output          # 安装到宿主

# 增量刷新（v1.1）
python3 tools/update_skill.py plan --skill-dir <已有的 skill>           # 1. 看哪些模块该刷
python3 tools/update_skill.py archive --skill-dir <skill>               # 2. 归档旧调研
python3 tools/update_skill.py mark-in-progress --tracks tools,workflows # 3. 标记开始更新
# (agent 重跑选定的几路调研)
python3 tools/update_skill.py finalize --skill-dir <skill>              # 4. 完成 + 写 changelog
```

---

## ⭐ 已蒸馏的行业

每个都是端到端跑过的样本，包含完整调研数据 + 生成的 SKILL.md + 一套可跑的 bash 工具：

| 行业 | 类别 | 语言 | 路径 |
|------|------|------|------|
| 🔥 **LLM agent 基础设施** | 技术 | 英文 | [llm-agent-infra-master/](prototypes/llm-agent-infra-master/) |
| ✅ **跨境电商运营** | 商业 | 中文 | [cross-border-ecommerce-master/](prototypes/cross-border-ecommerce-master/) |
| ✅ **小红书运营** | 内容运营 | 中文 | [xiaohongshu-ops-master/](prototypes/xiaohongshu-ops-master/) |
| ✅ **短视频投流** | 商业 + 算法 | 中文 | [short-video-ads-master/](prototypes/short-video-ads-master/) |
| ✅ **SEO 专家** | 半技术 | 中文 | [seo-master/](prototypes/seo-master/) |
| ✅ **恋爱高手** | 软技能 | 中文 | [love-coach-master/](prototypes/love-coach-master/) |
| ✅ **足踝外科** | 医疗（强监管） | 中文 | [foot-ankle-surgery-master/](prototypes/foot-ankle-surgery-master/) |
| ✅ **法律执业**（中国法） | 法律（强监管） | 中文 | [china-law-master/](prototypes/china-law-master/) |

8 个行业横切技术、商业、内容运营、软技能、医疗、法律 — 大师.skill 框架对各类行业都跑得通。

调研过程**完全透明**。每个样本都附完整的六路调研笔记 + 蒸馏文档，可以追溯每条心智模型、每条决策规则是从哪几个来源出来的。

想蒸馏不在列表里的行业？装大师.skill，说「造大师 XXX」就行。

---

## 🔬 工作原理

输入一个细分行业，大师.skill 做这几件事：

```
1. 行业澄清          ← 粒度太粗主动收窄（拒绝「AI」，引导到「LLM agent 基础设施」）
2. 创建目录          ← 所有产物都在 skill 自己的目录内，自包含
3. 六路并行调研      ← 6 个子 agent：行业大佬 / 工具 / 工作流 / 知识正典 / 信息源 / 术语
   ─ 调研评审关卡    ← 你确认调研质量再继续，不让垃圾输入污染下游
4. 框架蒸馏          ← 三重验证（跨场景 / 生成力 / 排他性）挡住行业八股
   ─ 蒸馏评审关卡    ← 你确认认知框架再生成
5. 写出 skill        ← 自动生成完整目录、调女娲蒸人物 sub-skill、emit bash 工具
6. 三测验证          ← 已知问题 / 边界问题 / 风格盲测
7. 双 agent 精炼     ← 优化 skill 的「激活即执行」程度
```

详见 [SKILL.md](SKILL.md) — 524 行的 agent 可加载工作流。方法论看 [references/extraction-framework.md](references/extraction-framework.md) — 三重验证、工具栈三层提炼、流派分歧处理、衰减速度表。

---

## 🧬 三代谱系

大师.skill 站在两个前作的肩膀上：

- **[同事.skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — 提供了「了解 → 多源采集 → 分析 → 写出」的元 skill 框架。
- **[女娲.skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — 提供了 6 个 agent 并行调研 + 三重质量关卡。**大师.skill 在 Phase 3 直接调女娲，蒸出行业最重要的 3 个人作为 sub-skill。**

三者同源，逐层放大。

---

## 📂 项目结构

```
master-skill/
├── SKILL.md                          # 大师本体（核心工作流规约）
├── prompts/                          # 提示词系统
│   ├── intake.md                     #   行业澄清
│   ├── research/01-06.md             #   六路调研提示词
│   ├── synthesis.md                  #   蒸馏指引
│   ├── quality_check.md              #   质量检查标准
│   └── sub-skill-figures.md          #   调女娲的子 agent 模板
├── tools/                            # 7 个 Python 工具
│   ├── skill_writer.py               #   生成 skill 目录
│   ├── cli_writer.py                 #   生成 bash 工具子目录（v0.6）
│   ├── update_skill.py               #   增量刷新（v1.1）
│   ├── install.py                    #   四宿主安装器
│   ├── research/merge_research.py    #   调研评审聚合
│   ├── research/quality_check.py     #   自动质量检查
│   └── transcribe/                   #   字幕下载 + 文本处理
├── references/
│   ├── skill-template.md             #   生成产物的标准结构
│   ├── extraction-framework.md       #   蒸馏方法论（想深入看这个）
│   └── cli-spec.md                   #   bash 工具的设计文档
└── prototypes/
    ├── llm-agent-infra-master/       #   完整样本（v1.0）
    └── cross-border-ecommerce-master/  #   中文精简样本（v1.1）
```

---

## ⚠️ 注意

**调研材料的质量 = skill 的质量**。不同维度的来源优先级不同：

| 维度 | 来源优先级（高到低） |
|------|------|
| 🌟 行业大佬 | 本人长篇（书 / 长访谈 / 博客系列）**›** 决策记录（公开发声 / 提交记录）**›** 二手转述 |
| 🛠️ 工具地图 | 官方文档 **›** 工程师生产案例 **›** 培训教程 / SEO 软文 |
| 📋 工作流 | 公司技术博客的真实流程 **›** 资深人长访谈 **›** 培训机构大纲 |
| 📚 知识正典 | 行业人推荐书单（至少 3 个独立来源都点过）**›** 学术综述 **›** 二手书评 |
| 📰 信息源 | 行业人订阅清单 **›** 主流媒体长稿 **›** 内容农场 |

- 中文环境下自动排除知乎、微信公众号、百度百科、CSDN（除非作者原文）
- 信息截止得越早，工具和工作流的模块衰减越快 — 用 `update 大师 X` 增量刷新
- 这是 v1.1，还在快速迭代。发现 bug 请提 issue。

---

## 📄 路线图

| 版本 | 内容 | 状态 |
|------|------|------|
| v0.1-0.4 | 工作流规约 + 提示词 + 工具 + 打磨 | ✅ |
| v1.0 | 完成第一个完整样本（LLM agent 基础设施），仓库公开 | ✅ |
| v0.6 | bash 工具流 — 生成的 skill 自带命令套件 | ✅ |
| v1.1 | 调用别的 skill + 增量刷新 + 中文样本 | ✅ |
| v1.2 | 决策树主题自动学 + 定时刷新 + 5 个行业样本（含小红书 / SEO / 恋爱） | ✅ |
| v1.3 | 短视频投流 / 足踝外科 / 法律 = 8 个行业横切覆盖 | ✅ |
| v2.x | PyPI 打包 / GitHub Action 自动更新 / 多语言文档 | 🔲 |

详见 [ROADMAP.md](ROADMAP.md)。

---

## 📜 许可证

MIT — 随便用，随便改，随便造。

<div align="center">

<br>

**🧬 同事.skill** 蒸馏一个**具体的人**做什么。<br>
**🌟 女娲.skill** 蒸馏**任何人**怎么想。<br>
**🎓 大师.skill** 蒸馏**一整个行业**的认知 + 工作流 + 工具。<br>

<br>

*把一整个行业的资深认知，蒸馏成一个 skill。*

<br>

MIT License © [voidborne-d](https://github.com/voidborne-d) · 中文 README · [English](README_en.md)

</div>

---

## ⭐ Star History

<a href="https://www.star-history.com/?repos=voidborne-d%2Fmaster-skill&type=date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
 </picture>
</a>
