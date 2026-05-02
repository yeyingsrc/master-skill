<div align="center">

# 🎓 大师.skill

### *你不再需要学习和寻找任何 skill。*
### *只需要大师.skill — 任何行业，它都为你蒸馏出一套最先进、最适合你的 skill。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-v1.1-brightgreen)]()
[![Stars](https://img.shields.io/github/stars/voidborne-d/master-skill?style=social)](https://github.com/voidborne-d/master-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://github.com/voidborne-d/master-skill)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/voidborne-d/master-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/voidborne-d/master-skill)

<br>

<table>
<tr><td align="left">

🎯 &nbsp;**换了个行业**，不知道从哪学起？资深人脑子里的隐性知识根本没写在 README 里。<br>
📰 &nbsp;**信息散落在 12 个 newsletter / 30 个 podcast / 5 个 Discord**，想跟上但永远在追？<br>
🤖 &nbsp;**给 AI agent 喂一个行业的全部 PDF**，它依然像个外行 — 因为「百科 ≠ 这行的人怎么想」？

</td></tr>
</table>

### ✨ 大师.skill 一次解决三件事

<br>

不是把行业百科塞进 prompt。是**蒸馏「这一行的资深人此刻在你旁边」的认知操作系统** — 心智模型、决策启发式、工具选型树、当前工作流、行业表达 DNA、反模式、诚实边界。

**告诉它你做哪个细分行业，30-60 分钟后，得到一个可装载的 `{industry}-master.skill`。**

<br>

[🚀 安装](#-安装) · [✨ 效果示例](#-效果示例) · [🛠️ 不只是对话](#️-不只是对话还有工具流-v06) · [🧬 三代谱系](#-三代谱系) · [⭐ 已蒸馏行业](#-已蒸馏的行业-prototypes)

[**English README →**](README_en.md)

[![Star History Chart](https://api.star-history.com/svg?repos=voidborne-d/master-skill&type=Date)](https://star-history.com/#voidborne-d/master-skill&Date)

</div>

---

> 📢 **2026.05.02 — v1.1 ship** · CLI 工具流 + cross-skill composition + 增量刷新.
> 生成 skill 不只是对话顾问, 还自带 bash 命令套件. [Release notes →](https://github.com/voidborne-d/master-skill/releases/tag/v1.1)

> 🔥 **2026.05.02 — v1.0 public** · LLM agent infra prototype 端到端跑通 (Phase 4 PASS — 10 mech / 1 partial / 0 fail), repo 公开.

---

## 🎯 它做什么

[同事.skill](https://github.com/titanwings/colleague-skill) 把**一个人**蒸馏成 skill (一个具体的同事 / 朋友 / 偶像).
[女娲.skill](https://github.com/alchaincyf/nuwa-skill) 把**任何人**的思维方式蒸馏成 skill (乔布斯 / 芒格 / 马斯克 / 张雪峰...).
**大师.skill** 把**一整个行业的认知操作系统**蒸馏成 skill.

每一层都是 **10× 跃迁**:

| | 范围 | 输出 |
|---|---|---|
| 🧬 同事.skill | **一个**具体的人 | 一个能模仿这个人 work / persona 的 skill |
| 🌟 女娲.skill | **任何**活着或死去的人 | 一个能用此人认知框架做判断的 skill |
| 🎓 **大师.skill** | **一整个**细分行业 | 一个让 AI 进入「这行的资深人」模式的 skill |

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

**这不是把行业百科塞进 prompt** — 是用**这一行的 mental model + playbook**给你判断。

每个 skill 还自带 **Agentic Protocol** — 拿到行业新问题时，先按这一行人的研究维度去搜事实，再用上面这套 OS 输出判断。**不是说得像，是做得像。**

---

## 🛠️ 不只是对话，还有工具流 (v0.6+)

> 「大师不只是说怎么干，它还附一套 bash 工具帮你干。」

每个生成的 `{industry}-master.skill` 自带 `cli/` 子树 — 把认知 OS 物化成命令行工具：

```
{industry}-master/
└── cli/
    ├── protocol/agentic.sh        # 拿到新问题 → 按 N 维度做功课 → 出 markdown 报告
    ├── decision/{cluster}.sh      # playbook 规则聚类成的交互决策树
    └── workflow/{slug}.sh         # SOP 走查 + 失败模式自检
```

每个脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 标准接口。一行命令出结构化报告：

```bash
# 拿到新问题：「该不该把 RAG 系统迁到 Vespa」
$ ./cli/protocol/agentic.sh
# → 引导你按 5 个研究维度收集信息 → 生成 agentic-protocol-{date}.md

# Framework 选型决策
$ ./cli/decision/framework-select.sh

# 走完一个完整工作流，自动失败模式自检
$ ./cli/workflow/build-rag-agent.sh

# 看背后的心智模型 / playbook (不交互, 直接打印)
$ ./cli/decision/framework-select.sh --explain
```

纯 bash 4 + POSIX coreutils，**零外部依赖**（没 jq / 没 Python）。由 [`tools/cli_writer.py`](tools/cli_writer.py) 自动从 synthesis 生成。完整 spec 在 [`references/cli-spec.md`](references/cli-spec.md)。

---

## 🌐 跨 skill 组合 (v1.1+)

> 「大师.skill 不重新发明轮子。Phase 3 自动调女娲.skill 蒸馏 top 3 figures，嵌入 sub-skills/。」

```
{industry}-master/
├── SKILL.md
└── sub-skills/                       ← 女娲蒸馏的 person sub-skill
    ├── {figure-1}/SKILL.md           ← 比如 Karpathy
    ├── {figure-2}/SKILL.md           ← 比如 Hamel Husain
    └── {figure-3}/SKILL.md           ← 比如 Eugene Yan
```

主大师 agent spawn 3 个**并行 subagent**，每个走完女娲.skill 完整 5 步流程，蒸馏出 person sub-skill 嵌入。

需要某位 figure 的视角时，agent 自动加载对应 sub-skill — 不用整体重新触发。

详见 [SKILL.md Phase 3.3-3.5](SKILL.md) + [`prompts/sub-skill-figures.md`](prompts/sub-skill-figures.md).

---

## 📦 它蒸馏了什么

行业 OS 不是行业百科。这是大师.skill 提取的 7 层：

| 层 | 说明 |
|---|---|
| **怎么判断** | 心智模型 — 这一行的资深人看问题的镜片 |
| **怎么决策** | 标准 playbook — 「如果 X，则 Y」的快速规则 |
| **用什么工具** | 工具栈 + 选型决策树 |
| **怎么干活** | 工作流 / SOP, 标注「2026-04 起这一步换成 Y」的时效 |
| **怎么沟通** | 行业表达 DNA — 黑话 / register / 外行破绽 |
| **不做什么** | 反模式 — 外行才会犯的错 |
| **知道局限** | 诚实边界 — 信息截止时间, 衰减最快的模块 |

### 诚实边界

每个 skill 都明确标注做不到什么：

- **工具 / 工作流模块**衰减最快 (建议每 3-6 月 update)
- **法规 / 标准节**衰减极高 (12 月内必更新)
- master skill **不能替代真实 production debugging 经验** — 给的是认知框架, 不是 incident response

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

启动大师.skill 的 host 中：

```
> 造大师 LLM agent infra
> 做个跨境电商运营的 master skill
> 我做的是足踝外科, 给我蒸一个

> update 大师 LLM-agent-infra      # 6 个月后增量刷新
```

大师.skill 跟你确认 6 件事 (行业 / 子方向 / 地域 / 你的角色 / 有没有一手素材 / 是新建还是更新), 然后启动 **6 路并行调研**: 行业大佬 / 工具地图 / 工作流 / 知识正典 / 信息源 / 术语标准.

30-60 分钟后你拿到一个 `{industry}-master.skill` 目录, 装到任意 Claude Code / OpenClaw / Codex / Hermes agent, 立即让它进入「这一行的资深人」模式.

### 🎛️ 调用生成的 master skill

```
> 用 LLM-agent-infra-master 帮我评估这个 framework 选型
> 用 跨境电商-master 看一下我这个亚马逊 listing
> @LLM-agent-infra-master --explain framework-select   # 用 CLI 形式调用
```

### 💻 命令行直接跑

```bash
# 5 命令端到端 pipeline
python3 tools/research/merge_research.py merge --skill-dir ./prototype/      # Phase 1.5
python3 tools/skill_writer.py create --skill-dir ./output ...                # Phase 3
python3 tools/research/quality_check.py check --skill-dir ./output           # Phase 4.4
python3 tools/install.py install --host claude --source ./output             # Deploy

# 增量刷新 (v1.1)
python3 tools/update_skill.py plan --skill-dir <existing-skill>
python3 tools/update_skill.py archive --skill-dir <skill> && \
  python3 tools/update_skill.py mark-in-progress --tracks tools,workflows
# (agent 重跑选定 tracks)
python3 tools/update_skill.py finalize --skill-dir <skill>
```

---

## ⭐ 已蒸馏的行业 (Prototypes)

每个 prototype 是端到端跑过一遍的 sample skill, 包含完整调研数据 + 生成的 SKILL.md + 可执行的 cli/ 工具流：

| 行业 | Locale | Phase 4 | CLI scripts | 路径 |
|------|--------|---------|-------------|------|
| 🔥 **LLM agent infra** | en (global) | ✅ PASS (10/12 mech) | 11 (1+6+3+lib+README) | [prototypes/llm-agent-infra-master/](prototypes/llm-agent-infra-master/) |
| ✅ **跨境电商运营** | zh-CN | mini scope | 5 (1+1+2+lib+README) | [prototypes/cross-border-ecommerce-master/](prototypes/cross-border-ecommerce-master/) |
| 🔲 短视频投流 | zh-CN | planned | — | (v1.x) |
| 🔲 足踝外科 | zh-CN | planned | — | (v1.x) |

调研过程**全透明**. 每个 prototype 都包含完整 6 路调研数据 + synthesis.md, 可以追溯每个心智模型 / playbook 规则的来源.

想蒸馏不在列表里的行业? 装大师.skill, 说「造大师 XXX」即可.

---

## 🔬 工作原理

输入一个细分行业之后, 大师.skill 做 **5 件事**:

```
Phase 0    行业澄清          ← 用户给坏粒度时主动收窄 (拒绝「AI」, 引导到「LLM agent infra」)
Phase 0.5  创建目录          ← 自包含, 所有产物都在 skill 内部
Phase 1    六轨并行调研      ← 6 个 subagent: figures / tools / workflows / canon / sources / glossary
Phase 1.5  调研 review 关卡  ← 用户确认调研质量再继续 (不让垃圾输入污染下游)
Phase 2    框架提炼          ← 三重验证 (跨场景复现 / 生成力 / 排他性) 挡住行业八股
Phase 2.5  提炼 review 关卡  ← 用户确认 OS 框架再生成
Phase 3    skill 写出        ← skill_writer 生成完整目录 (含自动调女娲蒸 sub-skill + 自动生成 cli/)
Phase 4    三测验证          ← 已知 / 边界 / 风格盲测
Phase 5    双 agent 精炼     ← 优化 skill 的「激活即执行」程度
```

详见 [SKILL.md](SKILL.md) — 524 行 agent 可加载的工作流规约.
方法论看 [references/extraction-framework.md](references/extraction-framework.md) — 三重验证、工具栈三层提炼、流派分歧处理、衰减速度表.

---

## 🧬 三代谱系

大师.skill 站在两个前作的肩膀上：

```
🧬 同事.skill     蒸馏一个具体的人          范围: 1 人
🌟 女娲.skill     蒸馏一种思维方式          范围: 任何活人 / 历史人物
🎓 大师.skill     蒸馏一个细分行业的 OS     范围: 一整个领域
```

- **[同事.skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — 证明「蒸馏一个人」是可行的. 提供了 intake → multi-source collect → analyze → write 的元 skill 模式.
- **[女娲.skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — 证明「蒸馏思维方式」比「蒸馏话语」更有价值. 提供了 6-agent 并行 swarm + 三重质量关卡 + Agentic Protocol. **大师.skill 在 Phase 3 调用女娲.skill 蒸馏 top 3 figures, 作为生成 skill 的 sub-skill**.

三者同源, 逐层放大 — 蒸馏一个你认识的人 → 任何活着或死去的人 → 一整个领域的人类知识。

---

## 📂 项目结构

```
master-skill/
├── SKILL.md                          # 大师本体 (524 行 agent 可加载)
├── prompts/                          # 5 phase prompt 系统
│   ├── intake.md                     #   Phase 0 行业澄清
│   ├── research/01-06.md             #   Phase 1 六路调研模板
│   ├── synthesis.md                  #   Phase 2 提炼指引
│   ├── quality_check.md              #   Phase 4 验证 rubric
│   └── sub-skill-figures.md          #   Phase 3 调女娲的 subagent prompt
├── tools/                            # 7 个 Python 工具
│   ├── skill_writer.py               #   Phase 3 写 skill 目录
│   ├── cli_writer.py                 #   v0.6 emit cli/ 子树
│   ├── update_skill.py               #   v1.1 增量刷新
│   ├── install.py                    #   4 host 安装器
│   ├── research/merge_research.py    #   Phase 1.5 review 聚合
│   ├── research/quality_check.py     #   Phase 4.4 机械 rubric
│   └── transcribe/                   #   yt-dlp + SRT/VTT 字幕处理
├── references/
│   ├── skill-template.md             #   生成产物的标准结构
│   ├── extraction-framework.md       #   提炼方法论 (深入看这个)
│   └── cli-spec.md                   #   CLI 工具流设计 spec
└── prototypes/
    ├── llm-agent-infra-master/       #   v1.0 完整 prototype
    └── cross-border-ecommerce-master/  #   v1.1 zh-CN mini prototype
```

---

## ⚠️ 注意

**调研材料质量 = skill 质量**. 不同维度的来源优先级不同：

| 维度 | 来源优先级 (高 → 低) |
|------|---------------------|
| 🌟 行业大佬 (Track 01) | 本人 long-form (书 / 长访谈 / blog 系列) **›** 决策记录 (公开发声 / 提交记录) **›** 二手转述 |
| 🛠️ 工具地图 (Track 02) | 工具官方 docs **›** 工程师生产案例 **›** 教程 / SEO 软文 |
| 📋 工作流 (Track 03) | 公司技术博客的真实 SOP **›** 资深人长访谈 **›** 培训机构 outline |
| 📚 知识正典 (Track 04) | 行业人推荐书单 (≥3 个独立来源都点过) **›** 学术综述 **›** 二手书评 |
| 📰 信息源 (Track 05) | 行业人订阅清单 **›** 主流媒体长稿 **›** 内容农场 |

- 中文 locale 自动排除知乎 / 微信公众号 / 百度百科 / CSDN (除原文)
- 信息越早 cutoff, 工具 / 工作流模块越快衰减 — 用 `update 大师 X` 增量刷新
- 这是 v1.1, 还在快速迭代. 发现 bug 请 file issue!

---

## 📄 路线图

| 版本 | 内容 | 状态 |
|------|------|------|
| v0.1-0.4 | SKILL spec + prompts + tools + polish | ✅ |
| v1.0 | LLM agent infra prototype 端到端验证, repo 公开 | ✅ |
| v0.6 | CLI 工具流 — 生成 skill 自带 bash 套件 | ✅ |
| v1.1 | Cross-skill composition + 增量刷新 + zh-CN prototype | ✅ |
| v1.x | cluster 关键词从 synthesis 自学 / cron refresh hook | 🔲 |
| v1.x | 更多行业 prototype (短视频 / 足踝外科 / 法律) | 🔲 |
| v2.x | PyPI 打包 / GitHub Action 自动 update / 多语言 | 🔲 |

详见 [ROADMAP.md](ROADMAP.md).

---

## ⭐ Star History

<a href="https://www.star-history.com/?repos=voidborne-d%2Fmaster-skill&type=date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
 </picture>
</a>

---

## 📜 许可证

MIT — 随便用，随便改，随便造。

<div align="center">

<br>

**🧬 同事.skill** 蒸馏了**一个人**做什么.<br>
**🌟 女娲.skill** 蒸馏了**任何人**怎么想.<br>
**🎓 大师.skill** 蒸馏了**一整个行业**的认知操作系统.<br>

<br>

*你不再需要去 awesome-skills 列表里挑.*<br>
*告诉大师.skill 你做哪一行, 它把这一行的人, 蒸馏成你能装载的 skill.*

<br>

MIT License © [voidborne-d](https://github.com/voidborne-d) · 中文 README · [English](README_en.md)

</div>
