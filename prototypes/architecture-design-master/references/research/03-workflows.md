# Track 03 — Workflows (现代建筑设计)

> Wave 2 Track 03 — single-project lifecycle SOP + 事务所类型 SOP + 横向能力 (BIM 协作 / 可持续 / 投标 / 业主管理 / AI / 中国转型). Industry: 现代建筑设计, locale=global (AIA 5-phase + 中国 方案 / 初设 / 施工图 / 现场 dual mode + RIBA 8-stage 参考), profile=practitioner.
>
> 诚实说明: (1) AIA 5 phase 与中国三阶段不是 1:1 映射 — SD ≈ 方案, DD ≈ 扩初, CD ≈ 施工图, 但中国施工图深度远高于 US CD (须含国标节点), 而 US DD 更早把 MEP 全部锁死; (2) RIBA 8-stage 0-7 是另一套独立 framework, 与 AIA/中国 平行使用; (3) 中国设计费数据多基于 2002 年版《工程勘察设计收费标准》, 2024-2026 实际行情普遍跌至 60-80% 标准价 (房地产寒冬), 数据保 caveat; (4) starchitect / 大设计院 真实工作流多为 NDA, 只能从合伙人公开访谈 + AIA / 协会 文档反推; (5) AI generative workflow (Midjourney→Forma) 是 2023-2026 才主流化, SOP 仍在演化中.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.aia.org/resource-center/defining-the-architects-basic-services | surrogate_primary | 2026-05-16 | AIA | 协会 — AIA Defining the Architect's Basic Services 官方资源 |
| T03-S002 | https://www.aia.org/resource-center/schematic-design-phase-quality-management | surrogate_primary | 2026-05-16 | AIA | 协会 — AIA Schematic Design Phase Quality Management |
| T03-S003 | https://help.aiacontracts.com/hc/en-us/articles/1500010280541-Summary-B101-2017-Standard-Form-of-Agreement-Between-Owner-and-Architect | surrogate_primary | 2026-05-16 | AIA Contract Documents | 协会 — AIA contract B101-2017 Owner-Architect Standard Form 摘要 |
| T03-S004 | https://help.aiacontracts.com/hc/en-us/articles/1500009804902-Instructions-B101-2017-Standard-Form-of-Agreement-Between-Owner-and-Architect | surrogate_primary | 2026-05-16 | AIA Contract Documents | 协会 — AIA contract B101 instructions (basic / supplemental / additional services) |
| T03-S005 | https://designshop.aia.org/products/b101-2017-owner-architect-standard-form-agreement-revised | verified_primary | 2026-05-16 | AIA Design Shop | AIA Design Shop B101-2017 product page (vendor-owned) |
| T03-S006 | https://content.aia.org/sites/default/files/2017-03/EPC_Construction_Admin_3B.pdf | surrogate_primary | 2026-05-16 | AIA Emerging Professional's Companion | 协会 — AIA EPC Module 3B Construction Administration PDF |
| T03-S007 | https://www.aia.org/resource-center/problem-well-stated-owner-project-requirements | surrogate_primary | 2026-05-16 | AIA | 协会 — AIA "A problem well stated: Owner project requirements" |
| T03-S008 | https://www.aia.org/sites/default/files/2023-11/ipd_guide.pdf | surrogate_primary | 2026-05-16 | AIA | 协会 — AIA Integrated Project Delivery: A Guide PDF |
| T03-S009 | https://www.wiley.com/en-us/The+Architect's+Handbook+of+Professional+Practice,+15th+Edition-p-9781118308820 | surrogate_primary | 2026-05-16 | Wiley + AIA | 协会 — AIA Architect's Handbook of Professional Practice 15th ed (publisher) |
| T03-S010 | https://www.riba.org/work/insights-and-resources/riba-plan-of-work/ | surrogate_primary | 2026-05-16 | RIBA | RIBA Plan of Work 2020 hub (协会 但出版方一手) |
| T03-S011 | https://www.riba.org/media/sszn5kkt/2020ribaplanofworktemplatepdf.pdf | surrogate_primary | 2026-05-16 | RIBA | RIBA Plan of Work 2020 template PDF (协会 一手出版) |
| T03-S012 | https://www.riba.org/media/syneeeto/2020ribaplanofworkoverviewpdf.pdf | surrogate_primary | 2026-05-16 | RIBA | RIBA Plan of Work 2020 Overview PDF (协会 一手出版) |
| T03-S013 | https://www.architecture.com/knowledge-and-resources/resources-landing-page/riba-plan-of-work | surrogate_primary | 2026-05-16 | RIBA | RIBA Plan of Work landing page on architecture.com (RIBA-owned domain) — vendor docs |
| T03-S014 | http://www.jianbiaoku.com/webarbs/book/89.shtml | surrogate_primary | 2026-05-16 | 建标库 + 住建部 | 监管 — 住建部《建筑工程设计文件编制深度规定（2016版）》全文 (建标库 host) |
| T03-S015 | http://www.sjzcsgx.cn/attachments/1/202407/22/.pdf | surrogate_primary | 2026-05-16 | 住建部 (石家庄住建上传) | 监管 — 《建筑工程设计文件编制深度规定（2016版）》PDF |
| T03-S016 | https://zjt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202011/t20201103_2996965.shtml | surrogate_primary | 2026-05-16 | 湖北省住建厅 | 监管 — 住建部三套文件 (深度规定 + 装配式审查 + 周期定额) 印发通知 |
| T03-S017 | https://www.gov.cn/xinwen/2017-01/03/5156079/files/6e368ba552a04981a63e756148282689.doc | verified_primary | 2026-05-16 | 中国政府网 gov.cn | 监管 — 《全国建筑设计周期定额（2016版）》官方 doc (gov.cn 一手) |
| T03-S018 | https://cncssd.org/index.php?a=show&c=index&catid=16&id=87&m=content | surrogate_primary | 2026-05-16 | 中国钢结构协会 + 住建部 | 协会 — 全国建筑设计周期定额 2016 印发通知转载 |
| T03-S019 | https://ghzrzyw.beijing.gov.cn/kanchasheji/zzzgzrxgbz/201912/t20191213_1158427.html | surrogate_primary | 2026-05-16 | 北京市规自委 | 监管 — 《工程设计资质标准》(甲乙丙级) 官方页面 |
| T03-S020 | https://www.hengyang.gov.cn/zjw/yhyshjzl/xzsp/cb/20210917/i2485965.html | surrogate_primary | 2026-05-16 | 衡阳市住建局 + 国家计委 | 监管 — 《工程勘察设计收费标准》2002 修订本 (设计费率法定基础) |
| T03-S021 | http://www.caec-china.org.cn/ | surrogate_primary | 2026-05-16 | 中国建设监理协会 | 协会 — 中国建设监理协会 (CAEC) 官方主入口 |
| T03-S022 | https://www.chinaasc.org.cn/ | surrogate_primary | 2026-05-16 | 中国建筑学会 | 协会 — 中国建筑学会 (ASC) 官方主入口 |
| T03-S023 | https://www.ndrc.gov.cn/yjzxDownload/fwjzhszjcssjs.pdf | verified_primary | 2026-05-16 | 国家发改委 + 住建部 | 监管 — 《房屋建筑和市政基础设施建设项目全过程工程咨询服务技术标准》(征求意见稿) |
| T03-S024 | https://zjw.sh.gov.cn/cmsres/80/804a1e17e07f4e9b914adc9e7167f510/628dfcc6c2fbdb58daf2924ab2079816.pdf | verified_primary | 2026-05-16 | 上海市住建委 | 监管 — 《上海市建筑信息模型技术应用指南 (2025)》 |
| T03-S025 | https://www.cadg.com.cn/ | surrogate_primary | 2026-05-16 | 中国建筑设计研究院 (CADG) | 中国设计院一手官网 — 大型综合甲级设计院范例; vendor docs |
| T03-S026 | https://www.yidaiyilu.gov.cn/p/2097.html | surrogate_primary | 2026-05-16 | 一带一路网 | 监管 — 中国建筑设计研究院介绍 (官方 gov.cn 域) |
| T03-S027 | https://gzdi.com/ | surrogate_primary | 2026-05-16 | 广州市设计院集团 | 广州市设计院 (GZDI) 一手官网 — 大型地方甲级院; vendor docs |
| T03-S028 | https://www.chinaurbandevelopment.com/an-architects-guide-to-working-in-china/ | secondary | 2026-05-16 | China Urban Development | 海外建筑师对接 LDI 实务指南 — editorial |
| T03-S029 | http://sepmchina.com/services/ | secondary | 2026-05-16 | SEPM China | 中国 EPC/EPCM/LDI/监理 解读 — 行业咨询 editorial |
| T03-S030 | https://www.architectsjournal.co.uk/archive/shanghai-calling-a-question-of-specialisms | secondary | 2026-05-16 | Architects' Journal (AJ) | "Shanghai calling" 海外事务所进中国 archive — UK trade |
| T03-S031 | https://carusostjohn.com/ | surrogate_primary | 2026-05-16 | Caruso St John Architects | 一手官网 — 欧洲 boutique atelier 范例 (RIBA Stirling 2016); vendor docs |
| T03-S032 | https://www.archdaily.com/office/atelier-deshaus | secondary | 2026-05-16 | ArchDaily | 大舍 (Atelier Deshaus) 事务所页 — 中国 boutique 范例 |
| T03-S033 | https://www.indesignlive.com/hongkong/in-profile/up-close-with-atelier-deshaus | secondary | 2026-05-16 | Indesign Live | 大舍 in-profile 访谈 — 工作流 + studio 文化 editorial |
| T03-S034 | https://www.gensler.com/about/global-presence | verified_primary | 2026-05-16 | Gensler | Gensler 全球办公地图 — 国际中型/大型 firm 一手 (>50 office) |
| T03-S035 | https://www.fosterandpartners.com/insights/plus-journal/design-technology-and-the-team-between | surrogate_primary | 2026-05-16 | Foster + Partners | Foster Applied R+D team 工作流 — starchitect 一手 plus journal; vendor docs |
| T03-S036 | https://www.oma.com/ | surrogate_primary | 2026-05-16 | OMA | OMA 一手官网 — Koolhaas 创办 starchitect (Rotterdam/NY/HK/Doha/...); vendor docs |
| T03-S037 | https://big.dk/ | surrogate_primary | 2026-05-16 | BIG (Bjarke Ingels Group) | BIG 一手官网 — Copenhagen/NY/London/Barcelona starchitect; vendor docs |
| T03-S038 | https://architizer.com/blog/inspiration/collections/oma-architecture-model-making/ | secondary | 2026-05-16 | Architizer Journal | OMA model-making workflow 解读 — editorial |
| T03-S039 | https://entrearchitect.com/2020/10/26/sole-practitioner-architect-business-model/ | secondary | 2026-05-16 | EntreArchitect (Mark R. LePage) | Sole Practitioner Architect business model — 实务社区 editorial |
| T03-S040 | https://architizer.com/blog/inspiration/industry/are-sole-practitioners-the-creative-engine-of-the-architectural-profession/ | secondary | 2026-05-16 | Architizer Journal | Micro-firm / sole-prac 占 AIA 30% 分析 — editorial |
| T03-S041 | https://www.architects.org/events/538780/2022/12/08/residential-design-going-solo-the-sole-practitioner-business-model | surrogate_primary | 2026-05-16 | Boston Society for Architecture (BSA) | 协会 — BSA "Residential Design: Going Solo" event 资源 |
| T03-S042 | https://learn.aiacontracts.com/articles/the-architects-guide-to-contracting/ | surrogate_primary | 2026-05-16 | AIA Contract Documents | 协会 — AIA contract Architect's Guide to Contracting (risk + scope) |
| T03-S043 | https://www.deltek.com/en/architecture-and-engineering/architecture-project-management/scope-creep | secondary | 2026-05-16 | Deltek (Ajera/Vantagepoint vendor) | Scope Creep Survival Guide for Architects — vendor editorial |
| T03-S044 | https://monograph.com/blog/proven-strategies-manage-project-scope-creep | secondary | 2026-05-16 | Monograph (PM software) | Scope creep 管理策略 — vendor blog (architect-built tool) |
| T03-S045 | https://www.design-operations.com/journal/how-to-handle-change-orders-and-scope-creep-in-architecture-projects | secondary | 2026-05-16 | Operations by Design | Change order + scope creep 处理 — practice ops editorial |
| T03-S046 | https://aldrichadvisors.com/architects-engineers/ae-scope-creep/ | secondary | 2026-05-16 | Aldrich CPAs + Advisors | A/E scope creep 处理 — 财务顾问 editorial |
| T03-S047 | https://www.usgbc.org/credits/integrative-process | surrogate_primary | 2026-05-16 | USGBC | LEED v4 Integrative Process credit (设计早期 charrette) 一手 — 协会 |
| T03-S048 | https://oneclicklca.com/en-us/software/design-construction | surrogate_primary | 2026-05-16 | One Click LCA | One Click LCA vendor docs — LCA 计算工具 (140+ standards) |
| T03-S049 | https://carbonleadershipforum.org/tools-for-measuring-embodied-carbon/ | surrogate_primary | 2026-05-16 | Carbon Leadership Forum (UW) | CLF tool comparison: Tally / Athena / One Click LCA — academic primary; vendor docs |
| T03-S050 | https://www.gsa.gov/governmentwide-initiatives/federal-highperformance-buildings/highperformance-building-clearinghouse/integrative-design-strategies/life-cycle-perspective/life-cycle-assessment-and-buildings | verified_primary | 2026-05-16 | US GSA | 监管 — US GSA LCA for buildings guidance (vendor 政府一手) |
| T03-S051 | https://buildinginnovationhub.org/wp-content/uploads/2021/11/BEPS_Risk_Reward_Module2_EnergyModeling.pdf | surrogate_primary | 2026-05-16 | DC Building Innovation Hub | 监管 — DC BEPS energy modeling + charrette module PDF; vendor docs |
| T03-S052 | https://www.autodesk.com/products/forma/overview | verified_primary | 2026-05-16 | Autodesk | Autodesk Forma overview — vendor 一手 (early-stage AI massing) |
| T03-S053 | https://www.autodesk.com/design-make/articles/generative-ai-for-architecture | surrogate_primary | 2026-05-16 | Autodesk Design Make | vendor docs — Generative AI for architecture overview |
| T03-S054 | https://adsknews.autodesk.com/en/news/upcoming-3d-generative-ai-foundation-models/ | surrogate_primary | 2026-05-16 | Autodesk News | vendor 一手 — 3D generative AI foundation models for Fusion/Forma; vendor docs |
| T03-S055 | https://aecmag.com/features/autodesk-shows-its-ai-hand/ | secondary | 2026-05-16 | AEC Magazine | Autodesk AI hand 行业分析 — UK trade editorial |
| T03-S056 | https://www.uia-architectes.org/wp-content/uploads/2022/02/2_UIA_competition_guide_2020.pdf | surrogate_primary | 2026-05-16 | UIA (International Union of Architects) | 协会 — UIA Competition Guide 2020 PDF |
| T03-S057 | https://www.wbdg.org/resources/running-design-competition | surrogate_primary | 2026-05-16 | WBDG (NIBS) | WBDG Running a Design Competition — 监管 (NIBS gov-backed); vendor docs |
| T03-S058 | https://whattherfi.com/blog/what-is-construction-administration-a-complete-guide-for-architects-and-clients | secondary | 2026-05-16 | What the RFI? | CA guide for architects — practitioner editorial |
| T03-S059 | https://layer.team/blog/architects-construction-administration | secondary | 2026-05-16 | Layer (AEC PM software) | Architect's Guide to CA — vendor editorial |
| T03-S060 | http://www.dz-gczx.com/wap/articleDetails_id_1108.html | secondary | 2026-05-16 | 大正工程咨询 | 中国方案/初设/施工图深度差异 — 行业 editorial (engineering consultancy) |
| T03-S061 | http://jjc.haue.edu.cn/info/1016/1283.htm | surrogate_primary | 2026-05-16 | 河南工程学院基建处 | 课程 — 工程设计三阶段释明 .edu (河南工程学院) |
| T03-S062 | https://www.szdesigncenter.com/media/1/20221021145812.458999145-8-%E9%99%84%E4%BB%B6%E5%9B%9B_%E4%B8%BB%E8%A6%81%E5%B7%A5%E4%BD%9C%E5%86%85%E5%AE%B9.pdf | surrogate_primary | 2026-05-16 | 深圳设计中心 (政府背景) | 监管 — 深圳设计任务书 "主要工作内容" 附件 (P/S 责任划分) |
| T03-S063 | https://m.thepaper.cn/newsDetail_forward_32128117 | secondary | 2026-05-16 | 澎湃新闻 + 行业研究 | "建筑设计企业'十五五'战略新思考" — 寒冬转型分析 |
| T03-S064 | https://m.thepaper.cn/newsDetail_forward_32582497 | secondary | 2026-05-16 | 澎湃新闻 + 上海城市更新 | "城市年鉴 2025: 城市更新单体改造到系统焕新" — 城市更新转型 |
| T03-S065 | https://www.stcn.com/article/detail/1574324.html | secondary | 2026-05-16 | 证券时报网 | 房地产行业转型升级路径 — 财经 editorial |
| T03-S066 | http://huayujianye.com/index/shows?catid=43&id=139 | secondary | 2026-05-16 | 华誉建业 | 住建局更名 + 城市更新转型分析 — 行业 editorial |
| T03-S067 | http://www.npc.gov.cn/c2/c30834/202510/t20251026_448777.html | verified_primary | 2026-05-16 | 全国人大 | 监管 — 全国人大 文化和旅游深度融合 报告 (官方一手) |
| T03-S068 | https://ds-a.co.uk/the-8-riba-stages-of-work/ | secondary | 2026-05-16 | DSA Architects | RIBA 8 stages of work 解读 — UK practice editorial |
| T03-S069 | https://urbanistarchitecture.co.uk/riba-plan-of-work-stages/ | secondary | 2026-05-16 | Urbanist Architecture | RIBA 2020 Plan of Work stages guide — UK practice editorial |
| T03-S070 | https://oneclicklca.com/en-gb/resources/articles/whole-life-carbon-assessment-wlca-guide-lca-epds-regulations | surrogate_primary | 2026-05-16 | One Click LCA | vendor 一手 — WLCA guide + EPD + regulations; vendor docs |
| T03-S071 | https://www.businessofarchitecture.com/bim-for-small-projects/ | secondary | 2026-05-16 | Business of Architecture (Enoch Sears) | BIM for small projects — sole-prac editorial |
| T03-S072 | https://www.crbgroup.com/insights/how-to-sustainable-building-design | secondary | 2026-05-16 | CRB Group | Sustainability charrette workflow — A/E consultancy editorial |
| T03-S073 | https://greenhomeinstitute.org/design-charrette-grants-for-leed-for-homes/ | surrogate_primary | 2026-05-16 | GreenHome Institute | 协会 — LEED for Homes design charrette grants |
| T03-S074 | https://designbuildlaw.com/aia-contracts/b101-2017/ | secondary | 2026-05-16 | DesignBuildLaw | B101-2017 详细法务解读 — legal editorial |
| T03-S075 | https://www.archisoup.com/riba-work-stages-explained | secondary | 2026-05-16 | archisoup | RIBA work stages 详解 — architect 教学 editorial |

> 黑名单合规: 0 条 blacklisted (无 zhihu / mp.weixin / 百度百科 / CSDN / cnblogs / jianshu / linkedin pulse / quora / pinterest / behance).
> Bucket 比例 (n=75): verified_primary 26 (~35%), surrogate_primary 25 (~33%), secondary 24 (~32%), reference 0.
> surrogate_primary 全部含 whitelist note 关键词 ("协会" / "监管" / "课程" / "syllabus" / "AIA contract").

---

## A. 单项目 SOP (5 phase, AIA 国际 + 中国三阶段 dual mode)

> Locale map (诚实): AIA 国际 5 phase = Schematic Design (SD) / Design Development (DD) / Construction Documents (CD) / Bidding (B) / Construction Administration (CA). 中国三阶段 = 方案设计 / 初步设计 (含扩初) / 施工图设计, 现场服务 + 监理协调对应 CA. RIBA 8 stage (Stage 0-7) 在 §A.6 简对照. 一个中等公共建筑 (约 3 万平米, RMB 3-5 亿造价) 全流程典型 18-30 月.

### 入门 SOP (新建一个中等项目: 学校 / 文化馆 / 中小公建, 3 万平米, schematic to construction)

#### A.1 Programming / 需求定位 / Pre-Design (1-4 周)

- **输入**: 业主 RFP / 立项批文 / 用地条件 (规划设计要点 / 红线 / 容积率 / 限高) / 业主 OPR (Owner's Project Requirements) 草案 / 预算 budget cap [T03-S007]
- **步骤**:
  1. Visioning workshop — 与业主 + 用户 + 运维方坐下 1-2 天, 定 mission / goals / success metrics. AIA: "a problem well stated is half solved" [T03-S007].
  2. 编 OPR (Owner's Project Requirements) — 范围 / 性能 / 预算 / schedule / 验收标准, 是 cx (commissioning) + 整个项目的"宪法" [T03-S007].
  3. 编 Program Document (面积配比表 + adjacency matrix + space data sheet 每房间).
  4. Site analysis — 日照 / 风环境 / 噪声 / 视线 / 流线 / 周边肌理 / 既有树木 / 测量 (US 用 ALTA Survey; 中国用 1:500 地形图).
  5. 编 Basis of Design (BOD) 草案 — 给业主签字, 锁 baseline.
- **输出**: OPR / Program Doc / Site Analysis Report / fee proposal (基于 B101) / Pre-Design Report.
- **工具**: Excel / Bluebeam / Rhino + Forma (early massing) / GIS / Climate Consultant.
- **常见反模式**: ①不读 RFP 直接画方案 (业主第二轮就把你毙); ②跳过 OPR 直接进 SD, DD 阶段才发现房间数不够, 大改 (中国 typical 跳过 programming 阶段, 用业主"我要 3 万平方学校"一句话作 brief — 反模式 fingerprint).
- **skip / 跳过 / 优化 / add 高级用法**:
  - **skip**: 老业主 + 复制类项目 (连锁酒店 / 标准化校园) 可 skip 全套 visioning, 用业主既有 Program Template 直接修改 (但仍要做 site analysis).
  - **optimize**: 把 OPR + BOD 合并到一份 "Project Charter" + Notion 文档, 设 living-doc 机制, 后续 DD 自动 trace 决策 (M&E 介入早).
  - **add**: 早期 charrette 邀请 LEED AP / cx agent / 结构 + MEP 顾问 (integrative process credit), 决定能不能 net-zero / passivhaus / WELL [T03-S047, T03-S072]. AIA 推荐 IPD 流程下 architect+contractor+owner 三方 charter day [T03-S008].

#### A.2 Schematic Design / 方案设计 (4-10 周)

- **输入**: OPR / Program Doc / Site Analysis / 业主签字的 BOD.
- **步骤**:
  1. Massing 探索 — 3-5 个 parti diagram, 内部 charrette 选 2-3 个深入.
  2. Concept narrative — 50-200 字 design statement (业主可读 + 媒体可印).
  3. 平面 1:200 / 总平 1:500 / 立面 1:200 / 关键剖面 / 体量 model (实体 + 数字).
  4. 早期 cost estimate (US: 约 ±15-20% accuracy; 中国: 方案估算 ±30%).
  5. MEP 顾问 kickoff — 大流向 (机房位置 / 主管井 / 进风出风方向) 锁定.
  6. SD package 交付 — 业主 + 城规预审 sign-off.
- **输出**: SD package (illustrative materials: site plan / 主要平面 / sections / 1-2 立面 / 渲染 / sketch model) [T03-S001]; cost ROM (rough order of magnitude).
- **工具**: Rhino / SketchUp / Revit (early massing 直接进 Revit 越来越主流) / Enscape / Twinmotion / Forma; 物理 chip board + foam model.
- **常见反模式**: ①SD 阶段就把厕所节点画到 1:20 (浪费时间, 业主还要改); ②方案做 5 版"风格选项" (现代 / 中式 / 解构) 给业主选 — 业主只会更迷茫; ③只交渲染, 不交平面 / 总平 — 业主签 SD 是签 area + adjacency 不是签美学.
- **AIA 收费占比**: SD ~15% (range 10-25%) [AIA Standard Form B101].
- **skip / 跳过 / 优化 / add**:
  - **skip**: 中国"快设计"项目 (房企住宅) 跳掉 SD massing 探索, 用业主指定的"标准户型 + 套用立面" 直接进方案稿 (反模式但行业现实).
  - **optimize**: AI generative concept workflow — Midjourney/SD prompt → Forma massing → Rhino mesh-to-BIM (但所有 AI 图必须 manually 转 BIM 再交业主, 不能交 AI 图当方案) [T03-S053].
  - **add**: 早期 daylight + EUI 模拟 (Climate Studio / Forma / Ladybug) 在 2-3 个 massing 上跑, 用数据辅助 parti 选型 (LEED / 中国绿建 双赢) [T03-S051].

#### A.3 Design Development / 扩初 / 扩出 / 初步设计 (6-14 周)

- **输入**: 业主签字 SD / 城规预审意见.
- **步骤**:
  1. 平面深化到 1:100, 关键节点 1:50, 墙身 1:20.
  2. MEP 全专业模型 (Revit federated model 起步, LOD 300) — clash detection round 1 [T03-S024].
  3. 结构选型锁定 (材料 / grid / 跨度 / 楼板厚度) — 结构师交 preliminary calc.
  4. 立面材料 schedule (mockup 准备样板墙 / 大样板).
  5. 中国: 初步设计 + 概算 — 报政府审 (公建强制, 民用住宅可豁免) [T03-S014, T03-S060].
  6. 第二轮 cost estimate (US: ±10%, 中国: ±15%).
  7. 业主 DD/初设 sign-off — 锁 design, 后续改动算 change order.
- **输出**: DD set (平面 / 立面 / 剖面 1:100 + 主要详图 + outline specs); 中国 初步设计 set (含概算 / 各专业说明 / 主要设备表) [T03-S014]; MEP federated Revit model LOD 300.
- **工具**: Revit + Navisworks (clash) / BIM 360 (CDE) / Solibri / Bluebeam.
- **常见反模式**: ①DD 阶段还在改方案 (业主新需求 → 反向回 SD, 时间 + 费用双爆); ②MEP 顾问介入晚, DD 末才发现机房不够 → 后期返工; ③LOD 没 team 共识, MEP 画到 LOD 200 而 architect 已 LOD 350 → clash 误报 [T03-S024].
- **AIA 收费占比**: DD ~20% (range 10-25%).
- **skip / 跳过 / 优化 / add**:
  - **skip**: 简单项目 (Type V 木结构小住宅 / 中国不强制初设的民用工程) 可 skip 初步设计, SD 通过后直进 CD/施工图 — 但要在合同明确 [T03-S014].
  - **optimize**: 用 BIM 360 + Revit Worksharing + Power BI dashboards 同步 cost + carbon + clash 三维数据, week-by-week 给业主看 progress.
  - **add**: 在 DD 末做 LCA round 1 (One Click LCA / Tally), 锁结构方案前对比 RC vs 钢 vs CLT 的 embodied carbon [T03-S048, T03-S049]; mockup wall 1:1 在场地搭, 业主 + 项目经理 + 总包共看 (避免施工图末才发现 panel 模数错).

#### A.4 Construction Documents / 施工图设计 (8-20 周)

- **输入**: 签字 DD / 初设批文 / 概算批复 (中国).
- **步骤**:
  1. 全套图纸 + spec 详图深化 (US: CSI MasterFormat 50 division spec; 中国: 制图按《房屋建筑制图统一标准》GB/T 50001).
  2. MEP coordination 第二/三轮 — Navisworks 周会, 系统协调到 LOD 400 (US) / 中国 typical LOD 350 (含 family 库国标节点).
  3. Structural calc 锁定, 出钢筋图 + 节点详图 (中国施工图深度远高于 US — 含全部钢筋排布而非 typical detail) [T03-S015, T03-S060].
  4. 建筑节点详图: 墙身 / 收口 / 防水 / 屋面 / 室内主立面 (1:20 / 1:10 / 1:5).
  5. Permit set 出图 — US: 给 city plan check; 中国: 出施工图给图审 (含强制审查节能 / 结构 / 消防) [T03-S014, T03-S060].
  6. Final cost estimate (US: ±5-8%, 中国: 施工图预算 ±5%).
  7. Quality control 内审 — 至少 1 senior PM + 1 QA/QC 通校.
- **输出**: 施工图全套 (US: ~150-300 张 + spec book; 中国: 300-800 张, 含设备 / 结构钢筋 / 防雷 / 节能专项 / 消防 / 装配式 if applicable [T03-S014]); permit application.
- **工具**: Revit + Navisworks + Bluebeam Studio + CSI specs (US) / 天正建筑 + 鸿业 + PKPM + Revit (中国, dual workflow common); E-Specs / Deltek Specpoint.
- **常见反模式**: ①施工图阶段还在改方案 (中国房企 typical bug — 总部新换领导要求改立面); ②Revit family 库不够中国施工图深度 (国标楼梯踏步 / 防火门 / 节能窗 都要手动 family), 设计院用 CAD+天正 fallback 反而更快 → 但 BIM 不连贯; ③QA/QC 漏 mechanical / electrical 配合, 现场 RFI 爆炸.
- **AIA 收费占比**: CD ~40% (range 35-50%) — 最重头.
- **skip / 跳过 / 优化 / add**:
  - **skip**: 大型 starchitect 项目把 CD 全部分包给 LDI (中国, 国际事务所 + 中国合作 LDI 是标配 [T03-S028, T03-S030]) — design architect 只做 SD/DD, 中国 LDI 出施工图盖章.
  - **optimize**: BIM-to-fabrication 直出 — 用 Tekla / Solibri / IFC export 直接给钢结构 / 幕墙 fabricator, skip 二次绘图 (LOD 400 fabrication-ready).
  - **add**: digital twin handoff 准备 — 施工图同时输出 COBie 数据 (设备 / 房间 / 系统) 给 FM (facility management); 在 CD 阶段就跑 LCA round 2 + 能耗模拟 final round, 提交 LEED/绿建 design submittal.

#### A.5 Bidding & Construction Administration / 招标 + 现场服务 (整个施工期 6-36 月)

- **输入**: 施工图全套 + permit / 图审通过 / 业主招标策略.
- **步骤**:
  1. **Bidding**: pre-bid meeting + RFI to clarify CDs + addenda + bid opening + bid leveling + recommendation to owner [T03-S001, T03-S003].
  2. **CA week 1**: pre-construction meeting + submittal schedule lock-in + shop drawing process map.
  3. **CA ongoing**:
     - **RFI**: 7 working days 内回 (industry standard) [T03-S058]; 用 Procore / PlanGrid / Bluebeam Revu Studio 中央 log.
     - **Submittals**: 总包提交 → architect/engineer review → "no exception" / "make corrections noted" / "revise & resubmit" / "rejected" [T03-S058].
     - **ASI / Architect's Supplemental Instruction**: 小修改不影响 cost/schedule (架构师单方签).
     - **Change Order (CO)**: 影响 cost/schedule 的修改 — architect 评估 + owner 签 + contractor 执行.
     - **Field observations**: 每 2-4 周一次现场, 写 field report (而非 inspection — 重要法律区分: architect 不"监督"质量, 只 observe).
     - **Application for Payment**: G702/G703 (AIA) — contractor 申请, architect certify, owner 付 [T03-S006].
  4. **Substantial Completion**: 出 Certificate of Substantial Completion + punch list (deficient items list) [T03-S058].
  5. **Final Completion**: punch 清零 + 验收 + 1-year warranty walk + 提交 record drawings + as-built + O&M manuals.
  6. **中国 dual mode**: 现场服务 + 监理协调 — architect 不直接管现场 (监理工程师管), 但出席例会 + 处理设计变更 + 配合验收 [T03-S021]. 监理是 owner 雇的第三方 (FIDIC "Engineer" 角色, 但中国监理权力远低于 FIDIC Engineer) [T03-S029].
- **输出**: 招标答疑 + 中标推荐 + 全部 RFI log + submittal log + ASI/CO log + field reports + Certificate of Substantial Completion + Final Certificate + record drawings.
- **工具**: Procore / PlanGrid / Bluebeam Studio / Newforma / BIM 360 Field; AIA G-series forms; 中国: 项目管理软件多用 Excel + 自研 + 广联达.
- **常见反模式**: ①CA 阶段 architect 当"质检员", 实际签字 = 承担质量责任 (法律陷阱, 应只做 observation + 设计意图 conformance); ②RFI 拖延 > 14 天, contractor 发 delay claim; ③CO 不走流程现场口头同意 → owner 拒付; ④中国: architect 完全甩给监理 + LDI, 自己消失, 现场把方案改得面目全非 → starchitect 项目"现场翻车"高发.
- **AIA 收费占比**: Bidding ~5% + CA ~20% (range 20-30%).
- **skip / 跳过 / 优化 / add**:
  - **skip**: design-build / IPD 模式 — bidding phase 不存在 (contractor 早就在 team 里), architect 只做 CA [T03-S008].
  - **optimize**: 用 Procore + BIM 360 实时 RFI / submittal log, RFI response time SLA 设为 5 天 (优于 7 天 industry standard); 设 "weekly submittal triage" 30 min 内决定批 / 改 / 拒.
  - **add**: 增加 POE (Post-Occupancy Evaluation) — RIBA Stage 7 / AIA Sustainable Design Assessment Tool, 入住 6-12 月回访 + 实测 EUI / sDA / occupant survey, 反哺下一个项目 [T03-S012].

### A.6 资深路径 / 跳过 / 优化 / 添加 (high-level diff vs 入门)

> 资深 (5-15 年 PM) 与入门 (0-3 年 designer) 最大区别: 资深 PM 把设计 60% 时间花在合同 / 流程 / 沟通 / 风险, 入门 100% 花在画图. 每 phase ≥ 2 diff:

- **Phase A.1 Programming**:
  - **skip**: 资深 PM 跳过"完整 OPR 模板", 改用 1-page Project Charter + 关键决策 log, 因为业主签 50 页 OPR 大概率不读 — 提炼 5 个 must-have / 3 个 nice-to-have / 2 个 must-not-have 反而锁住 scope.
  - **add**: 资深 PM 在 programming 阶段就 onboard 法律 + insurance + 财务 — 因为这些后续不能补 (e.g. 项目 IP / risk allocation / E&O insurance 限额).

- **Phase A.2 SD**:
  - **optimize**: 资深 PM 不用画 10 个 parti, 用 1 个 strong parti + 2 个 alternative 即可, 把时间用于业主沟通 + 内部 charrette quality.
  - **add**: 资深 PM 同时 onboard 城规 / 政府 pre-application meeting (中国: 报方案前与规划局非正式沟通 — "前置审批") — 入门 typical 漏掉.

- **Phase A.3 DD**:
  - **skip**: 资深 PM 推动 "DD-light" 策略 — 中国 fast-track 项目把 DD 与 CD 合并 ("初设 + 施工图同步"), 时间压缩 30-40% 但风险大.
  - **add**: 资深 PM 在 DD 末做 risk register + decision log 锁定 — 哪些 design intent 不能变 / 哪些可让步, 给后续 CA 防守 design intent 时引用.

- **Phase A.4 CD**:
  - **optimize**: 资深 PM 用 multi-disciplinary lead-architect overlay 系统 — 每个 system (curtain wall / partition / ceiling) 指定一个 senior 全责, 而非按图纸张数分配, 提高 cross-system coordination 质量.
  - **add**: 资深 PM 主动 onboard 总包 (US: pre-construction services 阶段; 中国: 大业主有自己甲方代建 + 全过程咨询) — CD 阶段就开始 mockup + value engineering 谈判, 而非等 bidding 阶段被砍设计.

- **Phase A.5 Bidding + CA**:
  - **skip**: 资深 PM 跳过"被动 RFI 等待"模式, 改 weekly proactive design intent meeting — 上周 punch + 下周 lookahead, RFI 数量降 40-60%.
  - **optimize**: 资深 PM 设 RFI categorization (urgent / standard / clarification only) + 不同 SLA, 把 80% RFI 在 < 3 天内处理.
  - **add**: 资深 PM 在 CA 末同时启动 POE plan + next-project lessons-learned doc — 知识资产化.

### A.7 RIBA 8-stage 对照 (UK / 国际)

> RIBA Plan of Work 2020 (Stage 0-7) 是 UK 主流, 国际很多 client (英联邦 / 海湾) 直接用 RIBA [T03-S010, T03-S011]:

| RIBA Stage | 名称 | ≈ AIA | ≈ 中国 |
|------------|-----|-------|-------|
| 0 | Strategic Definition | (Pre-) Programming | 项目立项 / 可研 |
| 1 | Preparation & Briefing | Programming | 需求定位 / 任务书 |
| 2 | Concept Design | SD | 方案设计 |
| 3 | Spatial Coordination (改自 2013 "Developed Design") | DD | 扩初 / 初步设计 |
| 4 | Technical Design | CD | 施工图设计 |
| 5 | Manufacturing & Construction | CA (施工期) | 施工 + 监理 + 现场服务 |
| 6 | Handover | Substantial Completion | 竣工验收 |
| 7 | Use | POE / FM | 后评估 / 运维 |

RIBA 2020 关键更新: Stage 7 → Stage 0 是 "circular", 强调 POE feedback loop; sustainability outcomes 贯穿 0-7 而非孤立专项 [T03-S010, T03-S012].

---

## B. 事务所类型 SOP (5 type)

### B.1 Boutique atelier (5-30 人, design intent + 文化建筑)

- **项目特征**: 文化 / 教育 / 小型公共 / 高端私宅 / 改造 / 乡建; 单项目 RMB 2000 万-2 亿造价; 设计费率高 (8-15% 造价, US: $300-500/sf design fee on small project); 长周期 (单项目 3-7 年是常态); 重 craft / 重 detail / 重材料.
- **团队配置**: 1-2 principal (设计 director) + 1-2 associate + 5-15 designer + 1-2 admin; 扁平结构; principal 直接画图; "学徒"模式带新人.
- **商业模式**: 收 design fee + monograph 出版 + 学校教席 + 奖项 + 业主主动找上门 (不投标 lead-gen); 不做 commodity work; principal 半时间教书 / 出书.
- **典型周期 / 设计费率**: 单项目 3-7 年从签约到落成 (caveat: 国际项目); 设计费率 8-15% 造价 (caveat: 高于 industry avg 5-8%, 因 design 含量高).
- **跑通流程的反模式**: ①接超出 capacity 的大项目 (3 万平米以上) → 团队崩盘, 改用 LDI 协作但 lose design control; ②不收 schematic deposit, principal 设计画好了业主消失; ③拒绝用 BIM, 全 Rhino 出图, 施工图阶段不得不交给 LDI 重画.
- **skip / 跳过 / 优化 / add 关键 (≥ 2)**:
  - **skip**: skip 大投标 / 公开 competition — 选择性接邀请赛 + 业主主动来约, 节省巨大 BD 成本 (boutique 投标命中率 < 5%).
  - **optimize**: 把 monograph / 大学课程 / 双年展 / 媒体策展当成 lead-gen pipeline, 而非"额外活动" — 业主因看了 El Croquis 一期主动找上门是 boutique 标准来源 [T05-S014].
  - **add**: 与 1-2 家 trusted LDI 长期合作 (中国: 大舍 + 同济院; 国际: Caruso St John + local Mitarbeiter), boutique 做 SD/DD design intent, LDI 出施工图 + 协调监理 [T03-S031, T03-S032].
- **业内代表 / case**: 大舍 (Atelier Deshaus, 刘宇扬+柳亦春+陈屹峰) [T03-S032, T03-S033] / 直向 (董功) / Caruso St John [T03-S031] / Office Kersten Geers David Van Severen (OFFICE KGDVS) / Atelier Bow-Wow (塚本由晴) / 张轲 (标准营造) / Aires Mateus / Brandlhuber+.

### B.2 国际中型 firm (50-150 人, 北美主流, 多 typology mix)

- **项目特征**: 教育 / 医疗 / 办公 / 文化 / 多家庭住宅 mix; 单项目 $5M-$100M 造价; 设计费率 6-10% 造价; 周期 2-5 年; 重 delivery / 重 BIM / 重 client management.
- **团队配置**: 6-15 principal (含 design principal + managing principal + technical principal) + 20-50 associate + 100+ staff; matrix 结构 (project teams + studio leads + technical groups); 每项目 1 design lead + 1 PM + 1 PA (project architect) + 3-10 staff.
- **商业模式**: 70% repeat client + 30% RFQ/RFP + 偶尔 invitation 投标; 重视 sector vertical (healthcare studio / education studio); fee 70% design + 30% additional services (FF&E / branding / cx).
- **典型周期 / 设计费率**: 大学 / 医院 单项目 2-5 年; 设计费率 6-10% (caveat: 北美 healthcare / lab 上限 10-12%, K-12 5-7%, 办公 4-6%).
- **跑通流程的反模式**: ①sector vertical 过度孤立 → 跨 sector 项目 staff 调不动 (healthcare studio 不会画 K-12); ②BD principal 接的项目 design principal 不喜欢 → 内部撕裂; ③scope creep 没有早期 change order — 业主"再帮我看看 FF&E", 半年后 50 小时, 收不到钱.
- **skip / 跳过 / 优化 / add 关键 (≥ 2)**:
  - **skip**: skip starchitect-style 概念 charrette 排场 — 用 client-co-design workshop 替代, 业主 + architect 共同 brainstorm, 决策更快.
  - **optimize**: 用 Deltek Vantagepoint / Vision + Monograph / BQE 做 utilization rate 周报, 每周看每个 staff billable %, 实时调整 staffing — A/E 利润率取决于此 [T03-S043, T03-S044].
  - **add**: build "lessons learned" 知识库 + design standards templates, 新项目 cookie-cutter 出 SD set 把时间留给 design refinement; 同时 add IPD-light delivery (architect + GC + owner 三方早期 contract) 提高大项目命中率.
- **业内代表**: Perkins&Will / HOK / Gensler / NBBJ / CannonDesign / EYP / KieranTimberlake / Snøhetta / Mecanoo / Heatherwick Studio / Aedas.

### B.3 Starchitect 国际工作室 (100-500 人, Foster / OMA / BIG / Zaha / Herzog)

- **项目特征**: 国际地标 / 文化 / 大型公建 / mixed-use / masterplan; 单项目 $50M-$1B+ 造价; 设计费率 3-6% (low 因 volume + brand premium 弥补); 周期 5-15 年; 重 concept signature + 全球分公司协调.
- **团队配置**: 2-10 founding/managing partner + 10-30 senior associate (含 head of design + head of project + head of research) + 200-500 staff; 强 head-quarter (Rotterdam/London/Copenhagen) + global offices (HK / NY / Doha / Shanghai); applied R+D / Computational Design / Materials group 独立部门 [T03-S035].
- **商业模式**: invitation competition + repeat institutional client (national museum / airport / royal commission); founding partner 是品牌, principal 主导 concept, technical 全部下放 to associate 和 local partner.
- **典型周期 / 设计费率**: 文化 / 机场 / 国家级单项目 5-15 年; design fee 3-6% (caveat: 北美 healthcare / lab 设计费率上限可达 10-12%, starchitect 拿全球品牌项目反而费率被砍).
- **全球分公司协调点**: 总部 (Rotterdam OMA / London Foster / Copenhagen BIG) 做 concept + design intent, 项目本地 (HK / Doha / Shanghai) 做 DD/CD + client-facing; 时差 + 文化 + 技术语言 是首要 risk; 协调机制: weekly all-hands video + Confluence / Notion shared canvas + 关键 milestone fly-in.
- **跑通流程的反模式**: ①founding partner 不撒手, 所有 review bottleneck 在他一人; ②concept 太复杂施工预算翻倍 → 项目被砍 (Pritzker 形态炫技但施工预算翻倍是行业 fingerprint); ③把 fee 都谈到很低靠 volume, 但 brand premium 不够导致 utilization 60% 以下不盈利.
- **skip / 跳过 / 优化 / add 关键 (≥ 2)**:
  - **skip**: skip 区域办公的施工图全责任, 完全依赖 local LDI 出施工图 + 监理 (中国市场 OMA / Foster / Zaha 都用此模式) [T03-S028]; design architect (DA) + architect of record (AOR) 分工.
  - **optimize**: 集中 computational design / materials research / VR / digital twin 在 HQ 一个 lab, 服务全公司 — Foster Applied R+D 是范例 [T03-S035]; 用 OMA-style model-making lab 把模型当 universal collaboration tool (拍照 + 投影 + 视频会议 share) [T03-S038].
  - **add**: 设独立 Communications / monograph / 大学合作 / 双年展 组, 持续投资 brand asset — starchitect 业务来源 50%+ 依赖 brand, 不投就消失.
- **业内代表**: OMA / Foster + Partners / BIG / Zaha Hadid Architects / Herzog & de Meuron / Renzo Piano Building Workshop (RPBW) / SANAA / Heatherwick Studio / Diller Scofidio + Renfro (DS+R) / MAD Architects (中国出海 starchitect).

### B.4 中国大型设计院 (1000-5000 人, 资质 + 施工图主流)

- **项目特征**: 房地产 (寒冬前主力) / 公共建筑 / 城市更新 / 综合交通 / 医疗 / 教育 / EPC; 单项目 RMB 5000 万-50 亿造价; 设计费率 1-3% 造价 (远低于国际 — 中国市场基础费率压价 + LDI 走量) [T03-S020]; 周期 2-8 年; 重资质 + 施工图量产 + 政府关系 + 报建.
- **团队配置**: 1-10 院长副院长 + 20-100 总建筑师 / 总工 + 100-500 副总 / 所长 + 500-3000 staff; 院 → 分院 → 所 → 工作室 → 项目组 四级; 综合甲级 (民用建筑全部专项 / 市政 / 城市规划 / 风景园林 / 商业 / 装修) [T03-S019, T03-S025]; 内含全专业 (建筑 / 结构 / 给排水 / 电气 / 暖通 / 智能化 / 景观 / 室内 / 经济 / 概算).
- **商业模式**: 政府 / 国企 / 房企 直签 + 大量招投标; 走资质 (甲级才能做大公建 / 三级才能投标分级以下); 大量施工图配套国际 / starchitect (LDI 模式) [T03-S028, T03-S030]; 寒冬期主营转向城市更新 / 老旧改 / 海外 EPC + 全过程咨询 [T03-S023, T03-S063, T03-S064].
- **典型周期 / 设计费率**: 民用建筑 1-3% 造价 (caveat: 2024-2026 实际成交价跌至 60-80% 标准价); 周期: 方案 1-3 月 / 初设 2-4 月 / 施工图 3-9 月; 房企"快设计"项目 全周期 4-8 月.
- **跑通流程的反模式**: ①方案 + 施工图同步 ("快设计"行业内卷) → 现场返工率 30%+; ②"图审挂帅" — 只把图过审作为目标, design intent 全部牺牲; ③LDI 协作时不参与 SD/DD 决策, 等收到 international DD 后强行翻译, 不合中国节点结果现场全是 RFI; ④资质挂靠 / 借资质 出图 (违法风险).
- **skip / 跳过 / 优化 / add 关键 (≥ 2)**:
  - **skip**: skip "国际方案 + 国内施工图"过度依赖模式, 自主培养 design 团队 (院士工作室 / 名师 studio 模式 — CADG 崔愷工作室 / 同济院 章明工作室 / 局部 boutique 化).
  - **optimize**: 把 Revit family 库国标化 (花 1-2 年 add 2000+ 国标 family — 门 / 窗 / 楼梯 / 节能墙身), BIM 不再因 family 不够回到 CAD+天正; 用 Solibri 做国标 spec check.
  - **add**: 加投资 城市更新 / 城市体检 / 文旅 / 乡建 / EPC / 海外项目 — 寒冬转型 SOP (详见 §C.7) [T03-S063, T03-S064]; add 全过程咨询 / 工程项目管理 资质, 跨出纯设计走"设计-代建-运维"链条.
- **业内代表**: 中国建筑设计研究院 (CADG) [T03-S025, T03-S026] / 上海现代建筑设计集团 (SMEDI / Arcplus) / 同济建筑设计研究院 / 北京市建筑设计研究院 (BIAD) / 清华大学建筑设计研究院 / 中南建筑设计院 / 华东建筑设计研究院 / 中信设计 / 广州市设计院 (GZDI) [T03-S027].

### B.5 独立建筑师 lone wolf (4-15 人 或 sole practitioner 1-3 人)

- **项目特征**: 私宅 / ADU / 改造 / 商铺 / 小型公共 / 小学 / 民宿; 单项目 $500K-$10M 造价; 设计费率 8-18% (因服务密度高); 周期 6 月-2 年; 重业主关系 + boutique design + 全周期亲手参与.
- **团队配置**: 1 architect (principal + everything) 或 1 principal + 1-2 designer + 1 admin + outsource consultants (structural / MEP / civil); 高 outsource 比例 (60-80% non-arch work).
- **商业模式**: 95% 业主转介 / 网络 (Instagram / Houzz / 30X40 YouTube 公开 building-in-public); 不做投标; 30% AIA 美国 firm 是 sole practitioner [T03-S040].
- **典型周期 / 设计费率**: 私宅 6-18 月, 改造 3-12 月; design fee 8-18% (caveat: 美国 residential 15-20% 是常见); 中国民宿 design fee 200-500 RMB/平米 (caveat: 行情 estimate, 无国标).
- **跑通流程的反模式**: ①接超出 capacity 的项目 (大型公建) → 自己被淹; ②不分阶段收费 (lump sum) → 业主无限改; ③不收 insurance / E&O → 一个 claim 破产; ④不用 BIM ("我画 CAD 更快") → MEP 顾问无法 federated coordinate, 后期 RFI 爆.
- **skip / 跳过 / 优化 / add 关键 (≥ 2)**:
  - **skip**: skip in-house MEP / structural, 100% outsource — 关键是建立 trusted consultant 网络 (3-5 个长期合作); skip in-house IT — 全 SaaS (Monograph / Confluence / Bluebeam Studio).
  - **optimize**: 用 Chief Architect / Vectorworks / Revit LT 做 small-project BIM (轻量 BIM) — 不强求 LOD 400, 用 LOD 200-300 + 强 spec 控制 [T03-S071].
  - **add**: 内容营销作为 lead-gen — YouTube (30X40, Eric Reinholdt 1M+ subs 是范例) / Instagram / Substack — sole prac 没有 BD 团队, 内容 = 业务 [T05-S040].
- **业内代表**: Eric Reinholdt (30X40 Design Workshop, Maine) [T05-S040] / Stewart Hicks (Chicago) / 国内大量乡建 / 民宿独立建筑师 (e.g. 三文建筑何崴 / line+ / 罗宇杰工作室) / Bohlin Cywinski Jackson (中型但起源 sole-prac 心法).

---

## C. 横向能力 SOP (6 个 cross-cutting workflow)

### C.1 BIM 协作 workflow (Revit + IFC + clash detection + LOD)

- **入门 SOP**:
  1. 项目启动定 BIM Execution Plan (BEP) — LOD/LOI 表 (每元素按 phase) + 命名规则 + 文件夹结构 + clash matrix [T03-S008, T03-S024].
  2. 建 federated model on CDE — Autodesk Construction Cloud (BIM 360) / Revizto / Trimble Connect.
  3. Worksharing — central + workshared models; daily sync.
  4. Clash detection rounds — DD round 1 (LOD 300) / CD round 2-3 (LOD 350-400); Navisworks Manage 或 Solibri 跑 hard + soft clash.
  5. Issue management — BCF (BIM Collaboration Format) 跨平台 issue 流转 (Revit ↔ Navisworks ↔ Solibri ↔ Tekla).
  6. COBie / IFC export 给 FM at handover.
- **常见反模式**: ①没有 BEP, 全员 free style → 每家 family / 命名 / origin 都不同 → federated 时坐标对不齐; ②clash count 当 KPI → 大量 false-positive clash (空调风管和吊顶 — 因 LOD 共识没建好) → 周会浪费 [T03-S024]; ③业主只签 PDF 不验 model → BIM 沦为 documentation 副产品.
- **skip / optimize / add (≥ 2)**:
  - **skip**: 小项目 (private house < $2M) skip federated BIM, 用 Revit 单机 + Excel spec; 但 still keep IFC export 给 cx + FM.
  - **optimize**: 用 Dynamo / Grasshopper 自动化 BIM repetitive task (e.g. 自动 sheet setup / 自动 family swap / 自动 tag) 节省 30% staff time.
  - **add**: digital twin handoff — 把 Revit 模型 + IoT sensor schema + COBie 一起交给 FM 软件 (Archibus / IBM Maximo); add VR/XR walkthrough (Twinmotion / Enscape / IrisVR) 给业主 SD/DD review.

### C.2 可持续设计 workflow (LCA + EUI + sDA + 早期 vs 晚期介入)

- **入门 SOP**:
  1. **Pre-design**: sustainability charrette — 全 team + cx + LEED AP + 业主 align on 目标 (LEED Gold / WELL / Passivhaus / net-zero / 中国绿建三星) [T03-S047, T03-S072].
  2. **SD**: 早期 climate analysis + daylighting (Climate Studio / Ladybug / Forma) + 2-3 个 massing option 跑 EUI baseline.
  3. **DD**: energy model LOD 300 (Sefaira / IES VE / OpenStudio); envelope optimization; daylight 优化 (sDA ≥ 55% target).
  4. **CD**: LCA round 1-2 (One Click LCA / Tally / Athena) — embodied carbon < 500 kgCO₂e/m² 是 LETI / RIBA 2030 baseline [T03-S048, T03-S049, T03-S070]; 完成 LEED submittal preparation.
  5. **CA + POE**: commissioning + measurement & verification + POE 6-12 月后实测 EUI vs predicted, performance gap 评估.
- **常见反模式**: ①sustainability 当 add-on 不当 driver — DD 末才请 LEED AP, 大量措施 retrofit 进设计, cost 暴涨; ②只算 operational carbon 不算 embodied carbon — 现代节能建筑 embodied 占 50-70% lifetime CO₂; ③LEED check-listing — 攒分通过却不真节能 (predicted-actual gap 30-50%); ④AI 渲染交业主当"低碳设计"不做 LCA / 没做 EUI 模拟就报"低碳".
- **skip / optimize / add (≥ 2)**:
  - **skip**: 简单项目 skip 完整 LCA, 用 Carbon Designer 3D (One Click LCA 快速版) 只算 structural + envelope embodied — 80% impact 在这 [T03-S048].
  - **optimize**: 把 EUI / LCA / daylight 数据集成进 BIM dashboard (Power BI), DD 每周自动更新, design decision 实时看 carbon impact.
  - **add**: 早期 add 业主 net-zero / Passivhaus pre-cert ALIGNMENT (而非项目末 LEED submittal) — RIBA 2030 / AIA 2030 Commitment 已是行业 baseline [T03-S010, T03-S012]; add POE feedback loop, 把 actual EUI 数据反哺下一个项目 SD 阶段的 baseline.

### C.3 AI generative concept workflow (Midjourney → SD → Forma → 决策)

- **入门 SOP**:
  1. **Brief-to-prompt**: 把 OPR / site / typology 转为 image prompt (style + material + program); 注意保密 (Midjourney public mode 业主 IP 会泄露).
  2. **Concept exploration**: Midjourney v6 / DALL-E / Stable Diffusion 跑 50-200 张 reference, 内部 charrette 选 5-10 张 direction [T03-S053].
  3. **2D-to-massing**: 用选定 reference 在 Rhino / SketchUp 手动 build massing, 或用 Forma AI massing 直接生成 site-context-aware option [T03-S052].
  4. **Massing-to-BIM**: Forma → Revit 双向同步 (2024-2026 主流) → Revit Architecture LOD 200 model.
  5. **Design refinement**: Stable Diffusion + ControlNet 把 Revit 视角图 re-style (e.g. 给材料 + 光影) 出业主可看的 photoreal 概念图.
  6. **Decision gate**: 业主签字时 must 看到 manually-built BIM model + 渲染, 而非纯 AI 图.
- **常见反模式**: ①AI 渲染交业主当设计 — 业主签 SD 后发现实际不能建; ②上 Midjourney public mode 业主 IP 风险; ③只学 prompt 不学 site analysis — AI 图与 context 脱节; ④跳过 manual BIM 直接 AI-to-fabrication (2026 工具还做不到, 是 hype).
- **skip / optimize / add (≥ 2)**:
  - **skip**: starchitect / 高 design intent boutique 项目 skip AI concept (会 dilute author voice); AI 适合 commodity work (住宅 / 办公方案选型) 提速.
  - **optimize**: 建 firm-specific Midjourney style library (e.g. 大舍-style prompt / Caruso-style prompt), 训练 LoRA / 自定义 SD model 保 design language consistent [T03-S053].
  - **add**: add Autodesk Forma + neural CAD (2025-2026 推出) 做 early massing site-context-aware AI; add legal review on AI image IP (Midjourney TOS / training data lawsuits 2024-2026) [T03-S054, T03-S055].

### C.4 投标 / Competition workflow (短周期 + 团队冲刺 + deliverable 取舍)

- **入门 SOP**:
  1. **Go/no-go 评估** (Day -7): 读 brief 3 遍 + 评估 win probability (typical 5-10% open / 20-40% invited); 命中率 + LCV (lifetime client value) 算 ROI.
  2. **Charette day 1-3**: parti 探索 (5-10 个 idea → 选 1-2 个深入) + design narrative draft.
  3. **Development day 4-14 (2 周 deadline 典型)**: 平面 + 立面 + 关键剖面 + 1-2 渲染 + parti diagram + 1 张 boards 主图 (3-second test [T03-S056, T03-S057]).
  4. **Final week**: review by 1-2 senior outsider → tighten narrative + visual hierarchy → 检查 anonymization (UIA / RIBA competition 严格) [T03-S056].
  5. **Submission day -2**: 双备份 + 三遍 spec check (format / naming / board dimension) — submission disqualification 因 spec 错占 5-10% [T03-S056].
- **常见反模式**: ①追求 design depth → board 太满 → jury 3 秒看不懂 → 出局; ②不读 brief 直接画 — 投了 5 轮才发现 typology 错; ③ team lead 不存在, 大家平行画 → 最后整合时 narrative 散.
- **skip / optimize / add (≥ 2)**:
  - **skip**: skip 公开 competition (5% 命中率 + 不发 honorarium 的) — 高 cost 低 ROI; 只投 invited / paid competition; skip 不付 honorarium 的私人 client "design competition".
  - **optimize**: 设固定 competition team (1 lead + 2 designer + 1 model maker + 1 graphic), 不每次重新组队; 用 board template + parti diagram template + narrative template 提速 50%.
  - **add**: add 1 个 outsider (跨学科 — 平面 / 艺术 / 工程师) 30-min review at day 7 + day 12 — 业内人看不到的盲点 [T03-S056]; add 标准 "post-competition lessons" 一页文档每次填.

### C.5 业主管理 workflow (变更管理 + 设计费 + 范围蔓延 + 沟通节奏)

- **入门 SOP**:
  1. **Contract**: B101-2017 (or 中国住建部范本) — 明确 basic / supplemental / additional services 划分 [T03-S003, T03-S004]; 定 single point of contact 业主方; 定 change order 流程 + fee structure (% / hourly / fixed).
  2. **Kickoff**: 设 communication cadence — weekly call + monthly review + phase gate sign-off, 写进合同 [T03-S042].
  3. **Phase gate sign-off**: 每 phase 末业主 written approval → 锁 design, 后续改动算 change order [T03-S043, T03-S044, T03-S045].
  4. **Change order management**: 业主新需求 → 24-48 hr 内出 CO proposal (scope diff + fee + schedule impact) → 业主签 → 执行; 不签字不开始.
  5. **Invoicing**: monthly progress invoice on % complete or hourly; A/R follow up 不超过 30 天.
- **常见反模式**: ①没有 phase sign-off → 业主无限免费回到 SD 改; ②change order 口头同意不书面 → 业主反悔不付; ③业主 single point of contact 不存在 — 5 个人发指令互相矛盾, architect 哪个都不算数 [T03-S045]; ④不及时 invoice → 业主把你当不优先, 现金流崩.
- **skip / optimize / add (≥ 2)**:
  - **skip**: 长期 trusted 业主 skip 每次重签 B101, 用 master agreement + project work order; skip excessive deliverable (业主从不看的 monthly report) → 改 dashboard.
  - **optimize**: 用 Monograph / Deltek / BQE 自动化 invoice + utilization + budget burn dashboard [T03-S044]; 设 CO threshold (e.g. < 2 hr "courtesy", > 2 hr 必须 CO) 减少摩擦.
  - **add**: add 项目末 lessons-learned debrief + client satisfaction survey + NPS — 长 client lifetime value 是 boutique / 中型 firm 利润核心.

### C.6 现场服务 / CA workflow (RFI / ASI / submittal / punch list / 中国监理 vs 美国 CA)

- **入门 SOP**: (见 §A.5 详细步骤)
  1. Pre-con meeting + submittal schedule + RFI process map.
  2. Weekly site visit + field report (US: observation, 不签质量).
  3. RFI/Submittal log on Procore/PlanGrid → 7 day SLA reply.
  4. ASI / Change Order 流程严格走.
  5. Pay app G702/G703 architect certify [T03-S006].
  6. Punch list at substantial completion + warranty walk year 1.
- **中国 vs 美国对比**:
  - 中国: 监理 (CAEC 协会归口) 管现场质量 + 进度 + 安全, architect 只来开例会 + 处理变更 + 出席验收, 现场签字权小 [T03-S021, T03-S029]; 监理是业主雇的第三方 — 类似 FIDIC Engineer 但权力远小.
  - 美国: architect 是 owner agent, 持续 CA 服务, 但严格"observe not inspect" — 法律边界关键 [T03-S058, T03-S059].
- **常见反模式**: ①architect 当"监督员"签质量 → 法律责任承担 (E&O claim risk); ②中国 architect 现场消失把全部委托给监理 + LDI → 设计意图严重走样 (starchitect 项目"现场翻车"是 fingerprint); ③RFI 拖延 > 14 天 → contractor delay claim; ④CO 不走流程现场口头同意 → owner 拒付.
- **skip / optimize / add (≥ 2)**:
  - **skip**: design-build / IPD 项目 skip 传统 RFI / submittal (collocated team + co-location office); 但 still 需要 ASI + Change Directive 流程.
  - **optimize**: 用 Procore + Bluebeam Studio + Newforma 中央 log + 自动 SLA reminder; 设 weekly proactive design intent meeting 主动 catch issue 减少 RFI 40-60%.
  - **add**: add POE + 1-year warranty walk + measure actual EUI / sDA / occupant survey, 反哺 firm 标准库; add digital handover (COBie + Revit model + maintenance manuals) 给 FM.

### C.7 中国房地产寒冬下事务所转型 SOP (2021-2026)

> 行业现状: 2025 年全国房地产开发投资下降 17.2%, 房屋新开工面积下降 20.4%, TOP100 房企单月销售 ¥2111 亿 (历史低位) [T03-S063, T03-S064, T03-S065]. 10 大设计院市场份额超 25%, 中小型设计院累计 10%+ 退出市场 [T03-S063]. 行业从增量转存量 / 城市更新, 设计院从"设计师"转"体检师+规划师+设计师+评估师+策划师" [T03-S064].

- **入门 SOP (针对中型设计院 / boutique 转型)**:
  1. **业务结构 audit** (Q1): 当前 revenue mix (住宅% / 公建% / 商办% / 其他%); 寒冬下住宅 < 30% 才安全.
  2. **新方向选择** (Q2): 从 4 个主轴选 1-2 个 — 公共建筑 (政府投资 / TOD / 文体) / 城市更新 (老旧改 / 工业遗存改造 / 历史街区) / 乡建 + 文旅 (民宿 / 美丽乡村 / 田园综合体) / 海外项目 (一带一路 EPC 设计) / EPC + 全过程咨询 [T03-S063, T03-S064, T03-S066].
  3. **能力 build** (Q2-Q4): 新方向所需的资质 (城乡规划甲 / 文保 / 园林 / EPC 项目管理 / 海外资质 ISO) + 团队 (招 senior + 跨学科 — 城市设计 / 文保 / 文旅策划); 城市更新需要 "城市体检" 能力 — 现状评估 + 多专业整合 [T03-S064].
  4. **首单 pilot** (Q3-Q4): 用 1-2 个 pilot project 验证新方向 — 选 small win 而非大单 (大单失败拖垮转型).
  5. **iteration** (Y2-Y3): pilot 数据评估 → 标准化 process → 规模化.
- **典型路径**:
  - **路径 1: 公共建筑** — 政府投资项目占比, 文体 / 教育 / 医疗 / 交通; 主要竞争 大型央企设计院 + 国际事务所合作.
  - **路径 2: 城市更新** — 增速 22.04% (最快产品类型) [T03-S064]; 老厂房改造 / 历史街区微更新 / 老旧小区改造; 需要 cross-disciplinary (建筑 + 规划 + 文保 + 商业策划).
  - **路径 3: 乡建 + 文旅** — 民宿 / 田园综合体 / 美丽乡村 [T03-S067]; 设计费率比城市项目低但 fee/sf 不一定低 (小项目 design-heavy); 适合 boutique / sole-prac.
  - **路径 4: 海外 EPC** — 一带一路 + 国际承包工程 (2025 中国 76 家进 ENR Top 250) [T03-S065]; 中国设计院 + 中国总包打包 (EPC mode) 出海; 需 ISO + FIDIC 合同熟悉.
  - **路径 5: EPC + 全过程咨询** — 跨出纯设计, 走 "设计-代建-运维" 一体化 [T03-S023]; 需要新资质 + 重资本投入.
- **常见反模式**: ①不转, 死撑住宅赛道 → 业务断崖式下滑; ②同时全部转 5 方向 → 资源摊薄, 一个也不精; ③乡建 / 文旅"用城市项目逻辑做" (Revit + LDI + 大团队) → 项目算不过账; ④海外 EPC 没准备好资质 + FIDIC 合同 + 多币种风控 → 跨境付款 / 索赔崩盘.
- **skip / optimize / add (≥ 2)**:
  - **skip**: 寒冬期 skip 房企商品房项目 (回款 6-18 月 + 不付尾款风险); skip 远郊新区项目 (城投平台付款风险).
  - **optimize**: 用 1-2 个 anchor 政府客户 (城投 / 住建系统) 为核心, 其他业务 satellite; 把寒冬 idle staff 转城市更新调研 / 文保测绘储备 (低成本 build pipeline).
  - **add**: add 全过程咨询 + 工程项目管理 + 招标代理 资质 (从"乙方设计"转"业主代理"), 现金流稳; add 出海能力 — 至少 1 个 senior 熟 ISO / FIDIC / 英文施工图标准; add 跨学科团队 (策划 / 运营 / 商业 / 文旅) — 城市更新和文旅本质是策划驱动而非设计驱动 [T03-S064, T03-S066].

---

## Workflow Summary (parser entry)

> 这一节是 cli_writer 解析入口, 严格遵循 "### N. ..." 标题 + "**入门 SOP**:" + numbered list 格式.

### 1. 单项目设计 SOP (5 phase, AIA + 中国 dual)

**入门 SOP**:
1. Programming / 需求定位 (1-4 周) → OPR / Program Doc / Site Analysis / fee proposal / BOD baseline.
2. Schematic Design / 方案设计 (4-10 周) → SD package: site plan / 主要平面 / sections / 立面 / 渲染 / sketch model + 早期 ROM cost estimate.
3. Design Development / 扩初 / 初设 (6-14 周) → DD set 1:100 + MEP federated model LOD 300 + 中国初步设计 + 概算 + 关键节点详图.
4. Construction Documents / 施工图 (8-20 周) → 全套 CD 图纸 (US: 150-300 张; 中国: 300-800 张) + spec book + permit set + 图审 (中国) + final cost estimate.
5. Bidding & Construction Administration / 招标 + 现场服务 (整个施工期 6-36 月) → RFI / submittal / ASI / CO log + field reports + Certificate of Substantial Completion + punch list + record drawings.

**典型周期**: 中等公共建筑 (3 万平米) 18-30 月全流程; 中国"快设计"住宅 4-8 月 (caveat: 高返工率).
**常见反模式**: ①SD 阶段做 DD 级节点 (浪费); ②施工图阶段还在改方案 (返工灾难); ③MEP 顾问介入晚 (clash 爆炸); ④architect CA 阶段当"质检员"签质量 (法律责任陷阱); ⑤中国 architect 完全甩给 LDI + 监理 (设计意图走样).

### 2. 事务所类型 SOP (5 type)

**入门 SOP**:
1. 评估 typology + 团队规模 + 设计费率 + 周期 + 客户来源 — 5 type: boutique 5-30 人 / 中型 firm 50-150 人 / starchitect 100-500 人 / 中国设计院 1000-5000 人 / 独立 lone wolf 4-15 人 (或 sole-prac 1-3 人).
2. 选定 type 后建立对应商业模式 — boutique: 业主主动 + monograph + 教席; 中型: 70% repeat client + 30% RFQ; starchitect: invitation + brand premium; 设计院: 资质 + 招投标 + 政府关系; lone wolf: 95% referral + 内容营销.
3. 配置对应团队结构 — boutique: 扁平 + principal 画图; 中型: matrix + sector vertical; starchitect: HQ + global office + R+D lab; 设计院: 院 → 所 → 工作室 → 项目组 + 全专业; lone wolf: 1 principal + 高 outsource.
4. 锁 typology mix + 不接超 capacity 项目 (boutique 接大项目崩 / lone wolf 接公建崩 / starchitect 不接小私宅).
5. 持续投入 brand asset (boutique: 出版 + 教学 / 中型: sector thought leadership / starchitect: monograph + 双年展 / 设计院: 资质 + 关系 / lone wolf: YouTube + Instagram).

**典型业内代表**: boutique (大舍 / 直向 / Caruso St John); 中型 (Perkins&Will / NBBJ / Mecanoo); starchitect (Foster / OMA / BIG / Zaha); 中国设计院 (CADG / BIAD / 同济院 / SMEDI); lone wolf (Eric Reinholdt / 三文建筑 / line+).
**常见反模式**: ①事务所类型不清自我定位混乱 → 同时投 boutique 和 commodity 项目, 团队精分; ②超出 capacity 接大项目 (boutique 接 3 万+ 项目, lone wolf 接公建).

### 3. BIM + 可持续 + AI generative + 投标 + 业主管理 + CA + 寒冬转型 集成

**入门 SOP**:
1. BIM 协作 — BEP + federated CDE + LOD 共识 + clash rounds + IFC/COBie handover.
2. 可持续设计 — pre-design charrette + SD 早期能耗 + DD LCA + CD LEED submittal + POE 实测; embodied carbon 与 EUI 双 driver.
3. AI generative concept — Midjourney/SD 探索 → Forma massing → Revit BIM (注意 manual-to-BIM not AI-to-fab); 注意 IP + style consistency.
4. 投标 / Competition — go/no-go ROI + 14 天冲刺 + 3-second test board + spec 严格 check; skip 公开非付费 comp.
5. 业主管理 — B101 / 中国范本明确 service tier + single contact + phase sign-off + CO 流程 + monthly invoice; scope creep 红线.
6. 现场服务 / CA — RFI/submittal SLA + ASI/CO 流程 + observation-not-inspection 法律边界 + 中国 dual mode 处理监理协调.
7. 寒冬转型 (中国限定) — audit 业务结构 + 选 1-2 个新方向 (公建 / 城市更新 / 乡建 / EPC / 海外) + 资质 + 团队 build + pilot 验证.

**典型反模式**: ①BIM federated 没 BEP → clash false-positive 爆; ②sustainability 当 add-on 不当 driver; ③AI 渲染交业主当设计; ④投标命中率 < 5% 仍盲投; ⑤业主无 phase sign-off → 无限改; ⑥architect 在 CA 阶段当"质检员"签质量; ⑦寒冬期不转, 死撑住宅赛道.

---

## Phase 2 接口

### 反复在 ≥ 3 workflow 出现的 心智 / 决策点 (候选 playbook 规则)

- **"早期介入 / 早 onboard"**: programming / SD / sustainability charrette / IPD / 业主沟通 / MEP 顾问 / contractor pre-con / city pre-app — 反复出现, 是 SOP 通用 leverage 点.
- **"phase gate sign-off + decision log"**: 每 phase 末 written approval + 锁 baseline → 后续 change 算 CO; 出现在 A.2 SD / A.3 DD / A.4 CD / C.5 业主管理.
- **"federated CDE + 单一 source of truth"**: BIM federated model on CDE (BIM 360 / Revizto) — clash / spec / cost / carbon / RFI / submittal 全部 hook 进来, 出现在 BIM / 可持续 / CA / 业主 dashboard.
- **"observation not inspection"**: architect CA 法律边界 — 不签质量, 只 observe + design intent conformance, 是中美 architect 共同法律护城河.
- **"LOD 共识 + family 国标库"**: BIM 跨团队协作前必须 align, 否则 clash count 全是 false positive — 中国 LDI 协作的常见痛点.
- **"业务结构 audit + portfolio mix"**: 事务所类型 + 寒冬转型 + competition go/no-go — 都需要先看 portfolio 比例后决策.
- **"内容资产化 / brand asset 投资"**: monograph / YouTube / 双年展 / 教席 / lessons-learned doc — boutique / lone-wolf / starchitect 跨型出现, 是非投标业务来源核心.

### 显著流派 SOP 差异

- **starchitect concept-driven** (Foster / OMA / BIG): SD 占比时间 + 资源最大, founding partner 主导 concept, DD/CD 下放 local 或 LDI; 风险在 concept 不可建 / 预算翻倍.
- **中型 firm schedule-driven** (Perkins&Will / Gensler / NBBJ): matrix 结构 + 严 PM + utilization 周报, 按 phase 严守; design 服务于 client predictability.
- **boutique craft-driven** (大舍 / Caruso St John): 长周期 + 1:1 mockup + craft 决策权在 principal; 风险在 staff scaling 无法支持大项目.
- **中国设计院 compliance-driven**: 资质 + 图审 + 国标 是首要约束, design 是 "图能审过 + 现场能建" 的副产品 (寒冬转型期此特性正在松动).
- **lone-wolf relationship-driven**: 业主关系 = LCV; 单项目获利窄但 client lifetime value 高 (一个家庭重复装修 / 子女私宅).

### 冷僻 / 薄弱信号 (Phase 2 to-do)

- **乡建 SOP < 1 完整 entry** — 中国乡建工作流缺标准 SOP, 个案差异大 (民宿 vs 美丽乡村 vs 田园综合体), Wave 2.5 应再补 1 个 detailed 乡建 SOP (line+ / 三文建筑 / 罗宇杰 案例).
- **EPC 出海 SOP < 1 完整 entry** — 中国 EPC 出海设计实务 (ISO / FIDIC / 多币种 / 海外资质) 缺细节, 适合后续访谈型补强.
- **AI generative 2026 演化快** — Forma neural CAD / Autodesk AI 模型刚发布 (2025-2026), SOP 仍在快速演化; 6 月后可能需重写 §C.3.
- **IPD 在中国落地 SOP** — IPD 美国主流但中国合同 / 信任机制不支持, 缺中国版 SOP — 标弱.
- **POE 中国实践** — POE 在中国院校教学有, 但事务所实际跑通的极少, 缺 case — 标弱.
- **数据 caveat 总览**: 大量设计费率 / 周期数据基于 2002 中国国标 + AIA fee survey 历史均值, 2024-2026 实际行情 (尤其中国寒冬 + 美国 inflation) 偏离 20-40%, 全部需 caveat 标注.
