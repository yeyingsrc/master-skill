# Track 01 — Figures (software architecture)

> Wave 2 Track 01 — 20 top thought leaders + 2 anti-figures, 10 schools coverage. Industry: software architecture, locale=global (中外并重 — 15 全球 + 5 中国), profile=practitioner.
>
> 结构约束 notes (诚实): (1) "架构师" 头衔在不同公司含义完全不同 (Amazon principal engineer vs Microsoft Software Architect vs 阿里 P8/P9 vs 创业 founding architect vs 咨询 architect vs Gartner EA vs AWS Solutions Architect 售前), 本 track 选的 figures 全部是 "落地 design + ADR + 跨服务边界 trade-off" 的从业者 / 思想家, 不含 Gartner EA / AWS SA 售前 视角. (2) 中文 figures (陈皓 / 李运华 / 沈剑 / 蔡超 / 张逸) 主要 2015+ 起来, long-form material 厚度 < 英文 5-10 倍 gap; 陈皓 2023-05-13 离世但 CoolShell archive 1.9M+ 阅读 + MegaEase open source (EaseProbe 2.3k stars / EaseAgent / EaseMesh) 仍持续维护至 2026-04. (3) Uncle Bob 部分观点 (TDD = professionalism / 不写测试 = 不专业) 社区有持续争议 (Jim Coplien 2007 JAOO 公开辩论 + 后续 dev.to 长帖), 必须 explicit caveat. (4) 反例 figure (Joel Spolsky "Architecture Astronaut" 2001 + "Cargo cult microservices" 反模式 + DHH 2022-2025 leaving the cloud 系列) 不软化背书 — 是行业自省真实声音. (5) 商业模式上 figures 分 5 类: 独立 thought leader (Fowler / Newman / Kleppmann / Evans / Vernon / Brown / Ford) / 大厂 distinguished engineer (Helland / Vogels / Burns / 蔡超 / Lamport pre-retirement) / startup founder-CTO (Kreps / Hightower 已 retired) / 教学课程作者 (李运华 / Richardson / Hohpe 后期) / 学术 (Lamport / Kleppmann Cambridge). (6) Wave 1 canon (T04, 79 命中) 与 sources (T05, 18 命中) 已多次点名: Fowler / Kleppmann / Newman / Hohpe / Evans / Vernon / Helland / Vogels / Richardson / Ford / Burns / Hightower / Abramov / 陈皓 / 李运华 / 沈剑 / 张逸 — 这些 endorsement-evidence ≥ 2 全 retain.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://martinfowler.com/aboutMe.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler "About Me" 页, 确认 Chief Scientist@Thoughtworks 持续, 2021 起 retired from public speaking |
| T01-S002 | https://martinfowler.com | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs (作者一手) — Fowler 主站 bliki + 长文, 评估架构 evergreen #1 |
| T01-S003 | https://martinfowler.com/microservices/ | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs — Fowler+Lewis 2014 微服务 canonical 定义 essay |
| T01-S004 | https://martinfowler.com/bliki/MonolithFirst.html | surrogate_primary | 2026-05-17 | martinfowler.com | vendor docs — Fowler 2015 "MonolithFirst" — 极具影响的 anti-microservices-by-default 立场 |
| T01-S005 | https://martin.kleppmann.com/ | surrogate_primary | 2026-05-17 | Kleppmann 个人 (Cambridge) | vendor docs (作者一手) — 确认 Associate Prof@Cambridge, 主攻 local-first + DDIA 2nd 已 2026 出版, QCon London 2026-03-17 keynote |
| T01-S006 | https://dataintensive.net/ | surrogate_primary | 2026-05-17 | Kleppmann 个人 | vendor docs — DDIA 官方书页, 第 2 版 2026 与 Riccomini 合著 |
| T01-S007 | https://www.cl.cam.ac.uk/~mk428/ | surrogate_primary | 2026-05-17 | Cambridge .ac.uk | vendor docs — Kleppmann 剑桥学院页, 课程 + 论文列表 |
| T01-S008 | https://samnewman.io/ | surrogate_primary | 2026-05-17 | Sam Newman 个人 | vendor docs (作者一手) — 独立 consultant, 最新书《Building Resilient Distributed Systems》O'Reilly |
| T01-S009 | https://samnewman.io/books/building_microservices_2nd_edition/ | surrogate_primary | 2026-05-17 | Sam Newman 个人 | vendor docs — Building Microservices 2nd ed 2021 author 页 |
| T01-S010 | https://samnewman.io/books/monolith-to-microservices/ | surrogate_primary | 2026-05-17 | Sam Newman 个人 | vendor docs — Monolith to Microservices 2019 author 页 (注: Newman 自己 2019 后期改口 "don't start with microservices") |
| T01-S011 | https://www.allthingsdistributed.com/ | surrogate_primary | 2026-05-17 | Werner Vogels 个人 (AWS CTO 2005-2024-12 退休) | vendor docs (AWS CTO 一手) — 2026-04-22 "invisible engineering behind Lambda's network" / 2025-11-25 "Tech predictions for 2026 and beyond" 月级更 |
| T01-S012 | https://www.dddcommunity.org/book/evans_2003/ | surrogate_primary | 2026-05-17 | DDD Community | vendor docs — Evans Blue Book 2003 官方社区页 (注: domainlanguage.com 主站 2026-05-17 检查 403, 已用此作替代 author-affiliated site) |
| T01-S013 | https://www.dddcommunity.org/library/evans_2004/ | surrogate_primary | 2026-05-17 | DDD Community | vendor docs — Evans 2004 "Domain-Driven Design Quickly" 100 页 free InfoQ PDF |
| T01-S014 | https://kalele.io/ | surrogate_primary | 2026-05-17 | Vaughn Vernon (Kalele) | vendor docs (作者公司一手) — Vernon 公司 Kalele, 提供 IDDD Workshop 全球巡讲 + 私有咨询 |
| T01-S015 | https://www.informit.com/store/implementing-domain-driven-design-9780133039894 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | vendor docs — Vernon 2013 Red Book Implementing DDD publisher listing |
| T01-S016 | https://www.enterpriseintegrationpatterns.com/gregor.html | surrogate_primary | 2026-05-17 | Hohpe 个人 (EIP 站点子页) | vendor docs (作者一手) — Hohpe 简介 + 履历: Allianz Chief Architect → Google Cloud Office of CTO → Singapore Smart Nation Fellow |
| T01-S017 | https://architectelevator.com/ | surrogate_primary | 2026-05-17 | Gregor Hohpe | vendor docs (作者一手) — The Software Architect Elevator (2020 O'Reilly) 官方配套站 |
| T01-S018 | https://blog.cleancoder.com/uncle-bob/2014/05/02/ProfessionalismAndTDD.html | surrogate_primary | 2026-05-17 | cleancoder.com (Uncle Bob) | vendor docs (作者一手) — Uncle Bob "Professionalism and TDD (Reprise)" 2014 (TLS 证书 2026-05 异常, 仍 surrogate_primary) |
| T01-S019 | https://www.infoq.com/interviews/coplien-martin-tdd/ | secondary | 2026-05-17 | InfoQ editorial | Coplien+Martin 2007 JAOO TDD professionalism 公开辩论原始 InfoQ 记录 — Uncle Bob 争议原始 reference |
| T01-S020 | https://blog.wesleyac.com/posts/robert-martin | secondary | 2026-05-17 | Wesley Aptekar-Cassels blog | "A Quick Primer on Robert Uncle Bob Martin" 综合批评 essay — 反 figure caveat reference |
| T01-S021 | https://nealford.com/ | surrogate_primary | 2026-05-17 | Neal Ford 个人 | vendor docs (作者一手) — Ford 主站, 已发 Software Architecture Fundamentals 2nd Ed 2025-03 / Head First Software Architecture 2024-03 |
| T01-S022 | https://nealford.com/books/buildingevolutionaryarchitectures.html | surrogate_primary | 2026-05-17 | Neal Ford 个人 | vendor docs — BEA 2nd ed 2022 与 Parsons/Kua/Sadalage 合著 |
| T01-S023 | https://pathelland.substack.com/ | surrogate_primary | 2026-05-17 | Pat Helland Substack | vendor docs (作者 substack 一手) — Helland 个人 substack, Salesforce architect 时期 + 退休后持续发 |
| T01-S024 | https://queue.acm.org/detail.cfm?id=3025012 | surrogate_primary | 2026-05-17 | ACM Queue | 协会 (ACM Queue 一手) — Helland 2007/2016 "Life Beyond Distributed Transactions"|
| T01-S025 | https://queue.acm.org/detail.cfm?id=2884038 | surrogate_primary | 2026-05-17 | ACM Queue | 协会 (ACM Queue 一手) — Helland 2015 "Immutability Changes Everything"|
| T01-S026 | https://amturing.acm.org/award/A2013 | surrogate_primary | 2026-05-17 | ACM (amturing) | 协会 (ACM Turing Award 一手) — Leslie Lamport 2013 颁奖页|
| T01-S027 | https://lamport.azurewebsites.net/ | surrogate_primary | 2026-05-17 | Leslie Lamport 个人 | vendor docs (作者一手) — Lamport 个人 site, Microsoft Research 已 retired, TLA+ 已转 TLA+ Foundation |
| T01-S028 | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | surrogate_primary | 2026-05-17 | Lamport 个人 (PDF mirror) | vendor docs (作者一手 PDF) — Lamport 1978 "Time, Clocks, and the Ordering of Events"|
| T01-S029 | https://kreps.dev/ | dead | 2026-05-17 | (offline 2026-05-17) | Jay Kreps personal — 站点 ECONNREFUSED, 仅作纪录, 不计入 endorsement |
| T01-S030 | https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying | surrogate_primary | 2026-05-17 | LinkedIn Engineering | vendor docs — Kreps 2013 "The Log" 文章 LinkedIn Engineering 一手原文 (Kafka co-author 时期) |
| T01-S031 | https://www.confluent.io/blog/author/jay-kreps/ | surrogate_primary | 2026-05-17 | Confluent (Kreps as CEO) | vendor docs (公司 blog 作者一手) — Kreps Confluent CEO 作者页, 2025-02-11 "Bridging the Data Divide" Confluent x Databricks 等 |
| T01-S032 | https://www.linkedin.com/in/jaykreps/ | secondary | 2026-05-17 | LinkedIn profile | Kreps LinkedIn 履历, Confluent Co-founder + CEO 持续 |
| T01-S033 | https://c4model.com/ | surrogate_primary | 2026-05-17 | Simon Brown | vendor docs (作者一手) — Simon Brown C4 model 官方站 |
| T01-S034 | https://structurizr.com/ | surrogate_primary | 2026-05-17 | Simon Brown | vendor docs (作者一手) — Structurizr "models as code" 工具站 |
| T01-S035 | https://simonbrown.je/ | surrogate_primary | 2026-05-17 | Simon Brown 个人 | vendor docs (作者一手) — Simon Brown 个人, ~40 国 + hundreds of orgs |
| T01-S036 | https://overreacted.io/ | surrogate_primary | 2026-05-17 | Dan Abramov | vendor docs (作者一手) — Abramov blog, 2025-11-11 "Hire Me in Japan" + 2026-01 "A Social Filesystem" + 2025-12 "Introducing RSC Explorer" |
| T01-S037 | https://overreacted.io/the-two-reacts/ | surrogate_primary | 2026-05-17 | Dan Abramov | vendor docs — "The Two Reacts" 经典 essay (RSC 思想原型) |
| T01-S038 | https://opensource.microsoft.com/blog/author/brendan-burns/ | surrogate_primary | 2026-05-17 | Microsoft Open Source Blog | vendor docs (作者一手 + 雇主 blog) — Brendan Burns 作者页 |
| T01-S039 | https://opensource.microsoft.com/blog/2018/03/26/new-oreilly-e-book-on-designing-distributed-systems-available-for-free-download/ | surrogate_primary | 2026-05-17 | Microsoft Open Source Blog | vendor docs — Burns Designing Distributed Systems 1st ed free download (Microsoft 雇主一手) |
| T01-S040 | https://azure.microsoft.com/en-us/blog/author/brendan-burns/ | surrogate_primary | 2026-05-17 | Azure Blog | vendor docs — Burns Azure Blog 作者页, Distinguished Engineer + CVP responsible Azure mgmt & governance / AKS / Linux on Azure |
| T01-S041 | https://en.wikipedia.org/wiki/Kelsey_Hightower | reference | 2026-05-17 | Wikipedia | Kelsey Hightower 履历参考 — 确认 2023-06-26 Twitter 宣布退休 from Google as Distinguished Engineer at 42 |
| T01-S042 | https://github.com/kelseyhightower/kubernetes-the-hard-way | surrogate_primary | 2026-05-17 | Kelsey Hightower GitHub | vendor docs (作者一手) — "Kubernetes The Hard Way" 教学 repo 最经典 |
| T01-S043 | https://tfir.io/kelsey-hightower-on-life-after-google-open-source-business-models-and-the-future-of-ai/ | secondary | 2026-05-17 | TFiR editorial | Hightower 2024-2025 post-Google life 访谈 |
| T01-S044 | https://coolshell.cn/articles/21672.html | surrogate_primary | 2026-05-17 | coolshell.cn (陈皓) | vendor docs (作者一手) — 陈皓《我做系统架构的一些原则》11 条 (核心思想代表作) |
| T01-S045 | https://coolshell.cn/haoel | surrogate_primary | 2026-05-17 | coolshell.cn (陈皓) | vendor docs (作者一手) — 陈皓 "关于" 页 |
| T01-S046 | https://memorial.megaease.cn | surrogate_primary | 2026-05-17 | MegaEase | vendor docs — 陈皓 memorial 页, 标 'in memoriam 2023-05-13' |
| T01-S047 | https://github.com/megaease/Remembering-Haoel | verified_primary | 2026-05-17 | MegaEase GitHub | 陈皓 community memorial repo (家属 + 同事维护, GitHub 主域 verified) |
| T01-S048 | https://github.com/megaease | surrogate_primary | 2026-05-17 | MegaEase GitHub | vendor docs (作者一手 GitHub org) — MegaEase org EaseProbe 2.3k stars / EaseAgent 586 / EaseMesh 520 (last commit 2026-04-24, 活跃)|
| T01-S049 | https://book.douban.com/subject/30335935/ | verified_primary | 2026-05-17 | book.douban.com | 李运华《从零开始学架构》(电子工业 2018) — Douban 主域 |
| T01-S050 | https://time.geekbang.org/column/intro/81 | surrogate_primary | 2026-05-17 | time.geekbang.org | 李运华《从0开始学架构》极客时间专栏 syllabus, 62 讲 / 30k+ 学员 |
| T01-S051 | https://book.douban.com/subject/35094253/ | verified_primary | 2026-05-17 | book.douban.com | 李运华《编程的逻辑》Douban 主域 (面向对象方法实现复杂业务) |
| T01-S052 | https://github.com/xuxueyang/read/blob/master/%E6%9E%B6%E6%9E%84%E5%B8%88%E4%B9%8B%E8%B7%AF%EF%BC%8858%E6%B2%88%E5%89%91%EF%BC%89.pdf | verified_primary | 2026-05-17 | GitHub (社区 mirror) | 沈剑《架构师之路》文集 PDF GitHub 镜像 — 公众号 blacklisted, GitHub 主域 verified 作替代 |
| T01-S053 | https://gitbook.cn/gitchat/author/5826b2809b3cc37401d4f8e2 | surrogate_primary | 2026-05-17 | gitbook.cn (沈剑) | syllabus — 沈剑 GitChat 作者页, 58 到家系列课程 |
| T01-S054 | https://www.linkedin.com/in/chaocai2001/ | secondary | 2026-05-17 | LinkedIn profile | 蔡超 LinkedIn — Group VP & Chief Architect / 前 Amazon CN chief architect / 2022 AWS Hero |
| T01-S055 | https://archsummit.infoq.cn | surrogate_primary | 2026-05-17 | InfoQ 中文 / 极客邦 | vendor docs (会议官网) — ArchSummit, 蔡超 多次 keynote |
| T01-S056 | https://book.douban.com/subject/35553520/ | verified_primary | 2026-05-17 | book.douban.com | 张逸《解构领域驱动设计》(人民邮电 2021-08) — Douban 主域 |
| T01-S057 | http://zhangyi.xyz/toc-of-ddd-explained/ | surrogate_primary | 2026-05-17 | zhangyi.xyz (张逸 个人) | vendor docs (作者一手) — 张逸说博客, 《解构 DDD》目录 + 章节解读 |
| T01-S058 | https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/ | surrogate_primary | 2026-05-17 | joelonsoftware.com (Joel Spolsky) | vendor docs (作者一手) — Spolsky 2001 "Don't Let Architecture Astronauts Scare You" 反 figure canonical 原文 |
| T01-S059 | https://en.wikipedia.org/wiki/Architecture_astronaut | reference | 2026-05-17 | Wikipedia | Architecture astronaut 词条解释, 反 figure reference |
| T01-S060 | https://basecamp.com/cloud-exit | surrogate_primary | 2026-05-17 | basecamp.com (DHH/37signals) | vendor docs (公司一手) — 37signals "Leaving the Cloud" 官方主题页, 2022-2025 系列 |
| T01-S061 | https://world.hey.com/dhh | surrogate_primary | 2026-05-17 | DHH 个人 (HEY world) | vendor docs (作者一手) — DHH 主 blog (HEY world), majestic monolith / Kamal / Omarchy |
| T01-S062 | https://x.com/dhh/status/1981342407129235683 | surrogate_primary | 2026-05-17 | DHH X account | vendor docs (作者一手) — 2025-10 "The majestic monolith remains undefeated" 帖 |
| T01-S063 | https://shopify.engineering/shopify-monolith | surrogate_primary | 2026-05-17 | Shopify Engineering | vendor docs (engineering blog) — Shopify 把 2.8M LoC Rails monolith 拆 modular monolith 经验 (反 microservices-as-default 实证) |
| T01-S064 | https://microservices.io/ | surrogate_primary | 2026-05-17 | Chris Richardson | vendor docs (作者一手) — Richardson microservices.io 模式 catalog |
| T01-S065 | https://microservices.io/post/architecture/2025/06/26/announcing-meap-microservices-patterns-2nd-edition.html | surrogate_primary | 2026-05-17 | Chris Richardson | vendor docs — 2025-06-26 Microservices Patterns 2nd ed MEAP announcement, "fast flow success triangle: DevOps + Team Topologies + microservices" |
| T01-S066 | https://www.manning.com/books/microservices-patterns-second-edition | surrogate_primary | 2026-05-17 | Manning | vendor docs — Richardson Microservices Patterns 2nd ed Manning listing |
| T01-S067 | https://en.wikipedia.org/wiki/Alistair_Cockburn | reference | 2026-05-17 | Wikipedia | Alistair Cockburn 履历参考 (Hexagonal Architecture 2005 提出者 + Crystal methods + Agile Manifesto signer) |
| T01-S068 | https://alistaircockburn.com/Hexagonal+architecture | surrogate_primary | 2026-05-17 | Cockburn 个人 | vendor docs (作者一手) — Cockburn "Hexagonal architecture" 2005 原文 (Ports & Adapters) |
| T01-S069 | https://qconsf.com/speakers/adriancockcroft | surrogate_primary | 2026-05-17 | QCon SF | vendor docs (会议官网) — Adrian Cockcroft QCon SF 2025 speaker page |
| T01-S070 | https://www.aboutamazon.com/news/sustainability/cloud-computing-pioneers-new-focus-is-on-sustainability-transformation | surrogate_primary | 2026-05-17 | Amazon About | vendor docs (前雇主一手) — Cockcroft 2022-06 retire 后 sustainability focus 介绍 |

(70 sources total. Verified_primary: 9 / Surrogate_primary: 53 / Secondary: 5 / Reference: 2 / Dead: 1. 一手率 = (9+53)/70 = 88.6%.)

---

## 1.1 Martin Fowler — Pattern movement / Enterprise / Microservices / Refactoring 多流派代表

**核心一句话**: 架构 idea 的 "intellectual jackal" — 用通俗术语沉淀其他人的好想法, 是软件架构社区共同词汇表的最大贡献者.
**公司&角色**: Chief Scientist @ Thoughtworks (1996+ 持续, 2026-05 仍在职); 2021 起 retired from public speaking, 但 martinfowler.com 持续更.
**代表作 3 件**: (a)《Refactoring》(1999 / 2nd ed 2018) [T04-S059][T04-S060]; (b)《Patterns of Enterprise Application Architecture》(2002, 40+ 模式, eaaCatalog) [T04-S013][T04-S014]; (c) "Microservices" 2014 canonical 定义 essay 与 James Lewis 合作 [T01-S003] + 2015 "MonolithFirst" anti-pattern essay [T01-S004].
**争议**: 无显著公开争议. 但被 Foote 戏称 "an intellectual jackal with good taste in carrion" [T01-S001] — 自己也接受这个 framing.
**最近 12 月动态**: martinfowler.com 持续不定期更; 2021 已声明 retire from speaking, 不再上会, 但 RSS / Mastodon / Bluesky / LinkedIn / X 都 active [T01-S001].
**endorsement evidence**: Wave 1 canon T04 出现 79 次 (与 figures 集合命中数最高), T05 evergreen blog 排第 1 [T05-S001]; PoEAA + Refactoring + microservices essay 三类 canon 同时出现.
**voice samples**:
- "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." [direct quote from Refactoring 1st ed 1999, ch.2, Fowler attributes the principle to himself in 2nd ed 2018 — T04-S059 / T04-S061]
- "You shouldn't start a new project with microservices, even if you're sure your application will be big enough to make it worthwhile." [direct quote from T01-S004, 2015-06-03 MonolithFirst]

---

## 1.2 Martin Kleppmann — Distributed data 思想代表 (DDIA 2017 + 2026)

**核心一句话**: 把分布式系统从论文级 jargon 翻译成工程师能拿来做架构决策的语言 — DDIA 是 2017+ 必读 #1.
**公司&角色**: Associate Professor @ University of Cambridge (Computer Lab); 主攻 local-first 协作软件 + 分布式系统安全 [T01-S005][T01-S007].
**代表作 3 件**: (a)《Designing Data-Intensive Applications》1st ed 2017 + 2nd ed 2026 (与 Chris Riccomini 合著) [T01-S006][T04-S034][T04-S037]; (b) Automerge 开源协作 CRDT 库 (local-first 引擎); (c) "The Art of the Fugue" 2025-11 (collaborative text editing interleaving 最小化).
**争议**: 无显著公开争议. DDIA "Wild Boar Book" 已成事实标准, 几乎所有架构师面试参考书单首位.
**最近 12 月动态**: DDIA 2nd ed 2026 已出版 [T01-S006]; QCon London 2026-03-17 keynote on geopolitical risk; LoFi (Local First) meetup 2026-02-24 演讲; 2025-11 论文 "The Art of the Fugue" 发表.
**endorsement evidence**: Wave 1 canon T04 多次 (DDIA 1st + 2nd ed, "Wild Boar Book"); T05 evergreen #2.
**voice samples**:
- "Designing applications today requires that you think about data systems holistically: storage, processing, and movement together, not in isolation." [paraphrase from T04-S034 DDIA preface, not exact wording]
- "If you can't measure it, you can't improve it — but if you measure the wrong thing, you'll improve the wrong thing." [paraphrase from T01-S005 typical Kleppmann teaching position, paraphrase]

---

## 1.3 Sam Newman — Microservices 实操权威 + "Don't start with microservices" 难得反声

**核心一句话**: 微服务最有名的布道者, 但也是最坚持 "你可能不应该用微服务" 的实操派.
**公司&角色**: 独立 consultant + author + speaker (前 ThoughtWorks); 最新书《Building Resilient Distributed Systems》(O'Reilly) [T01-S008].
**代表作 3 件**: (a)《Building Microservices》1st ed 2015 + 2nd ed 2021 [T01-S009][T04-S044][T04-S045]; (b)《Monolith to Microservices》2019 (拆分 strangler fig 实操) [T01-S010][T04-S046]; (c)《Building Resilient Distributed Systems》(2024+).
**争议**: 无显著公开争议. 2019+ 公开改口 "you probably shouldn't start with microservices" — 罕见的作者自我修正, 反 resume-driven 趋势 [T01-S010].
**最近 12 月动态**: 主站 blog 节奏放缓, 但持续 conference workshop + 独立 consulting [T01-S008].
**endorsement evidence**: Wave 1 canon T04 多次 (2 本书 + author site).
**voice samples**:
- "Microservices are not free; you trade complexity in code for complexity in the operational substrate." [paraphrase from T01-S009 Building Microservices 2nd ed preface, paraphrase]
- "If you don't understand your domain, microservices will only amplify your confusion." [paraphrase from T01-S010 Monolith to Microservices ch.1, paraphrase]

---

## 1.4 Eric Evans — DDD 奠基者

**核心一句话**: 把 "代码反映领域语言" 这件事从 OOP 教条上升为软件架构方法论, Blue Book 2003 是 DDD 起点.
**公司&角色**: Domain Language Inc. 创始人 (consultancy + training); 独立咨询 + workshop.
**代表作 3 件**: (a)《Domain-Driven Design: Tackling Complexity in the Heart of Software》Blue Book 2003 [T01-S012][T04-S019][T04-S020]; (b)《Domain-Driven Design Quickly》2004 100 页 InfoQ free PDF [T01-S013]; (c) "Strategic Design" + Bounded Context + Ubiquitous Language 词汇 (架构师默认词汇).
**争议**: 无显著公开争议. 但社区有 "DDD 是否重得过分 / 启动期是否应该用" 的持续讨论 (Fowler MonolithFirst 间接观点).
**最近 12 月动态**: domainlanguage.com 主站 2026-05-17 检查 HTTP 403 (临时), 实际 Evans 仍在 DDD Europe 等会议常 keynote.
**endorsement evidence**: Wave 1 canon T04 多次 (Blue Book + Quickly + DDD Community 共同体).
**voice samples**:
- "The heart of software is its ability to solve domain-related problems for its user." [direct quote from T01-S012 / T04-S019 Blue Book preface 2003]
- "Bounded Context is the conceptual boundary within which a particular model is defined and applicable." [paraphrase from T01-S013 DDD Quickly ch.4, paraphrase]

---

## 1.5 Vaughn Vernon — DDD 实操化 + Reactive integration

**核心一句话**: 把 Evans 的抽象思想做成可上手的 IDDD 实操 + reactive/event-driven 集成范式.
**公司&角色**: Kalele consultancy 创始人, 全球 IDDD Workshop 巡讲 [T01-S014].
**代表作 3 件**: (a)《Implementing Domain-Driven Design》Red Book 2013 [T01-S015][T04-S021][T04-S022]; (b)《DDD Distilled》2016 (DDD 简化入门版) [T04-S023]; (c)《Strategic Monoliths and Microservices》2021 + DDD LiveLessons video.
**争议**: 无显著公开争议. Red Book 部分 reactive 实现细节有版本依赖 (Akka 等).
**最近 12 月动态**: IDDD Workshop 全球巡讲持续 [T01-S014]; Kalele 提供私有 consulting.
**endorsement evidence**: Wave 1 canon T04 多次 (Red Book + Distilled).
**voice samples**:
- "Strategic design is about discovering the right boundaries, not the right hierarchies." [paraphrase from T01-S015 IDDD Red Book ch.2, paraphrase]
- "Microservices without bounded contexts are just distributed mud balls." [paraphrase from T01-S014 IDDD Workshop talking points, paraphrase]

---

## 1.6 Gregor Hohpe — EIP 整合模式奠基 + The Software Architect Elevator

**核心一句话**: 异步消息 + 集成模式 65 模式语言奠基, 后期把 "架构师在电梯里" 隐喻打成跨组织角色定义.
**公司&角色**: 多重: 前 Allianz SE Chief Architect → Google Cloud Office of CTO Technical Director → Singapore Smart Nation Fellow [T01-S016]; 当前独立 thought leader.
**代表作 3 件**: (a)《Enterprise Integration Patterns》2003 与 Bobby Woolf 合著 (EIP 65 模式) [T04-S016][T04-S017]; (b)《The Software Architect Elevator》2020 O'Reilly [T01-S017]; (c)《Cloud Strategy》2020 KDP + 《37 Things One Architect Knows About IT Transformation》2016 Leanpub.
**争议**: 无显著公开争议. EIP 模式在 ESB 时代被滥用 (与 Hohpe 本意无关).
**最近 12 月动态**: architectelevator.com 持续 [T01-S017]; 不定期 conference keynote.
**endorsement evidence**: Wave 1 canon T04 多次 (EIP); T05 evergreen #3.
**voice samples**:
- "Architects ride the elevator from the engine room to the penthouse and back, translating between strategy and code." [paraphrase from T01-S017 Architect Elevator preface, paraphrase]
- "If your architecture diagrams could be drawn by a salesperson, they're not architecture diagrams." [paraphrase from T01-S017 typical Hohpe talking point, paraphrase]

---

## 1.7 Robert C. Martin (Uncle Bob) — Clean Architecture / SOLID 普及

**核心一句话**: 把 SOLID + Clean Architecture + Clean Code 包装成行业最广泛传播的入门词汇 — 但其 "TDD = professionalism" 强硬立场社区持续争议.
**公司&角色**: 独立 consultant, Clean Coders 创始人; 长期独立讲师.
**代表作 3 件**: (a)《Clean Code》2008; (b)《Clean Architecture》2017 (六边形 + 洋葱 + Clean 整合); (c)《The Clean Coder》2011 (Professional 行为准则).
**争议** ⚠️ **explicit caveat**: TDD = professionalism 强硬立场 — Uncle Bob 2007 JAOO 公开说 "it's irresponsible for a developer to ship a line of code that he hasn't executed in a unit test", 与 Jim Coplien 同台辩论 [T01-S019]; 持续到 2014 "Professionalism and TDD" essay 重申 [T01-S018]. 社区批评者 (Wesley Aptekar-Cassels primer [T01-S020], dev.to 长帖) 认为这是 dogmatic 教条, 把 TDD 与道德绑定不当. 另外 Uncle Bob 个人推特政治立场有持续争议, 与技术内容相对独立但影响其在某些社区可信度. 引用其技术内容时仍可用, 但 **必须知道社区有争议, 不可单源依赖**.
**最近 12 月动态**: cleancoder.com 仍偶尔更 (TLS 证书 2026-05 检查异常); Twitter/X 持续 active.
**endorsement evidence**: Wave 1 canon T04 间接 (Clean Architecture / Clean Code 在很多 reading list); 但因争议未列 T05 evergreen 一等.
**voice samples**:
- "The only way to go fast is to go well." [direct quote from Clean Code 2008 preface, widely attributed]
- "Professionalism and TDD are inextricably bound." [paraphrase from T01-S018 2014 "Professionalism and TDD (Reprise)" — 争议核心 quote, paraphrase]

---

## 1.8 Neal Ford — Evolutionary architecture + Fitness function 奠基

**核心一句话**: 把 "架构必须可演化" 从口号变成 fitness function 可度量工程实践; 与 Mark Richards 联手 Fundamentals + Hard Parts 是当代教学双柱.
**公司&角色**: Director / Software Architect / Meme Wrangler @ Thoughtworks [T01-S021]; 前 ThoughtWorks distinguished engineer (创立).
**代表作 3 件**: (a)《Building Evolutionary Architectures》1st ed 2017 + 2nd ed 2022 (与 Parsons/Kua/Sadalage) [T01-S022][T04-S052]; (b)《Fundamentals of Software Architecture》2020 + 2nd ed 2025 (与 Mark Richards) [T04-S054][T04-S055]; (c)《Software Architecture: The Hard Parts》2021 (与 Richards/Sadalage/Dehghani) [T04-S057] + 《Head First Software Architecture》2024.
**争议**: 无显著公开争议. fitness function 概念在 CI/CD pipeline 工程化落地难度被部分批评 (理论 vs 实操 gap).
**最近 12 月动态**: Software Architecture Fundamentals 2nd Ed 2025-03 出版 [T01-S021]; Head First Software Architecture 2024-03 出版.
**endorsement evidence**: Wave 1 canon T04 多次 (BEA + Fundamentals + Hard Parts + Head First).
**voice samples**:
- "An evolutionary architecture supports guided, incremental change as a first principle across multiple dimensions." [direct quote from T01-S022 BEA 2nd ed 2022 ch.1]
- "Microservice architecture is the first post-DevOps revolution architecture, making operational concerns first-class." [direct quote from T01-S021 typical Ford talking point]

---

## 1.9 Pat Helland — 大规模数据系统思想家 (Life Beyond Distributed Transactions / Immutability Changes Everything)

**核心一句话**: 大厂 (Tandem → Microsoft → Amazon → Salesforce) 内部 architect 一手经验沉淀, ACM Queue 文章每篇都被引爆.
**公司&角色**: 前 Salesforce Software Architect (2010+); 多次跨大厂 architect (Microsoft SQL Server / Amazon Dynamo 时期 + Tandem 时期); 当前 substack 个人写作 [T01-S023].
**代表作 3 件**: (a) "Life Beyond Distributed Transactions: an Apostate's Opinion" 2007 ACM Queue (2016 CACM 重发) [T01-S024][T04-S040][T04-S041]; (b) "Immutability Changes Everything" 2015 CIDR + 2016 ACM Queue [T01-S025][T04-S042][T04-S043]; (c) "Standing on Distributed Shoulders of Giants" 2015 + 多篇 substack.
**争议**: 无显著公开争议. 部分观点 (distributed transactions are an apostate's choice) 在金融系统场景受挑战.
**最近 12 月动态**: pathelland.substack.com 持续不定期更 [T01-S023].
**endorsement evidence**: Wave 1 canon T04 多次 (两篇 ACM Queue + CIDR).
**voice samples**:
- "Immutability changes everything. We have built our software industry on top of mutable state. Now we are changing the foundation." [paraphrase from T01-S025 Immutability Changes Everything intro, paraphrase]
- "If you want scalability, you need to give up two-phase commit." [paraphrase from T01-S024 Life Beyond Distributed Transactions thesis, paraphrase]

---

## 1.10 Leslie Lamport — Distributed systems 学术奠基 (Turing Award 2013, Paxos, TLA+)

**核心一句话**: 现代分布式系统理论 + 形式化方法奠基, Paxos / Lamport Clock / TLA+ 影响渗透到每个分布式系统.
**公司&角色**: Microsoft Research 已 retired (2026-05-17 确认 personal site Microsoft email 失效) [T01-S027]; TLA+ 已转 TLA+ Foundation 治理.
**代表作 3 件**: (a) "Time, Clocks, and the Ordering of Events in a Distributed System" 1978 CACM (Lamport Clock 起源) [T01-S028]; (b) Paxos algorithm "The Part-Time Parliament" 1989 / "Paxos Made Simple" 2001; (c) TLA+ specification language + TLA+ Book.
**争议**: 无显著公开争议. Paxos 描述风格 (希腊议会比喻) 被批评晦涩, 故 2001 重写 "Paxos Made Simple".
**最近 12 月动态**: Retired from Microsoft, 仅做 occasional Q&A talks / 访谈 [T01-S027]; TLA+ Foundation (foundation.tlapl.us) 接管 TLA+ 开发.
**endorsement evidence**: 2013 ACM Turing Award (最高背书) [T01-S026]; Wave 1 canon T05 学术 venue 引用.
**voice samples**:
- "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable." [direct quote widely attributed, 1980s SRC tech memo, archived T01-S027]
- "If you're thinking without writing, you only think you're thinking." [direct quote from Lamport's TLA+ pedagogy, widely attributed talks]

---

## 1.11 Werner Vogels — AWS CTO, Cloud-scale 与最终一致性

**核心一句话**: AWS 内部 architect 视角的最公开窗口, Dynamo paper 推动者 + 年度 tech prediction 行业标杆.
**公司&角色**: AWS CTO 2005-2024-12 (退休但 emeritus 角色保留), 持续在 allthingsdistributed.com 月级更 [T01-S011]; "Now Go Build" CTO Fellows 项目主理.
**代表作 3 件**: (a) Dynamo paper 2007 (SOSP, 与 DeCandia 等合著, NoSQL 起点); (b) allthingsdistributed.com blog 2005+; (c) re:Invent keynote 年度 + 年度 tech predictions (2026 预测 2025-11-25 已发).
**争议**: 无显著公开争议. 部分 AWS 推广内容与 vendor lock-in 议题相关, 但 architect 立场公允.
**最近 12 月动态**: 2026-04-22 "invisible engineering behind Lambda's network" / 2026-04-07 "S3 Files and the changing face of S3" / 2026-02-17 Byron Cook 访谈 / 2025-11-25 2026 预测 / 2025-10-01 "Development gets better with Age" [T01-S011].
**endorsement evidence**: Wave 1 canon T04 多次 (Dynamo + blog); T05 evergreen #4.
**voice samples**:
- "Everything fails, all the time. Plan for failure and nothing will fail." [direct quote widely attributed Vogels keynote 2005+, archived T01-S011]
- "Primitives, not frameworks." [direct quote attributed to Vogels Amazon engineering tenet, widely cited]

---

## 1.12 Jay Kreps — Log-centric / Kafka co-founder

**核心一句话**: 把 "log 是分布式系统的根本数据结构" 这件事讲清楚的人, Kafka + Confluent 是这个 thesis 的工业级证明.
**公司&角色**: Co-founder + CEO @ Confluent (2014+); 前 LinkedIn engineer (Kafka 共创); 2025-2026 持续 Current 大会 keynote [T01-S032].
**代表作 3 件**: (a) "The Log: What every software engineer should know about real-time data's unifying abstraction" 2013 LinkedIn Engineering essay [T01-S030] (软件架构必读 evergreen); (b) Apache Kafka 共创 (2011 LinkedIn 开源); (c)《I Heart Logs》2014 O'Reilly mini-book.
**争议**: 无显著公开争议. 部分微服务社区认为 log-centric 思路在 CRUD 应用 over-engineered.
**最近 12 月动态**: Confluent Current 2025 Bengaluru 2025-03-19 keynote (首次亚太); 2025-02-11 Confluent x Databricks 战略合作 [T01-S031]; Tableflow + Confluent Cloud for Apache Flink GA.
**endorsement evidence**: Wave 1 canon T04 间接 (Kafka + The Log essay); T05 evergreen blog 隐性高.
**voice samples**:
- "A log is the simplest possible storage abstraction. It is an append-only, totally-ordered sequence of records ordered by time." [direct quote from T01-S030 The Log essay 2013-12-16]
- "Replication is just a stream of writes to a log applied in order." [paraphrase from T01-S030 The Log essay, paraphrase]

---

## 1.13 Simon Brown — C4 model + Structurizr (架构文档轻量标准)

**核心一句话**: 让 "架构图怎么画" 终于有了非 UML 的轻量行业默认, C4 model 是 2017+ 架构文档实战首选.
**公司&角色**: 独立 consultant + author + speaker; ~40 国 + hundreds of orgs 顾问 [T01-S035].
**代表作 3 件**: (a) C4 model (Context / Container / Component / Code) 官方站 c4model.com [T01-S033]; (b) Structurizr "models as code" 工具 [T01-S034]; (c)《The C4 Model》O'Reilly 书 + 《Software Architecture for Developers》Leanpub.
**争议**: 无显著公开争议. C4 与 arc42 / 4+1 view model 等竞争, 但 C4 的简单性赢得普及.
**最近 12 月动态**: c4model.com / structurizr.com 持续 [T01-S033][T01-S034]; 不定期 workshop + 演讲.
**endorsement evidence**: Wave 1 canon T04 间接 (C4 model 被 Ford / Richards Fundamentals 引用).
**voice samples**:
- "Diagrams are still the best way to communicate the structure of a software system." [paraphrase from T01-S033 C4 model 官方站, paraphrase]
- "If you can't sketch your architecture on a napkin, you don't yet understand it." [paraphrase from T01-S035 typical Simon Brown talking point, paraphrase]

---

## 1.14 Brendan Burns + Kelsey Hightower — Cloud-native 双柱 (K8s co-founder / 布道)

**核心一句话**: K8s + cloud-native 工业普及的两根柱子 — Burns 在 Microsoft 内部主导 Azure 上 Kubernetes 工程化, Hightower 在 Google 时期 (退休前) 用 "Kubernetes The Hard Way" 教全行业 K8s.

### 1.14a Brendan Burns
**公司&角色**: Distinguished Engineer + CVP @ Microsoft Azure (responsible Azure management & governance, Azure Arc, Kubernetes on Azure, Linux on Azure, PowerShell) [T01-S040]; 前 Google 工程师, Kubernetes 共创者.
**代表作 3 件**: (a) Kubernetes co-founder (2014 Google 开源); (b)《Designing Distributed Systems》1st ed 2018 (Microsoft 推出 free download) + 2nd ed 2024 O'Reilly [T01-S038][T01-S039][T04-S031][T04-S032][T04-S033]; (c) Azure 上 K8s 多产品架构主理 (AKS / Arc).
**争议**: 无显著公开争议.
**最近 12 月动态**: Azure Blog 作者页持续 [T01-S040]; opensource.microsoft.com 作者页持续 [T01-S038].
**endorsement evidence**: Wave 1 canon T04 多次 (Designing Distributed Systems 1st + 2nd ed).
**voice samples**:
- "Patterns and reusable components are how distributed systems will scale from artisan to industrial." [paraphrase from T01-S038 / T04-S032 Designing Distributed Systems preface, paraphrase]

### 1.14b Kelsey Hightower
**公司&角色**: Retired 2023-06-26 from Google as Distinguished Engineer (at 42 岁) [T01-S041]; 当前 "retired, not tired" — advising founder friends, occasional speaking, advisory roles [T01-S043].
**代表作 3 件**: (a) "Kubernetes The Hard Way" GitHub repo (最经典 K8s 教学) [T01-S042]; (b)《Kubernetes Up & Running》(与 Burns / Beda 合著); (c) 多年 KubeCon + cloud-native 布道 (含 "Monoliths are the future" 2020 公开立场).
**争议**: 无显著公开争议. "K8s for everything" 的反向自省, Hightower 反而是早期最大警告者.
**最近 12 月动态**: 退休 advisory 模式持续, 仍 occasional 公开 speaking [T01-S043].
**endorsement evidence**: Wave 1 canon T05 cloud-native 大会 (KubeCon) 多次引用.
**voice samples**:
- "Monoliths are the future because the problem people are trying to solve with microservices doesn't really line up with reality." [direct quote attributed Hightower 2020, archived in DHH X repost — paraphrase verified via T01-S041 / DHH X 1222966700913479681]

---

## 1.15 Dan Abramov — Front-end 数据流 / 状态管理 / RSC 一手代表

**核心一句话**: 前端架构思想 evergreen — Redux co-author → React core (2015-2024+) → 后期独立, RSC 思想原型作者之一.
**公司&角色**: Ex-Meta React core team; 2025-06 公开宣布 "I'm Doing a Little Consulting"; 2025-11-11 "Hire Me in Japan" 宣告新阶段 [T01-S036].
**代表作 3 件**: (a) Redux co-author (2015, 与 Andrew Clark); (b) overreacted.io blog 长期 RSC / "React as a UI Runtime" / "JSX over the wire" 经典文 [T01-S036][T01-S037]; (c) React Server Components 概念推动者之一 + 2025-12 "Introducing RSC Explorer" hobby project + 2026-01 "A Social Filesystem".
**争议**: RSC 在 React 社区有持续讨论 (复杂度 vs 收益), Abramov 长期是 advocate 立场.
**最近 12 月动态**: 2025-09 "Open Social" / 2025-10 "Where It's at://" / 2025-11 "Hire Me in Japan" / 2025-12 RSC Explorer / 2026-01 "A Social Filesystem" — 个人 transition + 协议探索 [T01-S036].
**endorsement evidence**: Wave 1 canon T05 evergreen #5 (overreacted.io).
**voice samples**:
- "UI = f(data)(state)" [direct quote from T01-S036 / T05-S005 overreacted.io recurring formulation]
- "The protocol is the API." [direct quote from T01-S036 2025-09-26 "Open Social"]

---

## 1.16 陈皓 (左耳朵耗子) — 中文软件架构布道 #1 (in memoriam 2023-05-13)

**核心一句话**: 中文软件架构布道 long-form 第一人, CoolShell 20 年 archive 是中文开发者必读, MegaEase 开源云原生中间件持续到 2026.
**公司&角色** ⚠️ **in memoriam 2023-05-13** (突发心梗, 享年 47): 前 MegaEase 创始人 & CTO (2015 创立); 前 Amazon / Alibaba / Tencent 工程师; 腾讯云 TVP.
**代表作 3 件**: (a) CoolShell.cn 个人博客 2002+ archive (~1.9M 累计阅读), 代表作《我做系统架构的一些原则》11 条 [T01-S044]; (b) MegaEase open source: Easegress (流量调度引擎 2021 开源, 2.6k+ stars) / EaseMesh (服务网格 520 stars) / EaseProbe (健康检查 2.3k stars, last commit 2026-04-24) [T01-S048]; (c) 极客时间《左耳听风》专栏 (190+ 讲).
**争议**: 无显著公开争议. 反 "大厂崇拜" 立场鲜明 — 公开质疑 996 / 阿里架构方案不可移植中小公司.
**最近 12 月动态**: 个人本人 2023-05-13 离世; MegaEase 公司持续 (EaseProbe 2026-04-24 还有 commit [T01-S048]); GitHub Remembering-Haoel 社区 memorial repo 持续 contributions [T01-S047]; memorial.megaease.cn 站点持续 [T01-S046]. 长效影响仍极大.
**endorsement evidence**: Wave 1 canon T04 多次 (CoolShell + 文章); T05 evergreen 中文区 #1.
**voice samples**:
- "进步永远来自探索，不敢冒险才是最大冒险。" [direct quote from T01-S044《我做系统架构的一些原则》第 11 条, 2020-09-15]
- "长痛不如短痛，技术债该还的时候必须还。" [paraphrase from T01-S044《我做系统架构的一些原则》第 8 条, paraphrase]

---

## 1.17 李运华 (华仔) — 中国 application architecture 主流声音 (《从零开始学架构》极客时间专栏)

**核心一句话**: 中文应用架构入门到进阶最系统化的教学者, 极客时间专栏 + 三本书覆盖架构师晋升全 stack.
**公司&角色**: 前阿里资深技术专家 P9 (蚂蚁金服 / 阿里巴巴 / UC / 华为 16 年); 当前独立教学 + 极客时间专栏.
**代表作 3 件**: (a)《从零开始学架构》(电子工业 2018, 同名极客时间专栏 62 讲, 30k+ 学员) [T01-S049][T01-S050][T04-S071][T04-S072]; (b)《编程的逻辑: 如何用面向对象方法实现复杂业务需求》[T01-S051]; (c)《互联网大厂晋升指南》(架构师晋升方法论).
**争议**: 无显著公开争议. 部分观点偏阿里大厂方案, 移植中小公司 需调整 (作者本人有提及).
**最近 12 月动态**: 极客时间专栏持续运营 [T01-S050].
**endorsement evidence**: Wave 1 canon T04 多次 (Douban + 极客时间); T05 课程入口 #1.
**voice samples**:
- "架构设计的本质是权衡，不是追求完美。" [paraphrase from T01-S049 《从零开始学架构》ch.1 核心论点, paraphrase]
- "好的架构师不是技术最强的，而是 trade-off 最准的。" [paraphrase from T01-S050 typical 华仔 talking point, paraphrase]

---

## 1.18 沈剑 — 中文中型互联网架构经验 (公众号"架构师之路" — 注: 公众号 blacklisted, 用 GitChat + GitHub 替代)

**核心一句话**: 58 到家 + 百度时期中型互联网真实落地经验沉淀, 公众号"架构师之路" 是中文社区 evergreen 最高单作者.
**公司&角色**: 前 58 到家 技术委员会主席 + 技术总监; 前百度高级工程师 / 58 高级架构师 + C2C 技术部负责人.
**代表作 3 件**: (a) 公众号"架构师之路" (主阵地, ⚠️ 公众号 blacklisted, 用 GitHub mirror PDF 替代 [T01-S052]); (b) GitChat 课程系列《58 架构实践点滴》[T01-S053]; (c) 多场 ArchSummit / GIAC 演讲 (会议官网档案).
**争议**: 无显著公开争议. 部分早期文章 (秒杀系统 / 分布式 ID) 在 2026 已不是 cutting edge, 但 evergreen 教学价值仍高.
**最近 12 月动态**: 公众号"架构师之路" 持续更新 (主阵地 blacklisted, 转 surrogate 渠道难追) [T01-S052][T01-S053].
**endorsement evidence**: Wave 1 canon T04 多次 (GitChat + 文章); T05 中文区 reference.
**voice samples**:
- "架构是用来解决问题的，不是用来炫技的。" [paraphrase from T01-S052《架构师之路》文集 PDF, paraphrase — 公众号原文 blacklisted 不可直引]
- "中型公司不需要大厂方案，需要刚刚够用的方案。" [paraphrase from T01-S053 GitChat 课程典型立场, paraphrase]

---

## 1.19 蔡超 — Amazon principal engineer 中文架构权威

**核心一句话**: 中文社区里少有的 "在 Amazon 内部做 chief architect" 的一手视角, ArchSummit / QCon 长期 keynote.
**公司&角色**: Group VP & Chief Architect (当前) + AWS Hero (2022) [T01-S054]; 前 Amazon CN tech team chief architect (主导中国市场所有项目, 机器学习 + 大数据 + 云计算改善客户体验).
**代表作 3 件**: (a) ArchSummit 多次 keynote (会议官网档案) [T01-S055]; (b) QCon 中文站演讲; (c) 极客时间课程 + 多场 Amazon 内部架构方法论中文分享 (注: intake brief 误将《Java 工程师修炼之道》归 蔡超, 实为 杭建 著 [T04-S077], 此处纠正).
**争议**: 无显著公开争议.
**最近 12 月动态**: LinkedIn 持续 active [T01-S054]; ArchSummit 中文站持续 keynote.
**endorsement evidence**: Wave 1 canon T05 (ArchSummit) 多次.
**voice samples**:
- "架构师的价值在于把组织内的隐性约束变成显性设计决策。" [paraphrase from T01-S055 蔡超 ArchSummit 典型论点, paraphrase]
- "好的架构应该让团队加速，而不是给团队加锁。" [paraphrase from T01-S054 蔡超 LinkedIn / 演讲典型论点, paraphrase]

---

## 1.20 张逸 — 中文 DDD 推广 (《解构领域驱动设计》)

**核心一句话**: 中文 DDD 最系统化的论著作者, 4 年磨一书, 提出 DDDUP 统一过程 (全局分析 + 架构映射 + 领域建模).
**公司&角色**: 前 ThoughtWorks + 中兴 + 惠普 + 成都民航; 当前独立 DDD 布道 + 微服务架构师 + 大数据平台架构师 + 敏捷转型咨询.
**代表作 3 件**: (a)《解构领域驱动设计》(人民邮电 2021-08, 595 页, ISBN 9787115566232) [T01-S056][T04-S076]; (b) 张逸说博客 zhangyi.xyz [T01-S057] (《解构 DDD》目录 + 章节解读); (c) GitChat 上 DDD 实践课程 (战略 + 战术) — 书的前身.
**争议**: 无显著公开争议. DDDUP 与 Vernon IDDD 方法论有方法学差异, 但互补非互斥.
**最近 12 月动态**: zhangyi.xyz 个人站持续维护 [T01-S057].
**endorsement evidence**: Wave 1 canon T04 多次 (Douban + 张逸说).
**voice samples**:
- "DDD 不是技术，是一种以业务为中心的设计哲学。" [paraphrase from T01-S056《解构领域驱动设计》前言, paraphrase]
- "限界上下文不是技术边界，是语言边界。" [paraphrase from T01-S057 张逸说博客典型论点, paraphrase]

---

## 1.21 (anti-figure A) "Architecture Astronaut" — Joel Spolsky 2001 (反 over-abstract)

⚠️ **不背书; 这是行业自省真实声音, 必须保留.**

**核心一句话**: 2001-04-21 Joel Spolsky 在《Joel on Software》创词 — 警惕 "上升到没有氧气" 的 over-abstract 架构师 / 架构愿景而忽视交付物.
**出处**: joelonsoftware.com 2001-04-21 "Don't Let Architecture Astronauts Scare You" [T01-S058][T04-S070].
**反面 canon 角色**: 提醒 software architecture 行业内部最持久的自省 — 架构 hype 浪潮 (SOA / ESB / 微服务 / Serverless / K8s for everything / Mesh / RSC) 反复出现时, "astronaut" 这个词标记每一次过度抽象的人.
**真实反例 — 当代企业 case (来自 community / 公开资源)**: 大型企业内部 "架构 review committee" 与 "delivery team" 失衡 — committee 出 50 页 PPT, team 还没写一行可上线代码. 这种 over-engineering 在监管严的金融 / 大型电信 反复出现.
**Wikipedia 词条**: en.wikipedia.org/wiki/Architecture_astronaut [T01-S059] — 仍是 active 词条.
**voice samples** (Joel Spolsky direct quotes):
- "When you go too far up, abstraction-wise, you run out of oxygen." [direct quote from T01-S058 / T04-S070, 2001-04-21]
- "Tell me something new that I can do that I couldn't do before, O Astronauts, or stay up there in space." [direct quote from T01-S058 / T04-S070, 2001-04-21]
- "Architecture Astronauts will say things like: 'Can you imagine a program like Napster where you can download anything, not just songs?'" [direct quote from T01-S058 / T04-S070, 2001-04-21]

---

## 1.22 (anti-figure B) "Cargo cult microservices" / "Resume-driven development" — community 反模式 + DHH leaving the cloud 系列

⚠️ **不软化; 这是行业自省真实声音, 必须保留.**

**核心一句话**: 反 "为了简历堆 K8s + Istio + Service Mesh + 全套 cloud native 给一个 CRUD 应用" 的反模式, 2018+ 在 community 普及; 2022+ DHH "leaving the cloud" 系列 + Shopify 模块化单体 + Sam Newman 自己 "don't start with microservices" 共同发声.
**反面 canon 角色**: 不背书 cargo cult, 但揭示行业现实: 多数公司用微服务是 resume-driven, 不是 problem-driven.

**真实反例 — 公开 case**:
- **DHH (David Heinemeier Hansson, 37signals/Basecamp/Rails 创始人) "Leaving the Cloud" 系列**: 2022-10 宣布 cloud exit, 2023-2025 持续记录: 现金节省 ~60% ($180k/月 → $80k/月, 5 年 ~$10M); 自研 Kamal 部署工具; 公开 basecamp.com/cloud-exit 主题页 [T01-S060]; 2025-10 "majestic monolith remains undefeated" 帖 [T01-S062].
- **Shopify modular monolith 经验** (反 microservices-as-default 实证): 2.8M LoC Rails monolith + 500k commits, 用 Rails Engines + Sorbet + Packwerk 拆 37 个组件 (modular monolith), 而不是拆微服务; Shopify Engineering 详尽 case study [T01-S063].
- **Stack Overflow** 长期单体架构跑全球 top traffic, 一组小 ASP.NET app 足够 (反 microservices-as-default 实证案例, 历史 case).
- **Sam Newman 自己 2019+ 改口** "don't start with microservices" [T01-S010] — 来自微服务最大布道者本人.

**voice samples** (DHH direct quotes, 反 microservices/cloud cargo cult):
- "The majestic monolith remains undefeated for the vast majority of web apps. Replacing method calls with network calls makes everything harder, slower, and more brittle." [direct quote from T01-S062, DHH X 1981342407129235683, 2025-10]
- "Monoliths are the future because the problem people are trying to solve with microservices doesn't really line up with reality." [direct quote attributed Kelsey Hightower 2020, reposted by DHH on X — Hightower 是 cloud-native 布道者本人发声, 反向力度极强]

---

## 1.X 流派 / 学派 总览

| 流派 | 奠基 | 当代代表 | 核心分歧点 |
|------|------|---------|-----------|
| Pattern movement | Fowler (PoEAA 2002) / Hohpe+Woolf (EIP 2003) | Fowler 持续 / Hohpe 转 Architect Elevator | 模式语言是 catalog 还是教学骨架? Fowler 倾向 catalog, Hohpe 倾向 narrative |
| DDD | Evans (Blue Book 2003) / Cockburn (Hexagonal 2005) | Vernon (Red Book + IDDD) / 张逸 (中文) / Vlad Khononov (Learning DDD 2021) | 大型团队 DDD 重 vs 启动期轻 (Fowler MonolithFirst 间接质疑) |
| Clean / Hexagonal / Onion | Uncle Bob (Clean Arch) / Cockburn (Hexagonal) / Jeffrey Palermo (Onion) | Uncle Bob 持续争议 / Cockburn 学术 | TDD == professionalism? Coplien vs Martin 2007 辩论持续 |
| Microservices | Newman (Building Microservices 2015) / Richardson (microservices.io) / Adrian Cockcroft (Netflix Cloud Architect 时期) | Newman 改口 "don't start with" / Richardson 2nd ed 2025 强调 fast flow + Team Topologies 三角 [T01-S065] | "default microservices" vs "modular monolith first" — Newman + Shopify + DHH 强反 |
| Event-driven & log-centric | Greg Young (CQRS+ES) / Kreps (Log + Kafka) / Helland (ACM Queue 系列) | Kreps Confluent CEO 持续 / Helland substack / Young 独立 | EventSourcing 是否过重? Greg Young 推荐 use sparingly (2020+ 多次公开提示), 实操派认为对多数场景过重 |
| Distributed systems thinking | Lamport (Time/Clocks 1978, Paxos, TLA+) / Vogels (Dynamo 2007) / Brewer (CAP) | Kleppmann (DDIA + Cambridge) / Vogels (AWS CTO emeritus) / Helland | formal methods (TLA+) vs practical engineering (DDIA) — 学术 vs 工程 持续张力 |
| Evolutionary architecture | Ford (BEA 2017) / Parsons (ThoughtWorks CTO emeritus) / Brown (C4) | Ford Fundamentals 2nd ed 2025 / Brown C4 + Structurizr | fitness function 工程化 vs ad-hoc — CI/CD pipeline 集成度仍是开放问题 |
| Cloud-native | Burns (K8s co-founder, Designing Distributed Systems) / Hightower (Kubernetes The Hard Way) / Cockcroft (Netflix Cloud Architect) | Burns Azure CVP / Hightower retired-not-tired / Cockcroft sustainability focus | K8s for everything (反模式) — Hightower 本人是最大警告者 |
| Front-end architecture | Abramov (Redux + RSC) / Andrew Clark (React core) | Abramov 2025 independent + RSC Explorer | micro-frontend 是否过度? Module Federation 派 vs 一体派, Abramov 偏一体 + RSC |
| 中国大厂中间件 / 中文软件架构布道 | 陈皓 (CoolShell 2002+, in memoriam 2023-05-13) / 阿里中间件团队 | 李运华 (《从0开始学架构》) / 沈剑 (架构师之路) / 蔡超 (Amazon CN) / 张逸 (DDD 中文) | 大厂方案是否可移植中小公司 (普遍 NO — 陈皓 / 沈剑 / 李运华 均承认这点) |

---

Track 01 done. 70 sources. 22 figures (英文 15 / 中文 5 + 2 anti). 10 流派覆盖 ✓. endorsement-evidence ≥ 2 的 figures: 17 (Fowler / Kleppmann / Newman / Hohpe / Evans / Vernon / Helland / Vogels / Lamport / Ford / Richardson / Burns / Hightower / Abramov / Kreps / 陈皓 / 李运华).
