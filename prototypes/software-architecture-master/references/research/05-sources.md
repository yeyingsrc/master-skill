# Track 05 — Sources (software architecture)

> Wave 1 Track 05 — newsletter / podcast / conference / community / reference center. Industry: software architecture, locale=global (中外并重 中文:英文 = 1:3-1:4), profile=practitioner.
>
> 结构约束 notes (诚实): (1) 英文一手信源密度远高于中文 (5-10x), 中文优质内容大量集中在 zh-CN 黑名单平台 (公众号 / 知乎 / 极客时间), 必须用 surrogate_primary 兜底; (2) ThoughtWorks Tech Radar 是 consulting firm 出品, 有 ThoughtWorks 偏好 bias, 不是中立行业共识 — 引用时标明; (3) Gartner Magic Quadrant / Forrester Wave 偏大厂 / 偏付费客户, 同样 bias; (4) QCon / GOTO 大会 video 永久免费公开是行业难得资源, KubeCon 同样; (5) 大厂 engineering blog (netflixtechblog.com / shopify.engineering / stripe.com/blog / engineering.linkedin.com / github.blog) 是 surrogate_primary 一手 (公司技术博客 = vendor docs); (6) 中文 podcast 数量极少 (3-5 个), 中文社区 lean podcast (捕蛇者说 / 编程胡说) 偶尔涉及架构.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://martinfowler.com | surrogate_primary | 2026-05-17 | Martin Fowler | vendor docs (作者一手) — bliki + 长文, 软件架构 evergreen #1, 1996+ |
| T05-S002 | https://microservices.io | surrogate_primary | 2026-05-17 | Chris Richardson | vendor docs (作者一手) — 微服务 pattern language 权威 catalog |
| T05-S003 | https://www.enterpriseintegrationpatterns.com | surrogate_primary | 2026-05-17 | Gregor Hohpe + Bobby Woolf | vendor docs — EIP 65 patterns, 2003 书的配套站, async messaging 词汇圣经 |
| T05-S004 | https://www.allthingsdistributed.com | surrogate_primary | 2026-05-17 | Werner Vogels (AWS CTO) | vendor docs (AWS CTO 一手) — 分布式系统 thinking, 年度技术预测 |
| T05-S005 | https://overreacted.io | surrogate_primary | 2026-05-17 | Dan Abramov | vendor docs (作者一手) — React/前端架构哲学, RSC + UI runtime |
| T05-S006 | https://preslav.me | surrogate_primary | 2026-05-17 | Preslav Mihaylov | vendor docs (作者一手) — Go/Java microservices 教学 blog |
| T05-S007 | https://blog.bytebytego.com | surrogate_primary | 2026-05-17 | Alex Xu + Sahn Lam | vendor docs — ByteByteGo Substack, 100 万+ subs, 系统设计 deep dive |
| T05-S008 | https://newsletter.pragmaticengineer.com | surrogate_primary | 2026-05-17 | Gergely Orosz | vendor docs (作者一手) — 107 万 readers (200k+ paid), $15/月 |
| T05-S009 | https://www.infoq.com/software-architects-newsletter/ | secondary | 2026-05-17 | InfoQ editorial | InfoQ 月刊 Architects Newsletter, editorial 整合, 免费 |
| T05-S010 | https://www.thoughtworks.com/radar | surrogate_primary | 2026-05-17 | ThoughtWorks Tech Advisory Board | vendor docs — Tech Radar (双年 4 月 + 10 月), ThoughtWorks bias |
| T05-S011 | https://softwareleadweekly.com | surrogate_primary | 2026-05-17 | Oren Ellenbogen | vendor docs (作者一手) — Software Lead Weekly, 31k subs, 周刊 |
| T05-S012 | https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-in-2025 | surrogate_primary | 2026-05-17 | Gergely Orosz | vendor docs — Pragmatic Engineer 2025 年报, 频率/数据基准 |
| T05-S013 | https://queue.acm.org | surrogate_primary | 2026-05-17 | ACM Queue editorial | 协会 (ACM 一手) — ACM Queue 双月刊, 2026-01-01 起 fully open access|
| T05-S014 | https://www.computer.org/csdl/magazine/so | surrogate_primary | 2026-05-17 | IEEE Computer Society | 协会 (IEEE 一手) — IEEE Software 双月刊, 实战架构 + 经验报告|
| T05-S015 | https://arxiv.org/list/cs.DC/recent | verified_primary | 2026-05-17 | arXiv (Cornell) | preprint 分布式计算 cs.DC, 配 cs.SE + cs.DB |
| T05-S016 | https://www.usenix.org/conference/osdi26 | surrogate_primary | 2026-05-17 | USENIX | 协会 (USENIX 一手) — OSDI '26 2026-07-13~15 Seattle, 开放 proceedings|
| T05-S017 | https://www.usenix.org/conference/nsdi26 | surrogate_primary | 2026-05-17 | USENIX | 协会 (USENIX 一手) — NSDI '26 2026-05-04~06 Renton WA, 开放 proceedings|
| T05-S018 | https://blog.acolyer.org | surrogate_primary | 2026-05-17 | Adrian Colyer | vendor docs (作者 archive) — Morning Paper 2014-2021-02-08, 顶会 paper 解读 |
| T05-S019 | https://softwareengineeringdaily.com | surrogate_primary | 2026-05-17 | Jeff Meyerson (founder, dec'd 2022) | vendor docs (作者一手) — 2015 起, 现 twice-weekly |
| T05-S020 | https://se-radio.net | surrogate_primary | 2026-05-17 | IEEE Computer Society | 协会 (IEEE 一手) — SE Radio, IEEE 旗下, 2006+ 周更|
| T05-S021 | https://www.thoughtworks.com/en-us/insights/podcasts/technology-podcasts | surrogate_primary | 2026-05-17 | ThoughtWorks | vendor docs — Thoughtworks Tech Podcast 双周更 |
| T05-S022 | https://www.software-engineering-unlocked.com | surrogate_primary | 2026-05-17 | Michaela Greiler | vendor docs (作者一手) — SE Unlocked podcast, 双周 |
| T05-S023 | https://maintainable.fm | surrogate_primary | 2026-05-17 | Robby Russell | vendor docs (作者一手) — Maintainable, 遗留代码 / tech debt 周更 |
| T05-S024 | https://www.youtube.com/gotoconferences | surrogate_primary | 2026-05-17 | GOTO Conferences | vendor docs — GOTO 历年大会 talk YouTube 永久免费 |
| T05-S025 | https://qconlondon.com | surrogate_primary | 2026-05-17 | InfoQ | vendor docs (会议官网) — QCon London 2026-03-16 ~ 19 |
| T05-S026 | https://qconsf.com | surrogate_primary | 2026-05-17 | InfoQ | vendor docs (会议官网) — QCon SF 2026-11-16 ~ 20 |
| T05-S027 | https://gotopia.tech | surrogate_primary | 2026-05-17 | Trifork | vendor docs (会议官网) — GOTO Berlin/Aarhus/Amsterdam/CPH/Chicago |
| T05-S028 | https://gotocph.com/2026 | surrogate_primary | 2026-05-17 | Trifork | vendor docs (会议官网) — GOTO Copenhagen 2026-09-28 ~ 10-02 |
| T05-S029 | https://aws.amazon.com/events/reinvent/ | surrogate_primary | 2026-05-17 | AWS | vendor docs — re:Invent 2026-11-30 ~ 12-04 Las Vegas |
| T05-S030 | https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/ | surrogate_primary | 2026-05-17 | CNCF | vendor docs (会议官网) — KubeCon EU 2026-03-23 ~ 26 Amsterdam |
| T05-S031 | https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/ | surrogate_primary | 2026-05-17 | CNCF | vendor docs — KubeCon NA 2026-11-09 ~ 12 Salt Lake City |
| T05-S032 | https://www.cncf.io/announcements/2025/12/10/cncf-unveils-schedule-for-kubecon-cloudnativecon-europe-2026/ | surrogate_primary | 2026-05-17 | CNCF | vendor docs — KubeCon EU 2026 schedule announcement |
| T05-S033 | https://2026.dddeurope.com | surrogate_primary | 2026-05-17 | Aardling / DDD Europe | vendor docs (会议官网) — DDD Europe 2026-06-08 ~ 12 Antwerp |
| T05-S034 | https://aws.amazon.com/architecture/well-architected/ | surrogate_primary | 2026-05-17 | AWS | vendor docs — Well-Architected 6 pillars (含 2021 Sustainability) |
| T05-S035 | https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html | surrogate_primary | 2026-05-17 | AWS | vendor docs — Well-Architected 6 pillars 详细 spec |
| T05-S036 | https://cloud.google.com/architecture/framework | surrogate_primary | 2026-05-17 | Google Cloud | vendor docs — Google Cloud Well-Architected 5 pillars |
| T05-S037 | https://learn.microsoft.com/en-us/azure/well-architected/pillars | surrogate_primary | 2026-05-17 | Microsoft | vendor docs — Azure Well-Architected 5 pillars |
| T05-S038 | https://learn.microsoft.com/en-us/azure/architecture/ | surrogate_primary | 2026-05-17 | Microsoft | vendor docs — Azure Architecture Center, reference 架构目录 |
| T05-S039 | https://www.reactivemanifesto.org | surrogate_primary | 2026-05-17 | Jonas Bonér / Dave Farley / Roland Kuhn / Martin Thompson | vendor docs — Reactive Manifesto 2014-09-16, 22k+ signatories |
| T05-S040 | https://12factor.net | surrogate_primary | 2026-05-17 | Adam Wiggins (Heroku) | vendor docs (Heroku 创始人一手) — 12-Factor App 2011-11 |
| T05-S041 | https://backstage.io/docs/features/techdocs/ | surrogate_primary | 2026-05-17 | Spotify / CNCF | vendor docs — Backstage TechDocs, docs-as-code |
| T05-S042 | https://netflixtechblog.com | surrogate_primary | 2026-05-17 | Netflix | vendor docs (engineering blog) — 微服务/混沌工程一手 |
| T05-S043 | https://shopify.engineering | surrogate_primary | 2026-05-17 | Shopify | vendor docs (engineering blog) — modular monolith 经典 case |
| T05-S044 | https://stripe.com/blog/engineering | surrogate_primary | 2026-05-17 | Stripe | vendor docs (engineering blog) — API 设计 / 支付架构 |
| T05-S045 | https://engineering.atspotify.com | surrogate_primary | 2026-05-17 | Spotify | vendor docs (engineering blog) — Backstage / squad model 源头 |
| T05-S046 | https://github.blog/engineering/ | surrogate_primary | 2026-05-17 | GitHub | vendor docs (engineering blog) — monorepo / scale 经验 |
| T05-S047 | https://www.infoq.cn/topic/architecture | secondary | 2026-05-17 | InfoQ 中文 editorial | editorial 平台 — 软件架构 频道, 译文 + 国内一手, 极客邦运营 |
| T05-S048 | https://time.geekbang.org | surrogate_primary | 2026-05-17 | 极客时间 (极客邦) | syllabus — 付费专栏目录, 含李运华/王宝令等 |
| T05-S049 | https://time.geekbang.org/column/intro/81 | surrogate_primary | 2026-05-17 | 李运华 (极客时间) | syllabus — 《从 0 开始学架构》课程, 30k+ 学员 |
| T05-S050 | https://archsummit.infoq.cn | surrogate_primary | 2026-05-17 | InfoQ 中文 / 极客邦 | vendor docs (会议官网) — ArchSummit 北京 / 上海 / 深圳 |
| T05-S051 | https://giac.msup.com.cn | surrogate_primary | 2026-05-17 | msup / 高可用架构 | vendor docs (会议官网) — GIAC 全球互联网架构大会 |
| T05-S052 | https://gmtc.infoq.cn | surrogate_primary | 2026-05-17 | InfoQ 中文 / 极客邦 | vendor docs (会议官网) — GMTC 全球大前端技术大会 |
| T05-S053 | https://qcon.infoq.cn | surrogate_primary | 2026-05-17 | InfoQ 中文 / 极客邦 | vendor docs (会议官网) — QCon 北京 / 上海 中文站 |
| T05-S054 | https://coolshell.cn | surrogate_primary | 2026-05-17 | 陈皓 (左耳朵耗子, 1976-2023) | vendor docs (作者一手) — CoolShell archive, 2002+ 文章长效 |
| T05-S055 | https://memorial.megaease.cn | surrogate_primary | 2026-05-17 | MegaEase | vendor docs — 陈皓 memorial, CoolShell mirror 跳板 |
| T05-S056 | https://www.megaease.com/blog/ | surrogate_primary | 2026-05-17 | MegaEase | vendor docs — MegaEase 公司技术 blog, 微服务 mesh / 网关 |
| T05-S057 | http://www.caict.ac.cn | reference | 2026-05-17 | 中国信通院 (CAICT) | 官方 — 信通院, 云原生 / 分布式架构 行业白皮书 |
| T05-S058 | https://www.ccf.org.cn | reference | 2026-05-17 | 中国计算机学会 CCF | 协会 — CCF, 软件工程 / 系统软件 专委会 + TF 系列大会 |

---

## 5.1 Evergreen blog (英文)

- **martinfowler.com** [T05-S001] / Martin Fowler / 1996+ / 不定期 (高峰每月数篇) / ThoughtWorks Chief Scientist (现 emeritus) / Why: refactoring + microservices + bliki, 几乎每个架构 term 的权威定义出处 (Strangler Fig / Two-Pizza Team / Continuous Delivery 都从这里普及).
- **microservices.io** [T05-S002] / Chris Richardson / ~2014+ / 跟随新 pattern 更新 / 《Microservices Patterns》作者 / Why: 微服务 pattern language 权威 catalog, Saga / API Composition / CQRS 等的 canonical 定义.
- **enterpriseintegrationpatterns.com** [T05-S003] / Gregor Hohpe + Bobby Woolf / 2003+ (书 2003-10 出版) / 低频 (Hohpe 现仍偶尔更) / Why: EIP 65 patterns, 异步消息 + ESB + 现在的 event-driven 体系仍在引用.
- **allthingsdistributed.com** [T05-S004] / Werner Vogels (Amazon CTO 2005-至今 → 2024-12 退休但仍发) / 月级 / Why: AWS 内部决策 + 年度技术预测 (2026 年预测被广引), Dynamo paper 推荐人.
- **overreacted.io** [T05-S005] / Dan Abramov (ex-Meta React core) / 不定期 / Why: 前端架构哲学一手, RSC / "JSX over the wire" / "React as a UI Runtime" 经典文.
- **preslav.me** [T05-S006] / Preslav Mihaylov (ex-Uber, now Plain) / 周/双周 / Why: Go + Java microservices / 分布式 算法的 hands-on 教学.
- **blog.bytebytego.com** [T05-S007] / Alex Xu + Sahn Lam / 每周 2 期 (周四 deep dive + 周六 fundamentals) / Why: 系统设计 visual deep dive, 100 万+ subs, 国际中文社区均强引用.

## 5.2 Newsletter (paid + free, 英文)

- **ByteByteGo** [T05-S007] / Alex Xu / 周 2 期 / 2022-04 起 / 100 万+ subs / 付费 $15/月 / Why: 视觉化系统设计标杆.
- **The Pragmatic Engineer** [T05-S008][T05-S012] / Gergely Orosz / 周 3 期 (周二长文 / 周三 podcast / 周四 big tech news) / 2021 起 / 107 万 readers, 200k+ 付费 / 付费 $15/月 / Why: Big Tech 内部一手访谈密度最高.
- **InfoQ Architects Newsletter** [T05-S009] / InfoQ editorial / 月刊 / 免费 / Why: editorial 整合, low-noise 月度入口.
- **ThoughtWorks Technology Radar** [T05-S010] / ThoughtWorks Tech Advisory Board / 双年 (4 月 + 10 月) / 免费 PDF + web / **bias**: ThoughtWorks consulting practice 偏好 (e.g. 长期 boost Clojure / Haskell / event sourcing). 最新 Vol 34 2026-04-15 发布, 主题 AI cognitive debt.
- **Software Lead Weekly** [T05-S011] / Oren Ellenbogen / 周刊 / 2013 起 / 31k subs / 免费 / Why: 偏 engineering management, 但架构师晋升必读.
- **ITNEXT The Newsletter of Things** / ITNEXT Medium publication / 月刊 / 免费 / Why: 平台聚合 (无单独 source manifest 条目, 通过 ITNEXT.io 入口).

## 5.3 学术 / industry journal + paper venue

- **ACM Queue** [T05-S013] / queue.acm.org / 双月刊 / 2003 起 / **2026-01-01 起 fully open access** / Why: ACM 学会 practitioner-facing 期刊, "by engineers for engineers".
- **IEEE Software** [T05-S014] / computer.org/csdl/magazine/so / 双月刊 / IEEE Computer Society / Why: 经验报告 + 案例研究密度高, software architecture 专题常见.
- **arXiv cs.DC / cs.SE / cs.DB** [T05-S015] / 滚动 preprint / 免费 / Why: 顶会 paper 提前 6-12 月可见, 大厂内部 paper 往往在此首发.
- **USENIX OSDI '26** [T05-S016] / 2026-07-13 ~ 15 Seattle / 开放 proceedings / Why: 系统设计顶会, 大厂 paper (Google / Meta / Microsoft) 集中地.
- **USENIX NSDI '26** [T05-S017] / 2026-05-04 ~ 06 Renton WA / 开放 proceedings / Why: 网络系统顶会, CDN / 分布式存储 / 网络架构 一手.
- **SIGMOD / VLDB / ICDE** / 数据管理三大顶会 / Why: 分布式数据库 / 一致性 / 存储引擎一手 (architecture decision 重大依据).
- **The Morning Paper archive** [T05-S018] / blog.acolyer.org / 2014-2021-02-08 / Why: Adrian Colyer 5 年顶会 paper 解读 archive, 入门顶会 paper 最佳缓冲层.

## 5.4 Podcast (英文 + 中文)

- **Software Engineering Daily** [T05-S019] / softwareengineeringdaily.com / Jeff Meyerson (创始人 2015, 2022-07 离世) / 现 twice-weekly / Why: 海量访谈库, 架构师 + 创业者交叉视角.
- **Software Engineering Radio** [T05-S020] / se-radio.net / IEEE Computer Society + IEEE Software 联合 / 2006+ 周更 / Why: IEEE 旗下教育型 podcast, 单话题 deep dive (1-2 小时), 不带广告.
- **Thoughtworks Technology Podcast** [T05-S021] / 双周 / Why: ThoughtWorks 视角的当前热议技术 + Tech Radar 配套延伸.
- **Software Engineering Unlocked** [T05-S022] / Michaela Greiler / 双周 / Why: code review / 团队效能 / 架构演化 实战.
- **Maintainable** [T05-S023] / Robby Russell (创办 oh-my-zsh) / 周更 / Why: 遗留系统 / tech debt / refactoring 的实战 podcast — 架构师"老房子改造"必听.
- **GOTO Conferences YouTube** [T05-S024] / 历年 talk 永久免费, 频率: 每月 5-10 个上传 / Why: 不是 podcast 但是音视频 reference center 级 archive.
- **中文 podcast**: 中文架构向 podcast 极少, 通用编程类 "捕蛇者说" / "津津乐道" 偶尔涉及 — 单独条目不进 manifest, 中文一手主入口仍是 ArchSummit/InfoQ 视频.

## 5.5 会议 (英文 + 中文)

英文:
- **QCon London 2026** [T05-S025] / 2026-03-16 ~ 19 (16-18 主会 + 19 InfoQ Certified Software Architect 半日 workshop) / Queen Elizabeth II Centre / 15 tracks 75+ speakers.
- **QCon San Francisco 2026** [T05-S026] / 2026-11-16 ~ 20 (16-18 主会 + 19-20 training) / Hyatt Regency / 60+ practitioners / 20 周年.
- **GOTO 大会全年** [T05-S027] / gotopia.tech (Trifork 主办) / 主要场次: Berlin / Aarhus / Amsterdam / Copenhagen / Chicago.
- **GOTO Copenhagen 2026** [T05-S028] / 2026-09-28 ~ 10-02 / TAP1, Copenhagen.
- **AWS re:Invent 2026** [T05-S029] / 2026-11-30 ~ 12-04 / Las Vegas (Caesars Forum 主会场 + 5 个 strip 会场).
- **Google Cloud Next** / 每年 4 月 / Las Vegas / vendor 大会 但 architecture-track 含金量高.
- **Microsoft Build (5 月) / Ignite (11 月)** / vendor 大会, Azure 架构师必跟.
- **KubeCon + CloudNativeCon Europe 2026** [T05-S030][T05-S032] / 2026-03-23 ~ 26 Amsterdam.
- **KubeCon + CloudNativeCon North America 2026** [T05-S031] / 2026-11-09 ~ 12 Salt Lake City.
- **KubeCon + CloudNativeCon China 2026** / 2026-09-08 ~ 09 Shanghai (与 OpenInfra Summit + PyTorch Conf 联办).
- **DDD Europe 2026** [T05-S033] / 2026-06-08 ~ 12 (workshops 8-10, conference 10-12) / Antwerp (Belgium, 不是 Amsterdam — 历史误传) / DDD 流派核心年会.

中文 (详 5.7).

## 5.6 Reference center (vendor architecture framework + manifesto)

- **AWS Well-Architected Framework** [T05-S034][T05-S035] / aws.amazon.com/architecture/well-architected / 6 pillars: Operational Excellence / Security / Reliability / Performance Efficiency / Cost Optimization / **Sustainability** (2021-12 加入) / 6 pillar 是当下 cloud arch review 行业事实标准.
- **Google Cloud Architecture Framework** [T05-S036] / cloud.google.com/architecture/framework / 5 pillars: Operational Excellence / Security Privacy & Compliance / Reliability / Cost Optimization / Performance Optimization.
- **Microsoft Azure Architecture Center** [T05-S037][T05-S038] / learn.microsoft.com/azure/architecture + .../well-architected/pillars / 5 pillars: Reliability / Security / Cost Optimization / Operational Excellence / Performance Efficiency. Architecture Center 含 reference architecture 目录.
- **Reactive Manifesto** [T05-S039] / reactivemanifesto.org / Jonas Bonér / Dave Farley / Roland Kuhn / Martin Thompson / 2014-09-16 / 4 properties: Responsive + Resilient + Elastic + Message-Driven / 22k+ signatories.
- **The Twelve-Factor App** [T05-S040] / 12factor.net / Adam Wiggins (Heroku 联创) / 2011-11 / 12 factors: codebase / dependencies / config / backing services / build-release-run / processes / port binding / concurrency / disposability / dev-prod parity / logs / admin processes. **注**: 现在被批评偏 Heroku-era 假设, 已有 "Beyond 12-Factor" (Kevin Hoffman) 扩展但 12-Factor 仍是基线词汇.
- **Backstage TechDocs** [T05-S041] / backstage.io/docs/features/techdocs / Spotify 内 5000+ docs site / docs-as-code 实践模板 / Backstage 现为 CNCF Incubating (2022-03 升级).

## 5.7 中文一手 (InfoQ 中文 / 极客时间 / ArchSummit / GIAC / 信通院 / CoolShell / MegaEase)

- **InfoQ 中文** [T05-S047] / infoq.cn/topic/architecture / editorial / 软件架构 频道含国内一手 (字节 / 阿里 / 腾讯 / 美团 架构师投稿 + 国际译文) + 季刊 PDF《架构师》(2025 Q1 / Q2 等) / Why: 中文 architecture 唯一 editorial 平台.
- **极客时间** [T05-S048] / time.geekbang.org / 付费专栏 (极客邦) / 旗下与架构相关重点专栏:
  - 李运华《从 0 开始学架构》[T05-S049] / 30k+ 学员 / 架构入门 + 决策模型.
  - 王宝令《Java 并发编程实战》 / 并发架构基础.
  - 蔡超《架构师的成长之路》 / 架构师能力模型.
  - ThoughtWorks 多门 / DDD + 微服务实战.
- **ArchSummit** [T05-S050] / archsummit.infoq.cn / InfoQ 中文 / 极客邦主办 / 北京 (春) / 上海 + 深圳 (秋) / Why: 中文架构师 #1 大会, 阿里/腾讯/字节 一线 case 集中地.
- **GIAC 全球互联网架构大会** [T05-S051] / giac.msup.com.cn / msup + 高可用架构社区主办 / 深圳常规站 / Why: 高并发 / 大流量 实战 case.
- **GMTC 全球大前端技术大会** [T05-S052] / gmtc.infoq.cn / InfoQ 中文 / 极客邦 / 北京 + 深圳 / Why: 中文前端架构 (微前端 / SSR / 跨端) 唯一年会.
- **QCon 北京 / 上海** [T05-S053] / qcon.infoq.cn / InfoQ 中文站 / Why: QCon 国际品牌中文版.
- **中国信通院 CAICT** [T05-S057] / caict.ac.cn / 官方智库 / Why: 云原生 / 分布式 / 信创架构白皮书行业标尺, 国企 / 监管 视角必看.
- **CCF 中国计算机学会** [T05-S058] / ccf.org.cn / 协会 / Why: 软件工程专委会 + TF 系列 (CCF TF14 软件工程) 讨论组.
- **CoolShell** [T05-S054] / coolshell.cn / 陈皓 (1976-2023-05-13) / archive / Why: 2002+ 长效文章, "左耳听风" 系列影响一代中文架构师 — 站长虽已故, MegaEase 团队维护 mirror.
- **MegaEase Memorial** [T05-S055] / memorial.megaease.cn / 陈皓 纪念站 + CoolShell mirror 跳板.
- **MegaEase blog** [T05-S056] / megaease.com/blog/ / MegaEase 公司技术 blog / Why: 服务网格 / API 网关 / 云原生 国产实践.

---

> 黑名单提醒 (踩坑预防): 不论作者多有名, 以下中文平台一律 blacklisted, 必须改引底层一手:
> - mp.weixin.qq.com (微信公众号) — 即使阿里中间件 / 美团技术团队 / 字节跳动技术团队 / 腾讯云原生, 改引 engineering blog 真域名 (阿里 → cn.aliyun.com/developer, 美团 → tech.meituan.com, 字节 → developer.volcengine.com).
> - zhihu.com / juejin.cn / csdn.net / cnblogs.com / jianshu.com / baike.baidu.com — 全部 secondary 转载, 找原始作者一手.
