# Test: 06-glossary.md dry-run on "LLM agent infra"

Walking 6-step flow against prototype industry "LLM agent infra" using public knowledge as of 2026-05.

---

## Step 1-2: Wide net + 5-type distribution

LLM agent infra 是技术行业，预期分布：术语 + 缩写多，标准少（行业还在形成 spec），法规仅 1-2 个（AI Act 等），认证几乎没有。

### Term / 术语 (target: 大部分 — 25-40)
- ReAct (loop) — Tier 1
- Chain-of-Thought (CoT) — Tier 1
- Retrieval-Augmented Generation (RAG) — Tier 1
- Tool use / function calling — Tier 1
- Agent / Autonomous agent — Tier 1
- Multi-agent orchestration — Tier 1
- Self-reflection / Reflexion — Tier 1
- Hybrid retrieval (sparse + dense) — Tier 1
- Vector embedding — Tier 1
- Prompt engineering — Tier 1
- In-context learning (ICL) — Tier 1
- Few-shot / zero-shot — Tier 1
- Eval / behavioral eval / LLM-as-judge — Tier 1
- Fine-tuning / LoRA / RLHF — Tier 1
- Streaming generation — Tier 1
- Token budget / context window — Tier 1
- Speculative decoding — Tier 2
- Prompt caching — Tier 2
- Structured output / JSON mode — Tier 2
- Generative UI — Tier 2
- HITL (Human-in-the-loop) — Tier 2
- Agentic RAG — Tier 2
- Reranking — Tier 2
- Sandboxed execution — Tier 2
- Trace / span (in observability context) — Tier 2

→ Term: 25 candidates

### Acronym / 缩写 (target: 8-15)
- LLM, RAG, RLHF, ICL, MoE, KV (cache), CoT, HITL, FSDP, LoRA, MCP, SDK, SLA, TTS / STT (boundary, applies if covering speech)

→ Acronym: 12-14

### Standard / 标准 (target: 3-8 — LLM agent infra has emerging spec landscape)
- OpenAPI 3.x (used as tool calling spec underlay)
- MCP (Model Context Protocol, Anthropic 2024)
- OpenAI Tool Calling spec (de facto)
- LangChain LCEL (vendor spec but widely adopted)

→ Standard: 4

### Regulation / 法规 (target: 2-4)
- EU AI Act (2024)
- China 生成式人工智能服务管理暂行办法 (2023-08)
- US Executive Order on Safe AI (2023)
- ISO/IEC 42001 (AI management standard, 2023)

→ Regulation: 4

### Certification / 认证 (target: 0-2)
- ISO/IEC 42001 (mentioned above as standard, can also be cert)
- (no widespread Anthropic / OpenAI dev certifications yet)

→ Certification: 0-1 (mostly N/A)

**Total: ~45 candidates** ✅ (above floor 40)

---

## Step 3-5: Filter + retain (apply 4-criteria)

Sample 5 retained entries:

### 1. RAG (Retrieval-Augmented Generation) — Tier 1, term

```markdown
- **Type**: term + acronym (2 in 1)
- **Tier**: tier-1
- **Definition (insider)**: 在 LLM 调用前先 retrieve 相关 context 喂入 prompt 的 architecture pattern. 实操上是 retrieval pipeline + LLM call 的组合
- **Definition (outsider-friendly)**: AI 回答问题时先查资料再回答的方法，减少胡编 (hallucination)
- **Etymology**: Lewis et al. 2020 paper "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- **常见误用 (outsider-tell)**:
  - 误用 1: 把 RAG 等同于「用 vector DB」 — 内行 RAG 包含 hybrid retrieval, reranking, query expansion 等多层
  - 误用 2: 缩写发音 — 念 "rag" (一个音节) 而不是 "R-A-G" (三个字母)，绝大多数内行口语用前者
- **关联术语**: hybrid retrieval, reranking, vector DB, embedding, agentic RAG
- **是否被错位包装**: Pinecone / Weaviate / Chroma 经常把自家产品营销成「the RAG database」, 实际上 RAG 不只是 vector DB 这一层
- **Source**: Lewis et al. 2020 / Vespa engineering blog / Track 04 canon
- **可信度**: high
- **Decay risk**: low (定义稳定，但 RAG 的实操内涵在演化 — 「裸 RAG → agentic RAG」是范式 shift)
```

### 2. MCP (Model Context Protocol) — Tier 1, standard

```markdown
- **Type**: standard
- **Tier**: tier-1
- **Definition (insider)**: Anthropic 2024-Q4 提出的 client-server protocol，让 LLM 客户端 (Claude Desktop, Cursor, etc.) 能 plug-and-play 不同的 tool / context 提供方
- **Definition (outsider-friendly)**: 像 USB 之于硬件 — 让 AI 应用能统一接入各种工具和数据源的标准
- **Etymology**: Anthropic blog post 2024-11 (Model Context Protocol)
- **常见误用**:
  - 把 MCP 跟 OpenAI Function Calling 混用 — 实际上是不同 layer (MCP 是 protocol, function calling 是 API spec)
- **关联术语**: tool use, function calling, OpenAPI
- **变化历史**:
  - 2024-11 release v0.1
  - 2025-Q2 v0.2 加入 progress notifications
  - 2025-Q4 LangChain / OpenAI 都开始原生支持
- **Source**: anthropic.com docs + GitHub spec repo
- **可信度**: high
- **Decay risk**: medium — protocol 还在 active 演化, 大版本可能在 2026-2027 年出现
```

### 3. EU AI Act — Tier 1, regulation

```markdown
- **Type**: regulation
- **Tier**: tier-1
- **Definition (insider)**: 全球首个 comprehensive AI 监管框架，按风险分级 (banned / high-risk / limited / minimal)，对 foundation model providers + 高风险 AI 系统 (含 agent infra 应用) 设置义务
- **Definition (outsider-friendly)**: 欧盟的 AI 法律，规定 AI 不能做什么 + 高风险 AI 怎么做才合规
- **Etymology**: EU Parliament adopted 2024-03, enters into force 2024-08, fully applicable 2026-08
- **常见误用**:
  - 误用 1: 「AI Act 只管 EU 内的公司」 — 实际上 extraterritorial，类似 GDPR，影响 AI 在 EU 提供服务的所有公司
  - 误用 2: 「foundation model + GPAI 是同一回事」 — Act 区分了 GPAI 和具体 application
- **变化历史**: 2024-03 adopt → 2024-08 force → 2026-08 full apply (Tier 1) → 2027-08 full apply (Tier 2)
- **Source**: official EU Council document + 多个 law firm 长稿解读
- **可信度**: high
- **Decay risk**: high — 实施细则 (delegated acts) 在过去 12 月内多次更新，未来 12 月仍会
```

### 4. CoT (Chain-of-Thought) — Tier 1, term + acronym

```markdown
- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 让 LLM 在最终答案前显式生成中间推理步骤的 prompting 技术. 现在更多指 reasoning trace
- **Outsider def**: 让 AI 一步步思考再回答，提高复杂问题准确率
- **常见误用**: 把 CoT prompt template 死记硬背成「请一步步思考」 — 现代 frontier model native CoT, 显式 prompt 反而可能 lower performance
- **Etymology**: Wei et al. 2022 "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- **关联术语**: ToT (Tree of Thoughts), self-consistency, reasoning trace, o1-style reasoning
- **Source**: paper + canon book
- **可信度**: high
- **Decay risk**: low (concept) / medium (exact prompt patterns are decaying as native reasoning models replace explicit CoT prompting)
```

### 5. "Trace" (in agent observability context) — Tier 2, term

```markdown
- **Type**: term (with overload concern)
- **Tier**: tier-2
- **Definition (insider)**: 在 agent observability 语境中，trace = 一个 agent 完整执行路径的结构化记录 (跨越多个 tool calls / sub-agents / LLM hops)
- **Outsider def**: AI agent 跑一次的完整足迹日志
- **常见误用**:
  - 误用 1: 把 trace 跟「log」混用 — log 是平铺文本，trace 是结构化的 hierarchical span tree
  - 误用 2: 跟 distributed-system trace 混 — 来源虽然类似 (OpenTelemetry-inspired) 但 agent trace 关注 LLM call 的 input/output/tool selection 等 LLM-specific 字段
- **关联术语**: span, observability, eval, replay
- **Source**: LangSmith / LangFuse / Phoenix docs + Track 04 canon
- **可信度**: high
- **Decay risk**: medium — 行业标准还在形成，未来 12 月可能有 OTel-AI 这类新 spec 改变定义
```

→ 5 sample cards 全部跑通 ✓

---

## Step 6: Phase 2 interface (filled)

```markdown
## Phase 2 提炼提示

**行业表达 DNA 直接素材**:
- 高频黑话 top 10:
  1. RAG (单音节，不念字母)
  2. CoT
  3. ReAct (双音节, "ree-act")
  4. eval (动词 / 名词都用)
  5. trace (in obs context)
  6. ship (动词，发布上线)
  7. 「out of the box」(指 framework 没修改就能用)
  8. 「in production」 (生产 vs demo 的 register marker)
  9. 「spaghetti agent」 (吐槽设计混乱的 agent)
  10. 「thin / thick framework」 (流派词)
- 行业拒绝的厂商话术 top 5:
  1. 「AI-powered」 (太营销，内行用 LLM 或具体模型名)
  2. 「Cognitive computing」 (IBM Watson 时代遗留)
  3. 「Intelligent automation」 (RPA 包装)
  4. 「Agentic transformation」 (consultancy 话术)
  5. 「Human-in-the-loop AI」(被滥用，专业语境用 HITL 更精确)
- 外行破绽 top 10:
  1. 念 "R-A-G" 而不是 "rag"
  2. 把 LLM 跟 chatbot 等同
  3. 用 "GPT" 指所有 LLM (类似把 Kleenex 当通称)
  4. 「ChatGPT 调用 API」(ChatGPT 是产品, API 是 OpenAI Models)
  5. 「prompt engineering 是技术」(2023 后 register 已转向「prompt eng 是 craft, 不是 engineering 学科」)
  6. 「fine-tune 一下就好」(low-effort dismissal of complex process)
  7. 「让 AI 自动做 X」(missing the eval / trust / oversight layer)
  8. RAG = vector DB
  9. Agent vs assistant 混用 (内行严格区分)
  10. 「你这个 model 几亿参数？」(参数量已不是核心比较维度)

**智识谱系线索**:
- MCP 标准 vs vendor function-calling spec 之争 - "open vs proprietary protocol" 流派分裂
- ISO/IEC 42001 出现 + EU AI Act + 行业 self-governance 之争 - "regulation-first vs innovation-first" 流派

**时效性信号**:
- 12 个月内已修订: EU AI Act 实施细则、MCP v0.2、各模型 provider 的 tool-use API 多次小迭代
- 12 个月内预计变化: MCP 大版本、EU AI Act fully-apply Tier 1 (2026-08), 中国生成式 AI 备案制度细则更新
→ master skill 时效衰减信号: HIGH（法规 + 标准均处于 active 演化期）

**workflow 触发种子** (喂给 wave 3 Track 03):
- EU AI Act 2026-08 fully apply → workflow「在 EU 部署 agent」会大改
- MCP 大版本 → 任何 agent client implementation 都要重写
- China 备案细则 → 中文 locale 的 agent 上线流程会改

**冷僻信号**: 总术语 ~45 (>25 floor)，Tier 1 18+ (≥15)，外行破绽充足 ✅ 不冷僻
```

---

## Findings — 06-glossary.md v0.1 dry run

### Pass

- 6 步流程跑通了，~45 候选，5 个 type 按 LLM agent infra 类行业的预期分布 (Term + Acronym 大头，Regulation 4 个，Certification 几乎空 — 模板正确支持「N/A by industry type」)
- 5 sample card 全部填得起来，含完整 outsider-tell 字段
- "term + acronym" 双 type entry (RAG, CoT) 跑通 — 模板支持 multi-type
- "Disputed" 字段没在 dry-run 中触发但模板有规定（reasoning 模型的 CoT 是否仍然需要 prompt 在内行 disputed 但未触发严重分歧）
- Phase 2 接口产出极有价值的 outsider-tell top 10 + workflow 触发种子 + 时效信号

### Issues found

1. **Multi-type entry (RAG = term + acronym) 处理不一致**：dry-run 中我把 RAG 标为 "term + acronym" 但模板规定 type 是单选枚举。建议补：「entry 可标 multi-type，例 `type: term + acronym`，处理时分别走 term + acronym 的统计」
2. **「厂商错位包装」字段 evidence 缺**：模板说要标这个，但 dry-run 中我直接写「Pinecone 经常把 RAG 等同于 vector DB」缺具体 source 引用。建议补：每个错位包装 claim 必须有 source link，不能凭印象
3. **outsider-tell 字段在 100% retained tier-1 上有，但 tier-2 上有些没填**：模板说 50% 要填，但其实 tier-1 应该全填、tier-2 可以放宽。建议补：「Tier 1 必填 outsider-tell, Tier 2 推荐填」
4. **Acronym 发音误用是 outsider-tell 的子类**：dry-run 中我处理 "RAG" 念法 / "CoT" 全展开 / "ReAct" 重音 等都是 acronym 发音问题。建议在模板的「常见误用」字段下加显式子类: `pronunciation_tell` (针对 acronyms)
5. **「Standard / Regulation / Certification 时间轴」总览在 LLM agent infra 这种行业适用，但传统行业 (法规 50 年都没改) 表会很冗长**：建议补：「时间轴在近 5 年内有显著变化的标 / 法规才进入总览，长期稳定的简单列出 issued 年份」

### Action items for next iteration

- [ ] 修 06-glossary.md：上面 5 条 issues
- [ ] 累计 finding: iter 11 (5) + iter 12 (5) = 10 → iter 13 cleanup pass
- [ ] iter 13 cleanup 后进入 synthesis.md / quality_check.md（v0.2 收尾）

---

## 测试总结

06-glossary.md 跑通 6 步，产出 ~45 retained terms + 完整 Phase 2 接口。Outsider-tell 字段是 master skill 的金矿 — 直接喂给 Phase 2.5 (表达 DNA) 提炼。

法规与标准的时效信号在 LLM agent infra 这种 active-regulation 行业极强（EU AI Act + MCP + China 备案细则等都在 active 演化）— 这是诚实边界节的硬支撑。

距 v1.0：~3-6 iter（cleanup + synthesis + quality_check + tools + prototype）。

**v0.2 prompts/ 收尾**: 6 个 research template 全完成 ✓ + intake.md ✓。还差 synthesis.md + quality_check.md，然后 v0.3 tools 阶段。
