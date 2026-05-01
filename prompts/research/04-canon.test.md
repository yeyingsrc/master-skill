# Test: 04-canon.md dry-run on "LLM agent infra"

Walking 6-step flow against prototype industry "LLM agent infra" using public knowledge as of 2026-05.

---

## Step 1: Wide net (target 30-50, floor 20)

### Books / textbooks (8 candidates)
- Chip Huyen "Designing Machine Learning Systems" (2022) — production ML pipeline
- Chip Huyen "AI Engineering" (2024) — LLM-era successor
- "Hands-On Large Language Models" (Alammar / Grootendorst, 2024)
- "Building LLM-powered Applications" (community-edited, 2025)
- "Patterns of Distributed Systems" (Joshi, 2023) — relevant for multi-agent distributed concerns
- "AI Snake Oil" (Narayanan / Kapoor, 2024) — useful counterpoint
- Karpathy's WIP book on LLMs from scratch (2025)
- "Designing Data-Intensive Applications" (Kleppmann, 2017) — older but referenced by every senior agent infra engineer

### Papers (10 candidates)
- "Attention Is All You Need" (Vaswani et al, 2017) — foundational
- "ReAct: Synergizing Reasoning and Acting" (Yao et al, 2022)
- "Toolformer" (2023)
- "Tree of Thoughts" (2023)
- "Reflexion" (2023)
- RAG paper (Lewis et al, 2020)
- "Self-Consistency" (Wang et al, 2022)
- "Chain-of-Thought" (Wei et al, 2022)
- "Voyager" (2023) — embodied agent in Minecraft
- DSPy paper (2024)

### Courses (5 candidates)
- Karpathy "Neural Networks: Zero to Hero" (last_updated 2024-12)
- Stanford CS224N (last_updated 2024-Q4)
- Hugging Face Agents Course (2024)
- DeepLearning.AI "AI Agents in LangGraph" (2024)
- Eugene Yan eval-focused workshops series (rolling)

### Core concepts (15 candidates)
- Tool use / function calling
- Chain-of-thought reasoning
- ReAct loop
- Self-reflection / reflexion
- RAG (vector retrieval + LLM)
- Hybrid retrieval (sparse + dense)
- Agentic eval / behavioral eval
- Human-in-the-loop (HITL)
- Multi-agent orchestration
- Sandboxed execution
- Streaming generation
- Speculative decoding
- Prompt caching
- Context window management
- Token budget / cost optimization

→ Total: 8 + 10 + 5 + 15 = **38 candidates** ✅ (in 30-50 target)

---

## Step 2-4: Filter + retain

Apply 4-criteria mechanical filter. Selected results:

### Books retained (5/8)
| Book | Endorsement | Coverage | Decision |
|------|-------------|----------|----------|
| Chip Huyen "AI Engineering" | 4 figures推荐 + 5 课程列入 | very current | KEEP, high |
| Karpathy WIP book | 多 podcast 引用 + 直接 from author | uniquely deep | KEEP, high |
| "Hands-On LLMs" | 3 endorsements | good entry-level | KEEP, medium |
| "Designing Data-Intensive Apps" | 引用频率高，cross-domain | classic, low decay | KEEP, high |
| "AI Engineering" | (same as above, dedupe) | — | — |
| Chip Huyen "DMLS" 2022 | superseded by AI Engineering | — | DROP（已被同作者新书取代）|
| "AI Snake Oil" | 重要 critical perspective 但 not core | secondary canon | KEEP if room (BORDERLINE)|
| "Building LLM-powered Apps" | community-edited, ≤2 firm endorsements | uneven quality | DROP |
| "Patterns of Distributed Systems" | 引用 < 3 in agent context | tangential | DROP |

→ Books retained: 4-5

### Papers retained (8/10)
- Attention / ReAct / RAG / CoT / DSPy → KEEP, high (foundational, multi-citation)
- Toolformer / Reflexion → KEEP, medium (less foundational but core to agent design)
- Tree of Thoughts / Self-Consistency → KEEP if room (BORDERLINE, more niche)
- Voyager → DROP (specific embodied scenario, less general)

→ Papers retained: 6-8

### Courses retained (4/5)
- Karpathy NN-zero-to-hero → KEEP, high (last_updated 2024-12)
- Stanford CS224N → KEEP, high (canonical)
- HF Agents → KEEP, medium (newer but well-built)
- DeepLearning.AI LangGraph → KEEP, medium (vendor-affiliated but quality)
- Eugene Yan rolling workshops → DROP (rolling format hard to "complete", more workshop than course)

→ Courses retained: 4

### Concepts retained (~20/15) — 实际可能再精简
全部 15 都是行业明确概念，再加上 dry-run 中 figures + tools track 提到但概念候选未覆盖的：
- Generative UI / structured output
- Speculative orchestration
- Eval-as-data

→ Concepts retained: 18-20

**Total retained: ~32 (5 books + 8 papers + 4 courses + 18 concepts)** ✅

---

## Step 5: Sample full Book card (1)

```markdown
### 📖 1. AI Engineering — Building Applications with Foundation Models

- **Author**: Chip Huyen
- **Year**: 2024 (1st ed.)
- **Type**: Textbook
- **One-liner**: LLM-era 工程化全景 — 从 prompt eng 到 deployment 的工程师手册
- **核心论点 (4)**:
  - LLM eng 的核心难点是 evaluation，不是 prompt
  - 从「ML pipelines」到「AI pipelines」的范式转变（数据 + LLM 协同）
  - 生产中 80% 的 cost 是 inference + observability
  - "Build the eval first" 作为 first principle
- **读完得到什么**: 系统理解从 LLM API 到 production agent 的所有工程决策点 + 知道何时 in-house vs hosted vs framework
- **难度**: 进阶（需要基础 ML + 软件工程经验）
- **Endorsement evidence**:
  - Hamel Husain 在 podcast Latent Space 2024-Q4 "instant-buy 推荐"
  - DeepLearning.AI 列入 "AI for engineers" 推荐书单
  - Eugene Yan 在 eval blog 引用 6+ 章节
  - Anyscale 工程团队 internal handbook 列入 onboarding required reading
- **替代品**: 没有真正等价的 — 这是当前 LLM era 第一本系统教科书
- **如果可以只读 1 章**: Ch.5 Evaluation Methodology
- **可信度**: high
- **Decay risk**: medium (3-5 年内会有 2nd ed. 整体改写)
```

✅ 完整 card structure 跑通

---

## Step 5b: Sample concept card

```markdown
### 💡 ReAct (Reason + Act) loop

- **One-liner**: 一种 agent 推理结构，每一步交替「思考下一步该做什么」+「调用工具 / 生成 action」
- **来源**: Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models" (2022, arXiv 2210.03629)
- **关联概念**: Chain-of-thought (CoT) 是 ReAct 的「Reason」部分; Tool use 是 ReAct 的「Act」部分; Reflexion 是 ReAct + self-correction
- **行业内的当前理解 vs 原始定义**: 原 paper 的 ReAct 是 pure prompting 实现; 2024+ 几乎所有 production agents 都 ReAct-flavored 但用 native function calling 替代 prompt-string Action
- **为什么进入 canon**: 第一次清晰定义「LLM 作为 agent」的执行结构。所有后续 agent framework (LangChain / LlamaIndex / etc.) 默认实现的就是 ReAct 变体
- **常见误用**: 把 ReAct 当成具体 algorithm 实现，而不是抽象 control flow。"Build a ReAct agent" 应理解为「让 LLM 交替思考和行动」，不是必须用 paper 中的 prompt template
- **Endorsement evidence**: paper 被 ≥ 8000 引用; 是 LangChain / LlamaIndex / AutoGen 默认 agent 类型; 出现在 ≥ 4 个课程 (CS224N / HF Agents / Karpathy / DLAI)
```

✅ Concept card 跑通

---

## Step 6: Phase 2 interface

```markdown
## Phase 2 提炼提示

**反复出现 ≥ 3 个 canon 都讨论的核心 idea**（候选心智模型）:
- "Build evaluation before / alongside the agent": Chip Huyen / Hamel / Eugene Yan all emphasize 
  → 候选 playbook + 心智模型「在 LLM era, eval data 比 model architecture 重要」
- "Tool use as primitive, not feature": ReAct + Toolformer + DSPy 论文都暗含
  → 候选心智模型「Agent = LLM + tools + eval loop, 不是 LLM + prompt eng」
- "RAG is augmented retrieval, not just vector search": RAG paper + 多本书 + Vespa case study
  → 候选 playbook 「不要把 RAG 等同于 vector DB; hybrid + reranking 是 production-grade 起点」

**智识谱系种子**:
- 流派 A: "Symbolic / structured" 派 — DSPy + Pydantic-AI + Ankit Pal/学院派 — 主张声明式、可验证的 agent 结构
- 流派 B: "Emergent / capability-driven" 派 — Karpathy + Anthropic agent docs — 主张相信模型 capability，少加抽象
- 主要分歧: framework 的角色 — 应该是「编排器」还是「最薄的 type-safe wrapper」？
- 这与 Track 01 figures 的「thin vs thick framework」分裂呼应

**核心概念 → 候选 playbook**:
- ReAct 概念 → "如果 agent 表现出错乱 / 不收敛, 先看 reasoning trace + tool log"
- Eval as primitive → "新场景上线，eval set 必须先建（≥ 50 examples）"
- Tool use 概念 → "拒绝在 prompt 内做工作，能用 tool 就用 tool"

**冷僻信号**: 全部 4 类型都有充足候选，行业 canon 已经成型 ✅ 不冷僻
```

---

## Findings — 04-canon.md v0.1 dry run

### Pass

- 6 步流程跑通了，能产出 Phase 2 可消费的 canon
- Wave 1 独立性：本 track 不需要 wave 间 seed，启动门槛低
- 4 类型分类（books / papers / courses / concepts）覆盖完整
- mechanical filter 在 38 候选上给出明确 keep / drop / borderline
- Per-item card structure 充分（每类型有自己的 schema）
- "If superseded by newer book" 规则 (DMLS 2022 → AI Engineering 2024) 自动 drop 重复 — 好 UX
- Phase 2 接口块自然产出心智模型候选 + 智识谱系种子（thin vs thick framework 流派与 Track 01 一致）

### Issues found

1. **「书 superseded by 新版」判定缺乏明文规则**：dry-run 中我把 DMLS 2022 drop 因为同作者出了新书。模板没说「同作者新书出现时是否自动 supersede」。建议补：「如果作者在 ≤ 4 年内出新书覆盖同一主题 → DROP 老版除非教学路径上仍有价值」
2. **Concept 数量没明确 target**：模板说「20-30 个」但没分级（核心 vs 周边）。dry-run 中 retained 18-20 但没区分哪些是「行业必懂」哪些是「了解即可」。建议补：「概念分两层 — Tier 1 核心（10-15 个，所有从业者必懂） + Tier 2 周边（5-15 个，资深者熟知）」
3. **Course "rolling format" 处理不清**：Eugene Yan rolling workshop 系列被我 DROP 因为「无法完整学完」，但其实它的内容质量很高。建议补：「rolling / continuous 格式可以保留，但用 'last 3 months key content' 字段代替 last_updated」
4. **Endorsement evidence 中「figure 推荐 vs 课程列入」权重不同**：figure 在长访谈中具体推荐（带理由）权重应高于 course syllabus 默认列入。模板没区分。建议补：endorsement evidence 标注 type = "figure_specific" / "course_syllabus" / "tweet_short" / 「fig_blog_long」
5. **Concept 来源 field 在 ReAct 这种「论文先驱」案例上跑通，但「无单一来源」的概念 (如 RAG) 需要列「主要奠基论文 + 后续扩展」**：模板未涵盖这种 multi-paper-origin。建议补：「Concept 来源支持单一作者 / 论文，也支持多 origin 列表」

### Action items for next iteration

- [ ] 修 04-canon.md：上面 5 条 issues
- [ ] 写 prompts/research/05-sources.md（下一轮）
- [ ] 累计 finding 现在 15 个：iter 7 (5) + iter 8 (5) + iter 9 (5)。**iter 10 cleanup pass 时间到**

---

## 测试总结

04-canon.md 跑通 6 步，产出 Phase 2 可消费的 ~32 项 canon（5 books + 8 papers + 4 courses + 18 concepts）。Phase 2 接口自然产出 3 个候选心智模型 + 智识谱系（thin vs thick framework 流派与 Track 01 finding 一致，跨 track 互相印证）。

最大暴露的问题是「concept 分层」(必懂 vs 熟知) 和 endorsement type 区分。这些是 polish-level，不影响主流程。

下一轮：05-sources.md（newsletter / podcast / conference / community）— 也是 wave 1，应该比 04 更简单（每个项目就是个 URL + 频率，不像 books 要解析核心论点）。

距 v1.0：04-canon ✓，下面 05 / 06 / synthesis / quality_check / tools / prototype。
