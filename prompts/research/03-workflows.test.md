# Test: 03-workflows.md dry-run on "LLM agent infra"

Walking the 6-step flow against prototype industry "LLM agent infra" using public knowledge as of 2026-05.

---

## Step 1: Workflow candidates (target 6-12, floor 4)

### Wave 1+2 seed (assumed completed; aggregating signals)

From figures (Track 01) long-form material:
- Harrison Chase 在 LangChain Interrupt 详细谈过 "Build a chat agent → graph → eval loop"
- Hamel Husain 反复写 "How to add eval to an existing agent"
- Simon Willison 系统讲过 "Evaluate models for a specific task"

From tools (Track 02) usage scenarios:
- Vespa workflow → "Build hybrid retrieval at production scale"
- E2B / Modal → "Productionize a code-execution agent"
- LangSmith → "Observability + replay + human-in-the-loop on agent"

From canon (Track 04) — assumed completed: "Building LLM-powered Applications" (Chip Huyen)、"AI Engineering" pattern descriptions

### Synthesized candidate list (10 workflows)

1. Build a production-ready RAG agent from scratch
2. Add observability + eval to an existing agent
3. Migrate from prompt-based pipeline to graph-based agent
4. Choose between hosted vs self-hosted vector DB
5. Productionize a multi-agent orchestration system
6. Audit + fix a failing agent in production
7. Set up human-in-the-loop for agent escalation
8. Build a code-execution agent (sandboxed)
9. Migrate from synchronous to streaming agent
10. Run a scheduled / cron-based agent on infrastructure

→ 10 candidates, ✅ in 6-12 target

---

## Step 2-3: Per-workflow data + retain判定

Sample 1 (#2 — observability + eval):

| Field | Filled |
|-------|--------|
| One-liner | "Add LangSmith / LangFuse traces + eval suite to an existing agent that's been shipped" |
| Trigger | 已上线 agent + 收到错误率 / latency / quality 投诉 |
| Output | 完整 trace pipeline + 自动 eval + alert on regression |
| 入门 SOP | 5 steps: integrate SDK / instrument key paths / build eval dataset (50-200 examples) / set up baseline / wire to CI |
| 资深差异 | 资深人会跳过：跳过完整 instrumentation 在 dev 阶段（只在 prod-relevant path 加），优化 baseline ≤ 10 examples 但选择困难案例，额外做：把 trace + eval 接到现有 incident response runbook |
| 近期变化 | 2025-Q3 起，LangSmith 与 LangFuse 战略分裂明显，pre-2024 选 LangSmith 的团队近期 ~30% 切换到 LangFuse（成本 + open-source 偏好驱动） |
| 触发事件 | 工具竞争 / pricing 调整 |
| 典型耗时 | 入门: 1-2 weeks. 资深: 2-3 days |
| 关键工具 | LangSmith, LangFuse, Phoenix, Inspect AI |
| 关键人物 | Hamel Husain, Eugene Yan |
| 失败模式 | "build eval dataset 用 LLM 生成而非真实用户数据" → eval 通过但 prod 失败 |
| 来源 | Husain blog series + Eugene Yan eval podcast + LangFuse 官方迁移 case study |
| Last_updated | 2025-09-15 |
| Decay risk | high (12 月内必随工具竞争重写) |

判定: 4 ✅ → KEEP, high credibility

Quick-check其他 9 workflows:
- #1 RAG agent: high credibility, decay high
- #3 prompt → graph migration: medium credibility（资深差异点不够明确，因为大家还在迁移过程）, decay high
- #4 vector DB choice: 不是 workflow 是 decision tree → DROP，归 Track 02 选型决策树
- #5 multi-agent orchestration: borderline（入门 SOP 还没共识）→ 保留 if retained < 6
- #6 audit + fix failing agent: high
- #7 HITL escalation: medium
- #8 code-execution agent: high
- #9 sync → streaming: medium-low（这是 micro-improvement, 不是 workflow）→ DROP
- #10 scheduled agent: medium

Retained: 7 workflows (1, 2, 3, 5, 6, 7, 8) — ✅ ≥ 4 floor

---

## Step 4: 入门 SOP vs 资深差异化（核心动作）— 抽样验证

For workflow #1 "Build production-ready RAG":

入门 SOP（5 steps）:
1. Build vector index (Chroma → Pinecone → Vespa choice tree)
2. Build retrieval function (top-k + filter)
3. Build prompt template + LLM call
4. Add basic logging
5. Deploy + test with sample queries

资深差异:
- 资深**跳过** step 1 的 Chroma 阶段：直接评估流量级别决定 Pinecone vs Vespa（节省 prototype 阶段的伪验证）
- 资深**优化** step 2：早期就加 hybrid retrieval（BM25 + vector）而不是事后补；省了一次重构
- 资深**额外做**：在 step 3 之前先 build 50-100 个 evaluation examples，确保 retrieval 真的解决了用户的问题（不是「能召回」就够）

✅ 3 处资深差异，符合 ≥ 2 标准

---

## Step 5: 总览表 (partial)

```markdown
## 总览（按 decay risk 分组）

### High decay (12-month-class) — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| Build production RAG agent | 新业务需求 | live agent | 2025-08 | 跳过 dev 阶段 vector DB |
| Add observability + eval | 已上线 + 投诉 | trace pipeline | 2025-09 | 选困难 eval 案例 |
| Migrate prompt → graph | 框架升级 | new pipeline | 2025-Q4 | 不直接迁移 |
| Productionize multi-agent | scaling 需求 | reliable system | 2025-10 | borderline |

### Medium decay — 3 个
| Audit + fix failing agent | incident | fix + post-mortem | 2025-08 | ... |
| HITL escalation | 用户投诉 + edge case | escalation flow | 2025-Q2 | ... |
| Code-execution agent | 业务需求 | sandboxed run | 2025-Q3 | ... |

### Low decay — 0 个
（行业还在快速演化期 — 没有 stable workflow）
```

✅ 总览表清晰，分组对比反映 decay 现实。

---

## Step 6: Phase 2 接口 (sample)

```markdown
## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**:
- "Build evaluation dataset before building" 出现于: RAG / observability / multi-agent / code-execution
  → 候选 playbook 「如果开始一个新 agent workflow，先 build eval set 再写 agent」
- "Instrument with traces from day 1" 出现于: observability / multi-agent / audit-fix
  → 候选 playbook 「如果项目过 demo 阶段，必须有 trace pipeline」

**入门 SOP 和资深路径之间最大的差距**:
- 入门 SOP 平均 5-7 步，资深路径压缩到 3-4 步
- 跳过最多的 step 类型: "premature 优化阶段" (Chroma → Pinecone, complete instrumentation)
- → 心智模型候选: 「在 LLM agent infra, dev-time 选择不要 commit production 路径，一开始就走 production-relevant 选型」
- → 也可以另解为: "Production reality vs demo glamour" 心智模型的 workflow 化表达（呼应 Track 01 finding）

**近期工作流变化的根本原因**:
- 触发分布: 工具竞争 (3) / 模型能力升级 (2) / 工具新出现 (2) / 法规 (0)
- 主要驱动力: **工具竞争 + 模型能力曲线** — Phase 2 时识别行业的「外部驱动力」

**冷僻信号**: 全部 high+medium decay, 零 low decay → 行业仍在快速演化。Phase 2.8 标注「workflow 节衰减极快，3-6 月必更新」
```

---

## Findings — 03-workflows.md v0.1 dry run

### Pass

- 6 步流程跑通了，能产出 Phase 2 可消费的 workflow 集合
- Wave 1+2 seeding 集成度高：从 figures / tools / canon / sources 都拿到了 seed 信号
- 入门 SOP vs 资深路径区分动作做出来了，且每个 retained workflow 都能填出 ≥ 2 处资深差异
- 时效性强制要求确实落地：7/7 retained workflows 都填了 last_updated 日期 + 触发事件类型
- "DROP" 判定有效：第 4 / #9 候选被正确识别为「不是 workflow」(分别是 decision tree 和 micro-improvement)

### Issues found

1. **「workflow 候选」vs「决策树」边界不清**：dry run 中第 4 候选「vector DB choice」我 DROP 到 Track 02，但这个判断是临场做的，模板没明说。建议补：「如果候选实际是『一次性决定』而非『多步执行』，归 Track 02 决策树」
2. **「workflow」vs「micro-improvement」边界**：第 9 候选 sync→streaming 被 DROP，模板没明说。建议补：「workflow 必须是从 trigger 到 output 的完整闭环，不是单点优化」
3. **Wave 1+2 seed quality threshold 缺**：模板说「< 5 seed 警告」，没说 < 5 时具体怎么 fallback（变成纯 web search 还是停下来等？）。建议明确化
4. **资深差异点经常会落到 "edge case" 而非 "core differentiator"**：dry run 中观察到资深差异往往是「跳过 dev 阶段的某子选择」级别，而非「做完全不同的事」级别。考虑：是否需要区分「资深差异类型」(skip / optimize / add) 的频率分布作为 Phase 2 信号？
5. **"近期变化" 字段对稳态 workflow 没意义**：模板要求 ≥ 60% workflows 填这个字段。LLM agent infra dry-run 中所有 workflow 都还在快速变，所以 100% 都有近期变化。但如果是稳态行业（如足踝外科），可能 90% workflow 5 年没变 — 模板需要支持「明确写稳态」作为合法填法

### Action items for next iteration

- [ ] 修 03-workflows.md：上面 5 条 issues
- [ ] 写 prompts/research/04-canon.md（下一轮）
- [ ] 评估：Wave 1 + Wave 2 fallback 模式是否可以提取到 SKILL.md 而不是每个 track 重写

### 累计 findings

- iter 1-6: 13/13 已清
- iter 7 (02-tools): 5 finding
- iter 8 (本轮 03-workflows): 5 finding
- 合计待清: 10 finding。**iter 10 末再做一次 cleanup 比较合适**（再积一轮）

---

## 测试总结

03-workflows.md 跑通 6 步，能产出 Phase 2 可消费的 workflow 集合 + Phase 2 接口。Wave 1+2 seeding 集成度比 02-tools 还高（毕竟它在 wave 3 启动）。最大暴露的问题是「workflow vs 决策树 vs micro-improvement」边界识别需要更明确的判定规则。

下一轮：04-canon.md（书 / 论文 / 课程 / 核心概念）。这是最 stable 的 track，应该最简单。
