# Test: intake.md dry-run

Walking three synthetic user inputs through `prompts/intake.md` to validate conversation flow and output structure.

---

## Scenario 1: Standard well-scoped input

```
USER: 我做 LLM agent infra，给我做一个 master skill
```

### Expected agent behavior
- Captures `industry: "LLM agent infra"` immediately ✓
- Notices user typed Chinese but the field is global English-speaking → flag locale ambiguity
- Asks 3 missing slots in one batch (focus, profile, local_materials)

### Expected reply
```
收到。「LLM agent infra」是好粒度。补三件事：
 1) 全景，还是聚焦某一面？(技术 / 商业 / 学术 / 操作)
 2) 你的角色？(从业者 / 学习中 / 投资 / 咨询)
 3) 手上有没有一手素材？长访谈 transcript / 内部文档 / 行业报告 / 你自己写过的东西。有就 paste；没有走纯网络搜索。
顺便：locale 这块我倾向 global（这行的核心讨论在英文圈），你觉得呢？
```

### Round 2

```
USER: 全景 / 从业者 / 没素材 / global 可以
```

### Expected output `intake.json`

```json
{
  "industry": "LLM agent infra",
  "industry_cn": "LLM agent 基础设施",
  "slug": "llm-agent-infra",
  "focus": "comprehensive",
  "locale": "global",
  "profile": "practitioner",
  "local_materials": {
    "mode": "none",
    "paths": [],
    "covered_tracks": []
  },
  "existing_skill": {
    "found": false,
    "path": null,
    "last_research_date": null,
    "decision": "new"
  },
  "warnings": []
}
```

**Verdict: PASS** — 2 轮搞定 6 项，无歧义。

---

## Scenario 2: User gives a too-broad industry

```
USER: 帮我做个 AI 行业的 master skill
```

### Expected agent behavior
- Captures `industry: "AI"` but flags as too broad
- Pushes back with concrete sub-options
- Does NOT proceed to other 5 slots until industry is narrowed

### Expected reply
```
「AI」太宽，蒸出来 OS 会稀薄到没用。能不能再具体一点？比如：
 - LLM 应用层：agent infra / RAG / prompt eng / fine-tuning / eval
 - 模型层：开源训练 / RL / multimodal / efficient inference
 - 商业 / 投资视角：AI infra 投资 / AI 产品分析
 你日常工作偏哪一块？
```

### Round 2

```
USER: agent infra
```

### Expected reply
```
LLM agent infra？还是某个 vertical agent 应用（如 coding agent / browser agent）？这两个调研路径很不同。
```

### Round 3

```
USER: LLM agent infra
```

→ Now proceeds as Scenario 1 from "其他 5 项" prompt.

**Verdict: PASS** — 框架正确挡住「AI」这种太宽的输入，引导到具体细分。但**消耗了 3 轮**才到 Scenario 1 的起点 — 这超出了「最多 2 轮拿到 6 项」的节奏目标。

**Issue found**: 「最多 2 轮」的节奏假设用户一开始就给好粒度。当用户给坏粒度时，需要先用 1-2 轮收窄，**然后**才走标准流程。intake.md 应该更新：「2 轮节奏的起点是『拿到合格粒度的 industry 之后』，收窄过程不计入。」

---

## Scenario 3: User has local materials

```
USER: 我想蒸一个跨境电商运营的 master skill。我手上有过去 6 个月的行业群聊记录、3 本书的 PDF、一份内部 SOP 文档。
```

### Expected agent behavior
- industry 粒度合格 ✓
- 用户主动说了 local_materials → 不要重问
- locale 推断 zh-CN（跨境电商运营是中文语境产业）
- 追问 focus / profile

### Expected reply
```
跨境电商运营，好粒度。素材很丰富 — 群聊记录 / 3 本书 PDF / 内部 SOP。补两件事：
 1) 你想要全景，还是某个角度优先？(技术 / 商业 / 学术 / 操作 — 我猜你偏 operational + business？)
 2) 你的角色？(从业者 / 学习 / 投资 / 咨询)
locale 我默认 zh-CN，对吗？
然后请把 PDF 和文档 paste 给我，或者给路径。
```

### Round 2

```
USER: 操作 + 商业，我是从业者，5 年了。zh-CN 对。文件在 ~/docs/ec/{books,sop,chats}/
```

### Expected output `intake.json`

```json
{
  "industry": "cross-border e-commerce operations",
  "industry_cn": "跨境电商运营",
  "slug": "cross-border-ecom-ops",
  "focus": "operational",
  "locale": "zh-CN",
  "profile": "practitioner",
  "local_materials": {
    "mode": "local-first",
    "paths": [
      "~/docs/ec/books/",
      "~/docs/ec/sop/",
      "~/docs/ec/chats/"
    ],
    "covered_tracks": ["canon (PDF)", "workflows (SOP)", "figures+expression-DNA (chats)"]
  },
  "existing_skill": {
    "found": false,
    "path": null,
    "last_research_date": null,
    "decision": "new"
  },
  "warnings": []
}
```

**Issue found**: `focus` 模板只允许单值（comprehensive/technical/business/academic/operational），但用户说「操作 + 商业」是组合的。intake.md 和 skill-template.md 的 frontmatter 应该接受**数组形式**或**主从指定**，例如 `focus: { primary: "operational", secondary: "business" }` 或 `focus: ["operational", "business"]`。

**Verdict: PASS with structural issue** — 流程跑通，但 focus 字段需要支持组合。

---

## Findings — intake.md v0.1 dry run

### Pass

- 单一良好粒度的输入 2 轮搞定 (Scenario 1)
- 太宽粒度被正确挡住并引导收窄 (Scenario 2)
- 用户主动信息不被重问 (Scenario 3)
- intake.json schema 字段都填得上

### Issues found

1. **「最多 2 轮」节奏的起点定义不清**：用户给坏粒度时收窄过程消耗了 1-2 轮，加起来 3 轮才完成。intake.md 应该改：「2 轮起点是『拿到合格粒度的 industry 之后』」
2. **focus 字段不支持组合**：用户经常会说「操作 + 商业」「技术 + 学术」这种组合视角。需要支持 array 形式或 primary/secondary 结构
3. **missing intake-completion-trigger**：intake.json 生成完后，应该有一个明确的「确认 → 进入 Phase 0.5」交互，现在 intake.md 写了「确认完毕展示给用户」但没规定用户怎么"批准"。建议加：用户回 "ok / 开始 / go / 确认" 等触发，否则用户改完再重确认。
4. **slug 生成规则**：`跨境电商运营 → cross-border-ecom-ops` 涉及中→英翻译，intake.md 没说由谁负责（agent 翻译 vs 用户给）。需要补：默认 agent 翻译，用户可覆盖。
5. **existing_skill 检查的执行时机**：intake.md 说"自动执行"，但放在哪一步？开头就检查（用户还没说 industry 怎么知道路径）？还是 industry 确认后才查？应明确：industry 确认后立即检查，比 focus/profile 的轮次更早。

### Action items for next iteration

- [ ] 修 intake.md：上面 5 条 issues
- [ ] 修 skill-template.md：focus 改为 array 或 primary/secondary 结构（或者保留单值但允许 "operational+business" 这种字符串）
- [ ] 写 prompts/research/01-figures.md（v0.2 next - 6 个 subagent 任务模板的第一个）

### Cumulative findings still pending

- (iter 1) Agentic Protocol dim count "5-8" → "3-10 by complexity" in SKILL.md  ← still TODO
- (iter 2) extraction-framework borderline rule + candidate-list prep + partial-generative-power state  ← still TODO
- (iter 3, this round) 5 issues above

### Findings addressed this round

- ✅ skill-template.md frontmatter 加了 `triggers` array（iter 1 finding）
- ✅ skill-template.md meta.json 加了 `triggers` + `focus` 字段
- ✅ skill-template.md frontmatter locale 扩展为 `en | zh-CN | ja | ko | global`

---

## 测试总结

intake.md 的核心节奏（2 轮拿 6 项）在「良好粒度输入」上跑通了，在「坏粒度」「丰富 local_materials」两个边缘场景上各暴露了 1-2 个具体可修的问题。意外发现：focus 字段单值约束在真实场景偏窄，需要扩展。

下一轮重点：写 prompts/research/01-figures.md（启动 6 个 research subagent 之首），然后逐步把 02-06 也写完。这之后 intake → research swarm → quality checkpoint 就能端到端跑一次最小 prototype。
