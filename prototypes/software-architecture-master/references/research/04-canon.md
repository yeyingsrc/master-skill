# Track 04 — Canon (software architecture)

> Wave 1 Track 04 — essential books / papers / canon documents. Industry: software architecture (application/system architecture, 不含 hardware / 纯 EA / 纯 DevOps / 纯 security), locale=global (中外双语并重 中文:英文 = 1:3-1:4), profile=practitioner.
>
> 结构约束 notes (诚实): (1) 软件架构 canon 90% 英文奠基 (Parnas 1972 → Kleppmann 2017 → Software Architecture The Hard Parts 2022); (2) 中文当代 canon 起步晚, 主要 2015+ (李运华 / 张开涛 / 张逸 / 李智慧 / 沈剑 公众号 / 陈皓 CoolShell), 厚度 中文:英文 = 1:3-1:4 是行业现实; (3) 经典 paper (Parnas 1972 / Helland / Vogels) 多在 ACM/IEEE 收费墙后, 也有 author 个人 site mirror 公开 PDF; (4) 部分 cloud-native 经典 (12-factor / Google SRE book) 完全公开免费 html — verified_primary; (5) zh-CN 黑名单严格不收知乎 / 公众号 / 百度百科 / CSDN / 掘金 / 简书 / cnblogs 等任何 blacklisted 站点 (即使作者本人原文也 surrogate_primary 兜底, 不可 verified_primary); 中文 canon 大量在 douban.com (book.douban.com 是 verified_primary, m./read./ebook 子域 是 secondary); (6) intake 简报里把《Java 工程师修炼之道》归到 蔡超 名下, 实查为 杭建 著 (电子工业 2018) — 此处按真实作者纠正记录; 蔡超 本人未发现公开必读书 canon, 仅有 ArchSummit / QCon 演讲与 微信公众号 文章 (公众号 blacklisted, 整条不收).

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://dl.acm.org/doi/10.1145/361598.361623 | verified_primary | 2026-05-17 | ACM CACM | Parnas 1972 "On the Criteria To Be Used in Decomposing Systems into Modules" — original Communications of the ACM record |
| T04-S002 | https://cacm.acm.org/research/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/ | verified_primary | 2026-05-17 | ACM CACM | Parnas 1972 CACM HTML mirror |
| T04-S003 | https://kilthub.cmu.edu/articles/journal_contribution/On_the_criteria_to_be_used_in_decomposing_systems_into_modules/6607958 | verified_primary | 2026-05-17 | CMU KiltHub | Parnas 1972 PDF mirror on CMU institutional repository |
| T04-S004 | https://www.cs.cmu.edu/~lanthony/classes/SoftwareDesign/Paper1.ppt | verified_primary | 2026-05-17 | CMU CS | Parnas 1972 teaching slides hosted by CMU CS dept |
| T04-S005 | https://dl.acm.org/doi/10.5555/207583 | verified_primary | 2026-05-17 | ACM DL | Brooks 1995 *The Mythical Man-Month* anniversary ed. ACM record |
| T04-S006 | https://archive.org/details/MythicalManMonth/ | secondary | 2026-05-17 | Internet Archive | Brooks 1995 anniversary edition scanned mirror |
| T04-S007 | https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959 | secondary | 2026-05-17 | Amazon | Brooks 1995 anniversary ed. retail listing |
| T04-S008 | https://ieeexplore.ieee.org/document/6312940/ | verified_primary | 2026-05-17 | IEEE Xplore | Parnas+Clements 1986 "A Rational Design Process: How and Why to Fake It" IEEE TSE original |
| T04-S009 | https://users.ece.utexas.edu/~perry/education/SE-Intro/fakeit.pdf | verified_primary | 2026-05-17 | UT Austin ECE | Parnas+Clements 1986 PDF mirror on UT Austin .edu |
| T04-S010 | https://ics.uci.edu/~taylor/classes/121/IEEE86_Parnas_Clement.pdf | verified_primary | 2026-05-17 | UC Irvine ICS | Parnas+Clements 1986 PDF mirror on UCI .edu |
| T04-S011 | https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612 | secondary | 2026-05-17 | Amazon | GoF 1994 *Design Patterns* (Gamma/Helm/Johnson/Vlissides) retail listing |
| T04-S012 | https://en.wikipedia.org/wiki/Design_Patterns | reference | 2026-05-17 | Wikipedia | GoF 1994 reference summary (23 patterns catalog) |
| T04-S013 | https://martinfowler.com/books/eaa.html | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler 2002 *PoEAA* official book page — author personal site (vendor docs / author one-source) |
| T04-S014 | https://martinfowler.com/eaaCatalog/ | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler PoEAA pattern catalog (40+ patterns) — author personal site (vendor docs) |
| T04-S015 | https://www.informit.com/store/patterns-of-enterprise-application-architecture-9780321127426 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | PoEAA publisher listing — publisher vendor docs |
| T04-S016 | https://www.enterpriseintegrationpatterns.com/ | surrogate_primary | 2026-05-17 | Hohpe+Woolf | EIP 2003 official site (65 patterns) — author site vendor docs |
| T04-S017 | https://martinfowler.com/books/eip.html | surrogate_primary | 2026-05-17 | martinfowler.com | EIP 2003 entry on Fowler Signature Series — author site vendor docs |
| T04-S018 | https://www.amazon.com/Enterprise-Integration-Patterns-Designing-Deploying/dp/0321200683 | secondary | 2026-05-17 | Amazon | EIP 2003 retail listing |
| T04-S019 | https://www.dddcommunity.org/book/evans_2003/ | surrogate_primary | 2026-05-17 | DDD Community | Evans 2003 Blue Book official community page — author-affiliated site vendor docs |
| T04-S020 | https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | Evans Blue Book publisher listing — vendor docs |
| T04-S021 | https://www.pearson.com/en-us/subject-catalog/p/implementing-domain-driven-design/P200000009616/9780133039887 | surrogate_primary | 2026-05-17 | Pearson | Vernon 2013 Red Book *Implementing DDD* publisher listing — vendor docs |
| T04-S022 | https://www.informit.com/store/implementing-domain-driven-design-9780133039894 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | Vernon 2013 Red Book InformIT listing — vendor docs |
| T04-S023 | https://www.informit.com/store/domain-driven-design-distilled-9780134434995 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | Vernon 2016 *DDD Distilled* publisher listing — vendor docs |
| T04-S024 | https://pragprog.com/titles/mnee2/release-it-second-edition/ | surrogate_primary | 2026-05-17 | Pragmatic Bookshelf | Nygard 2018 *Release It!* 2nd ed publisher page — vendor docs |
| T04-S025 | https://media.pragprog.com/titles/mnee2/antipatterns.pdf | surrogate_primary | 2026-05-17 | Pragmatic Bookshelf | *Release It!* 2nd ed Antipatterns sample chapter PDF — vendor docs |
| T04-S026 | https://12factor.net/ | surrogate_primary | 2026-05-17 | 12factor.net (Wiggins / Heroku) | vendor docs (作者一手) — Wiggins 2011 *The Twelve-Factor App* 公开 manifesto, 全文免费|
| T04-S027 | https://www.heroku.com/blog/twelve-factor-apps/ | surrogate_primary | 2026-05-17 | Heroku Blog | 12-factor Heroku origin post 2011 — vendor docs (engineering blog) |
| T04-S028 | https://www.heroku.com/blog/updating-twelve-factor-call-for-participation/ | surrogate_primary | 2026-05-17 | Heroku Blog | 12-factor 2024 update + open-source call — vendor docs |
| T04-S029 | https://sre.google/sre-book/table-of-contents/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — Beyer/Jones/Petoff/Murphy 2016 *Site Reliability Engineering* 免费 HTML|
| T04-S030 | https://sre.google/books/ | surrogate_primary | 2026-05-17 | sre.google (Google) | vendor docs (Google 一手) — SRE book series landing (SRE book + Workbook + Building Secure & Reliable)|
| T04-S031 | https://www.amazon.com/Designing-Distributed-Systems-Paradigms-Kubernetes/dp/1098156358 | secondary | 2026-05-17 | Amazon | Burns 2024 *Designing Distributed Systems* 2nd ed retail listing |
| T04-S032 | https://opensource.microsoft.com/blog/2018/03/26/new-oreilly-e-book-on-designing-distributed-systems-available-for-free-download/ | surrogate_primary | 2026-05-17 | Microsoft Open Source Blog | Burns 2018 *Designing Distributed Systems* 1st ed free download announcement — vendor docs (engineering blog) |
| T04-S033 | https://www.oreilly.com/library/view/designing-distributed-systems/9781098156343/ | surrogate_primary | 2026-05-17 | O'Reilly | Burns 2nd ed publisher listing — vendor docs |
| T04-S034 | https://dataintensive.net/ | surrogate_primary | 2026-05-17 | Kleppmann personal | Kleppmann 2017 *DDIA* official book site (the Wild Boar Book) — author personal site vendor docs |
| T04-S035 | https://martin.kleppmann.com/2017/03/27/designing-data-intensive-applications.html | surrogate_primary | 2026-05-17 | Kleppmann personal | DDIA author launch post 2017-03-27 — author personal site vendor docs |
| T04-S036 | https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/ | surrogate_primary | 2026-05-17 | O'Reilly | DDIA 1st ed publisher listing — vendor docs |
| T04-S037 | https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ | surrogate_primary | 2026-05-17 | O'Reilly | DDIA 2nd ed (Kleppmann+Riccomini, 2026-03) publisher listing — vendor docs |
| T04-S038 | https://www.allthingsdistributed.com/ | surrogate_primary | 2026-05-17 | Werner Vogels personal | Vogels (Amazon CTO) *All Things Distributed* blog — author personal site vendor docs |
| T04-S039 | https://www.allthingsdistributed.com/historical/archives/000534.html | surrogate_primary | 2026-05-17 | Werner Vogels personal | Vogels seminal "A Conversation with Werner Vogels" archive — vendor docs |
| T04-S040 | https://queue.acm.org/detail.cfm?id=3025012 | surrogate_primary | 2026-05-17 | ACM Queue | 协会 (ACM Queue 一手) — Helland 2007/2016 "Life Beyond Distributed Transactions"|
| T04-S041 | https://dl.acm.org/doi/10.1145/3009826 | verified_primary | 2026-05-17 | ACM DL | Helland "Life Beyond Distributed Transactions" CACM republication record |
| T04-S042 | https://queue.acm.org/detail.cfm?id=2884038 | surrogate_primary | 2026-05-17 | ACM Queue | 协会 (ACM Queue 一手) — Helland 2015 "Immutability Changes Everything"|
| T04-S043 | https://www.cidrdb.org/cidr2015/Papers/CIDR15_Paper16.pdf | verified_primary | 2026-05-17 | CIDR | Helland 2015 "Immutability Changes Everything" CIDR conference PDF |
| T04-S044 | https://samnewman.io/books/building_microservices_2nd_edition/ | surrogate_primary | 2026-05-17 | Sam Newman personal | Newman 2021 *Building Microservices* 2nd ed author page — author personal site vendor docs |
| T04-S045 | https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/ | surrogate_primary | 2026-05-17 | O'Reilly | Newman 2021 Building Microservices 2nd ed publisher listing — vendor docs |
| T04-S046 | https://samnewman.io/books/monolith-to-microservices/ | surrogate_primary | 2026-05-17 | Sam Newman personal | Newman 2019 *Monolith to Microservices* author page — vendor docs |
| T04-S047 | https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/ | surrogate_primary | 2026-05-17 | O'Reilly | Newman 2019 *Monolith to Microservices* publisher listing — vendor docs |
| T04-S048 | https://microservices.io/ | surrogate_primary | 2026-05-17 | Chris Richardson | Richardson *microservices.io* pattern catalog — author personal site vendor docs |
| T04-S049 | https://microservices.io/book | surrogate_primary | 2026-05-17 | Chris Richardson | Richardson 2018 *Microservices Patterns* book page — author site vendor docs |
| T04-S050 | https://www.manning.com/books/microservices-patterns | surrogate_primary | 2026-05-17 | Manning | Richardson 2018 Manning publisher listing — vendor docs |
| T04-S051 | https://www.manning.com/books/microservices-patterns-second-edition | surrogate_primary | 2026-05-17 | Manning | Richardson 2nd ed (in progress) Manning listing — vendor docs |
| T04-S052 | https://nealford.com/books/buildingevolutionaryarchitectures.html | surrogate_primary | 2026-05-17 | Neal Ford personal | Ford+Parsons+Kua+Sadalage 2023 *Building Evolutionary Architectures* 2nd ed author page — vendor docs |
| T04-S053 | https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ | surrogate_primary | 2026-05-17 | O'Reilly | BEA 2nd ed publisher listing — vendor docs |
| T04-S054 | https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/ | surrogate_primary | 2026-05-17 | O'Reilly | Richards+Ford 2020 *Fundamentals of Software Architecture* publisher listing — vendor docs |
| T04-S055 | https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ | surrogate_primary | 2026-05-17 | O'Reilly | Richards+Ford 2nd ed Fundamentals publisher listing — vendor docs |
| T04-S056 | https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_Fundamentals_of_Software_Architecture_Free_Chapter_en.pdf | surrogate_primary | 2026-05-17 | ThoughtWorks | Fundamentals free sample chapter PDF — vendor docs (engineering blog mirror) |
| T04-S057 | https://www.oreilly.com/library/view/software-architecture-the/9781492086888/ | surrogate_primary | 2026-05-17 | O'Reilly | Ford+Richards+Sadalage+Dehghani 2022 *Software Architecture The Hard Parts* publisher listing — vendor docs |
| T04-S058 | https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_software_architecture_hard_parts_ch7_en.pdf | surrogate_primary | 2026-05-17 | ThoughtWorks | Hard Parts free sample chapter 7 PDF — vendor docs |
| T04-S059 | https://martinfowler.com/books/refactoring.html | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler *Refactoring* 1st/2nd ed official book page — author personal site vendor docs |
| T04-S060 | https://martinfowler.com/articles/refactoring-2nd-ed.html | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler 2018 2nd ed launch essay — author site vendor docs |
| T04-S061 | https://www.informit.com/store/refactoring-improving-the-design-of-existing-code-9780134757599 | surrogate_primary | 2026-05-17 | InformIT (Pearson) | Refactoring 2nd ed publisher listing — vendor docs |
| T04-S062 | https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052 | secondary | 2026-05-17 | Amazon | Feathers 2004 *Working Effectively with Legacy Code* retail listing |
| T04-S063 | https://ptgmedia.pearsoncmg.com/images/9780131177055/samplepages/0131177052.pdf | surrogate_primary | 2026-05-17 | Pearson | Feathers 2004 free sample pages PDF — publisher vendor docs |
| T04-S064 | https://www.oreilly.com/library/view/tidy-first/9781098151232/ | surrogate_primary | 2026-05-17 | O'Reilly | Beck 2024 *Tidy First?* publisher listing — vendor docs |
| T04-S065 | https://tidyfirst.substack.com/p/empirical-software-design-qa | surrogate_primary | 2026-05-17 | Kent Beck Substack | Beck companion Substack 'Tidy First' Q&A — author site vendor docs |
| T04-S066 | https://teamtopologies.com/book | surrogate_primary | 2026-05-17 | teamtopologies.com | Skelton+Pais 2019 *Team Topologies* official book site — author site vendor docs |
| T04-S067 | https://itrevolution.com/product/team-topologies-second-edition/ | surrogate_primary | 2026-05-17 | IT Revolution | Team Topologies 2nd ed (2025) publisher listing — vendor docs |
| T04-S068 | https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/ | surrogate_primary | 2026-05-17 | Pragmatic Bookshelf | Hunt+Thomas 2019 *Pragmatic Programmer* 20th anniv ed — vendor docs |
| T04-S069 | https://itrevolution.com/product/accelerate/ | surrogate_primary | 2026-05-17 | IT Revolution | Forsgren+Humble+Kim 2018 *Accelerate* (DORA metrics origin) publisher page — vendor docs |
| T04-S070 | https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/ | surrogate_primary | 2026-05-17 | joelonsoftware.com | Spolsky 2001 "Don't Let Architecture Astronauts Scare You" — author personal site vendor docs (反面 canon) |
| T04-S071 | https://book.douban.com/subject/30335935/ | verified_primary | 2026-05-17 | book.douban.com | 李运华《从零开始学架构》(电子工业 2018) — Douban 主域 verified_primary |
| T04-S072 | https://time.geekbang.org/column/intro/81 | surrogate_primary | 2026-05-17 | time.geekbang.org | 李运华《从0开始学架构》极客时间专栏 — 极客时间课程 syllabus |
| T04-S073 | https://time.geekbang.org/column/article/40573 | surrogate_primary | 2026-05-17 | time.geekbang.org | 李运华专栏新书首发文 — syllabus |
| T04-S074 | https://m.douban.com/book/subject/26999243/ | secondary | 2026-05-17 | m.douban.com | 张开涛《亿级流量网站架构核心技术》(电子工业 2017) — m. 子域 secondary |
| T04-S075 | https://www.goodreads.com/book/show/42779758 | secondary | 2026-05-17 | Goodreads | 张开涛《亿级流量网站架构核心技术》Goodreads 镜像条目 |
| T04-S076 | https://book.douban.com/subject/35553520/ | verified_primary | 2026-05-17 | book.douban.com | 张逸《解构领域驱动设计》(人民邮电 2021-08, ISBN 9787115566232) — Douban 主域 verified_primary |
| T04-S077 | https://book.douban.com/subject/30185212/ | verified_primary | 2026-05-17 | book.douban.com | 杭建《Java 工程师修炼之道》(电子工业 2018) — Douban 主域 verified_primary (注: intake brief 误归 蔡超, 实查为 杭建 著) |
| T04-S078 | https://m.douban.com/book/subject/25723064/ | secondary | 2026-05-17 | m.douban.com | 李智慧《大型网站技术架构: 核心原理与案例分析》(电子工业 2013) — m. 子域 secondary |
| T04-S079 | https://coolshell.cn/articles/21672.html | surrogate_primary | 2026-05-17 | coolshell.cn (陈皓) | 陈皓《我做系统架构的一些原则》— 作者裸域 vendor docs |
| T04-S080 | https://coolshell.cn/haoel | surrogate_primary | 2026-05-17 | coolshell.cn (陈皓) | 陈皓 "关于" 页 — 作者裸域 vendor docs |
| T04-S081 | https://coolshell.cn/ | surrogate_primary | 2026-05-17 | coolshell.cn (陈皓) | CoolShell 首页 — 作者裸域 vendor docs |
| T04-S082 | https://gitbook.cn/gitchat/author/5826b2809b3cc37401d4f8e2 | surrogate_primary | 2026-05-17 | gitbook.cn (沈剑) | 沈剑 (58 到家 高级总监) GitChat 作者页 (《架构师之路》系列 — 公众号本身 blacklisted, GitChat 是 GitBook 官方平台) — syllabus |
| T04-S083 | https://gitbook.cn/books/5843621a3a39cd5239bb3a46/index.html | surrogate_primary | 2026-05-17 | gitbook.cn (沈剑) | 沈剑《58 架构实践点滴》GitChat 课程 — syllabus |
| T04-S084 | https://martinfowler.com/microservices/ | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler+Lewis 2014 "Microservices" canonical定义 essay — author personal site vendor docs |
| T04-S085 | https://martinfowler.com/bliki/MonolithFirst.html | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler 2015 "MonolithFirst" — Fowler 个人 site vendor docs |
| T04-S086 | https://martinfowler.com/bliki/StranglerFigApplication.html | surrogate_primary | 2026-05-17 | martinfowler.com | Fowler 2004 Strangler Fig (legacy 迁移核心 pattern) — vendor docs |

(86 sources total. Verified_primary: 16 / Surrogate_primary: 57 / Secondary: 11 / Reference: 1 / Blacklisted+Dead: 0. 一手率 = (16+57)/86 = 84.9%.)

---

## 4.1 奠基 (Foundational papers + books, 1972-1995)

- **Parnas 1972 — "On the Criteria To Be Used in Decomposing Systems into Modules"** (CACM 15(12)). 奠基: 提出 "信息隐藏 (information hiding)" 与 "按设计决策划分模块 (modular decomposition by decision hiding)" — 推翻当时主流的按流程图节点切模块的做法。直到 2026 仍是评判一切模块边界 (含 microservice 边界) 的根原则。一句话: *"Each module is characterized by its knowledge of a design decision which it hides from all others."* 必读. [T04-S001] [T04-S002] [T04-S003] [T04-S004]

- **Brooks 1975/1995 — *The Mythical Man-Month*** (Addison-Wesley, 20th anniv. 1995). Brooks 法则 "adding manpower to a late software project makes it later" + No Silver Bullet (1986) 章节. 软件工程组织 / 项目管理 / essential vs accidental complexity 的母本. 2026 仍是入门必备 (Brooks 2022 逝世后业内重读浪潮). [T04-S005] [T04-S006] [T04-S007]

- **Parnas+Clements 1986 — "A Rational Design Process: How and Why to Fake It"** (IEEE TSE SE-12(2)). 反完美主义经典: 承认 "真实软件设计永远不会按瀑布/理性流程推进, 但我们应当 *伪造* 文档让它看起来如此", 是后来 evolutionary / agile architecture 的伏笔. [T04-S008] [T04-S009] [T04-S010]

- **Gamma+Helm+Johnson+Vlissides (GoF) 1994 — *Design Patterns: Elements of Reusable Object-Oriented Software*** (Addison-Wesley). 23 个经典 OO 模式 (Singleton/Factory/Observer/Strategy/...). 30+ 年后争议增多 (尤其 Singleton 反模式化), 但模式词汇本身已是行业通用语. 写明: 部分模式社区已视为 anti-pattern (Singleton / 多重 Inheritance-based Decorator), Java/Kotlin 现代实践常用更轻量替代. [T04-S011] [T04-S012]

## 4.2 Enterprise pattern (2002-2003)

- **Fowler 2002 — *Patterns of Enterprise Application Architecture* (PoEAA)** (Addison-Wesley Signature). 40+ patterns: Repository / Unit of Work / Domain Model / Active Record / Data Mapper / Service Layer / Identity Map / Lazy Load. 现代 ORM (Hibernate/JPA/Entity Framework/SQLAlchemy/ActiveRecord) 设计直接源自此书. 在线 pattern catalog 永久免费. [T04-S013] [T04-S014] [T04-S015]

- **Hohpe+Woolf 2003 — *Enterprise Integration Patterns* (EIP)** (Addison-Wesley Signature). 65 messaging patterns: Channel / Message Router / Content-Based Router / Aggregator / Splitter / Saga / Pipes and Filters. Apache Camel / Spring Integration / Mulesoft / Kafka Streams 拓扑全部以这套词汇为基础. 官网 enterpriseintegrationpatterns.com 含每个 pattern 的图与描述 (永久免费). [T04-S016] [T04-S017] [T04-S018]

## 4.3 DDD

- **Evans 2003 — *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Blue Book)** (Addison-Wesley). DDD 母本. 战略 (Ubiquitous Language / Bounded Context / Context Map) + 战术 (Entity / Value Object / Aggregate / Repository / Domain Event / Domain Service). 难读但绕不开. 一句话: *"The heart of software is its ability to solve domain-related problems for its user."* [T04-S019] [T04-S020]

- **Vernon 2013 — *Implementing Domain-Driven Design* (Red Book)** (Addison-Wesley). Blue Book 的"操作手册": Aggregate 设计四条规则 / Bounded Context 集成模式 / Event-Driven 架构 / CQRS / Event Sourcing 落地. Java 例子但 C# 程序员同样适用. [T04-S021] [T04-S022]

- **Vernon 2016 — *Domain-Driven Design Distilled*** (Addison-Wesley). 200 页快速入门, 战略部分浓缩特别适合产品 / 架构师交流, 然后再回头啃 Blue/Red. [T04-S023]

## 4.4 Stability / production-grade

- **Nygard 2007/2018 — *Release It! Design and Deploy Production-Ready Software* (2nd ed)** (Pragmatic Bookshelf). Stability Patterns (Circuit Breaker / Bulkhead / Timeout / Fail Fast / Steady State / Decoupling Middleware) 与 Antipatterns (Cascading Failures / Blocked Threads / Unbalanced Capacities / Slow Responses) 的源头. 2nd ed (2018) 新增 cloud-native / microservices / DevOps. Circuit Breaker 词汇就是这本书给 Hystrix/Resilience4j 命名的. [T04-S024] [T04-S025]

## 4.5 Cloud-native + 12-Factor + SRE

- **Wiggins (Heroku) 2011 — *The Twelve-Factor App*** (12factor.net). 12 条 SaaS 应用构建准则 (Codebase / Dependencies / Config / Backing services / Build-release-run / Processes / Port binding / Concurrency / Disposability / Dev-prod parity / Logs / Admin processes). Kubernetes / Cloud Run / ECS 的部署假设全部以此为隐含规范. 永久免费 html, 2024 Heroku 开源治理. [T04-S026] [T04-S027] [T04-S028]

- **Beyer+Jones+Petoff+Murphy (Google) 2016 — *Site Reliability Engineering: How Google Runs Production Systems*** (O'Reilly + sre.google). 完整 Google SRE 实践: SLI/SLO/SLA / Error budget / Toil 自动化 / Blameless postmortem / Capacity planning / Load shedding / Cascading failure. 全书 sre.google 免费 HTML, 后续 *SRE Workbook* + *Building Secure and Reliable Systems* 同样免费. 架构师必读章节: Ch16 Tracking Outages, Ch22 Addressing Cascading Failures, Ch24 Distributed Periodic Scheduling, Ch6 Monitoring Distributed Systems. [T04-S029] [T04-S030]

- **Burns 2018/2024 — *Designing Distributed Systems* (1st/2nd ed)** (O'Reilly + Microsoft 免费 PDF). Kubernetes co-founder 整理的分布式 pattern: Sidecar / Ambassador / Adapter / Replicated Load-Balanced / Sharded / Scatter-Gather / Work Queue / Event-Driven / FaaS. 1st ed 微软免费送, 2nd ed (2024) 增 AI inference/training 章节. [T04-S031] [T04-S032] [T04-S033]

## 4.6 Distributed data (DDIA + Vogels + Helland)

- **Kleppmann 2017 — *Designing Data-Intensive Applications* (DDIA, the Wild Boar Book)** (O'Reilly). 2017-2026 软件架构师必读 #1, 无可争议. 三部曲: Foundations of Data Systems (Reliability/Scalability/Maintainability + Data Models + Storage + Encoding/Evolution) / Distributed Data (Replication/Partitioning/Transactions/Consistency-Consensus) / Derived Data (Batch/Stream/Future of Data Systems). 比所有大学教材都强. 2nd ed (Kleppmann+Riccomini, 2026-03) 新增 AI/ML 数据系统 / vector indexes / DataFrames / 本地优先 / GraphQL / 工作流引擎. [T04-S034] [T04-S035] [T04-S036] [T04-S037]

- **Helland 2007/2016 — "Life Beyond Distributed Transactions: An Apostate's Opinion"** (CIDR 2007, 重发 ACM Queue 2016, CACM 2017). 数据分片 + 无分布式事务 的工程哲学奠基, 核心: "几乎所有大型在线系统都不能依赖跨分片 ACID, 应使用 entity / activity / immutable message 概念". Saga / Idempotent message / Outbox pattern / Lambda Architecture 灵感来源. [T04-S040] [T04-S041]

- **Helland 2015 — "Immutability Changes Everything"** (CIDR 2015 + ACM Queue 2015 13(9)). 不可变数据从应用层到硬件层的递归扫描. 解释为什么 event sourcing / append-only log / immutable infrastructure / git / Kafka / S3 object store 都是同一根逻辑. 30 页, 必读. [T04-S042] [T04-S043]

- **Vogels (Amazon CTO) — *All Things Distributed*** (allthingsdistributed.com). 长跑 20+ 年的个人 blog, 收录 Dynamo paper 复盘 / Eventually Consistent / S3 设计经验 / Werner 每年 CTO 预测. 架构师定期回访的 RSS. [T04-S038] [T04-S039]

## 4.7 Microservices

- **Newman 2014/2021 — *Building Microservices: Designing Fine-Grained Systems* (1st/2nd ed)** (O'Reilly). 1st ed (2014) 给了 microservice 词汇一个工程定义, 2nd ed (2021) 全书重写, 加入 user interface / container orchestration / serverless / 服务网格 / 安全 / 测试. 2nd ed 是架构师 2026 的标准答案. [T04-S044] [T04-S045]

- **Newman 2020 — *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith*** (O'Reilly). 单体 → 微服务的可执行 playbook: Strangler Fig / Branch by Abstraction / Parallel Run / Decorating Collaborator + 数据库分解策略 (Shared DB → DB View → DB Wrapping Service → Saga). 单体不愿动的人请先看这本再决定. [T04-S046] [T04-S047]

- **Richardson 2018 — *Microservices Patterns: With examples in Java*** (Manning). 44 patterns 系统化分类: Decomposition / Communication / Transactional messaging (Saga + Outbox) / External API (BFF) / Service deployment / Observability / Security. microservices.io 是免费 catalog 镜像. 2nd ed 在 Manning MEAP 中. [T04-S048] [T04-S049] [T04-S050] [T04-S051]

- **Fowler+Lewis 2014 — "Microservices"** (martinfowler.com). microservice 这个术语 2014-03 的正式定义文 (9 characteristics: componentization via services / organized around business capabilities / products not projects / smart endpoints and dumb pipes / decentralized governance / decentralized data management / infrastructure automation / design for failure / evolutionary design). 必读起点. [T04-S084]

- **Fowler 2015 — "MonolithFirst"** (martinfowler.com). 反主流声音: 大多团队该先从 modular monolith 起步, 别一上来就 microservice. 与 Newman 立场互补. [T04-S085]

## 4.8 Evolutionary architecture

- **Ford+Parsons+Kua (+ Sadalage 2nd ed) 2017/2023 — *Building Evolutionary Architectures: Automated Software Governance* (1st/2nd ed)** (O'Reilly). 核心概念 *fitness function* — 把架构特性 (性能 / 可扩展性 / 安全 / 合规) 当成可自动验证的回归测试, 让架构能在长期演进中保持守护. 2nd ed (2023) 重定向到 automated governance, 加 ArchUnit / Conftest / Open Policy Agent 实例. [T04-S052] [T04-S053]

- **Richards+Ford 2020/2024 — *Fundamentals of Software Architecture: An Engineering Approach* (1st/2nd ed)** (O'Reilly). 软件架构 first principles 教材化首次系统尝试: architecture characteristics / architectural quanta / 组件设计 / pattern 全景 (Layered/Pipeline/Microkernel/Service-Based/Event-Driven/Space-Based/Microservices) + 沟通 / 团队 / 软技能. 2nd ed (2024) 全面修订. ThoughtWorks 提供免费样章 PDF. [T04-S054] [T04-S055] [T04-S056]

- **Ford+Richards+Sadalage+Dehghani 2022 — *Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures*** (O'Reilly). 续接 *Fundamentals*, 专攻 *没有最佳实践* 的难点: service granularity / 分布式事务 (Saga 8 种变体) / contract management / workflow & orchestration / 数据所有权 / reuse vs duplication / build vs buy. 通过虚构 Sysops Squad 故事承载 trade-off 讨论. *注: intake brief 写的作者列表里 "Tune" / "Tucker" 是错的, 实际是 Sadalage 和 Dehghani.* [T04-S057] [T04-S058]

## 4.9 Refactoring / legacy

- **Fowler+Beck+Brant+Opdyke+Roberts 1999 / Fowler 2018 — *Refactoring: Improving the Design of Existing Code* (1st/2nd ed)** (Addison-Wesley Signature). 1st ed (1999) Java 例; 2nd ed (2018) 全部改为 JavaScript + 加 functional 风格. 重构 catalog (Extract Function / Replace Conditional / Move Method / ...) 是改造一切遗留代码的字典. 2nd ed 配套永久访问的 web 版 catalog. [T04-S059] [T04-S060] [T04-S061]

- **Feathers 2004 — *Working Effectively with Legacy Code*** (Prentice Hall, Robert C. Martin Series). 定义: *legacy code = code without tests*. 24 个 dependency-breaking 技巧 (Seam / Subclass and Override Method / Extract Interface / Wrap Method / Sprout Class). 入手 brownfield 项目的必修. [T04-S062] [T04-S063]

- **Beck 2024 — *Tidy First? A Personal Exercise in Empirical Software Design*** (O'Reilly). XP 之父 Kent Beck 系列首本, 把代码整理 (tidying) 从 refactoring 中分离出来作为 *更小颗粒度的恒常实践*, 引入 *coupling / cohesion / discounted cash flow / optionality* 的经济学视角. 2024 后 Beck 的 Substack "Tidy First" 持续更新. [T04-S064] [T04-S065]

## 4.10 Team topology + 组织 + 反面 canon

- **Skelton+Pais 2019/2025 — *Team Topologies: Organizing Business and Technology Teams for Fast Flow* (1st/2nd ed)** (IT Revolution). 4 种基本团队类型 (Stream-aligned / Platform / Enabling / Complicated-Subsystem) + 3 种交互模式 (Collaboration / X-as-a-Service / Facilitating). 关注 *cognitive load* 边界. 与 DDD 的 Bounded Context 互锁. 是 Conway's Law 在 2020s 的具体可执行版. [T04-S066] [T04-S067]

- **Fowler 2004 — "StranglerFigApplication"** (martinfowler.com bliki). 遗留系统替换的核心 pattern (借生物学 strangler fig 命名). 配套 Newman 的 *Monolith to Microservices* 一起读. [T04-S086]

- **Spolsky 2001 — "Don't Let Architecture Astronauts Scare You"** (joelonsoftware.com). 反面 canon: 警惕脱离实际、把一切都抽象到云端的 "架构宇航员". 一句话: *"They invent these new architectures, but nobody wants them."* 与 4.8 evolutionary 的 just-enough architecture 立场互证. [T04-S070]

## 4.11 中文 canon (李运华 / 张开涛 / 张逸 / 李智慧 / 陈皓 / 沈剑)

- **李运华 2018 — 《从零开始学架构》** (电子工业出版社). 极客时间同名专栏 (35,000+ 订阅) 沉淀书. 4 大块: 架构设计基础 + 架构设计流程 (4 步法) + 高性能架构模式 + 高可用架构模式. 风格通俗, 国内 1-3 年程序员转架构师的最佳入门. *注: intake brief 把"亿级流量网站架构核心技术"误归到 李运华, 实查《从零开始学架构》才是李运华的代表作.* [T04-S071] [T04-S072] [T04-S073]

- **张开涛 2017 — 《亿级流量网站架构核心技术: 跟开涛学搭建高可用高并发系统》** (电子工业出版社). 京东资深架构师实战书, 系统讲 负载均衡 / 限流 / 降级 / 隔离 / 超时与重试 / 回滚 / 压测与预案 / 缓存 / 池化 / 异步化 / 扩容 / 队列. 国内电商/秒杀场景的 *事实标准 reference*. [T04-S074] [T04-S075]

- **张逸 2021 — 《解构领域驱动设计》** (人民邮电出版社, 异步图书, 595 页, ISBN 9787115566232). 国内 DDD 最系统化体系: 全局分析 + 架构映射 + 领域建模 三阶段, 提出 "领域驱动设计统一过程 (DDDUP)" + 业务服务 / 菱形对称架构 / 领域驱动架构 / 服务驱动设计. 张逸 (前 ThoughtWorks) 资历真实. Evans/Vernon 的中文土壤化作. [T04-S076]

- **李智慧 2013 — 《大型网站技术架构: 核心原理与案例分析》** (电子工业出版社, 218 页). 阿里前架构师, 系统讲 大型网站演化 5 个阶段 + 高性能 / 高可用 / 可伸缩 / 可扩展 / 安全 5 大架构特性 + 典型案例 (淘宝 / 维基百科 / Google Wave). 国内中文 web 架构入门书 长青销量 #1, 简短 + 概念清晰, 适合 0-1 年新人. [T04-S078]

- **杭建 2018 — 《Java 工程师修炼之道》** (电子工业出版社). 后端技术全景: 工程化 / 常用开发框架 (DI / ORM / 日志) / 数据存储 / 数据传输 / Java 高级编程 / 性能优化 / 安全. 入门指南 + 老手参考手册. *注: intake brief 把此书作者写成 "蔡超", 实查为 杭建 (前网易); 蔡超 本人未发现公开必读 canon, 仅 ArchSummit/QCon 演讲 + 公众号文章, 公众号 blacklisted, 整条不收.* [T04-S077]

- **陈皓 (左耳朵耗子) — CoolShell.cn** (coolshell.cn). 中文技术 blog 黄金时代的 *事实 canon*. 推荐 *《我做系统架构的一些原则》* (架构 11 原则: 收益 / 简单 / 演进 / 多写 vs 多读 / 用成熟方案 / 隔离故障 / 自动化 / 可观测 / 弹性 / 安全 / 一致性). 陈皓 (亚马逊高级研发 → 阿里云资深架构 → 天猫开发总监 → MegaEase 创始人, 2023 病故) 个人质感与西方 SRE/微服务理念在中文土壤的桥. [T04-S079] [T04-S080] [T04-S081]

- **沈剑 — GitChat《58 架构实践点滴》/《架构师之路》系列** (gitbook.cn). 58 到家 / 58 同城 高级总监 + 技术委员会主席的 10+ 年互联网架构实践: IM / 支付 / 跨库分页 / 微服务 / RPC 框架 / 消息系统 / 缓存一致性. *公众号本身 (mp.weixin.qq.com) blacklisted 不收; 但其 GitBook 官方平台 GitChat 课程内容是同一作者一手, 收入 surrogate_primary.* [T04-S082] [T04-S083]

## 4.12 (可选) 补充必读

- **Hunt+Thomas 1999/2019 — *The Pragmatic Programmer: Your Journey to Mastery* (20th anniv. ed.)** (Pragmatic Bookshelf). 工程师品味教材, 不专讲架构但所有架构师都应该已经吸收: DRY / Orthogonality / Tracer Bullets / Broken Windows / Stone Soup. 2019 重写 30% 反映 2010s 技术变化. [T04-S068]

- **Forsgren+Humble+Kim 2018 — *Accelerate: The Science of Lean Software and DevOps*** (IT Revolution). 4 年 State-of-DevOps 数据驱动, 提出 *DORA 4 key metrics* (Deployment Frequency / Lead Time / Change Failure Rate / MTTR). 把 "高效架构" 第一次有数据支撑地与 "高效组织" 绑定. 架构师与 CTO/工程负责人对话必备词汇. [T04-S069]
