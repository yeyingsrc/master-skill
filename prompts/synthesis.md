# Phase 2 — Synthesis (提炼)

> Phase 2 的执行剧本。SKILL.md Phase 2 调用本文件。

## 你的任务

读 6 轨 research notes (`{skill_dir}/references/research/01-06.md`)，按 [extraction-framework.md](../references/extraction-framework.md) 的方法论提炼出**行业 Master OS** 的 9 个组件，写到 `{skill_dir}/references/synthesis.md`，作为 Phase 3 的输入。

输出**不是 research 笔记的复盘**（那 Phase 1.5 已经做了）。输出是**可运行的认知操作系统**：心智模型 / playbook / 工具栈 / 工作流 / 表达 DNA / 质量基准 / 智识谱系 / 诚实边界 / Agentic Protocol。

## 输入位置

```
{skill_dir}/references/research/
  ├── 01-figures.md
  ├── 02-tools.md
  ├── 03-workflows.md
  ├── 04-canon.md
  ├── 05-sources.md
  └── 06-glossary.md
```

每个文件**末尾的「Phase 2 接口」段是你最重要的入口** — 各 track 已经为你筛好了候选信号。

## 输出位置

```
{skill_dir}/references/synthesis.md
```

文件存在则覆盖。

## 9 步执行（对应 SKILL.md Phase 2.1-2.9）

### Step 0: 候选清单准备 (跨 track 收集)

读完所有 6 轨 research，**先扫描各 track 的「Phase 2 接口」段**，汇集候选信号到 `{skill_dir}/references/synthesis-candidates.md`：

```markdown
# Synthesis Candidates (raw)

## 候选心智模型 (target 15-30)
| Candidate | 出现于 tracks | 出现 figures 数 | 类型 | 备注 |
|-----------|-------------|----------------|------|------|
| {{candidate 1}} | 01,03,04 | A/C/E/F (4) | cross-track | ... |
| ... |

## 候选 playbook 规则 (target 10-20)
| Pattern | 来源 |

## 候选工具流派分裂 (智识谱系)
| Split | A 派代表 | B 派代表 |

## 候选反模式
| Anti-pattern | 来源 |

## 候选时效信号 (诚实边界用)
| Signal | 来源 | Decay 强度 |

## 候选 Agentic Protocol 维度
| 维度 | 推导自哪个 mental model |
```

**候选数门槛与行业类型挂钩**（iter 18 修正）：

| 行业类型 | 最小候选数 | 例 |
|---------|----------|------|
| Technical (LLM agent infra / cloud infra / RAG) | ≥ 15 | 公开内容多，门槛高 |
| Academic (CV / 神经科学 / 生物信息) | ≥ 12 | paper-driven, 理论密度高 |
| Vertical 实操 (跨境电商 / 短视频投流) | ≥ 8 | 操作多，公开理论少 |
| Regulated specialized (足踝外科 / 量化金融) | ≥ 5 | 闭源主导，公开材料受限 |

候选低于阈值 → 信号薄弱，要么补 Phase 1 research，要么进入冷僻领域协议（Phase 2.8 诚实边界明确标注）。
候选 > 30 → 重复 / 雷同太多，先合并同类项再走三重验证。

### Step 1: 心智模型提炼 (对应 SKILL.md Phase 2.1)

按 [extraction-framework.md § 一](../references/extraction-framework.md) 的三重验证 (PASS / PARTIAL / FAIL) 评估每个候选：

- 验证 1 (跨场景复现): ≥ 2 子场景 + ≥ 2 独立 figures
- 验证 2 (生成力): 能推断行业人对新问题的立场
- 验证 3 (排他性): 仅在这一行特别成立

**候选 → 评级矩阵**：
- ✅✅✅ → 心智模型, KEEP
- ✅✅⚠️ (验证 3 PARTIAL) → 行业放大版心智模型，KEEP 但描述强制捕捉「放大程度」
- 任一 ❌ + 其他 ✅ ≥ 2 → 决策启发式, 推到 Step 2
- ≤ 1 ✅ → 行业八股, DROP (最多 glossary 一笔)

**目标产出**: 3-7 个心智模型。每个含：
- 名称
- 一句话描述
- ≥ 2 处来源证据 (跨场景)
- 应用方式 (when to invoke)
- 局限 (mandatory — 不写就降级)

**反模式 (DROP 这些常见陷阱)**:
- 「关注用户体验」「先做 MVP」「数据驱动」 → 通用商业道理 (验证 3 ❌)
- 「{X} 行业重视质量」 → 没排他性
- 「专家经验很重要」 → 没生成力

### Step 2: Playbook 提炼 (Phase 2.2)

= 行业内的「快速决策规则」。形如「如果 {场景}，则 {决策方向}」。

**来源** (按权重):
- Step 1 中验证未通过但 ≥ 2 ✅ 的候选 (从心智模型降级)
- Track 03 workflows 中跨多 workflow 反复出现的步骤模式
- Track 01 figures 在长访谈中说过的「我做这种决定的标准是 X」

**质量门槛** (每条必满足):
1. 场景具体（不是「重要决策时...」，而是「**当你面对从 0 到 1 的工具选型且产品需求不稳定时**...」）
2. 决策方向明确（「**默认选 X，除非满足 Y 才考虑 Z**」）
3. 至少 1-2 个具体案例
4. 可被新情况触发，不只适用于原始案例

**目标产出**: 5-10 条。少于 5 提炼不够; 超过 10 没区分主次。

### Step 3: 工具栈集成 (Phase 2.3) — 注意：本步是「集成」非「提炼」

直接消化 Track 02 的三层结构（必备 / 场景特化 / 新兴）+ 选型决策树。**主要工作是验证一致性**：

- 必备层 ≥ 3 个？数量太少 → 行业可能没成熟工具生态，回头看 Track 02 是否漏抓
- 选型决策树 5-10 节点 + 每节点有证据？不达标 → 让 Track 02 补完
- 避坑清单 ≥ 5 条？

**这一步主要是 sanity check，不是重新提炼**。Track 02 已经做了大部分工作。

### Step 4: 工作流集成 (Phase 2.4) — 注意：本步是「集成」非「提炼」

直接消化 Track 03 的「入门 SOP / 资深路径 / 近期变化」分组。验证：

- 每个 workflow 的入门 SOP 与资深路径是否分清?
- 资深差异（skip/optimize/add）至少 2 类 + ≥ 2 instances?
- 「近期变化」字段填了 (有变化 OR 明确「稳态」)?

**这一步同样主要 sanity check**。

### Step 5: 表达 DNA 提炼 (Phase 2.5)

按 [extraction-framework.md § 五](../references/extraction-framework.md) + Track 06 的 outsider-tell + Track 01 长访谈 register 综合：

| 维度 | 来源 |
|------|------|
| 高频用语 / 黑话 | Track 06 Tier 1 术语 + Track 01 figures 反复用的词 |
| 严肃 register | Track 01 长访谈 + Track 04 textbook 的语气 |
| 内 vs 外沟通差异 | Track 06 outsider-tell 反推 |
| 外行破绽 | Track 06 outsider-tell top 10 直接用 |
| 厂商话术拒绝 | Track 06 「行业拒绝的厂商话术」直接用 |

**关键约束**: 不模拟某个具体 figure，模拟「这一行的资深人聚一起讨论时的 register」。多人融合。

### Step 6: 质量基准 + 反模式 (Phase 2.6)

- **什么算「好」**: 3-5 条具体可验证的基准。来源: Track 03 资深差异点 + Track 04 canon 反复强调的标准
- **反模式**: 5-10 条外行 / 入门常犯错。来源: Track 06 outsider-tell + Track 03 失败模式

### Step 7: 智识谱系 (Phase 2.7)

按 [extraction-framework.md § 六](../references/extraction-framework.md) 处理流派分歧：

- 主要流派 / 学派 (≥ 2)
- 各派奠基人物 + 代表作 (从 Track 04 canon)
- 当前代表 (从 Track 01 figures)
- 核心分歧 (从 Track 02 工具流派 + Track 06 标准之争)

**关键**: 保留分歧而非抹平。「双方都对」是没营养的废话。

### Step 8: 诚实边界 (Phase 2.8)

按 [extraction-framework.md § 七 + § 八](../references/extraction-framework.md) 综合：

- 信息截止 `{research_date}`，工具 / 工作流模块衰减最快（每 3-6 月建议 update）
- 各 track 的薄弱维度（Phase 1.5 review 中的标注）
- 信源失衡（中英文 / 一手二手）
- 行业是否闭源 / 公开材料受限
- 法规 / 标准近期变化的预期影响（喂从 Track 06）

**至少 3 条具体局限**。「不能替代真人」太宽泛，不算合格。

### Step 9: Agentic Protocol 推导 (Phase 2.9)

按 [extraction-framework.md § 九](../references/extraction-framework.md)：从每个心智模型反推「这个模型让人首先关注什么」，凝结成研究维度。

**数量**: 3-10 个，按行业复杂度（简单 3-5 / 标准 5-7 / 复杂 7-10）。

每个维度三段：
- **看什么** — 具体到能否被搜索动作触发
- **在哪看** — 具体 source 而非「网上搜」
- **输出格式** — 1-2 句结构化结论，便于 Step 3 调用

**反模式**:
- ❌ 「搜索相关信息」(没具体到搜索动作)
- ❌ 跨行业相同的研究维度 (失去 Agentic Protocol 的核心价值 — 这一行的特定研究方式)
- ❌ 维度数量超过心智模型数 ×2 (Agentic Protocol 应该精炼，不是穷举)

---

## 输出文件结构

`synthesis.md` 的格式：

```markdown
# {{industry}} Master OS — Synthesis

> Phase 2 提炼结果。Phase 3 (skill writeup) 直接消化本文件。

## 1. 心智模型 (3-7 个)
### 1.1 {{name}}
[name / 一句话 / 证据 / 应用 / 局限]
...

## 2. 标准 Playbook (5-10 条)
...

## 3. 工具栈与选型决策树
[直接 reference Track 02 输出 + 一致性 sanity-check 摘要]

## 4. 工作流 / Pipeline
[直接 reference Track 03 输出 + 一致性 sanity-check 摘要]

## 5. 表达 DNA

## 6. 质量基准 + 反模式

## 7. 智识谱系

## 8. 诚实边界

## 9. Agentic Protocol — 研究维度
### 9.1 {{dimension 1}}
- 看什么:
- 在哪看:
- 输出格式:
...

## 元数据
- Synthesis date: {{YYYY-MM-DD}}
- Source counts: {{from Phase 1.5 review}}
- Cumulative findings issues: {{any unresolved cross-track contradictions}}
```

---

## 失败 / 边界处理

| 情况 | 处理 |
|------|------|
| 候选 < 15 (Step 0) | 信号薄弱，回 Phase 1.5 review，问用户是否补 research |
| 0 个候选三重通过验证 | 整个行业可能极冷僻 / 闭源 / 太新。**STOP**，向用户报告：「无心智模型可提炼。可能 (a) 行业刻意闭源 / (b) 行业过于新尚未形成 OS / (c) research 不充分。要怎么办？」 |
| 心智模型只有 1-2 个 | 冷僻协议生效，扩大诚实边界 |
| Track 间数据矛盾未在 Phase 1.5 解决 | 在 synthesis.md 顶部明确标注「跨 track 矛盾未解决：A 说 X，B 说 Y。需 Phase 2.5 review 时用户裁决」 |
| Agentic Protocol 维度推不出来 | 心智模型可能不够具体 — 退回 Step 1 重新精炼 |

---

## 与 Phase 5 (Refinement) 的衔接

Phase 2 → Phase 2.5 用户确认 → Phase 3 写出 SKILL.md → Phase 4 quality check (mechanical + subagent) → Phase 5 双 agent 精炼。

Phase 5 入口条件 (iter 18 新增): Phase 4 verdict ≥ PARTIAL（不接受 FAIL）+ 用户在 Phase 4 报告中确认「值得精炼」。Phase 5 是 polish layer，不修复 substantive 问题。FAIL 必须先回 Phase 2 / Phase 3。

## 与 Phase 2.5 (User Checkpoint) 的衔接

Phase 2 完成后，Phase 2.5 必须暂停展示提炼摘要给用户确认。本文件的输出**专门设计为**摘要友好：

- 9 个组件按节排列，便于摘要
- 每个心智模型 / playbook 有「一句话」字段，直接组合成摘要
- 「元数据」段列出 source counts + 未解决矛盾，让用户判断是否值得继续

---

## 质量自检（提交前）

- [ ] Step 0 候选清单 ≥ 15? `synthesis-candidates.md` 已写?
- [ ] Step 1 心智模型 3-7 个? 每个有 ≥ 2 处证据 + 局限?
- [ ] Step 2 playbook 5-10 条? 每条有具体场景 + 决策 + 案例?
- [ ] Step 3-4 工具栈 + 工作流的 sanity check 通过?
- [ ] Step 5 表达 DNA 包含 outsider-tell + 厂商话术拒绝?
- [ ] Step 6-8 质量基准 / 智识谱系 / 诚实边界都填了?
- [ ] Step 9 Agentic Protocol 3-10 个维度? 每个有「看什么 / 在哪看 / 输出格式」?
- [ ] 元数据段有 synthesis date + source counts?

任一不通过 → 补完再提交给 Phase 2.5 review。
