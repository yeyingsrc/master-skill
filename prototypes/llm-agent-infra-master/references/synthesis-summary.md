# Phase 1.5 Research Review

_Generated: 2026-05-02T10:15:10.963626+00:00_

| # | Track | 项数 | 来源 (P/S/R) | 一手比例 | Cold? |
|---|-------|------|-------------|---------|-------|
| 1 | Figures | 5 (floor 10) | 12/5/5 | 55% | 🔵 |
| 2 | Tools | 8 (floor 15) | 13/6/4 | 56% | 🔵 |
| 3 | Workflows | 3 (floor 3) | 8/3/1 | 67% | ✅ |
| 4 | Canon | 6 (floor 15) | 8/1/4 | 62% | 🔵 |
| 5 | Sources | 8 (floor 10) | 0/0/0 | 0% | 🔵 |
| 6 | Glossary | 12 (floor 25) | 0/0/0 | 0% | 🔵 |

## 总览

- 总来源数: 70
  - Primary: 41
  - Secondary: 15
  - Reference: 14
- 总体一手比例: 59%
- 冷僻 track 数: 5
  - 受影响: 01-figures, 02-tools, 04-canon, 05-sources, 06-glossary
- 整体行业判定: ⚠️  COLD INDUSTRY

## 质量关卡判定

- ❌ 个别 track 一手比例 < 40%: 05-sources (0%), 06-glossary (0%) — 该 track 的提炼质量明显弱于其他，建议针对性补 research
- ❌ 冷僻 track ≥ 3 个 (01-figures, 02-tools, 04-canon, 05-sources, 06-glossary) — 建议在 Phase 2.8 诚实边界明确标注信号薄弱维度

**关卡判定: ⚠️ NEEDS REVIEW** — 用户需要决定继续 / 补 research / 缩小行业范围

## 各 Track Phase 2 接口

### Figures (01-figures)
**反复出现 ≥ 3 figures 都谈到的关键词**:
- "Framework as scaffold, not foundation" (figures: Chase, Karpathy, Willison, Knoop)
- "Eval > model architecture" (figures: Husain, Chase, Husain-Yan-collab)
- "Production reality vs demo glamour" (figures: Husain, Willison, Chase)
- "Capability eats abstraction" (figures: Knoop, Chase, Karpathy)

**显著分歧 / 流派分裂**:
- "Thin frameworks" 派 (Chase post-pivot, Willison, ai-sdk crew) vs "Thick orchestration" 派 (CrewAI, AutoGen) — Track 01 sees Chase straddling but post-2025 Q1 he's clearly thin
- "Pure agent" (open-ended planning) vs "Workflow with LLM steps" (emerging consensus on the latter)

**冷僻信号**: 5 figures is below 13 target. Minimal-viable scope; not a real cold-industry indicator. ✅ industry not cold.

### Tools (02-tools)
**反复出现 ≥ 3 source 都强调的「工具选型原则」**:
- "Framework decay risk" → 选 framework 的标准是「能在一个周末剥掉吗」
- "Production reality vs demo" → demo 跑通 ≠ production-ready
- "Hybrid retrieval > pure vector" → 现代 RAG 不是 vector DB

**显著的工具流派分裂**:
- 厚框架 (CrewAI / AutoGen) vs 薄框架 (Pydantic-AI / 直接 SDK) — current visible main split
- Hosted RAG (Pinecone) vs Self-host RAG (Vespa / Qdrant) — splits along team-ops capability

**新兴工具信号**: 2 emerging (Pydantic-AI, Browser Use). Emergence-to-mainstream: 12-18mo (Cline 是参考样本).

**冷僻信号**: 8 tools is below 18 target — minimal-viable scope. ✅ industry not cold (real industry-wide tool count would be 30+).

### Workflows (03-workflows)
**反复出现 ≥ 3 个 workflow 都包含的步骤** (候选 playbook 通则):
- "Build evaluation dataset before / alongside the agent" (RAG / observability / audit-fix)
  → 候选 playbook: 「如果开始一个新 agent workflow，先 build eval set 再写 agent」
- "Instrument with traces from day 1" (observability / multi-agent / audit-fix)
  → 候选 playbook: 「如果项目过 demo 阶段，必须有 trace pipeline」

**入门 SOP 和资深路径之间最大的差距**:
- 入门 SOP 平均 5 步, 资深路径压缩到 3 步
- 跳过最多的 step 类型: "premature 优化阶段" (Chroma → Pinecone, complete instrumentation)
- → 心智模型候选: 「在 LLM agent infra, dev-time 选择不要 commit production 路径，一开始就走 production-relevant 选型」
- → 也是 "Production reality vs demo glamour" 心智模型的 workflow 化表达

**近期工作流变化的根本原因**:
- 触发分布: 工具竞争 (2) / 模型能力升级 (2) / 法规 (0)
- 主要驱动力: **工具竞争 + 模型能力曲线**

**冷僻信号**: 3 workflows is at floor (target 7), minimal-viable scope. ✅ industry not cold.

### Canon (04-canon)
**反复出现 ≥ 3 个 canon 都讨论的核心 idea** (候选行业心智模型):
- "Build evaluation before/alongside agent" (Huyen / Husain / Yan / Karpathy course)
  → 候选心智模型「在 LLM era, eval data 比 model architecture 重要」
- "Tool use as primitive, not feature" (ReAct / Toolformer / DSPy)
  → 候选心智模型「Agent = LLM + tools + eval loop, 不是 LLM + prompt eng」
- "RAG ≠ vector DB" (RAG paper + Vespa case studies + 多本书)
  → 候选 playbook 「不要把 RAG 等同于 vector DB; hybrid + reranking 是 production-grade 起点」

**智识谱系种子**:
- 流派 A: "Symbolic / structured" — DSPy + Pydantic-AI + 学院派 — 主张声明式、可验证的 agent 结构
- 流派 B: "Emergent / capability-driven" — Karpathy + Anthropic agent docs — 主张相信模型 capability，少加抽象
- 主要分歧: framework 的角色 — 应该是「编排器」还是「最薄的 type-safe wrapper」？
- 与 Track 01 figures 的「thin vs thick framework」分裂呼应

**冷僻信号**: 8 entries below 22 target — minimal-viable scope. ✅ industry not cold.

### Sources (05-sources)
**「这一行的资深人订阅最多的 top 3 sources」**:
1. Latent Space (newsletter + pod) — anchor publication
2. Eugene Yan newsletter — eval-focused
3. Ahead of AI / Cognitive Revolution — research/strategy view

→ master skill 「想跟最新动态」节直接列出

**「最近 3 个月话题热度」** (workflow change signals — confidence low because sources listed but content not deep-crawled):
- Browser-use vs Stagehand selection (multiple sources)
- CrewAI / AutoGen production critique
- Agent eval methodology evolution (LLM-as-judge → behavioral)
- Topic-heat: incomplete (sources listed but content not crawled)

**新 figures 候选** (喂给 wave 2 Track 01):
- Eugene Yan, Sebastian Raschka — already aware (in Track 01 candidate pool but not retained-5; could promote in non-minimal-viable run)
- Nathan Labenz — could add

**冷僻信号**: 8 sources is below 23 target — minimal-viable scope. ✅ industry not cold.

### Glossary (06-glossary)
**行业表达 DNA 直接素材** (喂给 Phase 2.5):

高频黑话 top 10:
1. RAG (单音节)
2. ReAct (双音节, "ree-act")
3. eval
4. trace
5. ship (动词)
6. in production
7. spaghetti agent (吐槽词)
8. thin / thick framework
9. eval-driven
10. agent-shaped problem (Willison 自创)

行业拒绝的厂商话术 top 5:
1. AI-powered
2. Cognitive computing
3. Intelligent automation
4. Agentic transformation
5. Human-in-the-loop AI (用 HITL 缩写代替)

外行破绽 top 10:
1. 念 "R-A-G" 而不是 "rag"
2. LLM = ChatGPT
3. 「在 production」滥用
4. RAG = vector DB
5. fine-tune 一下就好
6. agent vs assistant 混用
7. 「让 AI 自动做 X」(missing eval/trust layer)
8. ReAct 当具体 algorithm
9. tool use 当 framework feature
10. HITL 当 afterthought

**智识谱系线索**:
- MCP vs vendor function-calling: open-protocol vs proprietary 流派
- ISO/IEC 42001 + EU AI Act + self-governance: regulation-first vs innovation-first

**时效性信号**:
- 12 个月内已修订: EU AI Act 实施细则、MCP v0.2、各 model provider tool-use API
- 12 个月内预计变化: MCP 大版本、EU AI Act fully-apply Tier 1 (2026-08), 中国备案制度细则
→ master skill 时效衰减信号: HIGH

**workflow 触发种子** (喂给 Track 03 review):
- EU AI Act 2026-08 fully apply → "在 EU 部署 agent" workflow 大改
- MCP 大版本 → 任何 agent client implementation 都要重写

**冷僻信号**: 15 entries below 26 target — minimal-viable scope. ✅ industry not cold.
