# Test: extraction-framework.md applied to LLM agent infra

Walking 3 candidate mental models through the **triple gate** from `extraction-framework.md` § 一. Each candidate gets PASS / FAIL / DOWNGRADE. The point: prove the framework is operable on real-ish material, not just self-consistent.

---

## Candidate 1: "Framework 是临时的，能力是永恒的"

**Source notes** (synthetic, paraphrasing real public material):
- Harrison Chase 2025 LangChain Interrupt keynote — "we're moving from chains to graphs because chain abstraction broke as model capability grew"
- Anthropic tool-use docs evolution: function-calling → extended-thinking → computer-use (each pulls capability into the model itself)
- Multiple X/Twitter threads from agent engineers complaining about framework rotation cost

### Triple gate

| 验证 | 通过? | 证据 |
|------|------|------|
| 1. 跨场景复现 | ✅ | 出现在 framework 选型 + eval 工具选型 + multi-agent 编排 ≥ 3 个子场景 |
| 2. 有生成力 | ✅ | 能推断业内对「2026 新 ReAgent 框架要不要采用」「是否自建 prompt 优化 pipeline」的立场 |
| 3. 有排他性 | ✅ | 适用于「正在被模型曲线快速吃掉的层」(LLM infra / RAG framework / prompt eng 工具)，不适用于稳定行业（医疗器械、足踝外科）|

**Verdict: PASS** — 真心智模型。进入 SKILL.md 心智模型节。

---

## Candidate 2: "数据驱动决策"

**Source notes** (synthetic):
- Multiple LangChain blog posts mention "we instrument everything"
- DSPy paper emphasizes empirical optimization over hand-tuning
- 多家 agent 创业公司 case study 提到「先 logging，再优化」

### Triple gate

| 验证 | 通过? | 证据 |
|------|------|------|
| 1. 跨场景复现 | ✅ | 多场景多人 |
| 2. 有生成力 | 部分 | 能推断「面对新问题先 instrument」，但**任何技术行业都会这么推断** |
| 3. 有排他性 | ❌ | 「数据驱动」适用于所有产品 / 工程 / 商业领域，不是 LLM agent infra 独有 |

**Verdict: FAIL（行业八股）** — 不进入心智模型节，不进入 playbook（因为它太宽到无法触发具体决策），最多在 glossary 一笔带过。

**这一题验证了框架的关键作用**：能挡住「听起来很对但任何行业都成立」的废话。

---

## Candidate 3: "Production reality vs demo glamour"

= 一个 agent demo 看起来惊艳和它在生产环境跑得起来是两个完全不同的问题，行业人对前者祛魅、对后者上心。

**Source notes** (synthetic):
- 多个 HN 长讨论：「LangChain demo 能跑，prod 三个月就崩」
- Anthropic 工程师在 podcast 谈「我们花在 retry / fallback / observability 的时间远超 prompt」
- 业内吐槽「TikTok 上 agent 演示视频 vs 同公司真实 production 出错率」

### Triple gate

| 验证 | 通过? | 证据 |
|------|------|------|
| 1. 跨场景复现 | ✅ | framework 选型 / 性能调优 / 招聘判断 / 投资判断 都用得上 |
| 2. 有生成力 | ✅ | 推断「看到惊艳 demo → 追问 production case 的存在性」是这一行的反射动作 |
| 3. 有排他性 | 部分 | 「demo vs prod 差距」是所有快速发展技术的通病。但在 LLM agent infra **特别尖锐**——因为模型 stochasticity 让两者差距比传统软件大一个数量级 |

**Verdict: BORDERLINE PASS, mark as「行业放大版」** — 进入心智模型节，但描述里必须明确「在 LLM agent infra 比一般技术行业放大很多」，否则会失去排他性。

**这一题验证了框架的另一个作用**：把「相邻通用智慧」和「行业特化版本」区分开。第 3 验证不是简单 yes/no，而是「程度」——文档里要求心智模型的描述捕捉这个程度。

---

## Findings — extraction-framework.md 的 v0.1 dry run

### Pass

- 三重验证规则在 3 个 candidate 上都给出了清晰的判断（pass / fail / borderline），没有靠主观直觉
- 「跨人物」补充验证（不只是跨场景）正确挡住 candidate 2 的「单人多场景但行业通用」陷阱
- 排他性验证捕捉到了 candidate 3 的「程度差异」，提示了应该如何在 SKILL.md 中表述

### Issues found

1. **Borderline 评级缺乏处理规则**：candidate 3 处于「partially excl」，框架现在没明说「这种情况进还是不进」。需要补一条：「第 3 验证 partially passed → 标记为『行业放大版』，进入心智模型节但描述必须捕捉放大程度，不能裸用通用版」
2. **`triggers` field 缺失** — 这个问题在 skill-template.example.md 中已经记录，今轮没顺手修。应该 nextround 修
3. **缺 candidate 列表的产出建议** — 框架现在直接讲「逐个验证」，但 Phase 2 操作上，提炼 agent 应该先**列 15-30 个 candidate** 再筛选。这步骤应该明写。修建议：framework § 一 头加一段「候选清单准备：先扫描 6 轨 research，列出 15-30 个候选论点，然后逐个走三重验证」
4. **第 2 验证（生成力）在 candidate 2 的「部分」状态没明确处理规则**。应该补：「生成力『部分』 = 能生成但不区分行业 → 与 fail 同等对待」

### Action items for next iteration

- [ ] 修 extraction-framework.md：补「Borderline 处理规则」+ 「候选清单准备」+ 「生成力部分状态的处理」
- [ ] 应用 skill-template.md 上一轮的 5 个 finding（triggers 字段最优先）
- [ ] 写 prompts/intake.md 或 prompts/synthesis.md（v0.2 next）

---

## 测试总结

extraction-framework.md 的核心三重验证是**可操作的**——给 3 个 candidate 都给出了清晰判定，没有靠主观直觉。框架成功挡住了「行业八股」（candidate 2），并能捕捉「行业放大版」这种细微情况（candidate 3）。

文档本身有 4 处需要补充（见 issues），主要是处理 borderline 情况的规则没写全。下一轮可以一并修。
