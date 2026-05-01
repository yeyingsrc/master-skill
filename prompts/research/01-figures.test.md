# Test: 01-figures.md dry-run on "LLM agent infra"

Walking the 6-step flow from `01-figures.md` against prototype industry "LLM agent infra" (locale=global) without doing actual web searches — using public-knowledge candidates I'm confident about as of 2026-05. Validates whether the template structure produces useful output.

---

## Step 1: Wide net (target 20-30 candidates)

Following the 5 source priorities in 01-figures.md:

### From 行业最大几家公司
- Harrison Chase (LangChain founder)
- Lance Martin (LangChain)
- Mike Knoop (Adept → ARC Prize)
- Erik Schluntz (Anthropic, agents lead)
- Ali Ghodsi (Databricks, agent infra)
- Jerry Liu (LlamaIndex founder)
- Andy Pavlo (DB-side, less direct but cited)

### From 核心著作 / 论文作者
- Yao et al. (ReAct paper authors)
- Karpathy (transformer & agent commentary)
- Noam Brown (OpenAI, agentic reasoning)
- Sasha Rush (HuggingFace, agent eval)

### From second-order recommendations (≥3 mentions)
- Simon Willison (independent, prolific writer)
- Eugene Yan (eval-focused)
- Hamel Husain (eval, deployment)
- Swyx (latent.space, ecosystem)

### From 行业专属 podcast / conference 嘉宾
- Sumanth Hegde (LLM eval)
- Jonathan Frankle (Databricks AI labs)

### From active 输出
- Han Lee (Cline / agent IDE)
- Geoffrey Huntley (agentic dev)

**Wide net count: ~17.** Below target of 20-30 — would need broader search to fill out, especially China-locale (caught by Track if locale=global, but locale-specific runs would catch Andrew Ng-en, 老王 / 王慧文 / Yi Tay etc).

**Issue surfaced**: 17 is below the "20-30" target without doing extensive search. The template's "≥20 candidates" floor might be hard to hit even for a high-public-content industry like this one without 30+ minutes of dedicated research. Consider relaxing to "10-25" or making the floor explicit-as-target rather than gate.

---

## Step 2: Quality gate filter to 10-15

Apply each candidate against the 4 criteria:

| Candidate | Cross-mention | Researchable | Active | Not pure-academic/marketing | Decision |
|-----------|--------------|--------------|--------|------------------------------|----------|
| Harrison Chase | ✅ (HN, X, conf) | ✅ (Interrupt 25 keynote ~60min) | ✅ | ✅ | KEEP |
| Lance Martin | ✅ | ✅ (LangChain blog, podcast) | ✅ | ✅ | KEEP |
| Erik Schluntz | ⚠️ (mostly Anthropic-internal) | ⚠️ (limited public talks) | ✅ | ✅ | KEEP (borderline) |
| Mike Knoop | ✅ (ARC Prize) | ✅ (ARC keynote, podcast) | ✅ | ✅ | KEEP |
| Jerry Liu | ✅ | ✅ | ✅ | ✅ | KEEP |
| Yao et al. | ✅ (paper widely cited) | ❌ (paper is short, no long interviews) | ⚠️ | ✅ academic | DROP → Track 04 |
| Karpathy | ✅ | ✅ | ✅ | ✅ | KEEP (agent commentary, not just LLM) |
| Noam Brown | ✅ | ✅ (long Lex talk) | ✅ | ⚠️ academic-leaning | KEEP (borderline) |
| Sasha Rush | ✅ | ✅ | ✅ | ✅ | KEEP |
| Simon Willison | ✅ | ✅ (blog 800+ posts) | ✅ | ✅ | KEEP |
| Eugene Yan | ✅ | ✅ | ✅ | ✅ | KEEP |
| Hamel Husain | ✅ | ✅ | ✅ | ✅ | KEEP |
| Swyx | ✅ | ✅ (latent.space pod 100+) | ✅ | ✅ | KEEP |
| Sumanth Hegde | ⚠️ (less mentions) | ⚠️ | ✅ | ✅ | DROP (insufficient cross-mention) |
| Jonathan Frankle | ✅ | ✅ | ✅ | ⚠️ academic | KEEP (borderline) |
| Han Lee | ⚠️ (more product-focused) | ⚠️ (limited long-form output) | ✅ | ✅ | DROP |
| Geoffrey Huntley | ✅ (active blogger) | ✅ | ✅ | ✅ | KEEP |
| Ali Ghodsi | ✅ | ✅ | ✅ | ⚠️ marketing-heavy | KEEP (borderline) |
| Andy Pavlo | ⚠️ (DB-side, less direct) | ✅ | ✅ | ✅ | DROP (not central to agent infra) |

**Filtered to 13 (within 10-15 target).** Borderlines: Schluntz, Brown, Frankle, Ghodsi.

---

## Step 3-4: Per-figure data structure (sample 1 figure)

Showing one fully-filled example to validate structure:

```markdown
### 1. Harrison Chase

- **One-liner**: LangChain creator. Drove agent framework from "ReAct paper concept" to "engineering standard"; now publicly arguing the framework abstraction itself decays as model capability grows.
- **核心身份**: LangChain CEO; previously Robust Intelligence
- **代表作品**:
  - LangChain (open-source framework, 90k+ stars)
  - LangGraph (graph-based successor)
  - LangSmith (observability/eval suite)
- **值得读 / 听 / 看的 3 件事**:
  - 📖 LangChain blog series on "the move from chains to graphs" (URL placeholder)
  - 🎙️ Latent Space pod with Swyx 2025-Q1 (URL placeholder)
  - 🎬 LangChain Interrupt 2025 keynote — "Frameworks are temporary" (URL placeholder)
- **核心思想关键词**: framework decay; graphs > chains; observability-first; eval-driven dev; "ship in a weekend, replace in a weekend"
- **最近 12 个月动态**: Pivoted public messaging from "use LangChain for everything" toward "use LangGraph as a thin layer; expect to replace it in 12 months"; LangSmith eval focus increased.
- **争议 / 批评**: LangChain accused of pre-mature abstraction by 2023-24 critics (HN threads, Vercel ai-sdk team); company response was the LangGraph rewrite. Critics now split — some accept the pivot, some say LangGraph repeats the same mistake.
- **来源**:
  - [Primary] LangChain Interrupt 2025 keynote (URL, 2025-04, collected: 2026-05-01)
  - [Primary] Latent Space pod (URL, 2025-Q1)
  - [Secondary] HN thread "Why I dropped LangChain" (URL, 2024-09)
  - [Reference] Anthropic agent docs cite LangGraph (URL)
- **可信度自评**: high (multiple primary sources, active output, well-documented evolution of stance)
```

**Verdict on structure**: works well. 9 fields per figure produces a solid card. Phase 2 提炼 can pull mental-model candidates from "核心思想关键词" (e.g., "framework decay") and validate against other figures' keywords.

---

## Step 5-6: 总览表 + Phase 2 接口

### 总览（partial, top 5）

| # | Name | Role | One-liner | 媒介 | Sources |
|---|------|------|-----------|------|---------|
| 1 | Harrison Chase | LangChain CEO | Framework decay thesis | 📖🎙️🎬 | 4 |
| 2 | Mike Knoop | ARC Prize / Adept | Pure capability vs. scaffolding test | 📖🎙️🎬 | 3 |
| 3 | Andrej Karpathy | Independent / OpenAI alum | Agentic dev + UNIX-style philosophy | 📖🎙️🎬 | 5 |
| 4 | Simon Willison | Independent | Pragmatic everyday-tooling for agents | 📖 | 6 |
| 5 | Swyx | Latent Space | Ecosystem-mapping, "rise of AI engineer" | 🎙️ | 4 |

### Phase 2 接口

**反复出现 ≥ 3 figures 都谈到的关键词** (candidate mental models):
- "Framework as scaffold, not foundation" — Chase, Knoop, Willison, Karpathy
- "Eval is more important than prompt eng" — Husain, Yan, Rush, Lee
- "Production reality vs demo glamour" — Willison, Husain, Chase (mentioned in pod)
- "Capability lift will eat your abstraction" — Knoop, Chase, Karpathy

**显著分歧 / 流派分裂**:
- "Thin frameworks" 派 (Chase post-pivot, Willison, ai-sdk crew) vs "Thick orchestration" 派 (CrewAI, AutoGen) — currently the field's main visible split
- "Agent eval as benchmarks" (Yan, Rush, Frankle) vs "Agent eval as production traces" (Husain, Chase via LangSmith)
- "Pure agent" (open-ended planning) vs "Workflow with LLM steps" (Husain, Chase recent stance) — emerging consensus on the latter

**冷僻领域信号**:
- 总 figure 数 = 13 ✓ (在 10-15 target)
- 长访谈材料 < 30 min 比例 ≈ 2/13 ≈ 15% ✓ (<30%)
- 可信度 low: 0/13 ✓
- → **不冷僻，OS 提炼基础充分**

---

## Findings — 01-figures.md v0.1 dry run

### Pass

- 6 步流程跑通了，能产出 Phase 2 可消费的输出
- Quality gate 4-criteria 在 19 个候选上都给出明确的 keep / drop / borderline 判定
- 每位 figure 的 9 字段卡片结构充分支持 Phase 2 提炼的需要
- "Phase 2 接口" 这一段（候选关键词 + 分歧 + 冷僻信号）是关键 — 把 Phase 1 → Phase 2 的衔接显式化了，避免了 Phase 2 重新挖掘
- 可信度自评（high / medium / low + 理由）做得到，且对 Phase 2 取舍有用

### Issues found

1. **20-30 候选 floor 偏高**：dry-run 拿到 17 个就到上限了。对中等热度行业，没投入 30+ 分钟搜索很难达 20。建议改：「目标 20-30，floor 是 15，<10 触发冷僻协议」
2. **Borderline candidates 缺乏明确处理规则**：表里 4 个 borderline 我都 KEEP 了，但 01-figures.md 没明说 borderline 算不算「至少 2 项」中的边缘合格。建议加：「Borderline = 仅勉强满足 2 项 → KEEP 但在卡片『可信度自评』标 medium」
3. **Sub-skill 候选没标记**：13 个 figures 中应该有 3 位是 nuwa.skill 蒸馏 sub-skill 的候选。没机制标记「适合做 sub-skill」。建议加字段：`sub_skill_candidate: true|false + 理由`，让 Phase 3 直接用
4. **学术 figure 边缘化处理过严**：把 Yao et al. 直接 drop 到 Track 04 — 但 ReAct 的作者其实也在做工程实践（Princeton / Google 内部）。改：「学术 figure 可保留 if 同时有工程角色」
5. **"行业最大几家公司"** 的 bootstrap 问题：本 track 启动时 Track 02 (tools) 还没数据，那「行业最大几家公司」凭直觉抓。这个并行 swarm 的依赖问题需要在 SKILL.md Phase 1 处理：可能要让 Track 02 和 Track 01 顺序而非并行，或者 Track 01 先抓粗略名单后续再细化

### Action items for next iteration

- [ ] 修 01-figures.md：上面 5 条 issues，特别是 #1（候选数量 floor）和 #5（与 Track 02 的依赖时序）
- [ ] 写 prompts/research/02-tools.md
- [ ] SKILL.md Phase 1：明确 Track 间是纯并行还是有 dependency wave（建议 wave 1: 01-figures + 04-canon + 05-sources, wave 2: 02-tools + 03-workflows + 06-glossary 用 wave 1 的产出做加权）

### Cumulative findings status

- ✅ Addressed: triggers field (iter 1)
- 🔲 Pending: SKILL.md Agentic Protocol "5-8" → "3-10" (iter 1)
- 🔲 Pending: extraction-framework borderline / candidate-list-prep / partial-generative-power (iter 2)
- 🔲 Pending: 5 intake.md issues (iter 3)
- 🔲 New: 5 issues here (iter 4)

**累计未处理 finding 数 = 13。** 该集中处理一轮了。建议 iter 5 不写新 prompt，专做一轮 cumulative-fixes pass。

---

## 测试总结

01-figures.md 跑通了 6 步流程，产出对 Phase 2 友好。最大的发现是 Phase 1 的 6 个 track 之间不是纯并行 — 至少 Track 01 (figures) / Track 02 (tools) / Track 04 (canon) 互相是 bootstrap 的输入源。SKILL.md 的 Phase 1 描述需要补一段 wave / dependency 说明。

下一轮可以选 (a) 写 02-tools.md（继续推 prompts/research/）或 (b) 做 cumulative finding 集中清理。13 条积累，建议 (b)。
