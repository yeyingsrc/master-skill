# Phase 0A — Industry Intake

> Phase 0A 的具体执行剧本。SKILL.md Phase 0A 调用本文件。

## 你的任务

通过有节制的对话收集 6 项信息，然后产出一个 `intake.json`，作为 Phase 0.5 创建目录 + Phase 1 启动 6 轨调研 swarm 的输入。

**节奏要求**：最多 2 轮对话拿到 6 项。不要变成问卷，不要每条都追问，用户主动说的不要重问。

---

## 6 项必收集信息

### 1. industry（必填）

**问什么**：「你做的具体细分是什么？」（中英文都接受）

**好答案 vs 坏答案**：

| ✅ 好（够细，能调研） | ❌ 坏（太宽，必须收窄） |
|------------------|--------------------|
| LLM agent infra | AI |
| 跨境电商运营 | 电商 |
| 短视频投流 | 营销 |
| 足踝外科 | 医疗 |
| RAG 系统设计 | 大模型 |

**用户给坏答案时的反推话术**：
> "{industry} 范围有点宽，做出来的 master skill OS 会稀薄得没用。能不能再具体一点？例如：你日常遇到的问题主要在 {推测可能的子方向 1} / {子方向 2} / {子方向 3} 哪一块？"

如果用户坚持要做宽行业 → 警告一次后接受，但在 SKILL.md 诚实边界里写明「本 skill 跨度较宽，深度受限」。

### 2. focus（可选，默认 "comprehensive"）

**问什么**：「你想要全景画像，还是某个角度优先？技术 / 商业 / 学术 / 操作？」

| Focus | 含义 | 调研偏向 |
|-------|------|---------|
| `comprehensive` | 全景 | 6 轨等权 |
| `technical` | 技术视角 | Track 02 (tools) + 03 (workflows) 加权 |
| `business` | 商业视角 | Track 01 (figures) + 05 (sources) 加权 |
| `academic` | 学术视角 | Track 04 (canon) + 06 (glossary 中的标准) 加权 |
| `operational` | 实操视角 | Track 03 (workflows) 重权，4 + 6 次之 |

用户没主动说 → 默认 `comprehensive`。

### 3. locale（可选，默认 "global"）

**问什么**：「你主要在哪个语言区 / 地域工作？」

可选值：`zh-CN`、`en`、`ja`、`ko`、`global`。

- 选 `zh-CN` → 信源池切到 B 站 / 小宇宙 / 36氪 / 极客公园 / 晚点 / 财新 / 虎嗅 / 机器之心；**永远排除知乎、微信公众号、百度百科**
- 选 `en` → 信源池切到 X / YouTube / Substack / arXiv / Hacker News / 行业 podcast
- 选 `global` → 双语并行，但要警告用户：「双语可能在某些维度（特别是 Track 04 canon）出现严重失衡」

**关键判断**：
- 用户用中文沟通且没指定 → 默认 `zh-CN`，因为 master skill 最终要他用
- 用户用英文沟通且没指定 → 默认 `en`
- 用户做的是国际市场（如跨境电商） → 主动建议 `global`

### 4. profile（可选，默认 "practitioner"）

**问什么**：「你跟这个行业的关系？从业者 / 学习中 / 投资视角 / 服务咨询？」

| Profile | 影响 |
|---------|------|
| `practitioner` | master skill 假设用户已有基本背景，措辞可以专业 |
| `learner` | master skill 多解释黑话、补充入门路径 |
| `investor` | master skill 重点放在 Track 01 (figures) + 05 (sources)，强化「信号 vs 噪音」识别 |
| `consultant` | master skill 强调跨子领域 + 客户翻译能力 |

### 5. local_materials（强烈推荐询问）

**问什么**：「你手上有这行的一手素材吗？行业报告 PDF / 内部文档 / 你写过的文章 / 长访谈 transcript / 视频字幕？有的话直接丢给我，比网上搜到的二手转述质量高得多。」

**为什么必问**：用户提供的一手素材在信源优先级中权重最高（见 `references/extraction-framework.md` § 七）。漏问就是放着免费的高质量信号不要。

**用户的可能回答**：
- "有" → 切换到**本地语料模式**，把素材路径或内容收集到 `intake.local_materials_paths` 数组
- "没有" → 切换到**纯网络搜索模式**
- "只有 X 类" → 混合模式，标注哪些 track 由本地素材覆盖

### 6. existing_skill_check（自动执行）

**做什么**（不要问用户）：检查 `~/.claude/skills/` 下是否已有 `{slug}-master/` 目录。

- 已存在 → 询问用户：「我看到你装过 `{slug}-master`，上次调研日期 `{date}`。要新建一个版本，还是 update 老的？」
- 不存在 → 默认新建路径

如果路径环境不是 Claude Code（例如 OpenClaw / Codex / Hermes），按 SKILL.md 的 HOST_SKILLS_ROOT 解析规则去对应路径检查。

---

## 对话节奏剧本

### 标准节奏（用户给的信息全 / 半全）

```
USER: 我做 LLM agent infra，给我做一个 master skill
ASSISTANT:
  → industry: "LLM agent infra" ✓
  → 推断 locale: en（用户用中文沟通但行业是 global 英文圈，建议 global）
  → focus / profile / local_materials 缺
  → 一次问完三项

ASSISTANT 回复:
"收到。「LLM agent infra」是好粒度。补三件事：
 1) 你想要全景，还是聚焦某一面？(技术/商业/学术/操作)
 2) 你跟这个行业的关系？(从业者/学习中/投资/咨询)
 3) 手上有没有一手素材？长访谈 transcript / 内部文档 / 行业报告 PDF / 你自己写过的东西。有就 paste 路径或内容；没有我走纯网络搜索。"

USER: 全景，从业者，没素材
ASSISTANT: 「确认：industry=LLM agent infra, focus=comprehensive, locale=global, profile=practitioner, local_materials=none。开始 Phase 0.5 创建目录。」
```

### 用户给坏粒度时的剧本

```
USER: 帮我做个 AI 行业的 master skill
ASSISTANT:
  → industry: "AI" — 太宽，必须收窄

ASSISTANT 回复:
「『AI』太宽了，蒸出来的 OS 会稀薄到没用。能不能再具体一点？例如：
 - LLM 应用层：agent infra / RAG / prompt eng / fine-tuning / eval
 - 模型层：开源模型训练 / RL / multimodal / efficient inference
 - 商业 / 投资视角：AI infra 投资 / AI 产品分析
 - 你的实际工作偏哪一块？」

USER: 主要做 agent
ASSISTANT: 「LLM agent infra？还是 vertical agent 应用（如 coding agent / browser agent）？这两个调研路径很不同。」

USER: agent infra
ASSISTANT: 收 industry=LLM agent infra，继续问其他 5 项
```

### 用户拒绝细化的边界

```
USER: 我就做 AI 行业的 master skill，不要再问了
ASSISTANT:
  → 接受 industry="AI"，但记一笔 warn

ASSISTANT 回复:
「OK，industry=AI（注意：跨度大，OS 提炼会稀薄，会在最终 skill 的『诚实边界』节明确标注本 skill 跨度受限）。继续问其他几项...」
```

---

## 输出 — `intake.json`

收集完 6 项后，生成（Phase 0.5 立即用）：

```json
{
  "industry": "LLM agent infra",
  "industry_cn": "LLM agent 基础设施",
  "slug": "llm-agent-infra",
  "focus": "comprehensive",
  "locale": "global",
  "profile": "practitioner",
  "local_materials": {
    "mode": "none | local-first | local-only | mixed",
    "paths": [],
    "covered_tracks": []
  },
  "existing_skill": {
    "found": false,
    "path": null,
    "last_research_date": null,
    "decision": "new | update"
  },
  "warnings": []
}
```

字段规则：
- `slug`：industry 转 kebab-case，去掉空格 / 特殊字符。例：`LLM agent infra` → `llm-agent-infra`、`跨境电商运营` → `cross-border-ecom-ops`
- `industry_cn`：如果 locale 是 zh-CN 必填，否则可选
- `local_materials.mode`：见 SKILL.md Phase 1 的模式判断表
- `warnings`：用户拒绝细化、locale 不平衡、existing skill 但要求新建等需要在最终 SKILL.md 诚实边界节复述的事

确认完毕展示给用户：

```
确认：
  industry: LLM agent infra
  focus: comprehensive
  locale: global
  profile: practitioner
  local_materials: none
  existing_skill: 无
  warnings: 无

进入 Phase 0.5（创建目录）→ Phase 1（六轨调研）。预计调研时间 30-60 分钟。
```

用户确认 → 进入 Phase 0.5。
用户要改 → 改完再确认一次再进。

---

## 反模式

- ❌ 一次问 6 个问题（用户跑掉）
- ❌ 用户已说的还在重复问（让用户烦）
- ❌ 不警告坏粒度直接接受（输出垃圾 skill）
- ❌ 不问 local_materials（错过最高质量信号）
- ❌ 把 intake 写成问卷格式（不是 form，是对话）
