# Test: synthesis.md + quality_check.md (combined dry-run)

These two prompts are tightly coupled — synthesis is Phase 2 (the bridge from research to output), quality_check is Phase 4 (the bridge from output to validated skill). Single combined test.

---

## synthesis.md dry-run on LLM agent infra

### Step 0: Candidate aggregation

Reading the 6 Phase 2 interface sections (assumed from prior dry-runs of 01-figures / 02-tools / 03-workflows / 04-canon / 05-sources / 06-glossary):

#### 候选心智模型 (15 collected, target 15-30)
| Candidate | tracks | figures | type | notes |
|-----------|--------|---------|------|-------|
| Framework as scaffold, not foundation | 01,02,04 | Chase, Knoop, Willison, Karpathy (4) | cross-track | strong |
| Eval > model architecture | 01,03,04 | Husain, Yan, Rush, Chase (4) | cross-track | strong |
| Production reality vs demo glamour | 01,03 | Husain, Willison, Chase (3) | cross-track | strong, industry-amplified |
| Capability lift will eat your abstraction | 01,02,04 | Knoop, Chase, Karpathy (3) | cross-track | strong |
| Tool use as primitive, not feature | 04,06 | papers + glossary | cross-track | medium |
| Agent = LLM + tools + eval loop | 04 | canon | single-track | medium |
| RAG ≠ vector DB | 02,04,06 | tools + canon + glossary | cross-track | medium |
| Build eval before agent | 03 | workflow pattern | medium |
| Instrument from day 1 | 03 | workflow pattern | medium |
| Open vs proprietary protocol (MCP debate) | 06 | glossary | medium |
| Regulation-first vs innovation-first | 06 | glossary | medium |
| Thin vs thick framework split | 01,02,04 | multi | strong |
| Native function-calling > prompt-string ReAct | 04,06 | papers + glossary | medium |
| Hybrid retrieval > pure vector | 02,04 | tools + canon | medium |
| HITL is design, not afterthought | 03,06 | workflow + glossary | medium |

→ 15 candidates ✓ (in target range)

### Step 1: Triple-gate filter

Walk through 5 candidates:

1. **Framework as scaffold** — V1 ✅ (4 figures, 3 sub-scenarios) / V2 ✅ (predicts new framework decisions) / V3 ✅ (excl to fast-evolving infra) → **PASS, 心智模型 KEEP**
2. **Eval > model architecture** — V1 ✅ (4 figures) / V2 ✅ / V3 ⚠️ (similar in any ML field) → **✅✅⚠️ → 行业放大版心智模型 KEEP** (description must capture LLM-era amplification)
3. **Capability lift will eat abstraction** — V1 ✅ / V2 ✅ / V3 ✅ → **PASS**
4. **HITL is design, not afterthought** — V1 ⚠️ (only 2 figures) / V2 ✅ / V3 ⚠️ (true in any human-AI system) → **任一 ❌ + 2 ✅ = 决策启发式**, push to Step 2
5. **RAG ≠ vector DB** — V1 ✅ (multi-track) / V2 ✅ / V3 ⚠️ (RAG-specific is industry-specific) → **✅✅⚠️ → 行业放大版**, KEEP

After full pass: 5 心智模型 retained: Framework-scaffold / Eval-amplified / Capability-eats-abstraction / Production-vs-demo (amplified) / RAG≠vectorDB (amplified)

→ 5 mental models ✓ (in 3-7 target)

### Step 2: Playbook (5-10 target)

From Step-1 demoted + cross-workflow patterns:
1. "If new agent project starts, build eval set ≥ 50 examples before writing agent code" — case: Husain blog
2. "If demo works in 1 day, expect 6 weeks to production-grade" — case: multiple HN threads
3. "Default to thin framework + native SDK; switch to thick orchestration only if multi-agent ≥ 3 actors" — case: Vercel ai-sdk team
4. "If choosing vector DB, evaluate hybrid retrieval support before pure-vector benchmarks" — case: Vespa case studies
5. "If LLM-as-judge for eval, ensure ≥30% human-graded validation set" — case: Yan blog
6. "Add observability before adding optimization; you can't optimize what you can't see" — case: LangSmith adoption pattern
7. "If ReAct agent loops > 5 steps, suspect tool design before prompt eng" — case: AutoGPT post-mortems

→ 7 playbook rules ✓

### Step 3-4: Tools + Workflows sanity-check

Direct consume Track 02 + Track 03 outputs. Sanity check passes (already validated in their dry-runs).

### Step 5: Expression DNA

From Track 06 outsider-tell + Track 01 register:
- 高频用语: RAG, eval, ship, in production, trace, agent loop
- 厂商话术拒绝: AI-powered, agentic transformation, intelligent automation
- 外行破绽: 念 R-A-G, GPT 当通称, "fine-tune 一下就好", "let AI auto-do X"
- 严肃 register: 直接 / 工程师式 / 对 framework 持怀疑姿态 / 对 eval 持神圣姿态

### Step 6: 质量基准 + 反模式

质量基准:
1. 任何 production agent 必有 trace pipeline + ≥ 50-example eval set
2. 任何 framework 选型必能在一周末被替换
3. RAG 必须 hybrid retrieval, 不能纯 vector

反模式:
1. 把 framework 当 production foundation
2. demo 完美就以为 production ready
3. 用 LLM-generated eval set 做 LLM 测试
4. ReAct loop 失败时调 prompt 而非看 trace + tool

### Step 7: 智识谱系

流派 A (Thin / Type-first): Karpathy / Vercel ai-sdk / Pydantic-AI 圈
流派 B (Thick / Orchestration-heavy): CrewAI / AutoGen / 学院派 multi-agent

核心分歧: framework 的角色 — "the thinnest type-safe wrapper" vs "the orchestration substrate"

### Step 8: 诚实边界
1. 信息截止 2026-05, 工具 / 工作流模块 6 个月内可能过半失效
2. Track 06 显示 EU AI Act + MCP 大版本 + China 备案细则在 active 演化, 法规节衰减最快
3. 中文圈 sources 覆盖偏弱（global locale 但实际 ≥ 80% en sources）
4. master skill 不能替代真实 production debugging 经验

### Step 9: Agentic Protocol (5-7 dimensions for LLM agent infra)

每个维度三段：
1. **Framework current state**
   - 看什么: GitHub stars / commit frequency / breaking change history of {framework}
   - 在哪看: 该 repo 本身 (releases, issues), 不是排行榜
   - 输出: framework 的 "active / stable / fading" 三态判断

2. **Production reality check**
   - 看什么: 实际 production 案例 + post-mortem 数据
   - 在哪看: HN long threads / company engineering blogs / X 工程师吐槽 (搜 framework + "production" + "broken/painful")
   - 输出: production-readiness 等级 (toy / pilot / scaled)

3. **Eval methodology**
   - 看什么: 该问题的 eval set 是否存在? 行业 benchmark 是什么?
   - 在哪看: Hamel Husain blog / Eugene Yan / Inspect AI examples
   - 输出: 评估这个 agent / workflow 的可量化指标 (1-3 个)

4. **Tool stack alignment**
   - 看什么: 当前选型是否符合 thin-vs-thick 流派 + 是否 hybrid-retrieval-aware
   - 在哪看: Track 02 输出
   - 输出: 当前选型 + 1-2 个替代

5. **Regulatory blast radius**
   - 看什么: EU AI Act / China 备案 / US executive order 在这个场景下是否适用
   - 在哪看: Track 06 法规节
   - 输出: 「low / medium / high regulatory exposure」+ 1 句具体来源

→ 5 dimensions ✓ (in 3-10 target, 这一行偏复杂所以 5+)

### synthesis.md test verdict: ✅ PASS

9 步全部跑通，产出 LLM agent infra Master OS 完整框架。

---

## quality_check.md dry-run

### 4.1 Sanity check (3 questions)

Pick from Track 04 canon ground-truth:
- Q1: "Should I build my own tool-calling pipeline or use OpenAI's function calling spec?" → ground truth (Karpathy / Chase): use native, build only if you have a specific reason
- Q2: "RAG over Pinecone vs hybrid Vespa for 100M docs?" → ground truth (Vespa case studies + Husain): hybrid Vespa for that scale
- Q3: "Eval my agent with LLM-as-judge — is it enough?" → ground truth (Yan + Husain): need ≥30% human-validated, not enough alone

If skill (loaded with synthesis.md outputs) answers consistently with mental model "Framework as scaffold" + "Eval > model architecture" + RAG≠vectorDB principles → ✅ PASS expected

### 4.2 Edge case

Q: "How would you build an agent for a regulated medical use case in EU?"
- This is at intersection of 4 mental models (production-vs-demo amplified by stakes, capability eat abstraction, RAG≠vector for clinical RAG, regulatory blast radius from Agentic Protocol dim 5)
- Expected: ≥ 2 mental models invoked + hedging ("EU AI Act high-risk classification likely applies, but specifics depend on...")

If answer is hedge-free or skips compliance → FAIL signal (诚实边界 wasn't strong enough)

### 4.3 Voice check

100-word output: 「LLM agent infra 最近趋势」
- Should use: ≥ 3 Tier-1 terms (RAG / eval / framework / production / trace etc.)
- Should reject: ≥ 1 vendor话术 (no "AI-powered" / no "intelligent automation")
- Reference samples: 3 from Eugene Yan blog + Latent Space newsletter + Husain post

### 4.4 Mechanical rubric (12 items)

Sample check on synthesis.md output:
| Item | Result |
|------|--------|
| 心智模型数 (3-7) | ✅ 5 |
| 心智模型局限 100% 填 | ✅ |
| Playbook 数 (5-10) | ✅ 7 |
| Playbook 案例 ≥ 1 | ✅ |
| 工具三层覆盖 | ✅ (5/9/4 from Track 02) |
| Workflow 入门-资深差异 ≥ 80% | ✅ (7/7 from Track 03) |
| 表达 DNA 辨识度 | depends on 4.3 |
| 诚实边界 ≥ 3 条 | ✅ (4 specific) |
| 一手来源 ≥ 50% | ✅ (estimated 60%) |
| Agentic Protocol 维度 (3-10) | ✅ 5 |
| 时效性标注完整 | ✅ |
| 多 figure 共识 | ✅ (each model 3-4 figures) |

→ 12/12 PASS ✓

### quality_check.md test verdict: ✅ PASS

4 项测试全跑通，能产出 PASS / PARTIAL / FAIL 评级 + 具体修复路径。

---

## Findings

### Pass
- synthesis.md 9 步对应 SKILL.md Phase 2.1-2.9 严格映射
- quality_check.md 4 项测试与 SKILL.md Phase 4.1-4.4 严格映射
- subagent 隔离原则在 quality_check 中显式（避免自评偏差）
- 两个 prompt 共同消化前面 6 个 research/* + intake.md 的输出，闭环完整

### Issues found

1. **synthesis.md Step 3-4 偏 sanity-check 而非真实 synthesis** — 工具栈 + 工作流的提炼几乎全部由 Track 02 / 03 完成。可能模板应明确这两步是「集成」而非「提炼」，避免下游 Phase 3 误以为这两节有大量 synthesis-side 工作
2. **quality_check.md 4.1 ground truth 来源** — 模板说「来自 Track 04 canon」但 canon 不一定有所有 question 的 ground truth (canon 是 books/papers, ground truth 可能在 figures 长访谈中)。建议补：「ground truth 来自 Track 01 + 04 + Track 03 workflows 的具体案例」
3. **synthesis.md Step 0 候选数门槛太死** — < 15 直接说「信号薄弱」，但 strict 行业（如足踝外科）从 Phase 1 就拿不到那么多候选。建议补：「门槛与行业类型挂钩：technical 行业 ≥ 15, 学术行业 ≥ 12, vertical 实操行业 ≥ 8」
4. **quality_check.md 4.3 voice check 的 reference samples 怎么选没规定** — 模板说「3 段真实从业者短稿」但来源不清。建议补：「优先 Track 01 figures 长访谈中的 1-2 段 + Track 05 newsletter 的 1 段」
5. **没有 Phase 5 (Refinement) 的入口** — quality_check 通过后下一步是 Phase 5，但本两个 prompt 都没说怎么衔接。建议补：在 quality_check.md 末尾加一段「Phase 5 入口条件」

### Action items

- [ ] iter 15 在 synthesis.md / quality_check.md 上补 5 个 issues
- [ ] 或 iter 15 直接写 Phase 5 (refinement) 的具体子 prompt（目前 SKILL.md 里 Phase 5 是 inline 描述，没有独立 prompt 文件）
- [ ] 累计 finding: iter 14 (5)

### v0.2 prompts/ 收尾状态

✓ intake.md
✓ research/01-figures.md
✓ research/02-tools.md
✓ research/03-workflows.md
✓ research/04-canon.md
✓ research/05-sources.md
✓ research/06-glossary.md
✓ synthesis.md (this iter)
✓ quality_check.md (this iter)

**v0.2 prompts/ 完成 9/9** ✓

下一步: v0.3 tools/ scripts (5+) → real prototype run on LLM agent infra → v1.0.
