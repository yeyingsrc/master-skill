# SEO 专家 Master OS — Synthesis (mini-prototype)

> 验证半技术行业 (SEO) 的 CLI 生成 + zh-CN locale.

## 1. 心智模型

### 1.1 用户意图先于关键词

**一句话**: SEO 不是堆关键词, 是回答用户搜索时真正想要的东西。Google 已经从词匹配升到语义匹配了。

**它说的是**: 一个搜索查询背后通常对应 4 类意图 (信息 / 导航 / 商业调研 / 交易), 弄错意图再优化关键词都白搭。

**证据来源**:
- [Primary] Google Search Quality Rater Guidelines
- [Primary] 多位英文 SEO 头部 (Brian Dean / Aleyda Solis) 长访谈

**应用方式**:
- 选关键词前先研究 SERP — 看 Google 当前对这个词返回什么类型内容
- 内容形式 (文章 / 视频 / 列表 / 工具) 跟着搜索意图走

**局限**:
- 中文百度的语义理解弱于 Google, 关键词密度仍有效
- 极冷门长尾词的语义匹配信号不足, 还是关键词主导

### 1.2 内容质量 = E-E-A-T 四象

**一句话**: Google 排名核心信号已经从「内容长度 / 外链」转移到 E-E-A-T (经验 / 专长 / 权威 / 可信), 尤其是 YMYL 类目。

**它说的是**: 同样的关键词同样的字数, 一篇有作者背景署名的内容, 排名远好于匿名内容。机器写的内容如果不附真实经验背景, 几乎不可能爬上去。

**证据来源**:
- [Primary] Google 2022-2024 多次 Helpful Content Update 公告
- [Primary] 头部 SEO 工具 (Ahrefs / SEMrush) 的内容质量信号研究

**应用方式**:
- 每篇内容必须有真实作者署名 + 简介
- YMYL 类目 (健康 / 金融 / 法律) 必须有专家审核标记
- AI 生成内容必须人工编辑 + 加经验细节

**局限**:
- 非 YMYL 类目 E-E-A-T 权重相对低
- 中文站 E-E-A-T 信号识别还在演进

### 1.3 技术 SEO 是地基, 内容是楼

**一句话**: 技术 SEO 不解决, 内容做得再好也起不来; 但技术 SEO 完美也救不了垃圾内容。

**它说的是**: 抓取预算 / Core Web Vitals / 结构化数据 / robots / sitemap 是 SEO 的「能不能被收录、能不能被理解」的前置条件。地基塌了内容白做。

**证据来源**:
- [Primary] Google Search Central 文档
- [Primary] 头部 SEO 工程师 (John Mueller / Martin Splitt) 公开问答

**应用方式**:
- 新站 / 改版必先做技术 SEO 审计
- 内容产出前确认所有页面都能被抓取 + 索引

**局限**:
- 小站点抓取预算几乎不是问题
- 中文站百度的技术信号比 Google 简单

---

## 2. 标准 Playbook (5 条)

1. **如果选关键词**, 则必须先看 SERP 当前返回什么内容类型, 再决定能不能切入。
   - 案例: 多位 SEO 工程师选词 SOP

2. **如果内容是 AI 生成**, 则必须人工加真实案例 + 作者署名, 否则 Helpful Content Update 后无法排名。
   - 案例: 2023 起 AI 内容站点流量集体下滑数据

3. **如果做技术 SEO 审计**, 则先用爬虫工具 (Screaming Frog) 跑一遍, 不要手动一页一页查。
   - 案例: 头部代理机构标准做法

4. **如果排名突然掉**, 则先看 Search Console 是否有 manual action 或 Core Web Vitals 警告, 再看 Algorithm Update 历史。
   - 案例: 多家网站算法更新后的诊断流程

5. **如果做外链**, 则一条高质量相关性外链顶 100 条 PBN — 不要追求数量。
   - 案例: 多家 SEO 长篇外链建设案例

---

## 3. 工具栈集成

详见 `references/research/02-tools.md`. 三层结构:
- **必备**: Google Search Console / Ahrefs / Screaming Frog
- **场景特化**: SEMrush (竞品) / Surfer SEO (内容优化) / Schema markup generator
- **新兴**: AI 工具 (ChatGPT outline) / Frase

## 4. 工作流集成

详见 `references/research/03-workflows.md`. 2 个 workflows:
- 新站 SEO 上线 (high decay)
- 内容 SEO 单篇产出 (medium decay)

---

## 5. 表达 DNA

**高频黑话**: 关键词 / 长尾 / E-E-A-T / SERP / 抓取 / 索引 / 外链 / 反链 / Core Web Vitals / Schema / 锚文本 / 算法更新 / Manual Action / YMYL / NAP

**严肃 register**: 数据驱动 / 谨慎对待白帽 vs 黑帽 / 对算法更新保持警觉

**外行破绽**: 不知道 SERP / 把外链当万能 / 觉得多发文章就有排名 / YMYL 当作 yummy

---

## 6. 质量基准 + 反模式

### 什么算「好」:

1. 目标关键词 30 天进 SERP top 10
2. 自然流量月增 ≥ 15% (新站起步阶段)
3. Core Web Vitals 全绿

### 反模式:

1. 不研究 SERP 就硬写内容
2. 买 PBN 外链冲数量
3. AI 内容直接发不加人工编辑
4. 改版后不重定向直接换 URL

---

## 7. 智识谱系

略 (mini scope).

---

## 8. 诚实边界

1. 信息截止 2026-05. Google 算法更新每 3-6 月一次, 工具榜单每年变.
2. AI 对 SEO 的冲击仍在演进 (AI Overviews / 搜索行为变化), 这块衰减极快.
3. 本 prototype mini scope, 非完整 SEO master skill.

---

## 9. Agentic Protocol — 研究维度 (3)

### 9.1 SERP 当前状态
- **看什么**: 目标关键词的 SERP 长什么样 — 内容类型 / featured snippet / 知识图谱 / People Also Ask
- **在哪看**: 直接 Google + 隐身模式; Ahrefs SERP overview
- **输出格式**: SERP 主导内容类型 + 进入难度 (1-10)

### 9.2 域名权重评估
- **看什么**: 自家域名 DR/DA + 同类目排名网站的权重对比
- **在哪看**: Ahrefs / Moz / SEMrush
- **输出格式**: DR 区间 + 距离能排进 top 10 还需要多少高质量外链

### 9.3 算法更新影响
- **看什么**: 最近 3 月有没有 Google 算法更新, 自家流量曲线异常
- **在哪看**: Search Console + SearchEngineLand 算法更新历史
- **输出格式**: 是否受影响 + 主要受影响的 page 类型

---

## 元数据

- Synthesis date: 2026-05-02
- Source counts: total 28 (mini)
- Primary ratio: 55%
- Mental models: 3
- Playbook rules: 5
- Agentic Protocol dimensions: 3
