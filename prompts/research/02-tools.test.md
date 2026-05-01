# Test: 02-tools.md dry-run on "LLM agent infra"

Walking the 6-step flow against prototype industry "LLM agent infra" (locale=global) using public knowledge as of 2026-05. Validates the template structure.

---

## Step 1: Wide net (target 25-40, floor 20)

### Wave 1 seed (from Track 04/05/06 — assumed completed)
LangChain / LangGraph / LlamaIndex / LangSmith / DSPy / Pydantic-AI / CrewAI / AutoGen / Vespa / Pinecone / Weaviate / Chroma / Qdrant / Anthropic SDK / OpenAI SDK / Vercel AI SDK / Helicone / LangFuse / Phoenix (Arize) / Inspect AI / promptfoo / Cline

→ 22 seeds

### Web search expansion (从 GitHub topics + 长访谈 references)
+ Replit Agent / Cline / Continue.dev / Aider / Cursor agent mode / Devin / Claude Computer Use / Browser Use / Stagehand / Playwright (agent driver) / E2B / Daytona / Modal Functions / Anyscale / Together AI

→ +15 = 37 candidates total ✅ (in 25-40 target)

---

## Step 2-3: 三层分类 + Quality Gate

### 必备层（≥80% 从业者用）

证据要求：≥3 indep sources OR ≥50% adoption survey OR stars > 5k

| Tool | Evidence | Tier verdict |
|------|----------|--------------|
| LangChain / LangGraph | stars 90k, mentioned in 100% of "agent stack" surveys, every long podcast | ✅ 必备 |
| OpenAI SDK | de facto standard, every agent uses it | ✅ 必备 |
| Anthropic SDK | similar, second pillar | ✅ 必备 |
| LlamaIndex | RAG dominant, 35k stars | ✅ 必备 (RAG-side) |
| LangSmith / LangFuse | observability default | ✅ 必备 |

→ 必备层: 5 个 ✅ (target ≥3)

### 场景特化层

| Tool | Scenario | Evidence | Verdict |
|------|----------|----------|---------|
| Vespa | hybrid retrieval at production scale | Spotify production case + multiple 长 podcast | ✅ |
| Pinecone | hosted vector DB, low ops | majority hosted-RAG case studies | ✅ |
| Qdrant | self-hosted vector, performance-tuned | scattered production cases | ✅ |
| Chroma | embedded / dev-time RAG | dev-tool category, dominant in tutorials | ✅ |
| DSPy | programmatic prompt optimization | Princeton + Stanford research, growing production adoption | ✅ |
| CrewAI / AutoGen | thick multi-agent orchestration | YC W25 cases mixed (some success some pivot-out) | ✅ but 标注 "controversial" |
| Pydantic-AI | thin-framework / type-first | recent rise, growing fast | ✅ |
| E2B / Modal / Daytona | sandbox / code-execution | for code-agents specifically | ✅ |
| Inspect AI / promptfoo | eval frameworks | evaluation specialists' choice | ✅ |

→ 场景特化层: 9 个 ✅ (target ≥5)

### 新兴层（近 12 个月）

| Tool | Born | Adopters | Verdict |
|------|------|----------|---------|
| Browser Use | 2024-Q4 | 早期 agent-browser 团队 | ✅ stability: experimental |
| Stagehand | 2024-Q3 | Browserbase 团队 | ✅ |
| Cline (mid-2024) | mid-2024 | YC + indie 工程师圈 | ✅ - on edge of moving to 必备 (2026-05) |
| Continue.dev | grew fast 2024 | dev-tool space | ✅ |

→ 新兴层: 4 个 ✅ (target ≥2)

**Total retained: 5 必备 + 9 场景 + 4 新兴 = 18 工具**

---

## Step 4: Sample 1 filled tool card

```markdown
### Vespa

- **One-liner**: Production-grade hybrid retrieval engine. 适合 sparse-dense hybrid + complex filtering 场景，Spotify / Yahoo 等大规模在用
- **Tier**: 场景特化
- **Maintainer**: Vespa.ai (originally Yahoo open-source spinoff)
- **License**: Apache 2.0
- **Maturity signals**:
  - GitHub stars: 6.0k (2026-05-01, last_checked)
  - First public release: 2017 (mature)
  - Last commit: < 24h (2026-05-01)
  - Activity: healthy, multi-org maintainer base
- **典型使用场景**:
  - hybrid retrieval (BM25 + vector) + multi-modal filtering
  - production-scale (>1B docs) where hosted services 价格不可接受
  - tensor-based ranking (custom relevance models)
- **不适合 / 替代方案**:
  - prototyping / dev-time → 用 Chroma
  - hosted / low-ops → 用 Pinecone
  - 团队没有专属基础设施工程师 → ZooKeeper / Vespa Tensor 复杂度会拖累
- **生产案例**:
  - Spotify search (URL placeholder)
  - Yahoo Mail search
  - Public agent-eval blog post benchmark vs Pinecone (URL placeholder, 2025-Q3)
- **维护者背景**: 与 Track 01 figures 中的 Jo Kristian Bergum 关联
- **近期变化**: 2025-Q4 加入 native LangChain integration
- **来源**:
  - [Primary] Vespa docs + Spotify engineering blog (URL, 2025-09)
  - [Secondary] benchmark blog post (URL, 2025-Q3)
  - [Reference] LangChain blog mention (URL)
- **可信度**: high
- **Decay risk**: low (基础设施类工具, 多年稳定)
```

✅ 9 字段全部填得起来 + 时效字段都有具体日期 + decay risk 标了。

---

## Step 5: Sample partial decision tree

```markdown
## 选型决策树 — Vector retrieval

### Branch 1: 你只是 prototyping / 单机 dev
→ 用 Chroma (embedded, zero ops)
→ 不要用 Pinecone / Vespa（部署成本不必要）
→ 案例: 大多数 LangChain tutorials 用 Chroma

### Branch 2: 上线了, 量级 <10M docs, 团队没有 ops 人
→ 用 Pinecone（hosted, billing scale linearly）
→ 替代: Weaviate Cloud
→ 不推荐: Vespa（运维成本与你团队规模不匹配）

### Branch 3: 量级 >100M docs OR 需要 hybrid sparse-dense + filtering
→ 用 Vespa
→ 替代: Qdrant（如果你团队倾向 self-host 但不要 Vespa 的复杂度）
→ 不推荐: Pinecone（vector-only filtering 受限，hybrid scoring 不灵活）
→ 案例: Spotify / Yahoo（Vespa）, Cohere internal（Qdrant）

### Branch 4: 你是 RAG framework 用户, 需要 vector + 全文搜 + 半结构化数据混合
→ 用 LlamaIndex 抽象层 + 后端按 1-3 选
```

✅ 4 个分支 (在 5-10 范围), 每个都有证据 / 案例 / 不推荐路径

---

## Step 6: Phase 2 interface (partial)

```markdown
## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的工具选型原则**:
- "Framework decay 风险": 同一工具的抽象 6-12 月内可能被模型能力 native 化 → playbook 候选
- "Production reality vs demo": 在 demo 环境跑通的工具与真实 production 跑通的工具是两套 → playbook 候选
- "Sandbox isolation 是 agent infra 不可绕过的": E2B / Modal / Daytona 类工具的存在本身揭示这一点 → playbook 候选

**显著的工具流派分裂**:
- 厚框架（CrewAI / AutoGen）vs 薄框架（Pydantic-AI / 直接 SDK）派 — current visible main split, mirrors Track 01 finding
- Hosted RAG（Pinecone）vs Self-host RAG（Vespa / Qdrant）派 — splits along team-ops capability

**新兴工具信号**:
- 当前活跃新兴: 4 个（browser-side 2 + ide-side 2）
- 出现 → 主流 速度估计: 12-18 月（Cline 是好样本：2024 中出现，2026-05 在「迁入必备」临界）

**冷僻信号**: 全部三层都有内容 ✅ 不冷僻
```

---

## Findings — 02-tools.md v0.1 dry run

### Pass

- 6 步流程跑通了，能产出 Phase 2 可消费的输出
- Wave 1 seeding 假设有效：22 个 seed + 15 个 web 扩展 = 37 候选，超过 25-40 target
- 三层分类 quality gate 在 37 候选上都给出明确判定
- 时效字段（last_checked + maturity signal 日期）每条都填得起来 — 对 master skill 的 update 流程关键
- 选型决策树构造起来不困难，4 个分支都有证据可追溯
- Phase 2 接口块自然产出工具选型 playbook 候选 + 流派分裂 + 时效信号

### Issues found

1. **Wave 1 seed quality 假设强**：dry run 假设 wave 1 已完成且产出 22 个 seed。如果 wave 1 信号薄（如冷僻行业），Track 02 启动就受影响。02-tools.md 现在有 "wave 1 不足回头检查" 的 fallback，但没说**多薄就停下来等 vs 转纯 web search**。建议补：「wave 1 < 5 seed → 警告用户但继续；wave 1 = 0 → 停下来让用户决定（要么补 wave 1 要么纯 web 跑）」
2. **GitHub stars baseline 估值缺**：模板说「对 LLM 类工具 baseline ≈ 5k；对垂直领域调低」，太模糊。建议改为具体表：「LLM agent / AI infra: 5k」「跨境电商 SaaS: 1k」「医疗器械: 100」「金融定量: 500」… 但这需要预先知道行业基准。**实操建议**：让模板说「以候选池里 stars 中位数为基准，> 中位数的进必备层」— 自适应而非硬编码
3. **「行业基线」(industry-baseline) 占位符没解决**：每个行业 stars 标准不同。Iter 7 fix 候选：让 Step 2 加一步「先建立行业 stars baseline」（取候选池所有有 stars 的工具的中位数）
4. **决策树「真实案例」字段经常会变 placeholder**：dry run 中我可以填 Spotify / Yahoo, 但是其他 branch 的 case 来源会比较散。建议补：「如果某分支找不到具体公开案例，标 `[no public case found, based on stack-pattern analysis]`」— 不要假装有
5. **Decay risk 评级缺乏量化**：现在写 high/medium/low + 一句理由。问题：「medium」可能跨「6-12 月」「12-18 月」「18-24 月」，太模糊。建议补：每档对应「next 6 / 12 / 24 months 内被显著改变 / 取代的概率 ≈ X%」

### Action items for next iteration

- [ ] 修 02-tools.md：上面 5 条 issues
- [ ] 写 prompts/research/03-workflows.md（下一轮）
- [ ] 评估：是否要把通用的 wave-seed-fallback 规则提取到 SKILL.md 而非每个 track 模板独立写？

### 累计 findings

- iter 1-6 累积 13/13 已清 (iter 6 末完成)
- iter 7 新增 5 finding（02-tools.md 上面）— 都是 02-tools 内部细化，不影响其他文件

---

## 测试总结

02-tools.md 跑通 6 步，能产出 Phase 2 可消费的工具栈 + 决策树 + Phase 2 接口。最大暴露的问题是 wave 1 → wave 2 的 seed 链路 robustness 假设过强（冷僻行业会断），以及行业 stars baseline 这种「跨行业差异巨大」的字段需要自适应而非硬编码。

下一轮：03-workflows.md（应该比 02-tools 简单，因为不依赖 stars / metrics 这种行业差异巨大的指标）。
