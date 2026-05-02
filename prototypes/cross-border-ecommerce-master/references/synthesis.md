# 跨境电商运营 Master OS — Synthesis (mini-prototype, T8 verification scope)

> Phase 2 提炼结果 (mini-viable scope, 验证 zh-CN locale + 非技术行业 CLI generation).

## 1. 心智模型

### 1.1 合规优先于流量

**一句话**: 在欧美主流站点，新品类上线前先解决「能不能合规开卖」，再考虑「能不能跑出量」。

**它说的是**: 合规风险（VAT / GS / WEEE / 包装法）一旦命中, 整个 listing 直接下架, 之前所有 ASIN 投入归零。流量优化是合规之后的事。

**证据来源**:
- [Primary] 亚马逊德国站卖家长访谈 2024-2025
- [Primary] VerpackG 实施细则 + 多家代理服务公司白皮书
- [Reference] 跨境电商类 podcast 反复强调

**应用方式**:
- 选新站点前, 先列合规清单, 估算注册成本和时间
- 合规账户 / 注册号 / 检测报告 必须在首发前到位

**局限**:
- 在低门槛品类 / 美国站早期 (FTC 监管不严) 适用度低
- 在中国站 / 东南亚 → 反向, 流量先, 合规追

### 1.2 选品决定 90% 命运

**一句话**: 在亚马逊体系里, 一个品的最终成败 90% 在选品阶段已经决定, 后续运营只能放大这 10% 空间。

**它说的是**: 高竞争度低差异化的品 + 再好的运营也跑不出来; 选品错了, 投流 / 节奏 / 供应链优化都是补丁。

**证据来源**:
- [Primary] 多位 7 位数 GMV 卖家公开采访
- [Primary] Helium 10 / Jungle Scout 创始人课程
- [Secondary] 卖家社区 (跨境老炮 / 知无不言英文版) 反复总结

**应用方式**:
- 选品阶段拿出 ≥ 60% 团队时间; 运营优化 ≤ 20%
- 选品决策框架: 类目天花板 / 头部集中度 / 供应链门槛 / 差异化空间

**局限**:
- 自主品牌 / DTC 路径下, 选品权重降到 ~50%, 品牌力可补
- 极小众细分 (类目天花板低) 选品再好也撑不起团队

### 1.3 Listing 是文案 + 数据的混合艺术

**一句话**: Listing 不是文案写作, 是用关键词数据反推买家心智 + 用图反推转化率峰值。

**它说的是**: 标题 / bullet point / A+ 内容 → 不是「写得好」, 是「关键词覆盖 + 卖点排序 + 转化率验证」三者的合击。

**证据来源**:
- [Primary] Helium 10 / Sellerise 关键词工具方法论
- [Primary] 知名运营 在 podcast / 长视频 详细拆解过的 listing
- [Reference] 行业培训课程

**应用方式**:
- 写 listing 前必先做关键词调研 (≥ 30 个 long-tail + 高相关度词)
- 主图 / 副图分批 A/B 测, 不一次性定稿
- 文案放第二位, 关键词覆盖放第一位

**局限**:
- 高搜索词重叠的标准品适用度高
- 自主品牌 / 用户教育型品类 → 文案权重提升

---

## 2. 标准 Playbook (5 条)

1. **如果上欧洲站新品类**, 则 VAT / 包装法 / GS-CE 必须在首发前完成注册, 不能边卖边补。
   - 案例: 多家德国站卖家因包装法未注册被举报下架

2. **如果选品阶段供应链优势 < 30%**, 则不上, 换品。
   - 案例: 跨境老炮社区反复总结的「自杀式选品」

3. **如果新品冷启动**, 则前 7 天必投 brand search + auto campaign + 联盟客优惠码组合。
   - 案例: 头部卖家方法论

4. **如果 listing 主图点击率 < 类目平均 0.5%**, 则换图先于改标题或 bullet。
   - 案例: 多家工具厂商案例数据

5. **如果遇到差评攻击**, 则联系亚马逊 + 在 30 天内做 listing optimization 补回评分均值, 不能拖。
   - 案例: 服务商 (Trustinsight 等) 反复案例

---

## 3. 工具栈集成 (来自 Track 02)

详见 `references/research/02-tools.md`. 三层结构:
- **必备**: Helium 10 / 卖家精灵 / Amazon Seller Central
- **场景特化**: Sellerise / Brand Analytics / Pacvue (大账户)
- **新兴**: Aitomic (AI listing 生成) / Stackline (品牌分析)

## 4. 工作流集成 (来自 Track 03)

详见 `references/research/03-workflows.md`. 2 个 workflows:
- 新品上架 (high decay — 平台规则每年改)
- Listing 优化 cycle (medium decay)

---

## 5. 表达 DNA

**高频黑话**: ASIN / SKU / FBA / FBM / VAT / CPC / TACOS / 排名 / 节奏 / 一手 / 跟卖 / 黑科技 / 测评 / 站外 / 库存周转

**严肃 register**: 数据驱动 / 谨慎用「黑科技」 / 强调合规 / 对于「保排名」服务保持距离

**外行破绽**: 把 FBA 当 FBM / 把 ACOS 当 ROAS / 不知道仓库分拨费 / 把刷单当 marketing

---

## 6. 质量基准 + 反模式

### 什么算「好」:

1. 新品 30 天达到 BSR 类目前 1000
2. listing 转化率 ≥ 类目均值 1.2x
3. 库存周转 < 60 天

### 反模式:

1. 不做关键词研究就写 listing
2. 不准备合规材料就上欧站
3. 把刷单当核心策略
4. 同时上太多 SKU (注意力稀释)

---

## 7. 智识谱系

略 (mini prototype 不细化).

---

## 8. 诚实边界

1. 信息截止 2026-05. 平台规则 / 投流策略每 3-6 月需 update.
2. 法规变化极快. 包装法 / VAT 一站式申报实施细则随时可能调整.
3. 本 prototype 是 mini-viable scope, 仅用于验证 zh-CN locale + 非技术行业 CLI generation 链路.
4. 完整 master skill 应有 ≥ 13 figures / ≥ 18 tools / ≥ 7 workflows.

---

## 9. Agentic Protocol — 研究维度 (3)

### 9.1 合规可行性
- **看什么**: 目标站点 + 品类是否需要 VAT / WEEE / 包装法 / 检测报告 / 认证
- **在哪看**: 各国站点法规页 + 第三方代理服务公司白皮书
- **输出格式**: low / medium / high 合规风险等级 + 1 句具体说明

### 9.2 类目竞争结构
- **看什么**: 类目天花板 (Top 100 月销总和) + 头部集中度 + 供应链门槛
- **在哪看**: Helium 10 / Jungle Scout / 卖家精灵
- **输出格式**: 类目机会 score (1-10) + 1 句关键瓶颈

### 9.3 投流 ROI 评估
- **看什么**: 类目平均 ACOS / TACOS / 头部卖家投流策略
- **在哪看**: Brand Analytics + Pacvue 案例 + 行业 benchmark
- **输出格式**: 预期 ACOS 区间 + 1 句获利节奏

---

## 元数据

- Synthesis date: 2026-05-02
- Source counts: total 30 (mini scope)
- Primary ratio: 55%
- Mental models: 3
- Playbook rules: 5
- Agentic Protocol dimensions: 3
