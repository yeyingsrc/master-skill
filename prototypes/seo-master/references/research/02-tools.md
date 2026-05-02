# Track 02 — Tools (SEO 专家)

> 调研日期: 2026-05-02。

## 元数据
- 必备 5 / 场景特化 6 / 新兴 3

---

## 必备层

### 1. Google Search Console (GSC)
- **One-liner**: Google 官方网站表现监控, 查询展示 / 点击 / 排名
- **License**: 免费
- **典型场景**: 所有 SEO 必装
- **避坑**: 数据有 1-3 天延迟; index coverage 报告必须每周看

### 2. Google Analytics 4
- **One-liner**: Google 官方流量分析 (2023 起替代 UA)
- **License**: 免费 (有付费版)
- **典型场景**: 流量来源分析 + 内容表现
- **避坑**: GA4 跟旧版逻辑差异大

### 3. Ahrefs
- **One-liner**: SEO 工具最广泛使用, 关键词 / 外链 / 内容三大模块
- **License**: 99-999 USD/月
- **典型场景**: 关键词调研 + 竞品外链 + 内容差距
- **避坑**: 数据库刷新有延迟

### 4. Screaming Frog SEO Spider
- **One-liner**: 网站爬虫, 技术 SEO 审计核心工具
- **License**: 免费 (≤ 500 URL) / £199/年
- **典型场景**: 技术审计 / sitemap 验证 / redirect 检查

### 5. SEMrush
- **One-liner**: SEO + 投放综合工具, Ahrefs 主要替代
- **License**: 119-449 USD/月
- **典型场景**: 竞品分析 + 关键词机会 + PPC 跨投

---

## 场景特化层

### 6. Surfer SEO
- **One-liner**: 内容优化工具, 比对 SERP top 内容信号
- **License**: 89-219 USD/月
- **典型场景**: 内容写作 / 优化期

### 7. Schema markup generator
- **One-liner**: 结构化数据 markup 生成
- **License**: 多个免费工具
- **典型场景**: 任何内容站需要 rich snippet

### 8. Sitebulb
- **One-liner**: Screaming Frog 的高级替代, 可视化更好
- **License**: 39-159 USD/月
- **典型场景**: 大型 enterprise 网站审计

### 9. Cloudflare (Speed + CDN)
- **One-liner**: CDN + Web Vitals 优化基础设施
- **License**: 免费 (基础) - 200 USD/月 (Pro)
- **典型场景**: 任何关心 Core Web Vitals 的站

### 10. Frase / Clearscope
- **One-liner**: 内容简报 + AI 辅助大纲
- **License**: 45-200 USD/月

### 11. 5118 / 站长之家 (中文圈)
- **One-liner**: 中文 SEO 数据 + 百度生态分析
- **License**: 免费 + 付费
- **典型场景**: 中文站点必装

---

## 新兴层

### 12. AI 内容生成 (ChatGPT / Claude / Gemini)
- **One-liner**: 大纲 / 草稿生成
- **典型场景**: 内容初稿 + 关键词扩展
- **避坑**: 必须人工编辑 + 加经验细节, 否则 Helpful Content Update 干掉

### 13. 智能 SEO 监控 (Pi Datametrics / SEOmonitor)
- **One-liner**: 大型站点的智能监控 + 警报
- **License**: 200+ USD/月
- **典型场景**: 大型 enterprise 站

### 14. AI Overviews 监控工具
- **One-liner**: 跟踪 Google AI Overviews 占用关键词
- **Status**: 早期 (2024-2025 起势)
- **典型场景**: 高搜索量关键词的 AIO 影响评估

---

## 选型决策树

| 场景 | 工具栈 |
|------|-------|
| 个人博客 / 小型站 | GSC + GA4 + Ahrefs Lite 或 5118 |
| 中型内容站 / 电商 | + SEMrush + Screaming Frog + Surfer + Schema markup |
| 大型 enterprise / 跨语言 | + Sitebulb + Cloudflare + AI Overviews 监控 |

---

## 避坑

1. AI 写完直接发 → Helpful Content Update 后流量崩
2. 不装 GSC / GA4 → 改版 / 算法更新出问题查不出来
3. 关键词工具只看一家 → 数据偏差大, 至少两家交叉
4. 改版不做 redirect → 大量历史排名归零
5. Core Web Vitals 一次性优化完不监控 → 后续代码 / 图片把指标拖回来

## 来源
- [Primary] 各家官方文档
- [Primary] 头部 SEO 从业者工具评测 (Brian Dean / Aleyda)
- [Secondary] Search Engine Land 工具榜单
