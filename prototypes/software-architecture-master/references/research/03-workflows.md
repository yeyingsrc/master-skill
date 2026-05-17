# Track 03 — Workflows (software architecture)

> Wave 2 Track 03 — 三轴 workflow: 单系统设计 SOP (主线 A) + 公司规模分流 (主线 B 4 种) + 横向场景 7 case (主线 C) + AI 辅助 (主线 D). Industry: software architecture, locale=global (中外并重), profile=practitioner.
>
> 结构约束 notes (诚实): (1) 'best practice' 是 context-dependent 大公司 ≠ 中小公司 SOP — 大公司读 Google SRE book + Spanner paper; 创业公司读 Pieter Levels 'one-man startup' + Basecamp; 不能笼统说 'always use X'. (2) "default microservices" 是 2014-2018 hype 后被广泛反思的反模式 — Sam Newman 2nd ed *Building Microservices* (2021) 整本书重申 'do not start with microservices, modular monolith first'; Stack Overflow / Shopify / Basecamp DHH "leaving the cloud" 2023-2024 系列都是反例. (3) 中国大厂方案 (阿里 Dubbo + Sentinel + Nacos 全栈) ≠ 中小公司方案 — 99% 中国软件公司是 SpringBoot + MySQL + Redis 单体 + 1 台 ECS; 中文社区文章 99% 写大厂经验导致中小公司 mis-apply 是常见反模式. (4) AI / LLM 辅助 (Copilot / Cursor / Claude Code) 2024-2026 是 hype 高点, 6-12 月 decay; 价值集中在 boilerplate / ADR draft / pattern lookup / 不替代设计判断 — Veracode 2025-2026 数据 45% AI 生成代码引入 OWASP Top 10 漏洞, "vibes coding" (Karpathy 2025-02 创造词) hangover 已成行业话题. (5) Conway's Law (1968) + inverse-Conway maneuver (Skelton+Pais 2019) 是组织 ↔ 架构 同构方法论核心 — 架构边界 = 团队边界, 不能只设计技术不设计组织. (6) ADR (Nygard 2011) + C4 model (Brown 2006-2011) + fitness function (Ford+Parsons+Kua 2017) 是当代架构文档 + 守门 轻量标准, 与 RUP / 4+1 view (Kruchten 1995) 互补不互斥; ADR 是事后 rationale 记录而非 up-front design doc, 与 Parnas+Clements 1986 "Rational Design Process: How and Why to Fake It" 哲学一脉相承.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://martinfowler.com/bliki/StranglerFigApplication.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler 2004 Strangler Fig 原文 (legacy 改造 #1 pattern) |
| T03-S002 | https://martinfowler.com/bliki/OriginalStranglerFigApplication.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — 原始 Strangler 命名出处 |
| T03-S003 | https://martinfowler.com/articles/strangler-fig-mobile-apps.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Strangler Fig 在 mobile 场景下的应用 |
| T03-S004 | https://martinfowler.com/bliki/MonolithFirst.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler 2015 "MonolithFirst" 反 premature microservices |
| T03-S005 | https://martinfowler.com/articles/dont-start-monolith.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Stefan Tilkov 反论, monolith first 不绝对 (诚实对照) |
| T03-S006 | https://martinfowler.com/articles/break-monolith-into-microservices.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Zhamak Dehghani 拆分 monolith 具体步骤 |
| T03-S007 | https://martinfowler.com/articles/microservice-trade-offs.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Microservice Trade-Offs |
| T03-S008 | https://martinfowler.com/microservices/ | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler+Lewis 2014 "Microservices" 经典 essay |
| T03-S009 | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler bliki ADR 词条 |
| T03-S010 | https://martinfowler.com/bliki/ConwaysLaw.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Conway's Law 入门 (1968 原文+ inverse 论) |
| T03-S011 | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | surrogate_primary | 2026-05-17 | cognitect.com (Nygard) | vendor docs (作者一手) — Nygard 2011-11-15 ADR 原始博文, 当代 ADR 起点 |
| T03-S012 | https://github.com/joelparkerhenderson/architecture-decision-record | verified_primary | 2026-05-17 | GitHub | ADR 模板与样例集合 (Nygard / MADR / Y-statement 等), CC0 |
| T03-S013 | https://adr.github.io/ | surrogate_primary | 2026-05-17 | GitHub Pages | vendor docs (协会主页) — ADR 社区组织 (含 madr / log4brains / adr-tools)|
| T03-S014 | https://c4model.com/ | surrogate_primary | 2026-05-17 | c4model.com (Simon Brown) | vendor docs (Simon Brown 一手) — C4 model 官方站 |
| T03-S015 | https://static.simonbrown.je/pth2024-c4.pdf | surrogate_primary | 2026-05-17 | simonbrown.je | vendor docs (作者一手) — Brown 2024 C4 model 演讲 slides |
| T03-S016 | https://simonbrown.je/ | surrogate_primary | 2026-05-17 | simonbrown.je | vendor docs (作者一手) — Simon Brown 个人裸域 |
| T03-S017 | https://nealford.com/books/buildingevolutionaryarchitectures.html | surrogate_primary | 2026-05-17 | nealford.com | vendor docs (作者一手) — Building Evolutionary Architectures + fitness function 出处 |
| T03-S018 | https://evolutionaryarchitecture.com/ | surrogate_primary | 2026-05-17 | evolutionaryarchitecture.com | vendor docs — BEA 配套站, fitness function 范例库 |
| T03-S019 | https://samnewman.io/patterns/architectural/bff/ | surrogate_primary | 2026-05-17 | samnewman.io | vendor docs (作者一手) — Newman BFF 原型 pattern 页 |
| T03-S020 | https://samnewman.io/books/monolith-to-microservices/ | surrogate_primary | 2026-05-17 | samnewman.io | vendor docs (作者一手) — Monolith to Microservices 章节索引 (含 strangler / branch-by-abstraction) |
| T03-S021 | https://samnewman.io/books/building_microservices_2nd_edition/ | surrogate_primary | 2026-05-17 | samnewman.io | vendor docs (作者一手) — Building Microservices 2nd ed (2021) 重申 monolith first |
| T03-S022 | https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html | surrogate_primary | 2026-05-17 | aws.amazon.com | vendor docs — AWS Prescriptive Guidance strangler fig 3 步 (transform/coexist/eliminate) |
| T03-S023 | https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html | surrogate_primary | 2026-05-17 | aws.amazon.com | vendor docs — AWS branch-by-abstraction (深 stack 改造) |
| T03-S024 | https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig | surrogate_primary | 2026-05-17 | learn.microsoft.com | vendor docs — Azure Architecture Center strangler fig |
| T03-S025 | https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends | surrogate_primary | 2026-05-17 | learn.microsoft.com | vendor docs — Azure BFF pattern 官方说明 |
| T03-S026 | https://aws.amazon.com/blogs/mobile/backends-for-frontends-pattern/ | surrogate_primary | 2026-05-17 | aws.amazon.com | vendor docs (engineering blog) — AWS BFF pattern blog |
| T03-S027 | https://aws.amazon.com/architecture/well-architected/ | surrogate_primary | 2026-05-17 | aws.amazon.com | vendor docs — Well-Architected 6 pillars (含 2021 Sustainability) |
| T03-S028 | https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html | surrogate_primary | 2026-05-17 | aws.amazon.com | vendor docs — Well-Architected 6 pillars spec |
| T03-S029 | https://world.hey.com/dhh/we-have-left-the-cloud-251760fb | surrogate_primary | 2026-05-17 | world.hey.com (DHH) | vendor docs (作者一手) — DHH 2023-06 "We have left the cloud" 终章 |
| T03-S030 | https://world.hey.com/dhh/keeping-the-lights-on-while-leaving-the-cloud-be7c2d67 | surrogate_primary | 2026-05-17 | world.hey.com (DHH) | vendor docs (作者一手) — DHH 迁移中段记录 |
| T03-S031 | https://basecamp.com/cloud-exit | surrogate_primary | 2026-05-17 | basecamp.com (37signals) | vendor docs — 37signals 官方 Leaving the Cloud 系列 landing |
| T03-S032 | https://shopify.engineering/shopify-monolith | surrogate_primary | 2026-05-17 | shopify.engineering | vendor docs (engineering blog) — "Under Deconstruction: The State of Shopify's Monolith" 2024 状态 |
| T03-S033 | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity | surrogate_primary | 2026-05-17 | shopify.engineering | vendor docs (engineering blog) — Shopify 2019 原始 modular monolith 帖 |
| T03-S034 | https://github.com/Shopify/packwerk | verified_primary | 2026-05-17 | GitHub (Shopify) | Shopify Packwerk 开源 — Rails 模块化静态分析工具 (modular monolith 实现关键) |
| T03-S035 | https://stackoverflow.blog/2016/02/17/stack-overflow-the-architecture-2016-edition/ | surrogate_primary | 2026-05-17 | stackoverflow.blog | vendor docs (engineering blog) — Stack Overflow architecture 2016 (9 服务器经典) |
| T03-S036 | https://stackoverflow.blog/2016/03/29/stack-overflow-the-hardware-2016-edition/ | surrogate_primary | 2026-05-17 | stackoverflow.blog | vendor docs (engineering blog) — Stack Overflow hardware 2016 详细 |
| T03-S037 | https://nickcraver.com/blog/2016/02/17/stack-overflow-the-architecture-2016-edition/ | surrogate_primary | 2026-05-17 | nickcraver.com | vendor docs (作者一手) — Nick Craver (former SO Architecture Lead) 个人站镜像 |
| T03-S038 | https://nickcraver.com/ | surrogate_primary | 2026-05-17 | nickcraver.com | vendor docs (作者一手) — Nick Craver 个人裸域 (SO arch blog series 索引) |
| T03-S039 | https://sre.google/sre-book/table-of-contents/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — SRE book 免费 HTML, SLO/SLI/SLA + 4 Golden Signals|
| T03-S040 | https://sre.google/workbook/implementing-slos/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — SRE Workbook implementing SLOs|
| T03-S041 | https://sre.google/workbook/error-budget-policy/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — SRE Workbook error budget policy|
| T03-S042 | https://sre.google/workbook/alerting-on-slos/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — SRE Workbook alerting on SLOs (burn-rate)|
| T03-S043 | https://opentelemetry.io/docs/ | surrogate_primary | 2026-05-17 | opentelemetry.io (CNCF) | vendor docs (CNCF 协会一手) — OpenTelemetry 官方文档 (trace+metric+log 单一规范)|
| T03-S044 | https://www.infoq.com/news/2026/02/opentelemetry-observability/ | secondary | 2026-05-17 | InfoQ | OTel 2026-02 "Demystifying OpenTelemetry" 指南发布报道 |
| T03-S045 | https://teamtopologies.com/book | surrogate_primary | 2026-05-17 | teamtopologies.com | vendor docs (作者一手) — Skelton+Pais 2019 *Team Topologies* (Stream-aligned/Enabling/Complicated-subsystem/Platform 4 team types + inverse Conway) |
| T03-S046 | https://itrevolution.com/articles/conways-law-critical-for-efficient-team-design-in-tech/ | surrogate_primary | 2026-05-17 | itrevolution.com | vendor docs (publisher engineering blog) — Conway's Law + inverse maneuver 中等深度解读 |
| T03-S047 | https://backstage.io/ | surrogate_primary | 2026-05-17 | CNCF | vendor docs (CNCF 协会一手) — Backstage 官方 (Spotify 起家 → CNCF incubating)|
| T03-S048 | https://backstage.spotify.com/ | surrogate_primary | 2026-05-17 | backstage.spotify.com | vendor docs (作者一手) — Spotify Backstage 官方 portal landing |
| T03-S049 | https://engineering.atspotify.com/2025/4/celebrating-five-years-of-backstage | surrogate_primary | 2026-05-17 | engineering.atspotify.com | vendor docs (engineering blog) — Backstage 5 周年, 3000+ 公司采用, Spotify 内 280+ squad |
| T03-S050 | https://engineering.atspotify.com/2024/4/supercharged-developer-portals | surrogate_primary | 2026-05-17 | engineering.atspotify.com | vendor docs (engineering blog) — Supercharged Developer Portals + 内研 2.3x 活跃数据 |
| T03-S051 | https://launchdarkly.com/docs/guides/infrastructure/deployment-strategies | surrogate_primary | 2026-05-17 | launchdarkly.com | vendor docs — Canary / blue-green / dark launch / feature flag 策略对比官方指南 |
| T03-S052 | https://learn.microsoft.com/en-us/training/modules/implement-canary-releases-dark-launching/ | surrogate_primary | 2026-05-17 | learn.microsoft.com | vendor docs — MS Learn canary + dark launch 训练模块 |
| T03-S053 | https://redis.io/active-active/ | surrogate_primary | 2026-05-17 | redis.io | vendor docs — Redis Enterprise active-active (CRDT 实现) 官方页 |
| T03-S054 | https://www.infoq.com/articles/database-merge-replication-crdt/ | secondary | 2026-05-17 | InfoQ | Active-active geo distribution merge replication vs CRDT 对比 |
| T03-S055 | https://www.cockroachlabs.com/docs/stable/multiregion-overview.html | surrogate_primary | 2026-05-17 | cockroachlabs.com | vendor docs — CockroachDB multi-region 概念 (region locality, follower reads) |
| T03-S056 | https://docs.pingcap.com/tidb/stable/overview | surrogate_primary | 2026-05-17 | pingcap.com (TiDB) | vendor docs — TiDB 官方架构 (HTAP + MySQL 兼容 + 中国一手 NewSQL) |
| T03-S057 | https://www.vldb.org/pvldb/vol13/p3072-huang.pdf | surrogate_primary | 2026-05-17 | VLDB | vendor docs (VLDB 协会一手 PDF) — TiDB Raft-based HTAP VLDB 2020 paper|
| T03-S058 | https://buoyant.io/linkerd-vs-istio | surrogate_primary | 2026-05-17 | buoyant.io | vendor docs — Linkerd 母公司对比 (注意: Buoyant bias, 但数据可参) |
| T03-S059 | https://linkerd.io/ | surrogate_primary | 2026-05-17 | linkerd.io | vendor docs — Linkerd 官方站 (CNCF 毕业, Rust micro-proxy) |
| T03-S060 | https://istio.io/ | surrogate_primary | 2026-05-17 | istio.io | vendor docs — Istio 官方站 (CNCF 毕业, Envoy proxy) |
| T03-S061 | https://thenewstack.io/istios-complexity-leads-some-users-to-linkerd/ | secondary | 2026-05-17 | thenewstack.io | The New Stack — Istio 复杂度导致迁 Linkerd 的案例报道 |
| T03-S062 | https://dubbo.apache.org/en/overview/what/overview/ | surrogate_primary | 2026-05-17 | dubbo.apache.org | vendor docs — Apache Dubbo 官方 (阿里捐 Apache, 中国微服务 RPC 主流)|
| T03-S063 | https://github.com/alibaba/Sentinel | verified_primary | 2026-05-17 | GitHub (Alibaba) | Sentinel 开源 (流控 / 熔断 / 系统自适应保护) |
| T03-S064 | https://github.com/alibaba/spring-cloud-alibaba | verified_primary | 2026-05-17 | GitHub (Alibaba) | Spring Cloud Alibaba 一站式微服务栈 (Nacos + Sentinel + Seata + RocketMQ) — 中国大厂主流 |
| T03-S065 | https://nacos.io/ | surrogate_primary | 2026-05-17 | nacos.io | vendor docs — Nacos 官方 (动态服务发现 + 配置中心) |
| T03-S066 | https://www.anthropic.com/engineering/building-effective-agents | surrogate_primary | 2026-05-17 | anthropic.com | vendor docs (Anthropic 一手) — 2024-12 Anthropic "Building Effective Agents" 经典指南 (workflow vs agent 区分) |
| T03-S067 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | surrogate_primary | 2026-05-17 | anthropic.com | vendor docs (Anthropic 一手) — Effective context engineering (memory / compaction / sub-agent) |
| T03-S068 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | surrogate_primary | 2026-05-17 | anthropic.com | vendor docs (Anthropic 一手) — Long-running agents harness 设计 |
| T03-S069 | https://www.anthropic.com/engineering/writing-tools-for-agents | surrogate_primary | 2026-05-17 | anthropic.com | vendor docs (Anthropic 一手) — Writing tools for agents (tool descriptor 设计) |
| T03-S070 | https://docs.smith.langchain.com/ | surrogate_primary | 2026-05-17 | langchain.com | vendor docs — LangSmith 官方文档 (LLM 追踪 / 评估 / token + latency + cost 三维 observability) |
| T03-S071 | https://langfuse.com/docs | surrogate_primary | 2026-05-17 | langfuse.com | vendor docs — Langfuse (开源 LLM observability 备选, self-host 友好) |
| T03-S072 | https://en.wikipedia.org/wiki/Vibe_coding | reference | 2026-05-17 | Wikipedia | "vibe coding" 词条 (Karpathy 2025-02 创造) — 反模式参照 |
| T03-S073 | https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/ | surrogate_primary | 2026-05-17 | cloudsecurityalliance.org | vendor docs (协会) — CSA 2026 Research Note: Veracode 45% AI 代码引入 OWASP Top 10 漏洞 |
| T03-S074 | https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools | surrogate_primary | 2026-05-17 | platform.claude.com | vendor docs (Anthropic 一手) — Claude Cookbook context engineering 实操 |
| T03-S075 | https://arxiv.org/abs/2501.09136 | verified_primary | 2026-05-17 | arXiv | "Agentic RAG: A Survey" 2025-01 学术综述 (RAG → agentic RAG 演进) |
| T03-S076 | https://arxiv.org/abs/2506.03401 | verified_primary | 2026-05-17 | arXiv | "RAGOps" arXiv preprint — 生产 RAG pipeline 运维实践 |
| T03-S077 | https://shiftmag.dev/leaving-the-cloud-314/ | secondary | 2026-05-17 | shiftmag.dev | 第三方对 DHH 离云 case 的 ROI 算账 (从 $3.2M/yr → $360K/yr) |
| T03-S078 | https://www.thoughtworks.com/en-us/insights/articles/embracing-strangler-fig-pattern-legacy-modernization-part-one | surrogate_primary | 2026-05-17 | thoughtworks.com | vendor docs — ThoughtWorks strangler fig 落地经验 (legacy 改造 12-36 月时长参考) |
| T03-S079 | https://www.qianxin.com/news/detail?news_id=12841 | secondary | 2026-05-17 | qianxin.com | 奇安信 — 信创替换 + 业务升级齐头并进 案例 (中国 B4 enterprise) |
| T03-S080 | http://www.gjbmj.gov.cn/ | secondary | 2026-05-17 | 国家密码管理局 | 国密 (SM2/3/4/9) 主管部门 — 信创合规背景 |
| T03-S081 | https://www.djbh.net/ | secondary | 2026-05-17 | djbh.net | 网络安全等级保护网 — 等保 2.0 政策背景 (公安部主管) |
| T03-S082 | https://book.douban.com/subject/26299029/ | verified_primary | 2026-05-17 | book.douban.com | 张开涛/亿级流量网站架构 (电子工业 2017) — 中国大厂秒杀/限流/熔断 SOP 参考 |
| T03-S083 | https://coolshell.cn/articles/21672.html | surrogate_primary | 2026-05-17 | coolshell.cn | vendor docs (陈皓一手) — 《我做系统架构的一些原则》中文社区少有的 first-principle 总结 |
| T03-S084 | https://martinfowler.com/articles/cant-buy-integration.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler "You Can't Buy Integration" (反 vendor lock-in 全栈购买的反模式) |
| T03-S085 | https://blog.acolyer.org/2016/09/14/the-tail-at-scale/ | surrogate_primary | 2026-05-17 | blog.acolyer.org | vendor docs (Adrian Colyer Morning Paper) — Dean+Barroso "The Tail at Scale" 解读 (大规模长尾延迟治理 SOP 起点) |

(85 sources total. Verified_primary: 13 / Surrogate_primary: 64 / Secondary: 7 / Reference: 1 / Blacklisted+Dead: 0. 一手率 = (13+64)/85 = 90.6%.)

---

## 3.A 单系统设计 SOP (C4 + ADR + fitness function 流, 8 phase)

> 主轴: C4 model (Brown) 提供"图怎么画" + ADR (Nygard 2011) 提供"决策怎么记" + fitness function (Ford+Parsons+Kua 2017) 提供"演进怎么守门". 三者非顺序而是叠加, 每个 phase 都用. 时长是 mid-size feature/system (1-3 team, 3-6 月交付) 基线, 大幅 ±50% 视规模.

### 3.A.1 需求理解 (1-3 周)

- **输出物**: requirements brief / 利益相关者清单 (decision-makers + affected teams + ops) / NFR (Non-Functional Requirements: SLO target uptime% + RTO 恢复时间 + RPO 数据丢失窗口 + p95/p99 latency + budget cap + compliance: 等保 / GDPR / SOX / 国密).
- **关键问句**: "5 年后 traffic 增长 10x 还是 100x?" "中断 1h 损失多少钱?" "数据合规辖区在哪?" "现有团队会不会用 X?".
- **反模式**: 跳过 NFR 直接技术选型 (没 SLO 就没法画 architecture trade-off 平衡线); 把"我们要 high availability"当 NFR (没数字 = 没 NFR); 默认抄大厂 (Stack Overflow / Netflix) 架构而不问自己规模.

### 3.A.2 上下文 (C1 Context diagram, 1-2 周)

- **输出物**: C4 L1 Context 图 (1 张) — 中心 system + 外部 actors (用户 / 第三方 SaaS / 上下游系统) + 数据流方向. 配 1 页 plain-text 说明.
- **工具**: c4model.com 推荐 Structurizr (Brown 自研 DSL→渲染), 替代 PlantUML / draw.io / Mermaid C4 plugin.
- **反模式**: C1 画成 deployment 图 (那是 C2); 把内部模块塞进 C1 (那是 C2/C3); 没 actor 只画"系统在云上"流程意义不明.

### 3.A.3 容器 (C2 Container diagram, 2-4 周)

- **输出物**: C4 L2 Container 图 — system 内部独立可部署单元 (web app / API / mobile app / DB / queue / cache / cron worker), 标注技术栈 + 协议. 配 ADR-001 决定单体 vs 微服务 + ADR-002 决定数据库选型.
- **关键决策点**: "modular monolith first" 是 Fowler / Newman 共识默认 (T03-S004, T03-S021) — 除非团队 ≥50 人且有 ops 平台支撑微服务 premium, 否则单体起步, 拆分等真痛了再说 (见 3.B.1).
- **反模式**: C2 一上来 10+ 微服务 (premature microservices); container 边界 = 团队办公室隔间 (Conway's Law 没逆向用, 反而被动反映组织混乱); 没标协议 (HTTP/gRPC/AMQP/Kafka) 让 ops 团队懵.

### 3.A.4 组件 (C3 Component diagram, 4-8 周)

- **输出物**: C4 L3 Component 图 — 每个 container 内部主要 component (Controller / Service / Repository / Domain Model) + 关键 sequence (rare: C4 L4 Code 用 IDE/自动生成, 不手画).
- **DDD 衔接**: 此 phase 是 bounded context 边界落地点 — Evans Blue Book + Vernon Red Book 的战术模式 (Aggregate / Entity / Value Object / Repository) 是 C3 的词汇表.
- **反模式**: 把 UML class diagram 当 C3 (粒度过细, 半年后过期); component 命名 = 技术 (UserController) 而非领域 (Subscription, Checkout) — 不利后续 bounded context 重切.

### 3.A.5 决策 ADR + POC (2-6 周)

- **输出物**: ADR repo (`docs/adr/NNNN-title.md` git tracked, Nygard 模板 = Title + Status + Context + Decision + Consequences, 见 T03-S011/T03-S012). 每个高风险决策配 POC: 2-5 天 spike, 端到端跑通 1 个 happy path + 1 个 failure mode.
- **决策密度**: 一个 mid-size 系统 ADR 总数 15-40 条 (Nygard 经验值), 太少 = 决策没记录, 太多 = ADR 颗粒度太细 (微观决策应进代码注释而非 ADR).
- **反模式**: ADR = 上线后回填 (失去决策时的真实 trade-off context); ADR 只记 "Decision" 不记 "Consequences" (后人不知道副作用); 没 Status 流转 (Proposed → Accepted → Deprecated → Superseded by ADR-NNN) 导致 ADR 库内自相矛盾.

### 3.A.6 渐进上线 (canary / feature flag / dark launch, 1-4 周)

- **输出物**: 部署 pipeline (CI → staging → canary 1-5% → progressive 10/25/50/100%); feature flag service (LaunchDarkly / Unleash / Flagsmith / 自研); kill switch + 回滚 runbook.
- **关键技巧** (T03-S051, T03-S052): (a) **dark launch** = 部署但不释放给用户 (后端跑新逻辑空走, 比对结果); (b) **canary** = 小流量比例放量, 观察 RED 指标; (c) **flag-driven release** = 部署 ≠ 发布, 用 flag 控制发布权限 (内部 → beta → 全量); (d) **rollout-id 关联**: log + trace + metric 都打 flag 决策 + canary bucket + 代码版本 tag, 否则出事查不出谁触发.
- **反模式**: canary 没 SLO 守门只看人眼 (不可重复); flag 永不清理 (5 年后代码里 200+ 死 flag, 比拆未删的 commented code 更难); dual-write 没 backfill 跳 read 切换 (数据形态不兼容时直接断).

### 3.A.7 监控反馈 (RED / USE / Golden Signals, 持续)

- **输出物**: OpenTelemetry instrumentation (trace + metric + log 三支柱单 SDK, T03-S043) + dashboards 三套:
  - **4 Golden Signals** (Google SRE T03-S039): latency / traffic / errors / saturation — 面向 service.
  - **RED** (Weaveworks Tom Wilkie 2015): Requests rate / Errors rate / Duration — 面向 request-level service.
  - **USE** (Brendan Gregg 2012): Utilization / Saturation / Errors — 面向 resource (CPU / mem / disk / net).
- **SLO + error budget** (T03-S040, T03-S041): 99.9% SLO → 季度 error budget = 43.2 min 不可用; 超支 → 冻结非紧急发布直至恢复 (释放压力给可靠性工作).
- **反模式**: dashboard 200 张图无人看 (没 SLO 锚点); alert 噪声 (PagerDuty 一天 50 条, 人都麻木); 监控只看 infra (CPU/mem) 不看 user-facing (p99 latency / checkout success rate).

### 3.A.8 演进 (refactor / fitness function 守门, 持续)

- **输出物**: fitness function 测试集 (T03-S017): (a) **atomic** vs **holistic** (单维 vs 跨维); (b) **triggered** vs **continual** (CI 触发 vs 实时监测); (c) **static** vs **dynamic**. 范例: ArchUnit (Java 包依赖)、jdeps、Mermaid C4 自动出图比对、负载测试 p95 < 200ms 守门、API breaking change linter (oasdiff)、bundle size 上限 CI check.
- **何时拆分 / 合并 container**: 当一个 container 出现 (i) 部署节奏冲突 (2 队伍想同时改) (ii) 性能瓶颈 (一个 endpoint 拖垮整库) (iii) 团队边界变化 (新独立团队接管) — 才考虑拆 (见 3.C.1).
- **反模式**: 写完 fitness function 没人跑 (waterfall ADR 通病); 用 "代码 review 把关" 替代 fitness function (人肉守门不可扩展); refactor 用 Big Bang 而非 strangler fig (T03-S001) / branch-by-abstraction (T03-S023).

---

## 3.B 公司规模分流 (4 种 SOP)

### 3.B.1 创业期 (5-15 eng, 1-3 services) — modular monolith first

- **默认栈**: 1 个 modular monolith (Rails / Django / SpringBoot / Phoenix / Laravel) + PostgreSQL (单库, read-replica 备份) + Redis (cache + queue) + 1 cloud provider 单 region + Cloudflare CDN. **不**上 K8s, **不**上 Kafka, **不**上 service mesh, **不**上多 DB.
- **架构治理**: ADR 进 git markdown (`docs/adr/`), 没 formal review board; 重大决策 = CTO + 1 senior eng 30 min whiteboard; 一周 architecture sync 不超 1 h.
- **observability**: 1 个 SaaS (Sentry + 1 个 APM 如 Datadog free tier / Honeycomb / Grafana Cloud), 不自建 Prometheus stack.
- **case 反例 1: Stack Overflow** (T03-S035, T03-S037) — 月 PV 13 亿, 200+ 站点, 跑在 9 台 on-prem 服务器的 .NET 单体上, 实际 web 层峰值 1 台就够 ("Due to optimizations and new hardware, Stack Overflow only needs 1 web server"). CTO David Fullerton 同时承认 "If we started today, we'd go with microservices from day one" — 这句话是诚实保留, 但 9 服务器 monolith 仍是反 "microservices first" hype 的活样本.
- **case 反例 2: Basecamp/HEY (37signals)** (T03-S029, T03-S031, T03-S077) — DHH 2022-10 宣布离云, 2023 完成 7 个产品迁回自管硬件, 年成本从 $3.2M (AWS) → $360K (bare metal); $600K 硬件投入 6 个月回本. 关键论点: 中等规模稳定 workload 不需要 cloud elasticity 溢价.
- **case 正例 3: Shopify modular monolith** (T03-S032, T03-S033, T03-S034) — 即使 Shopify 这种规模 (核心 monolith 280 万行 Ruby, 50 万 commit, Black Friday 2024 峰值 2.84 亿 req/min) 主体仍是 modular monolith, 用自研 Packwerk (T03-S034) 做包依赖静态分析强制边界. 创业公司应学 Shopify 的"模块化纪律" 而非"拆服务".
- **反模式**: "premature microservices" (花 30% 工时维护 service mesh + k8s + 6 个 git repo, 用户量却 200 DAU); "K8s for CRUD app" (3 个 node 跑 1 个 nginx + 1 个 API); 默认抄 Netflix 架构图 (Netflix 是 7000+ eng / 700+ service 的极端体).

### 3.B.2 Scale-up (50-200 eng, 10-30 services) — 渐进拆 microservice

- **入口信号**: monolith 部署节奏冲突 (一周 ≥5 次 PR 冲突 merge), 单库性能瓶颈, 团队 ≥4 独立 squad. — 此时按 **bounded context** (DDD) 拆 3-5 个核心服务, 不是全拆.
- **拆分手法**: Newman *Monolith to Microservices* (T03-S020) — Strangler Fig 外层拦截 (T03-S001) + Branch by Abstraction 深层 (T03-S023). 单服务拆出工期 2-6 周, 整个拆分周期典型 12-24 月.
- **ADR 升级**: ADR repo 单独仓库, PR review 流程 (≥2 senior approval); weekly 30 min architecture sync; 重大跨团队决策走 ADR-as-RFC (写完留 5-7 天评论窗口).
- **observability 升级**: OpenTelemetry SDK 统一全 service (T03-S043), trace context propagation 必须; backend 可以 Datadog (省心贵) 或 Grafana stack (Prometheus + Loki + Tempo + Grafana, 自建省钱重).
- **service mesh 选择** (T03-S058, T03-S061): 默认 **Linkerd** 而非 Istio — Linkerd 单命令安装, Rust micro-proxy, p99 延迟 40-400% 低于 Istio (Buoyant benchmark 自家数据, bias 自知). Istio 适合 ≥200 service + 强多协议路由需求.
- **multi-region 起点**: 单 cloud 多 AZ → 跨 region read replica → active-passive (DR) → 真需要 active-active 再做 (见 3.C.2).
- **反模式**: 一下拆 20 service (没团队接得住); 拆 service 但 DB 还共享 (distributed monolith, 比单体更糟); 引入 Kafka 但只当 queue 用 (杀鸡牛刀).

### 3.B.3 大厂 (1000+ eng, 100+ services) — formal RFC / principal engineer 网络 / 平台团队

- **架构治理**: formal **RFC** 流程 (Google "design doc" / Amazon "PR/FAQ" / Meta "engineering doc"); **architecture review board** (架构委员会, 月度过重大决策); **principal engineer** 横向网络 (跨组撑技术决策一致性).
- **平台团队** (Team Topologies T03-S045 中的 **Platform team**): 内部 Internal Developer Platform (IDP) — Spotify Backstage (T03-S047, T03-S049) 是 de facto 标杆, 3000+ 公司采用, Spotify 内 280+ squad 用 Backstage 管 2000+ 后端服务. Backstage 用户内研数据 (T03-S050) 2.3x 活跃 / 17% 短 cycle / 2x deploy 频次 (Spotify 自数据, 注意 bias).
- **inverse Conway maneuver** (T03-S045, T03-S046): 主动重组团队结构 → 反向倒推架构边界. Skelton+Pais 4 team types: Stream-aligned (按业务流) + Enabling (赋能教练) + Complicated-subsystem (深技术: ML 引擎 / video codec) + Platform.
- **SRE + error budget** (T03-S039 - T03-S042): 全面引入, dev 与 SRE 共担, 超 budget 冻结发布是硬规.
- **multi-DC / 异地多活**: 见 3.C.2.
- **case 参考**: Google SRE book free html (T03-S039) / Netflix Tech Blog / Meta engineering blog / 阿里 Apache Dubbo + Sentinel + Nacos (T03-S062 - T03-S065, 注意 中国大厂主流, 中小公司不必照抄).
- **反模式**: RFC 流程 6 周走完决策已过期; 平台团队脱离产品团队闭门做"自嗨"框架; 架构委员会变成 rubber-stamp; 引 Backstage 但没人填 catalog (空壳).

### 3.B.4 Enterprise / 传统行业 (银行 / 保险 / 电信 / 政府) — 重 governance + Compliance + 信创

- **角色定位**: 架构师 = 治理 + 项目把关 + 厂商管理. 写设计实操比例 ≤30%, 70% 是评审 / 合规对齐 / 厂商谈判 / 培训.
- **release cycle**: 季度甚至半年发布 (与互联网公司日发布相比), 因 UAT + 合规审 + 信息安全审 + 监管报备链路长.
- **vendor 优先**: Oracle DB / IBM WebSphere / SAP / Tibco ESB / 国内信创替代 (达梦/人大金仓 替 Oracle; OpenGauss / GaussDB 替 PG; 麒麟 / 统信 UOS 替 RHEL; 华为 / 飞腾 / 龙芯 CPU 替 Intel).
- **中国 specifics (T03-S079, T03-S080, T03-S081)**:
  - **信创** (信息技术应用创新): 国资委 2022 79 号文要求央国企 2027 前完成 100% 国产化替代; 党政 → 金融 → 能源 → 电信 顺序推进 ("2+8+N" 行业).
  - **等保 2.0** (公安部主管, djbh.net): 网络安全等级保护, 银行系统普遍 等保 3 级, 重要系统 等保 4 级.
  - **国密** (国家密码管理局, gjbmj.gov.cn): SM2 (非对称) / SM3 (Hash) / SM4 (对称) / SM9 (标识), 金融行业新建系统强制要求国密 双轨 (国密 + RSA/SHA-256 双算法).
  - **银行架构 split**: 短期 core banking 仍集中式 (主机 + Oracle), 非核心 (互金 / 渠道 / 数据) 用"分布式 + 微服务" (Spring Cloud Alibaba T03-S064 是中国主流栈), 远期 core 也分布式 — 节奏典型 5-10 年.
- **反模式**: 用互联网公司 SOP 套银行 (合规跑不通); 不读监管文 (等保 / 银保监 / 央行) 直接画图; 国密以为是"加密算法选个就行" (实际是测评 + 双轨 + key management + 改协议族 整套).

---

## 3.C 横向场景 7 个 (case workflow)

### 3.C.1 单体拆微服务 (strangler fig pattern, 6-18 月)

1. **识别 seam**: 找 monolith 内"准独立"模块 (低出度依赖 + 高内聚), 典型: 通知 / 搜索 / 推荐 / 计费 / 报表.
2. **建抽象** (branch-by-abstraction, T03-S023): 在 monolith 内引入 interface, 调用方改走 interface, 实现仍是老代码.
3. **新写实现 (微服务)**: 起 1 个独立 service, 实现同 interface 协议; 双写期 (dual-run): 老 + 新并跑, log 比对结果.
4. **流量切换** (strangler perimeter, T03-S022): API gateway / nginx / Cloudflare worker 在边界拦截, 按比例切流量到新 service.
5. **眼前监控 + 回滚 ready**: SLO 守门, 任何 regression 立即回切.
6. **删老代码**: 100% 流量稳定 ≥2 周后, 删除 monolith 对应模块. (此步常被跳过, 留下"假拆分" — 老代码还在, 拆分价值打折)
- **时长基线**: 1 个简单服务拆出 4-8 周; 整个 monolith 进入"模块化-微服务混合"稳态 6-18 月; 完全 phase-out monolith 通常做不到 (e.g. Shopify 5+ 年仍以 modular monolith 为核心).
- **反模式**: Big Bang 重写 (Joel Spolsky 经典 "Things You Should Never Do Part I" 论调一致); 拆 service 但 DB 不拆 (distributed monolith); 没双写期直接切流量.

### 3.C.2 全球多活 (multi-region active-active)

- **触发条件**: (a) 跨大洲用户 + p99 latency 要求 < 200 ms; (b) DR RTO < 30 s (region 级灾难 zero downtime); (c) 监管要求数据本地化 (GDPR / 等保 / 数据出境).
- **一致性策略**:
  - **CRDT-based** (T03-S053, T03-S054): Counter / Set / LWW-Map / OR-Set — 数据天然 commutative, 多 region 并写最终一致. Redis Enterprise / Riak / Yjs / AntidoteDB.
  - **Sticky session** (region affinity): 同一 user 路由同一 home region, 跨 region 只读. 简单但单 region 故障 user 痛.
  - **异步 multi-master + LWW**: 多 region 都可写, 冲突按 timestamp 取胜 (会丢数据, 适合非关键数据如 view counter).
  - **NewSQL multi-region** (T03-S055, T03-S056, T03-S057): CockroachDB / TiDB / Spanner — region-aware table partitioning, follower reads, 全局 ACID 但写延迟 = 2-region RTT.
- **必备 drill**: 季度 chaos drill (Netflix Chaos Monkey 流派) — 实际拔 region 网线测 failover, 不只 paper drill.
- **反模式**: 上了 multi-region 但没做 conflict resolution 设计 (静默数据 corruption); DR runbook 2 年没演练 (灾难真来时找不到人); active-active 当 active-passive 用 (90% 流量在主 region, 另一 region 是 cold standby — 钱白花).

### 3.C.3 数据库选型决策树 (OLTP → 分库分表 → 多写主从 → NewSQL → polyglot persistence)

1. **OLTP 单库** (默认): PostgreSQL / MySQL 单实例 + read replica. 覆盖 95% < 1 TB / < 10k QPS 系统. **不要离开这层直到痛**.
2. **垂直拆库**: 按 bounded context 拆 (订单库 / 用户库 / 商品库) — 跨库不能 join, 跨库事务要 saga.
3. **分库分表** (sharding): user_id mod N / range / consistent hash. ShardingSphere / Vitess / 中国 MyCat. 痛点: cross-shard query / re-shard / global uniqueness.
4. **多写主从**: 单 region 多 master + LWW / Paxos / Raft. 痛点: split-brain.
5. **NewSQL** (T03-S055, T03-S056, T03-S057): CockroachDB (Spanner 派, PG 兼容, 全球一致首选) / TiDB (Raft + HTAP + MySQL 兼容, 中国一手, APAC 流行) / YugabyteDB (PG 兼容, 双 API). 透明 scale 但写延迟 + 运维复杂.
6. **polyglot persistence**: 主库 PG + 搜索 Elasticsearch + 缓存 Redis + 时序 InfluxDB / TimescaleDB + 图 Neo4j + 列存 ClickHouse + 对象存储 S3 — 按 workload 选, 不是全选.
- **反模式**: 一开始就 sharding (premature); 用 MongoDB 当 OLTP 主库 (然后发现要事务); polyglot 8 套 DB 但只 1 个 DBA (运维爆炸).

### 3.C.4 API gateway + BFF (Backend for Frontend per client)

- **单 API gateway 够**: ≤ 3 client (web/iOS/Android), API 形态接近, 后端 ≤ 10 service. 用 Kong / Tyk / AWS API Gateway / Envoy / Spring Cloud Gateway.
- **需要 BFF** (Newman T03-S019, Azure T03-S025, AWS T03-S026): client 差异大 (web 要 dashboard 聚合 / mobile 要省流量精简 / IoT 设备要 protobuf), 或后端 ≥ 20 service 一次用户操作要 fan-out 5+ 下游. 每个 client 团队拥有自己 BFF, BFF 与 client 同节奏发布.
- **Netflix 原型**: Android team 自管 BFF 替换全 API 后端, 不需协调中央 API team — Netflix 2013 BFF 公开 case.
- **反模式**: BFF 变成"小单体" (一个 BFF service 服务 5 个 client); BFF 当业务逻辑沉淀点 (业务逻辑应在领域 service, BFF 只做 aggregation + shape); 团队没分对 BFF 又跨团队所有权混乱.

### 3.C.5 Observability 落地 (OpenTelemetry + RED + USE + 4 Golden Signals)

- **standard 选择**: **OpenTelemetry** (T03-S043) — CNCF 毕业, vendor-neutral, trace + metric + log 统一 SDK + collector. 2024-2026 已是默认共识.
- **vendor 路线** A (省心贵): **Datadog 全栈** — trace + metric + log + APM + RUM + LLM observability 一套, 适合 ≥ 100 service 中大公司, 但成本随 host count 线性 (年开销 $50K-$1M+).
- **vendor 路线** B (省钱重): **Prometheus + Grafana + Loki + Tempo** (Grafana stack) 或 **VictoriaMetrics + ClickHouse-based** 组合. 适合有 ops 工程能力 + 量大成本敏感.
- **dashboard 三层**: (i) **Service health** (Golden Signals + SLO burn-rate, T03-S042); (ii) **Request-level** (RED per endpoint); (iii) **Resource** (USE per host/pod/disk/net).
- **LLM observability** (T03-S070, T03-S071): LangSmith (LangChain 自家) / Langfuse (open source) / Helicone / Arize Phoenix — token / latency / cost / hallucination score 四维. 与传统 APM 是新分类, 不互相替代.
- **反模式**: 没 trace 只看 metric (出事 30+ service 不知谁第一个失败); alert 没绑 SLO (噪声爆炸); LLM 不监控 cost (一个 bug 一晚跑掉 $5000 OpenAI 账单).

### 3.C.6 Legacy refactoring / 反向 Conway-maneuver (12-36 月)

- **场景**: 老 monolith / 老 J2EE / 老 SOA 重构 + 团队结构 既反映又制约 该架构. 单纯改代码无效, 必须 重组团队 同步改架构.
- **流程** (Team Topologies T03-S045 + Conway's Law T03-S010):
  1. **Map 现状**: 画 team-to-component 矩阵, 找出 (a) 单 component 多团队改 (cohesion 低) (b) 单团队改多 component (耦合高) — 都是 Conway misalignment.
  2. **目标架构 + 目标团队结构同步设计**: 决定 stream-aligned team 边界 (按 user-facing flow 切), 决定 platform team / enabling team 数量.
  3. **小步重组**: 一次只动 1-2 team 边界 + 对应 service 拆/合, 等 3-6 月稳定再下一步.
  4. **配合 strangler fig**: 技术上同步用 3.C.1 流程.
- **时长**: 典型 12-36 月. 大厂级别 (1000+ eng) 可达 5 年.
- **反模式**: 重组 team 后没切 service 边界 (新 team owns 旧服务的一半, Conway 反弹); 切 service 但 team 没动 (1 service 2 team 协作开销爆炸); HR/管理层 "重组" 用于政治目的非架构对齐.

### 3.C.7 LLM-native 应用架构 (RAG / agent loop / eval / cost-aware) — 2024-2026 当前 vertical

- **核心组件 stack** (T03-S066, T03-S067, T03-S075, T03-S076):
  - **RAG layer**: vector store (Pinecone / Qdrant / Weaviate / pgvector) + chunker + embedder + retriever + re-ranker (cross-encoder, 提升 recall 15-30%). 默认 hybrid (BM25 + dense vector) + rerank.
  - **Agent loop**: ReAct (thought-action-observation) / plan-execute / 多 agent 编排. Anthropic 指南 (T03-S066) 强调 **workflow ≠ agent**: 固定步骤用 workflow (DAG), 不确定路径用 agent (循环).
  - **Context window 管理** (T03-S067): structured note-taking (agent 写出到 memory file 再读回) / sub-agent (主 agent 调 sub, 只拿 summary 回) / tool result clearing (老 tool call 结果定期清).
  - **Tool use** (T03-S069): tool descriptor 写法影响 LLM 选择正确率, "good tool description = good tool"; tool 数量 > 30 时引入 tool search 二级检索.
  - **Eval pipeline**: golden dataset + LLM-as-judge + human spot-check + production sampling, 与传统 ML eval 不同的是 open-ended output 没单一 ground truth.
  - **Cost-aware routing**: 简单 query → 小模型 (Haiku / GPT-4o-mini); 复杂 query → 大模型 (Opus / GPT-4o / o3); 路由层做 cost + quality trade-off. semantic cache (>0.95 similarity 命中) 减 30-50% LLM calls.
  - **Observability** (T03-S070, T03-S071): token + latency + cost + tool call traceability + hallucination score 五维, LangSmith / Langfuse 起点.
- **反模式**: 单 prompt 塞 100k token (没分 sub-agent); 没 eval pipeline 凭"感觉调 prompt"; 用 GPT-4o-class 处理所有 query (成本 10x 浪费); 没 cost guardrail (失控 bug 一夜烧光 budget).
- **诚实 disclaimer**: 此 vertical 2024-2026 hype 高点, pattern 6-12 月迭代一次. 不要把今天的 LangChain / LangGraph / CrewAI 当永久标准 — 选择能可替换的最薄抽象层.

---

## 3.D AI 辅助架构师工作流 (2024-2026 vertical)

### 3.D.1 哪类任务 LLM 提速 (✓ green light)

- **ADR draft + 模板填充**: 给 LLM context (问题背景 + 已知 option), 让它出 Nygard 模板首稿, 人审改. 5x 提速.
- **boilerplate 生成**: CRUD endpoint / DTO / migration / Dockerfile / k8s manifest / OpenAPI spec / test fixture. Copilot / Cursor 强项.
- **pattern lookup**: "这个场景该用 saga 还是 2PC?" — LLM 能 cite GoF / EIP / microservices.io patterns 给出 candidate, 但 trade-off articulation 仍要人做.
- **test generation**: 给定函数签名 + 1-2 happy path test, 让 LLM 补 edge cases + property-based test. 配合人 review.
- **code review 辅助**: LLM 标记 style / 明显 bug / security smell (SQL injection / IDOR), 作为 first-pass; final review 仍要人.
- **commit message + PR description**: 给 diff 让 LLM 写, 90% 可用首稿.
- **文档同步**: API doc / README / changelog 从 code 生成.

### 3.D.2 哪类任务 LLM 不应用 (✗ red light)

- **service boundary 决定**: bounded context 切在哪需要业务领域知识 + 团队 capacity + 演进预测, LLM 给出的 boundary 看似合理实际是训练集众数, 与 real context mismatch.
- **polyglot persistence 选型**: "我系统该用什么 DB" — LLM 会给 generic 决策树, 不会问你 RTO/RPO / 团队 ops 能力 / 公司 vendor 关系 / 监管 / 现有 DBA 经验, 答案对了一半 = 错了一半.
- **跨系统 trade-off articulation**: "拆 service 还是不拆", "上 K8s 还是不上", "active-active 还是 active-passive" — 这些是 stakeholder dialogue + 政治 + 预算 + 5 年路线图问题, LLM 没 context 拿来 hallucinate.
- **business ↔ tech 翻译**: 与 CFO 沟通 ROI / 与 product 谈 NFR / 与 ops 谈 capacity — 架构师核心价值, 不是技术内容.
- **新颖问题首发设计**: 训练集罕见或 cutting-edge 问题, LLM 容易 confidently wrong; 此处人优于 AI.
- **case 风险数据** (T03-S072, T03-S073): Veracode 2025-2026 多轮测试: 45% AI-generated code 引入 OWASP Top 10 漏洞, 多 vendor 多 model 都 ≈ 此水平, 未见改善. "vibe coding" (Karpathy 2025-02 创造词) 在生产代码场景已成 industry 反模式标签; Simon Willison 区分 "review-后 ≠ vibe coding, 是用 LLM 当打字助手", 这是诚实定义.
- **正确姿势**: LLM = junior eng + 永不疲倦的 typist + pattern matcher. 把它当 senior 用 = 把项目命交它手. ADR 决定权 / service boundary 决定权 / 监管合规 决定权 永远在人.

---

## 3.X 反模式 workflow (7 条)

1. **premature microservices**: 5 人创业团队上 10+ service + K8s + service mesh. (Fowler T03-S004 "MonolithFirst" / Newman T03-S021 "Building Microservices 2nd ed 整本书重申")
2. **K8s for CRUD app**: 200 DAU 业务跑在 3-node EKS, 月烧 $3000 集群费 + 1 人月 ops, 业务量本可 1 个 $20 VPS 跑. (与 3.B.1 DHH leaving cloud T03-S029 是同一类决策错位)
3. **over-engineering up-front design**: 6 个月画 50 张 UML 不写一行代码, 上线发现需求已变. (Parnas+Clements 1986 "Rational Design Process: How and Why to Fake It" 早就警告: 设计是迭代发现的, 不是 up-front 算出来的)
4. **waterfall ADR**: ADR 文档写完归档, 工程师不读, 半年后没人记得为什么这么定. (修正: ADR 必须 git tracked + 在 PR review 时引用 + Status 流转 + 新人 onboarding 必读 top 10)
5. **fitness function ad-hoc**: 写了 1-2 个 fitness function 在 README 但 CI 没接, 等于没写. (修正: 进 CI pipeline, 失败 block PR; 见 T03-S017)
6. **inverse-Conway maneuver 半截活**: 重组 team 后没切 service 边界, 或切 service 后没动 team — 新 team owns 老服务半截 / 新服务 2 team 协作. (T03-S045, T03-S046)
7. **"vibes coding" 全包**: 全 AI 生成代码无人 review, 90 天后 codebase 不可维护 + 45% OWASP 漏洞 + 业务逻辑没人能解释. (T03-S072, T03-S073) 修正: AI = junior eng 配 senior 审查, 不是 senior 替代品.

---

Track 03 done. 85 sources. 三轴 SOP (A 8 phase + B 4 公司规模 + C 7 case + D AI 辅助) ✓. 反模式 7 条.
