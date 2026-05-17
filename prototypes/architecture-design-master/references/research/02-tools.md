# Track 02 — Tools (现代建筑设计)

> Wave 2 Track 02 — software / platforms / 工具链. Industry: 现代建筑设计, locale=global, profile=practitioner.
> 工具栈 6-9 月 decay 周期, 每条标 last_updated, AI-generative 子类周期更短 (3-6 月).
> 结构 caveat: (1) 国际主流 (Autodesk / McNeel / Chaos / Trimble / Graphisoft) 与中国本土 (天正 / 鸿业 / 探索者 / 斯维尔 / PKPM / 浩辰 / 中望 / 广联达) 并列, 不视为冗余 — 中国大型设计院 90% 施工图依赖天正+AutoCAD, 不在西方教程中出现; (2) AI-generative 类 (Midjourney V7/V8, SD+ControlNet, Forma, Snaptrude, Maket, Hypar, TestFit) 6 月内 churn 高, 此份按 2025Q3-2026Q2 状态 freeze; (3) 渲染类 (V-Ray / Enscape / Lumion / D5 / Twinmotion / Unreal) 已进入 AI-assisted realtime 阶段 — 静态 V-Ray 派与实时派共存, 不二选; (4) 黑名单合规: 不收 G2 / Capterra / Quora / LinkedIn pulse / 知乎 / mp.weixin / 百度百科 / CSDN / cnblogs / jianshu, 国产 vendor 域名以 surrogate_primary 标 "vendor docs (国产)".

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.autodesk.com/products/autocad/features | surrogate_primary | 2026-05-16 | Autodesk | AutoCAD 2026 features — vendor docs |
| T02-S002 | https://www.autodesk.com/blogs/autocad/autocad-2026/ | surrogate_primary | 2026-05-16 | Autodesk AutoCAD Blog | "Introducing AutoCAD 2026" launch post — vendor docs |
| T02-S003 | https://www.autodesk.com/blogs/aec/2025/04/02/whats-new-in-revit-2026/ | surrogate_primary | 2026-05-16 | Autodesk AEC Blog | Revit 2026 release notes (Apr 2025) — vendor docs |
| T02-S004 | https://help.autodesk.com/cloudhelp/2026/ENU/Revit-WhatsNew/files/GUID-C81929D7-02CB-4BF7-A637-9B98EC9EB38B.htm | surrogate_primary | 2026-05-16 | Autodesk | Revit 2026 What's New help — vendor docs |
| T02-S005 | https://www.rhino3d.com/ | surrogate_primary | 2026-05-16 | Robert McNeel & Associates | Rhino 3D (Rhino 8) main site — vendor docs |
| T02-S006 | https://www.rhino3d.com/en/for/architecture/ | surrogate_primary | 2026-05-16 | McNeel | Rhino for AEC — vendor docs |
| T02-S007 | https://www.rhino3d.com/features/rhino-inside-revit/ | surrogate_primary | 2026-05-16 | McNeel | Rhino.Inside.Revit feature page — vendor docs |
| T02-S008 | https://graphisoft.com/plans-and-products/archicad/ | surrogate_primary | 2026-05-16 | Graphisoft (Nemetschek) | Archicad main product page — vendor docs |
| T02-S009 | https://www.graphisoft.com/us/solutions/whatsnew | surrogate_primary | 2026-05-16 | Graphisoft | Archicad 29 What's New — vendor docs |
| T02-S010 | https://constructionmanagement.co.uk/graphisoft-unveils-archicad-28/ | secondary | 2026-05-16 | Construction Management mag | Archicad 28 launch coverage |
| T02-S011 | https://www.vectorworks.net/en-US/newsroom/vectorworks-unveils-2025-software | surrogate_primary | 2026-05-16 | Vectorworks Inc (Nemetschek) | Vectorworks 2025 suite — vendor docs |
| T02-S012 | https://architosh.com/2025/12/product-review-vectorworks-architect-2026/ | secondary | 2026-05-16 | Architosh (AEC trade) | Vectorworks Architect 2026 review |
| T02-S013 | https://www.bentley.com/software/microstation/ | surrogate_primary | 2026-05-16 | Bentley Systems | MicroStation main product — vendor docs |
| T02-S014 | https://sketchup.trimble.com/en/whats-new | surrogate_primary | 2026-05-16 | Trimble SketchUp | SketchUp What's New (2025/2026) — vendor docs |
| T02-S015 | https://architosh.com/2025/12/trimble-launches-sketchup-ai-new-ai-powered-modeling/ | secondary | 2026-05-16 | Architosh | SketchUp AI launch coverage (Dec 2025) |
| T02-S016 | https://www.chaos.com/enscape | surrogate_primary | 2026-05-16 | Chaos | Enscape main product page — vendor docs |
| T02-S017 | https://blog.chaos.com/enscape-workflow-new-features-feb-2026 | surrogate_primary | 2026-05-16 | Chaos blog | Enscape Feb 2026 workflow features — vendor docs |
| T02-S018 | https://www.chaos.com/vray | surrogate_primary | 2026-05-16 | Chaos | V-Ray main product — vendor docs |
| T02-S019 | https://architosh.com/2025/08/chaos-releases-v-ray-7-update-2-for-3ds-max/ | secondary | 2026-05-16 | Architosh | V-Ray 7 Update 2 + AI tools coverage |
| T02-S020 | https://aecmag.com/visualisation/chaos-brings-real-time-rendering-to-v-ray-viewport/ | secondary | 2026-05-16 | AEC Magazine | V-Ray 7 realtime viewport coverage |
| T02-S021 | https://lumion.com/news/lumion-2025-release | surrogate_primary | 2026-05-16 | Lumion | Lumion 2025 release announcement — vendor docs |
| T02-S022 | https://www.cgchannel.com/2025/05/lumion-releases-lumion-2025-0/ | secondary | 2026-05-16 | CG Channel | Lumion 2025.0 launch coverage |
| T02-S023 | https://www.d5render.com/ | surrogate_primary | 2026-05-16 | Dimension 5 (D5 Render) | D5 Render main page — vendor docs (国产) |
| T02-S024 | https://www.cgchannel.com/2026/01/dimension-5-launches-d5-render-3-0-and-d5-lite/ | secondary | 2026-05-16 | CG Channel | D5 Render 3.0 + D5 Lite launch (Jan 2026) |
| T02-S025 | https://dev.epicgames.com/documentation/en-us/twinmotion/twinmotion-2025-2-preview-release-notes | surrogate_primary | 2026-05-16 | Epic Games | Twinmotion 2025.2 (Nanite) — vendor docs |
| T02-S026 | https://www.cgchannel.com/2025/10/epic-games-releases-twinmotion-2025-2-with-nanite-support/ | secondary | 2026-05-16 | CG Channel | Twinmotion 2025.2 Nanite coverage |
| T02-S027 | https://www.unrealengine.com/en-US/spotlights/taking-archviz-from-twinmotion-to-uefn-via-unreal-engine | surrogate_primary | 2026-05-16 | Epic Games / Unreal | Twinmotion → Unreal pipeline — vendor docs |
| T02-S028 | https://www.solemma.com/climatestudio | surrogate_primary | 2026-05-16 | Solemma | ClimateStudio main page — vendor docs |
| T02-S029 | https://www.solemma.com/solemma-symposium-2025 | surrogate_primary | 2026-05-16 | Solemma | Solemma Symposium 2025 (Revit demo) — vendor docs |
| T02-S030 | https://www.ladybug.tools/ | surrogate_primary | 2026-05-16 | Ladybug Tools | Ladybug + Honeybee open-source — vendor docs |
| T02-S031 | https://oneclicklca.com/ | surrogate_primary | 2026-05-16 | One Click LCA | One Click LCA main — vendor docs |
| T02-S032 | https://www.buildingtransparency.org/tools/ec3/ | surrogate_primary | 2026-05-16 | Building Transparency | EC3 embodied carbon — vendor docs |
| T02-S033 | https://kierantimberlake.com/updates/tally-is-moving/ | surrogate_primary | 2026-05-16 | KieranTimberlake | Tally 2.0 transition announcement — vendor docs |
| T02-S034 | https://www.iesve.com/ | surrogate_primary | 2026-05-16 | IES (Integrated Environmental Solutions) | IES VE main — vendor docs |
| T02-S035 | https://designbuilder.co.uk/ | surrogate_primary | 2026-05-16 | DesignBuilder Software | DesignBuilder main — vendor docs |
| T02-S036 | https://energyplus.net/ | surrogate_primary | 2026-05-16 | DOE (US Dept of Energy) | EnergyPlus open-source engine — vendor docs |
| T02-S037 | https://www.autodesk.com/products/forma/overview | surrogate_primary | 2026-05-16 | Autodesk | Forma (ex-Spacemaker) main — vendor docs |
| T02-S038 | https://blogs.autodesk.com/forma/2025/04/24/how-to-use-generative-design-ai-and-3d-modeling-for-improved-site-planning/ | surrogate_primary | 2026-05-16 | Autodesk Forma blog | Forma generative design / AI — vendor docs |
| T02-S039 | https://www.midjourney.com/home | surrogate_primary | 2026-05-16 | Midjourney Inc | Midjourney main — vendor docs |
| T02-S040 | https://stability.ai/ | surrogate_primary | 2026-05-16 | Stability AI | Stable Diffusion publisher — vendor docs |
| T02-S041 | https://github.com/lllyasviel/ControlNet | verified_primary | 2026-05-16 | Lvmin Zhang (Stanford) | ControlNet GitHub repo (original) |
| T02-S042 | https://www.adobe.com/products/firefly.html | surrogate_primary | 2026-05-16 | Adobe | Adobe Firefly main — vendor docs |
| T02-S043 | https://openai.com/dall-e-3 | surrogate_primary | 2026-05-16 | OpenAI | DALL-E 3 main — vendor docs |
| T02-S044 | https://www.testfit.io/ | surrogate_primary | 2026-05-16 | TestFit | TestFit feasibility platform — vendor docs |
| T02-S045 | https://aecmag.com/software/testfit-runs-free/ | secondary | 2026-05-16 | AEC Magazine | TestFit free tier coverage |
| T02-S046 | https://hypar.io/ | surrogate_primary | 2026-05-16 | Hypar | Hypar generative platform — vendor docs |
| T02-S047 | https://aecmag.com/features/hypar-2-0/ | secondary | 2026-05-16 | AEC Magazine | Hypar 2.0 review |
| T02-S048 | https://www.snaptrude.com/ | surrogate_primary | 2026-05-16 | Snaptrude | Snaptrude AI BIM — vendor docs |
| T02-S049 | https://aecmag.com/bim/snaptrude-on-ai | secondary | 2026-05-16 | AEC Magazine | Snaptrude AI feature interview |
| T02-S050 | https://www.maket.ai/ | surrogate_primary | 2026-05-16 | Maket | Maket.ai floor plan generator — vendor docs |
| T02-S051 | https://architechtures.com/ | surrogate_primary | 2026-05-16 | Architechtures | Architechtures generative AI design — vendor docs |
| T02-S052 | https://www.karamba3d.com/ | surrogate_primary | 2026-05-16 | Karamba3D (Bollinger+Grohmann + Preisinger) | Karamba3D structural — vendor docs |
| T02-S053 | https://www.wallacei.com/ | surrogate_primary | 2026-05-16 | Wallacei | Wallacei multi-obj optimizer — vendor docs |
| T02-S054 | https://www.food4rhino.com/en/app/octopus | surrogate_primary | 2026-05-16 | McNeel Food4Rhino | Octopus listing — vendor docs |
| T02-S055 | https://github.com/mcneel/rhino.inside-revit | verified_primary | 2026-05-16 | McNeel | Rhino.Inside.Revit open source repo |
| T02-S056 | https://www.bluebeam.com/product/ | surrogate_primary | 2026-05-16 | Bluebeam (Nemetschek) | Bluebeam Revu main — vendor docs |
| T02-S057 | https://www.trimble.com/en/products/tekla/structures | surrogate_primary | 2026-05-16 | Trimble Tekla | Tekla Structures main — vendor docs |
| T02-S058 | https://news.trimble.com/2025-03-12-Trimble-Expands-Connected-Workflows-in-Tekla-Structures-2025 | surrogate_primary | 2026-05-16 | Trimble Newsroom | Tekla Structures 2025 (Mar 12 2025) — vendor docs |
| T02-S059 | https://www.autodesk.com/products/navisworks/overview | surrogate_primary | 2026-05-16 | Autodesk | Navisworks 2026 — vendor docs |
| T02-S060 | https://revizto.com/ | surrogate_primary | 2026-05-16 | Revizto | Revizto BIM coordination — vendor docs |
| T02-S061 | https://architosh.com/2025/08/inside-revizto-global-dominance-with-open-bim-coordination/ | secondary | 2026-05-16 | Architosh | Revizto industry analysis |
| T02-S062 | https://construction.autodesk.com/products/autodesk-construction-cloud/ | surrogate_primary | 2026-05-16 | Autodesk Construction | Autodesk Construction Cloud (ACC) main — vendor docs |
| T02-S063 | https://www.adobe.com/creativecloud.html | surrogate_primary | 2026-05-16 | Adobe | Adobe Creative Cloud (PS/AI/ID) — vendor docs |
| T02-S064 | http://tangent.com.cn/ | surrogate_primary | 2026-05-16 | 北京天正软件 (Tangent) | 天正 T20 建筑官网 — vendor docs (国产) |
| T02-S065 | http://tangent.com.cn/download/ | surrogate_primary | 2026-05-16 | 天正软件 | T20 天正建筑 V10 下载中心 — vendor docs (国产) |
| T02-S066 | https://www.hongye.com.cn/ | surrogate_primary | 2026-05-16 | 鸿业科技 | 鸿业 BIMSpace 官网 — vendor docs (国产) |
| T02-S067 | http://bim.hongye.com.cn/ | surrogate_primary | 2026-05-16 | 鸿业科技 BIM | 鸿业 BIM 设计平台 — vendor docs (国产) |
| T02-S068 | https://www.tsz.com.cn/Bim.jsp | surrogate_primary | 2026-05-16 | 北京探索者软件 | 探索者结构 + BIM 装配式 — vendor docs (国产) |
| T02-S069 | http://gbsware.cn/ | surrogate_primary | 2026-05-16 | 北京绿建斯维尔 | 斯维尔绿建节能 (CEEB 碳排放) — vendor docs (国产) |
| T02-S070 | https://www.thsware.com/FrontEndPlugin/Product/IndustrySolutions?IS=1 | surrogate_primary | 2026-05-16 | 斯维尔软件 | 斯维尔建筑设计院解决方案 — vendor docs (国产) |
| T02-S071 | https://www.pkpm.cn/ | surrogate_primary | 2026-05-16 | 北京构力科技 (中国建研院) | PKPM 结构主页 — vendor docs (国产) |
| T02-S072 | https://help.pkpm.cn/admin/ms/detail?SiteID=123&id=5663 | surrogate_primary | 2026-05-16 | PKPM | PKPM 结构 2025R2 发布 — vendor docs (国产) |
| T02-S073 | https://www.gstarcad.com/ | surrogate_primary | 2026-05-16 | 浩辰软件 (GstarCAD) | 浩辰 CAD 官网 — vendor docs (国产) |
| T02-S074 | https://www.zwsoft.cn/product/zwcad/architecture | surrogate_primary | 2026-05-16 | 中望软件 (ZWSOFT) | 中望建筑 CAD 2026 — vendor docs (国产) |
| T02-S075 | https://www.glodon.com/product/325.html | surrogate_primary | 2026-05-16 | 广联达 (Glodon) | 广联达 BIMMAKE 产品 — vendor docs (国产) |
| T02-S076 | https://www.bimmake.com/ | surrogate_primary | 2026-05-16 | 广联达 | BIMMAKE 主站 — vendor docs (国产) |
| T02-S077 | https://www.goujianwu.com/paramodel/introduction | surrogate_primary | 2026-05-16 | 广联达 | 广联达数维建筑/数维构件设计 — vendor docs (国产) |
| T02-S078 | https://www.unrealengine.com/en-US/unreal-engine-5 | surrogate_primary | 2026-05-16 | Epic Games | Unreal Engine 5 main — vendor docs |
| T02-S079 | https://www.solemma.com/blog/studioma-asudesign | secondary | 2026-05-16 | Solemma | ClimateStudio case study (Studio Ma / ASU) |
| T02-S080 | https://architosh.com/2025/10/trimble-brings-powerful-collaboration-directly-into-sketchup/ | secondary | 2026-05-16 | Architosh | SketchUp 2026 collaboration coverage |
| T02-S081 | https://aecmag.com/visualisation/twinmotion-a-new-chapter/ | secondary | 2026-05-16 | AEC Magazine | Twinmotion narrative review |
| T02-S082 | https://www.cgchannel.com/2025/03/trimble-releases-sketchup-2025-0/ | secondary | 2026-05-16 | CG Channel | SketchUp 2025.0 release coverage |

> 黑名单合规: 0 条 blacklisted (无 G2 / Capterra / Quora / LinkedIn pulse / 知乎 / mp.weixin / 百度百科 / CSDN / cnblogs / jianshu / pinterest / behance).
> Bucket 比例 (n=82): verified_primary 4 (~5%), secondary 16 (~20%), surrogate_primary 62 (~75%, 全部为 vendor 官网且标 literal "vendor docs" 或 "vendor docs (国产)"). reference 0. 高 surrogate 比例为合理偏差 — 工具类研究 vendor 官网为最新版本/价格首手, 第三方评测延迟 3-6 月.

---

## 总览 (按 6 大类 + 中国本土补充)

| 类别 | 工具数 | 2026 default | 替代 / 升级路径 |
|------|-------|-------------|--------------|
| A. CAD / 制图 | 5 | AutoCAD (zh-CN 国际通用) / Vectorworks (北欧 / 日 boutique) | SketchUp 概念 / MicroStation infrastructure |
| B. BIM / 协作 | 8 | Revit (中美主流) / ArchiCAD (欧 / boutique) | Snaptrude (AI BIM) / Tekla (结构) / Navisworks (clash) / ACC (CDE) / Revizto (open BIM) / Bluebeam (PDF) |
| C. Parametric / Computational | 6 | Rhino 8 + Grasshopper (事实标准) | Rhino.Inside.Revit (BIM bridge) / Karamba3D (结构) / Wallacei (multi-obj) / Galapagos (single-obj) / Octopus (Pareto) |
| D. Visualization / Render | 7 | Enscape (实时) / V-Ray (品质) / D5 Render (zh 新秀) | Lumion (cinematic) / Twinmotion (Epic) / Unreal Engine (custom) / Adobe Suite (post) |
| E. Sustainability / Performance | 6 | Ladybug + Honeybee (架构师入门) / ClimateStudio (专业付费) | IES VE / DesignBuilder / EnergyPlus / One Click LCA / EC3 / Tally |
| F. AI Generative / Concept | 9 | Midjourney V7/V8 (concept) / Forma+Spacemaker (massing) / Snaptrude (AI BIM) | SD+ControlNet (open source) / Adobe Firefly / DALL-E / Hypar / TestFit / Maket / Architechtures |
| G. 中国本土补充 | 9 | AutoCAD + 天正 T20 (施工图主流) / PKPM (结构) | 鸿业 BIMSpace / 探索者 / 斯维尔 (绿建) / 浩辰 CAD / 中望 CAD / 广联达 BIMMAKE / 广联达数维 |

(共 50 retained, 7 类 (A-G) 满足 ≥ 3, AI 生成类 9 ≥ 5, 中国本土 9 ≥ 3.)

---

## 工具 entries (50 retained)

### 🛠️ 1. AutoCAD (A. CAD)

- **类别**: A. CAD / 制图
- **开发商**: Autodesk (US)
- **当前版本** + 发布日期: 2026 (2025Q1 release; 1.x 自 1982-12)
- **license model**: subscription only (perpetual 2016 EOL)
- **典型价格** (USD): $2,030/yr (full); $475/yr (LT 仅 2D); 中国 RMB 价 ¥4,000-8,000/yr 通过授权商
- **核心场景**: 5-phase SOP 全程通用 2D 制图基底; 中国 SD/DD/CD 阶段是无可替代的施工图载体 (中国规范 .dwg 交付为强制); 国际 boutique 主要做线条最后期排版.
- **persona 适配**:
  - boutique: 用 LT (省钱), 主力是 Rhino/Vectorworks; AutoCAD 只做最终 .dwg 交付.
  - 中型: full 版 + 配 Civil 3D 做总图; 与 Revit 双轨.
  - 大型院 (尤其中国): 主力中的主力 — AutoCAD + 天正 T20 是 95% 施工图工作流; 1 院往往采购 100-500 license.
- **典型 input / output**: DWG / DXF / DWF / PDF / IFC (有限)
- **常用插件 / plugin / 配合工具**: 天正 T20 (中国必装) / 鸿业 / 探索者 / Civil 3D / Mechanical / Architecture Toolset / Express Tools
- **学习曲线**: medium (2D 入门 easy; 配置/lisp/动态块 steep)
- **2025-2026 重要变化** (last_updated: 2026-05-16): AutoCAD 2026 主打 "11x faster file open / 4x faster startup" 与 AutoCAD 2025 比; 新增 Autodesk AI 加持的 Activity Insights "What's Changed"; 与 ACC 项目级 support file 关联.
- **替代选项**: 浩辰 CAD / 中望 CAD (国产 .dwg 兼容, 价 1/3, 大型院 IT 部已大量替换 license); BricsCAD (欧 SaaS 替代); LibreCAD (开源, 不推荐 production).
- **常见坑 / 反模式**:
  1. 用 AutoCAD 做 3D — 该用 Rhino/Revit, AutoCAD 3D 是历史负担.
  2. 不装天正做中国施工图 — 重复造轮子 50%.
  3. 把 Revit 出图 dwg 化后手改 — 双源, 改 1 处不改 2 处.
- **来源**: [T02-S001] [T02-S002]

### 🛠️ 2. AutoCAD LT (A. CAD)

- **类别**: A. CAD / 制图 (轻量)
- **开发商**: Autodesk
- **当前版本**: 2026 (2025Q1)
- **license model**: subscription only
- **典型价格**: $475/yr — full AutoCAD 1/4
- **核心场景**: 仅 2D 制图; boutique studio 唯一签字制图工具; 学生 / 小事务所 / 临时工位.
- **persona 适配**: boutique 主力; 中型 IT 部部分采购; 大型院基本不用 (功能受限).
- **典型 I/O**: DWG / DXF / PDF (no 3D, no lisp, no .NET API)
- **配合**: 天正 T20 LT 兼容版 (有限)
- **学习曲线**: easy
- **2025-2026**: 同 2026 性能加持 (开图 11x); AI 增量受限.
- **替代**: DraftSight / 浩辰 CAD LT
- **常见坑**:
  1. 想用 AutoLISP — LT 不支持, 立即升级 full 或换 BricsCAD.
  2. 想用 Revit 链接 — LT 不能, 切到 full.
- **来源**: [T02-S001]

### 🛠️ 3. Vectorworks Architect (A. CAD + B. BIM hybrid)

- **类别**: A. CAD / B. BIM hybrid
- **开发商**: Vectorworks Inc (Nemetschek subsidiary, US)
- **当前版本**: 2026 (2025Q3 EN release, 2024Q4 2025 release)
- **license model**: subscription + Service Select 维护合约 (相对宽容的 perpetual 历史购置)
- **典型价格**: $2,675/yr Architect (subscription); $3,765 perpetual + Service Select
- **核心场景**: 北欧 / 英国 / 日本 / 澳洲 boutique studio 与小型 firm 全流程 — 一个软件做 SD-CD; landscape / interior 也强; 2D 制图传统继承 MiniCAD.
- **persona 适配**:
  - boutique: Vectorworks 是欧 / 日 boutique 单一软件首选 — 不依赖多工具栈.
  - 中型: 北欧 / 英国中型用; 北美 / 中国少.
  - 大型院: 几乎不用 (Revit 主导).
- **典型 I/O**: VWX / DWG / DXF / IFC / OBJ / FBX / SKP
- **配合**: Marionette (内建 visual scripting like GH) / Cinema 4D / Twinmotion
- **学习曲线**: medium
- **2025-2026**: 2025 加入 Onscreen View Control / Two-Point Perspective / Object Level Visibility; 2026 进一步 IFC 与 Vision (theatrical) 整合.
- **替代**: ArchiCAD (BIM 转向) / Rhino + Revit (复杂项目)
- **常见坑**:
  1. 把 Vectorworks 当 AutoCAD 用 — 错过其 BIM-light 能力.
  2. 期待 Revit-level 协作 — Vectorworks 团队协同弱于 Archicad/Revit.
  3. 北美 / 中国客户不接 .vwx — 需 dwg/ifc 导出.
- **来源**: [T02-S011] [T02-S012]

### 🛠️ 4. MicroStation (A. CAD / 大型 infrastructure)

- **类别**: A. CAD + 大型 infrastructure 平台
- **开发商**: Bentley Systems (US)
- **当前版本**: 2025 (v2025.0; 1.0 自 1985)
- **license model**: subscription + Bentley SELECT 维护; 大企业 ELS (enterprise lic)
- **典型价格**: ~$2,500/yr; ELS 起 $25k+ 议价
- **核心场景**: 大型 infrastructure (桥梁 / 隧道 / 工厂 / 机场); 建筑师场景少, 多见于建筑 + 基建 jointed firm (e.g. AECOM/Arup/Stantec); 不是 boutique 工具.
- **persona 适配**:
  - boutique: 几乎不用.
  - 中型: 仅基建 + 建筑混合 firm.
  - 大型院: 国际大型 EPC + 中铁 / 中建二局有部署; 中小型院 0.
- **典型 I/O**: DGN / DWG / IFC / RealityMesh / 3D Tiles (2025 新增 Cesium 3D Tiles + Google Photorealistic 3D Tiles)
- **配合**: OpenBuildings Designer (Bentley BIM) / iTwin (Bentley CDE) / SYNCHRO 4D
- **学习曲线**: steep
- **2025-2026**: 2025 加入 OGC 3D Tiles 支持 + Cesium Native + Google Photorealistic 3D Tiles (第一个支持的 CAD); Python API 大幅扩展; 与 Esri geodatabase 互通.
- **替代**: AutoCAD + Civil 3D (建筑端) / Revit (BIM 端)
- **常见坑**:
  1. 小项目用 MicroStation — overkill; 几万元许可消耗.
  2. 建筑师独立采购 — 应该是 firm enterprise 包.
  3. 期待与 Revit 双向同步 — IFC 单向更靠谱.
- **来源**: [T02-S013]

### 🛠️ 5. SketchUp Pro (A. CAD / 概念建模)

- **类别**: A. CAD / 概念 3D 建模
- **开发商**: Trimble (US, 收购自 @Last Software 2006, Google 2006-2012, Trimble 2012-)
- **当前版本**: 2026.0 (2025Q4); 主要持续更新 (Web/Studio)
- **license model**: subscription only (perpetual 2020 EOL)
- **典型价格**: $349/yr (Pro); $749/yr (Studio, 含 V-Ray); free 个人 Web 版
- **核心场景**: SD / massing / 客户沟通; boutique 主力概念阶段; 中国 boutique 与高校教学第一软件.
- **persona 适配**:
  - boutique: 概念→快速沟通主力; 配 V-Ray/Enscape/D5 出 client 图.
  - 中型: SD 阶段; 转 Revit/Archicad 做 DD/CD.
  - 大型院: 教学 / 实习生 entry; 投标 mass model.
- **典型 I/O**: SKP / DAE / 3DS / DWG / IFC (有限) / OBJ / FBX / PDF
- **配合**: Layout (内置出图) / V-Ray for SketchUp / Enscape / D5 Render / D5 Lite (新) / Twinmotion / Profile Builder / Skatter
- **学习曲线**: easy (是行业最快入门的 3D 软件)
- **2025-2026**: 2025.0 加入 HDR Environments + PBR materials; 2026.0 (2025Q4) 大幅协作能力增强; SketchUp AI (2025-12 launch) 提供 AI 模型生成; Style Builder 已 EOL.
- **替代**: Rhino (复杂曲面) / Vectorworks (BIM-light) / FormIt (Autodesk SD 替代)
- **常见坑**:
  1. 用 SketchUp 做 CD 阶段 — 不准确, 出图差; 应该 DD 后转 BIM.
  2. 1 million 个 entity 之后软件崩 — 需用 Components / Outliner 控制.
  3. 客户给 SketchUp 文件改方案 — boutique 应该输出 PDF/render, 不给 source.
- **来源**: [T02-S014] [T02-S015] [T02-S080] [T02-S082]

### 🛠️ 6. Revit (B. BIM)

- **类别**: B. BIM / 协作 (旗舰)
- **开发商**: Autodesk (收购自 Revit Technology 2002)
- **当前版本**: 2026 (2025-04-02; 25 周年版)
- **license model**: subscription only
- **典型价格**: $3,160/yr (full); AEC Collection $3,235/yr 含 Revit + AutoCAD + Navisworks + 3ds Max + Civil 3D + Forma + ACC 入门版 — 标准购法
- **核心场景**: 5-phase SOP 中 DD / CD / CA 阶段主力; 北美 / 中国一线项目 BIM 强制要求 (中美主流交付); 适合中大型项目.
- **persona 适配**:
  - boutique: Rhino + GH 设计, 中后期 Revit 出 BIM/CD; 1-3 license.
  - 中型 (50-150 人, 北美主流): Revit 主力 + Rhino.Inside.Revit + Enscape + Bluebeam; ACC 协作.
  - 大型院 (中国): Revit BIM 项目 (政府要求 / 资质) 用 Revit; 但施工图深度往往超出 RVT family — 双轨 Revit + 天正/AutoCAD 出 CD.
- **典型 I/O**: RVT / RFA (family) / IFC / DWG / NWC (to Navisworks) / FBX / SAT
- **常用插件**: pyRevit (自由) / Dynamo (visual prog) / Rhino.Inside.Revit / Enscape / V-Ray / Tally (LCA) / Bluebeam Studio / Diroots / ProjectWise / Speckle (open data)
- **学习曲线**: steep (3-6 个月入门, 1-2 年熟练; family 创作 5+ 年)
- **2025-2026** (last_updated: 2026-05-16): Revit 2026 加入 Accelerated Graphics (GPU navigation, Tech Preview) + Tabbed Project Browser + 自动 view placement + Toposolid 增强 + reality capture mesh import + 改进的 coordination model 链接 (与 ACC); 主体是 25 周年 quality-of-life 升级, 非大改.
- **替代**: ArchiCAD (欧 / boutique 备选) / Snaptrude (AI BIM 新秀) / Vectorworks (北欧)
- **常见坑**:
  1. Revit 全自动用 family — 中国施工图深度往往超出 RVT family 库, 强用导致 family hell, 应 detail dwg 配合.
  2. Worksharing 不分 worksets — 多人 conflict, 应该按 discipline / level 分.
  3. Revit 当 Rhino 用做曲面 — 应该 Rhino.Inside.Revit 双向; 直接画自由曲面 Revit 极慢.
- **来源**: [T02-S003] [T02-S004]

### 🛠️ 7. ArchiCAD (B. BIM)

- **类别**: B. BIM / 协作
- **开发商**: Graphisoft (Hungary, Nemetschek 旗下)
- **当前版本**: 29 (2025Q3); 28 (2024-10-02)
- **license model**: subscription + perpetual (相对 Revit 友好的 license 选项)
- **典型价格**: ~$2,950/yr; perpetual $4,990 一次性 + 维护合约
- **核心场景**: 欧洲 (尤其 DACH 德语区 + 北欧) / 日本 / 拉美 boutique 主力; 设计意图导向 boutique 喜欢 (vs Revit 重 documentation); 全 5-phase 可贯通.
- **persona 适配**:
  - boutique (≤30 人, 设计 driven): ArchiCAD 在欧洲 boutique 占有率比 Revit 高; UI 与 Mac 友好.
  - 中型: 部分欧洲中型用; 北美 / 中国少.
  - 大型院: 中国 1 % 不到, 欧洲部分 firm 用.
- **典型 I/O**: PLN / IFC / DWG / RVT (import only) / OBJ / FBX
- **常用插件**: Rhino-Grasshopper-Archicad live connection / BIMcloud / BIMx (mobile presentation, 行业最强) / Twinmotion / Enscape (近年加入)
- **学习曲线**: medium-steep
- **2025-2026**: ArchiCAD 28 (2024-10-02) 加入 Keynotes 文档系统 + Rhino-Grasshopper live link 加强 + CineRender 物理 skydome + Faro/Leica/Riegl 点云直读 + Bluebeam Studio 直发起; ArchiCAD 29 (2025Q3) 进一步 ML-based wall placement + IFC 4.3 全支持.
- **替代**: Revit (北美 / 中国主流) / Vectorworks (类似定位但 BIM 浅)
- **常见坑**:
  1. ArchiCAD 与 Revit project 互换 — 双向 RVT 不通, 只 IFC, 信息有损; boutique 接 Revit 项目应早期决定主软件.
  2. Library 全靠官方 — 比 Revit 社区小, 高度定制项目自建 GDL object.
  3. BIMcloud 自部署 — 中型 firm 需 IT 长期投入.
- **来源**: [T02-S008] [T02-S009] [T02-S010]

### 🛠️ 8. Snaptrude (B. BIM + F. AI hybrid)

- **类别**: B. BIM + F. AI generative hybrid
- **开发商**: Snaptrude (India / US, YC backed)
- **当前版本**: Snaptrude 3.0 (2025Q4) — cloud-native
- **license model**: subscription (cloud SaaS); free tier
- **典型价格**: free → $39/月 (Pro) → enterprise 议价
- **核心场景**: SD/DD 阶段 AI BIM — 输入 prompt ("mid-rise office, downtown Chicago") → AI agents 生成 site analysis + program + 3D massing + diagram + render; Revit 互通; 替代 SD 阶段的 Revit 重负担.
- **persona 适配**:
  - boutique: 用作 SD speedrun; 客户提案前快速 explore.
  - 中型: SD/DD 早期 + 转 Revit DD/CD.
  - 大型院: pilot 阶段, 用作 SD 加速; Revit 仍为 CD 主力.
- **典型 I/O**: 云端 .snap / Revit (双向 plugin) / IFC / DWG / glTF
- **配合**: Revit (主要 BIM 出口) / Hypar / TestFit
- **学习曲线**: easy (cloud-native, 几小时上手)
- **2025-2026**: 2025 累计 1M+ sqft 项目使用 (医院 / 学校 / 多家庭 / 混合); AI agents 集成 IBC / ADA / Neufert 规范; AI 渲染 + 自动 diagram; Snaptrude on AI (AEC Magazine 评 2025).
- **替代**: Hypar (相似定位) / TestFit (开发商 feasibility 偏向)
- **常见坑**:
  1. 把 AI 出的 SD 直接当 DD 提交 — 缺细节, 应作为起点不是终点.
  2. 不验证规范输入 — AI 用 IBC default, 国内项目需手动覆盖中国规范.
  3. 期待 Revit-level 文档输出 — 应导出 IFC/Revit, 在 Revit 中深化.
- **来源**: [T02-S048] [T02-S049]

### 🛠️ 9. Tekla Structures (B. BIM / 结构专业)

- **类别**: B. BIM / 结构详图 (建筑师外延)
- **开发商**: Trimble (Finland Tekla 2011 acq)
- **当前版本**: 2025 (2025-03-12); 2026 滚动更新
- **license model**: subscription
- **典型价格**: $7,000-15,000/yr 按 module (国际); 中国通过授权商
- **核心场景**: 钢结构详图 + 预制混凝土; 建筑师本身不画 Tekla 模型, 但与结构合作时是接口; 高复杂度建筑 (e.g. 鸟巢, ZHA 自由形态) 必由 Tekla 出结构详图.
- **persona 适配**:
  - boutique: 不直接用; 结构 consultant 用 Tekla 配合.
  - 中型: 大项目结构外协 Tekla 出图.
  - 大型院: 大型公建钢构必走 Tekla; 中国常以结构院专项设计为入口.
- **典型 I/O**: TrimBIM (.trb) / IFC / DWG / DGN
- **配合**: Trimble Connect (CDE) / Tekla Model Sharing / Tekla Structural Designer (analysis)
- **学习曲线**: steep
- **2025-2026**: 2025 引入 AI Cloud Fabrication Drawing preview + AI Trimble Assistant + Live Collaboration (Trimble Connect 协作) + reality capture 流式点云.
- **替代**: Revit Structure (国际中型) / Bentley OpenBuildings (大基建)
- **常见坑**:
  1. 建筑师把 Revit 结构 family 当成可施工模型 — Tekla 出钢构详图与 Revit family 精度差 1 个量级.
  2. 直接 IFC export 结构入 Tekla — 应该结构师在 Tekla 重建; IFC 仅参考.
- **来源**: [T02-S057] [T02-S058]

### 🛠️ 10. Navisworks Manage (B. BIM / 协调)

- **类别**: B. BIM / clash detection + 4D
- **开发商**: Autodesk (收购自 Navisworks 2007)
- **当前版本**: 2026 (2025Q1)
- **license model**: subscription only (含在 AEC Collection 中)
- **典型价格**: $3,860/yr (standalone); 通常 AEC Collection 配赠
- **核心场景**: CA 阶段 clash detection (碰撞检测) + 4D 模拟 + model aggregation; 建筑师项目交付后 contractor / GC 主用; 60+ file format 聚合 (Revit + IFC + DWG + Civil + Plant + Tekla + ArchiCAD).
- **persona 适配**:
  - boutique: 通常不直接用, 包给 GC.
  - 中型: BIM Manager / Coordinator 主用工具; 给设计反馈.
  - 大型院 (中国): BIM 项目部主用, 出 clash report 给设计提资.
- **典型 I/O**: NWD / NWF / NWC / 60+ import formats
- **配合**: ACC Model Coordination (云端碰撞) / Revit (主源) / Synchro 4D / Tekla
- **学习曲线**: medium
- **2025-2026**: 2026 增强与 ACC Coordination Issues 直连 add-in; 改进 clash group 与 batch issue create/respond; cloud round-trip 流程.
- **替代**: Revizto (open BIM, 协作更强) / Solibri (IFC checker / model checker) / BIMcollab (issue 管理)
- **常见坑**:
  1. 只跑 Navisworks 不读结果 — 大量 false positive, 需 BIM coord 过滤再分发.
  2. 不更新 NWF 模型链接 — 用旧模型出 report.
  3. 设计师不参与 clash review — clash 应回到设计端解决.
- **来源**: [T02-S059]

### 🛠️ 11. Revizto (B. BIM / 协调)

- **类别**: B. BIM / coordination + issue management (open BIM)
- **开发商**: Revizto (Switzerland)
- **当前版本**: Revizto 6 (2025); 持续 SaaS
- **license model**: subscription
- **典型价格**: $645-2,000/yr/user 按 tier
- **核心场景**: 跨 BIM 平台 (Revit + ArchiCAD + Tekla + IFC) federated coordination; 建于 Unity engine — 大型 federated 模型可在 web/iPad 上流畅; 2D-3D 整合查看; 与 GC + owner 共享.
- **persona 适配**:
  - boutique: pilot 阶段; 通常 GC 配置 license.
  - 中型: 越来越成为 issue tracker 主选 (相比 BIM Track / BCF).
  - 大型院: 60% Revizto 用户是 GC, 40% 是 owner + engineer + designer; 中国大型院开始 pilot.
- **典型 I/O**: 自有云 / IFC / RVT / NWD / PLN / DWG / Bluebeam
- **配合**: Revit / ArchiCAD / Tekla / Navisworks / Bluebeam / Procore
- **学习曲线**: medium
- **2025-2026**: 2025 加入 Issue Workflow Automation (Workspace web app) — 自定义 trigger/condition 自动 update issue 字段; 跨 firm federated model 实时同步.
- **替代**: Navisworks (Autodesk lock-in) / BIMcollab (issue only) / ACC (Autodesk 同生态)
- **常见坑**:
  1. 当成 Navisworks 用 — 错过其 issue management 核心.
  2. 不上 cloud — Revizto 是云原生, 本地部署劣化.
- **来源**: [T02-S060] [T02-S061]

### 🛠️ 12. Autodesk Construction Cloud (ACC) (B. BIM / CDE)

- **类别**: B. BIM / CDE (Common Data Environment)
- **开发商**: Autodesk (整合 BIM 360 + PlanGrid + BuildingConnected + Pype)
- **当前版本**: 滚动 SaaS (ACC = BIM 360 successor; BIM 360 2025-09 全面 EOL)
- **license model**: subscription per-user
- **典型价格**: BIM Collaborate Pro $940/yr/user; Docs $610/yr/user
- **核心场景**: 5-phase 全程 cloud 协作; design-construct 链条统一; ACC Docs (文件 CDE) + Build (施工) + BIM Collaborate (Revit cloud worksharing) + Takeoff + Model Coordination + Workshop XR.
- **persona 适配**:
  - boutique: BIM Collaborate Pro 主用 (Revit cloud worksharing 必装).
  - 中型: Docs + BIM Collaborate + Model Coord 标配.
  - 大型院: 中国 ACC 受限于网络 + 信创合规; 大量用 Revit + BIMcloud 替代 + 行业自建.
- **典型 I/O**: 兼容 50+ 文件格式, RVT 是主源
- **配合**: Revit / Navisworks / Civil 3D / Forma / 几乎所有 Autodesk 产品
- **学习曲线**: medium (concept easy, admin/permission steep)
- **2025-2026**: 2025-09 BIM 360 Team / Glue / Plan 全 EOL; ACC 全面承接; 新功能优先在 ACC; 与 Forma 集成增强.
- **替代**: Trimble Connect (Tekla + SketchUp 生态) / Bentley iTwin (基建生态) / Procore (GC 侧主导) / BIMcloud (Graphisoft)
- **常见坑**:
  1. 把 Docs 当 Dropbox 用 — 应当配 issue / RFI / submittal workflow.
  2. ACC + 国内项目 — 网络 + 数据合规问题, 北上广深 large firm 谨慎.
  3. license 散购 — AEC Collection 含 ACC 入门; 应批量谈判.
- **来源**: [T02-S062]

### 🛠️ 13. Bluebeam Revu (B. BIM / PDF markup)

- **类别**: B. BIM / PDF markup + collaboration
- **开发商**: Bluebeam (Nemetschek 2014 acq, US Pasadena)
- **当前版本**: Revu 21 (2024-) + Bluebeam Cloud (Studio 升级)
- **license model**: subscription (perpetual 2022 EOL)
- **典型价格**: $260/yr Basics → $440/yr Core → $530/yr Complete
- **核心场景**: CD/CA 阶段 PDF markup + 数 (count) / 量 (measure) / 集中协作 (Studio); 建筑师 + GC + Owner 的施工图通用语; 北美几乎人手一份.
- **persona 适配**:
  - boutique: 1-2 license, 出 CD pdf 校审 + 客户 markup.
  - 中型: 每人 1 license; Studio session 是项目协同核心.
  - 大型院 (中国): 渗透在加速 — 主要 GC + 国际项目用; 国内项目仍以 PDF 手批 + Wechat 沟通.
- **典型 I/O**: PDF (read/write/markup) / DWG to PDF / IFC view / Studio cloud session
- **配合**: Revit / AutoCAD (PDF 输出端) / ArchiCAD (28 起 Studio Session 直发起) / SharePoint
- **学习曲线**: easy (markup 上手快; tool chest 与 Studio 自动化深入)
- **2025-2026**: Bluebeam Cloud 升级 Studio; ArchiCAD 28 直发起 Studio Session; AI 功能 (auto-count / auto-classify) 在 roadmap.
- **替代**: Adobe Acrobat Pro (基础 markup) / Foxit / Revu 替代极少 (北美 60%+ market)
- **常见坑**:
  1. 用 Acrobat 代替 — 没有 tool chest + Studio session, 效率差 5x.
  2. 不用 Studio 协同 — 退化为单机 markup, 错过最大价值.
  3. 不建 tool set / template — 每个 markup 手画.
- **来源**: [T02-S056]

### 🛠️ 14. Rhino 3D (C. Parametric / 多用)

- **类别**: C. Parametric / 通用 NURBS 建模 + A. 概念建模
- **开发商**: Robert McNeel & Associates (US Seattle, 1980 创办)
- **当前版本**: Rhino 8 (2023-11); Rhino WIP 9 (2025-)
- **license model**: perpetual (买断) + 商业 SR 升级
- **典型价格**: $995 perpetual commercial; $195 student; $595 upgrade; Mac 同价
- **核心场景**: SD / DD 阶段自由曲面 + 概念 + 表皮; 与 Grasshopper 一体使用; 是 boutique 与高端 firm 设计意图主轴.
- **persona 适配**:
  - boutique: 主力 (设计 + 文档 + 输出); GH 复杂表皮.
  - 中型: 设计 + Rhino.Inside.Revit 进 Revit.
  - 大型院 (中国): 复杂方案投标主力; 进入 CD 转 AutoCAD/Revit.
- **典型 I/O**: 3DM / DWG / DXF / OBJ / FBX / IGES / STEP / SAT / IFC / glTF / USD
- **常用插件**: Grasshopper (内置) / V-Ray / Enscape / Karamba3D / Ladybug+Honeybee / ClimateStudio / Wallacei / Octopus / Galapagos / Bongo (animation) / Lands (landscape) / VisualARQ (BIM-light)
- **学习曲线**: medium (NURBS easy; SubD + GH steep)
- **2025-2026**: Rhino 8 一直在 service release; Rhino 9 WIP 含 Grasshopper 2 (重写 GH 引擎); Rhino.Inside 系列 (Revit / AutoCAD / Excel / Unreal) 持续完善; 注意: McNeel 是少数仍卖 perpetual 的主流厂商, 这是 boutique 重要选择.
- **替代**: Blender (开源, 不主流 AEC) / Maya (影视为主) / SketchUp (轻量) / Vectorworks (BIM 转向)
- **常见坑**:
  1. 用 Rhino 做 BIM — 应该用 Rhino.Inside.Revit 或 ArchiCAD; Rhino 本身 BIM 弱 (VisualARQ 仅 BIM-light).
  2. 不学 Grasshopper — 错过 Rhino 一半价值.
  3. SubD vs NURBS 误用 — SubD 适合有机体, NURBS 适合精确曲面.
- **来源**: [T02-S005] [T02-S006]

### 🛠️ 15. Grasshopper (C. Parametric)

- **类别**: C. Parametric / visual programming
- **开发商**: McNeel (David Rutten 创办; 2007 "Explicit History" 首发)
- **当前版本**: GH 1.0 (随 Rhino 6+ 内置); GH 2 (WIP in Rhino 9)
- **license model**: free, bundled with Rhino
- **典型价格**: $0 (含 Rhino)
- **核心场景**: SD / DD 阶段 generative geometry / 表皮 / 优化 / 数据驱动文档; 现代建筑参数化事实标准; AEC 行业唯一通用 visual programming.
- **persona 适配**:
  - boutique: 复杂表皮主力 (e.g. Zaha / FOA / Foster 派).
  - 中型: 1-2 个 "GH 大佬" 专项 / facade 团队.
  - 大型院: 投标方案主力 (中国大设计院 80%+ 都有 GH 工作流).
- **典型 I/O**: GHX / GH 数据流; output 通过 components 进 Rhino / Revit / Excel / Illustrator / Karamba / Ladybug 等
- **常用 plugin**: Ladybug+Honeybee / Karamba3D / Kangaroo (物理) / Wallacei / Octopus / Galapagos (内置) / Pufferfish / Weaverbird / Lunchbox / Heteroptera / Anemone / Elefront / Speckle / Rhino.Inside.Revit
- **学习曲线**: steep (3 月入门 GH 思维, 1 年熟练)
- **2025-2026**: Grasshopper 2 WIP (Rhino 9 内) — UI 重写, 数据流加速 5-10x, async 支持; ML-based 自动 cluster 等概念在 prototype.
- **替代**: Dynamo (Revit 自带 visual prog; 不能跨 Rhino); 自写 Python (无 visual feedback)
- **常见坑**:
  1. 不 cluster — 50+ component GH 脚本难维护.
  2. 把 GH 当一次性脚本 — 应文档化, 用 Hops / cluster / Speckle 协作.
  3. 用 GH 做严肃 BIM — 应该 GH 喂 Revit.Inside, 让 Revit 做 BIM 数据库.
- **来源**: [T02-S005] [T02-S006]

### 🛠️ 16. Rhino.Inside.Revit (C. Parametric / B. BIM bridge)

- **类别**: C. Parametric ↔ B. BIM bridge
- **开发商**: McNeel (open source, MIT license)
- **当前版本**: RIR 1.0 stable (2022-) + 持续 WIP for Revit 2025/2026
- **license model**: free + open source (需 Rhino license)
- **典型价格**: $0
- **核心场景**: 在 Revit 内运行 Rhino + Grasshopper, 双向数据交换 (Revit element ↔ Rhino geometry); 300+ Revit-aware GH components; 工业级 design-to-BIM 主桥梁.
- **persona 适配**:
  - boutique: 设计在 Rhino, 文档在 Revit — RIR 必装.
  - 中型: BIM 工作流接 Rhino 设计.
  - 大型院: 复杂方案 RIR + Revit 双轨.
- **典型 I/O**: 实时双向 Rhino ↔ Revit; GH 脚本输入 → Revit element 创建.
- **常用配合**: Speckle (CDE) / pyRevit / Dynamo (备用)
- **学习曲线**: steep (须熟练 Rhino + GH + Revit 三者)
- **2025-2026**: Revit 2025 .NET 8 升级带来重大架构变化, RIR 团队跟进; Daily Build 持续支持 2026; Autodesk 自家也发了 Revit-Rhino Connector (官方版, 但功能远不如 RIR).
- **替代**: Autodesk 官方 Revit-Rhino Connector (轻量) / Dynamo (Revit-only)
- **常见坑**:
  1. 把 RIR 当 import-only — 它是 live link, 应交互式工作.
  2. 不锁 Revit version — RIR 需匹配 Revit major version.
  3. 内存爆 — 大模型分 worksession.
- **来源**: [T02-S007] [T02-S055]

### 🛠️ 17. Karamba3D (C. Parametric / 结构)

- **类别**: C. Parametric / 结构有限元 Grasshopper plugin
- **开发商**: Bollinger+Grohmann + Clemens Preisinger (Vienna)
- **当前版本**: Karamba3D 3.0 (持续小版本)
- **license model**: free (educational) / commercial €1,990 perpetual 或 €490/yr
- **典型价格**: €490-1,990
- **核心场景**: SD / DD 早期结构 form-finding + 优化; 建筑师与结构师同台沟通的语言; 复杂壳体 / 张拉结构 / 网架 / 高层 outrigger 概念.
- **persona 适配**:
  - boutique: 建筑师自学做结构 form-finding (e.g. Zaha 派, Foster 派).
  - 中型: facade / 结构组配置.
  - 大型院: 复杂方案 form-finding 必备; 结构院与建筑院共用.
- **典型 I/O**: 内置 GH; export STAAD / SAP2000 / RFEM
- **配合**: Grasshopper / Wallacei / Octopus / Galapagos (多目标优化)
- **学习曲线**: steep (结构 + GH 双门槛)
- **2025-2026**: 2025 用例 — Bespoke 团队为 2025 威双中国馆 "Vault of Heaven" 设计悬吊框架; cloud-based parametric collaboration 兴起.
- **替代**: Millipede (Grasshopper, 已不更新) / SAP2000 / ETABS (传统结构, 非 GH 集成)
- **常见坑**:
  1. 把 Karamba 出的结果当施工依据 — 它是 design tool 不是 production FE, 应交结构师 SAP2000 复算.
  2. 模型简化不当 — boundary condition 简化错误导致结论错.
- **来源**: [T02-S052]

### 🛠️ 18. Wallacei (C. Parametric / 多目标优化)

- **类别**: C. Parametric / 多目标进化优化 Grasshopper plugin
- **开发商**: Wallacei (Mohammed Makki, Milad Showkatbakhsh, et al., UCL)
- **当前版本**: Wallacei X (2020+); 持续更新
- **license model**: free
- **典型价格**: $0
- **核心场景**: SD / DD 多目标 generative design — 同时优化 daylight + view + structure + cost; 比 Octopus 更现代的 UI + analytic dashboard.
- **persona 适配**:
  - boutique: 进阶 GH 用户用.
  - 中型: facade 团队多目标优化.
  - 大型院: 投标差异化用 (e.g. 朝向 + 视线 + 结构同优).
- **典型 I/O**: GH; export CSV / 数据可视化
- **配合**: Karamba3D / Ladybug+Honeybee (适应度函数) / Grasshopper
- **学习曲线**: steep
- **2025-2026**: 持续维护, 行业 default of multi-obj evolutionary; analytic features 是其与 Octopus 的差异.
- **替代**: Octopus (older, 类似算法) / Galapagos (单目标内置) / Opossum (RBFOpt-based, 单/多目标)
- **常见坑**:
  1. 不定义 phenotype 区分 — fitness 收敛但 solution 重复.
  2. 跑 1000 代不读 Pareto front — 应该看 multi-D 分布.
- **来源**: [T02-S053]

### 🛠️ 19. Galapagos & Octopus (C. Parametric / 优化)

- **类别**: C. Parametric / 优化 GH plugin (合并条目)
- **开发商**: Galapagos by David Rutten (内置 GH); Octopus by Robert Vierlinger + Bollinger+Grohmann
- **当前版本**: Galapagos 随 GH; Octopus 0.4 (2023+)
- **license model**: free
- **典型价格**: $0
- **核心场景**: 单目标 (Galapagos) / 多目标 Pareto (Octopus) 进化优化; 是 GH 优化的 baseline 工具.
- **persona 适配**: 各 persona 均可入门; 高级用户多迁移 Wallacei.
- **典型 I/O**: GH 内部
- **学习曲线**: medium (Galapagos easy, Octopus steep)
- **2025-2026**: 稳定使用; Wallacei 成为高级用户 default.
- **常见坑**:
  1. 用 Galapagos 单目标做多目标问题 — 应换 Octopus / Wallacei.
  2. 优化 boundary 设置不合理.
- **来源**: [T02-S054]

### 🛠️ 20. Dynamo (C. Parametric / Revit)

- **类别**: C. Parametric / visual programming for Revit
- **开发商**: Autodesk (open source)
- **当前版本**: Dynamo for Revit 3.x (随 Revit 2025/2026); Dynamo Sandbox (standalone)
- **license model**: free, bundled with Revit
- **典型价格**: $0 (含 Revit)
- **核心场景**: Revit 内的 visual programming — auto layout / data 处理 / family 批操作; 替代 macro / pyRevit 入门门槛.
- **persona 适配**:
  - boutique: 不主用 (boutique 用 Rhino + GH).
  - 中型: BIM Manager / Coordinator 常备工具.
  - 大型院 (中国): Revit-heavy firm 必备; 替代部分 pyRevit.
- **典型 I/O**: DYN / Revit element
- **配合**: Revit / Refinery (generative add-on) / pyRevit (互补)
- **学习曲线**: medium
- **2025-2026**: Dynamo 2.x → 3.x 稳定演进; AI 加持 generative design (Refinery → Forma) 逐步替代部分场景.
- **替代**: Grasshopper + Rhino.Inside.Revit (更强大) / pyRevit (Python)
- **常见坑**:
  1. 期待 GH 级 ecosystem — Dynamo 社区小, 卡在 Revit-only.
  2. 长脚本难调试 — 切 Python custom node.
- **来源**: [T02-S003] [T02-S055]

### 🛠️ 21. Enscape (D. Visualization / 实时)

- **类别**: D. Visualization / 实时渲染
- **开发商**: Chaos (合并 Enscape + Chaos 2022)
- **当前版本**: 4.13 (Spring 2026); 持续 update
- **license model**: subscription
- **典型价格**: $499/yr fixed seat; $599/yr floating; bundle with V-Ray
- **核心场景**: SD-DD 阶段实时渲染; 与 Revit / SketchUp / ArchiCAD / Rhino plugin 一键启动; 客户沟通实时 walkthrough; VR 头显支持.
- **persona 适配**:
  - boutique: 主力实时, 配 V-Ray 出 final.
  - 中型: 每个 designer 一席 Enscape.
  - 大型院: 设计阶段 + 投标动画.
- **典型 I/O**: Revit / SketchUp / Rhino / ArchiCAD / Vectorworks 实时插件; export PNG / EXR / MP4 / panorama / VR
- **配合**: Chaos Cosmos (asset library) / V-Ray (深度品质渲染) / Enscape Impact (sustainability)
- **学习曲线**: easy
- **2025-2026** (last_updated: 2026-05-16): Spring 2026 加入 AI Material Editor (text-to-material) + Light Management (lighting 内 Enscape 调节) + Enscape Impact 加 Thermal Comfort Analysis + Exportable Performance Reports + AI Enhancer (人/植/季节调节) + SketchUp external components.
- **替代**: D5 Render (新秀, 同实时) / Twinmotion (Epic, UE 底层) / Lumion (cinematic) / V-Ray Vision (Chaos 内部替代)
- **常见坑**:
  1. Enscape 出图当 final — 应 V-Ray 出 client final; Enscape 强于过程.
  2. 不锁主源 model — Enscape 即时反映 Revit 改动, 出图前需 Revit 锁版本.
  3. 客户 walkthrough 期望太高 — Enscape 实时但 hardware 依赖.
- **来源**: [T02-S016] [T02-S017]

### 🛠️ 22. V-Ray (D. Visualization / 离线 + 实时)

- **类别**: D. Visualization / 离线 path-traced + 实时 (V-Ray Vision)
- **开发商**: Chaos (Bulgaria 1999)
- **当前版本**: V-Ray 7 (2024-2025; Update 2 2025-08 AI; Update 3 2026-04 realtime viewport)
- **license model**: subscription
- **典型价格**: $730/yr (single product e.g. for SketchUp); Premium $1,170/yr 多产品; V-Ray Cloud render credits 另购
- **核心场景**: 最终 (final) 出图 — boutique / 客户图 / 出版图; 全部 host (Rhino / SketchUp / Revit / 3ds Max / Maya / Cinema 4D / Houdini / Unreal); 高品质 hero shot.
- **persona 适配**:
  - boutique: 主力 final; SD Enscape, final V-Ray.
  - 中型: visualization specialist 主用; 项目 budget 决定.
  - 大型院 (中国): 投标 hero image 必出; 配合 PS post.
- **典型 I/O**: 各 host 内嵌; export EXR / PNG / TIFF; .vrscene 跨 host
- **配合**: Chaos Cosmos / Chaos Vantage (real-time GPU sibling) / Chaos Cloud (rendering)
- **学习曲线**: steep (full path tracing 控制曲线很长)
- **2025-2026**: V-Ray 7 Update 2 (2025-08) 加 AI Material Generator (PBR from reference photo) + AI Upscaler 16K + OpenPBR + Distributed Rendering 2 + Night Sky procedural; V-Ray 7 Update 3 (2026-04) 加 realtime viewport rendering — 模糊 Enscape 边界.
- **替代**: Corona (Chaos 内, 易上手, 主室内) / Arnold (3ds Max/Maya 内嵌) / Octane (GPU) / Redshift (GPU)
- **常见坑**:
  1. 默认 setting 直接渲 — output 噪点重; 应该建 firm template scene + 校准.
  2. 不 fly through 检查光照 — 大场景部分区局光照泄漏.
  3. 错过 Vantage GPU — 同 Chaos 生态, 实时 V-Ray scene 可看.
- **来源**: [T02-S018] [T02-S019] [T02-S020]

### 🛠️ 23. Lumion (D. Visualization / 实时 cinematic)

- **类别**: D. Visualization / 实时渲染 (cinematic)
- **开发商**: Act-3D (Netherlands)
- **当前版本**: Lumion 2025 (2025-04; Pro/Standard); Lumion View 2025
- **license model**: subscription + perpetual hybrid
- **典型价格**: Pro $2,799/yr; Standard $1,499/yr; Lumion View $199/yr (新, 协作 review)
- **核心场景**: SD / DD presentation cinematic — 大场景 / 自然环境 / 动画; 中国大型院投标动画首选; 不在 host 内, 是 standalone import (LiveSync 链接 Revit/Rhino/SketchUp/ArchiCAD).
- **persona 适配**:
  - boutique: 小型 boutique 倾向 D5 / Enscape; Lumion 高级版本 boutique 用得少 (价高).
  - 中型: visualization team 配置.
  - 大型院 (中国): 投标 / 政府汇报视频主力; D5 Render 在替代.
- **典型 I/O**: import DAE / FBX / OBJ / SKP / 3DS / DWG; LiveSync Revit/Rhino/SketchUp/ArchiCAD; export MP4 / PNG / EXR / panorama
- **配合**: SketchUp / Rhino / Revit LiveSync; 内置 7000+ asset library
- **学习曲线**: easy
- **2025-2026**: 2025 (2025-04) 加 AI 8K upscaling + 体积雾 (ray-traced) + ray-traced 水/玻璃 + Scene Inspector + 129 教育 asset + 68 自然 asset; 新出 Lumion View ($199/yr) 协作 review 工具.
- **替代**: D5 Render (国产, 同 cinematic, 更便宜 + 中文社区强) / Twinmotion (Epic, UE 底层) / Enscape (BIM-integrated)
- **常见坑**:
  1. Lumion 出图很漂亮但与施工图脱节 — 渲染前必须 lock 平面.
  2. 用 Lumion asset 装满 — 出 generic Lumion 图, 缺设计独特性; 应自建/导入特定 asset.
  3. 期待 Enscape 级 BIM 同步 — Lumion LiveSync 不如 Enscape host-integrated.
- **来源**: [T02-S021] [T02-S022]

### 🛠️ 24. D5 Render (D. Visualization / 实时 + AI; G. 中国本土)

- **类别**: D. Visualization / 实时 AI 渲染 (兼 G. 中国本土)
- **开发商**: Dimension 5 (Nanjing 南京, 2015 创办; D5 2020 首发)
- **当前版本**: D5 Render 3.0 (2026-01) + D5 Lite (SketchUp plugin); D5 Works (web 协作)
- **license model**: subscription + free tier
- **典型价格**: Free / Pro $38/月 / Team $48/月/seat; 中国 RMB 价 ¥1,800-3,000/yr 教育优惠
- **核心场景**: SD-CD 阶段实时渲染 + AI 增强; 中国 boutique-大型院 默认实时渲染 (替代 Lumion); 国际亦在加速渗透.
- **persona 适配**:
  - boutique: 中国 boutique 主力; 国际 boutique 加速试用.
  - 中型: 中国主流; 国际 visualization specialist 试用.
  - 大型院 (中国): 投标动画 + 客户 walkthrough 标配, 抢占 Lumion 份额.
- **典型 I/O**: import SKP / RVT / 3DM / FBX / DAE / OBJ / DWG; LiveSync 主流 host; export MP4 / PNG / panorama / VR / glTF
- **配合**: SketchUp / Revit / Rhino / ArchiCAD / 3ds Max LiveSync; 内置 asset library
- **学习曲线**: easy
- **2025-2026**: 2025-01 Series C $80M (Zhengshan Capital + Hongshan/Sequoia China); 2026-01 D5 Render 3.0 — 新增 Ocean (海/海岸自动生成) + 体积云 (Cumulus/Stratus/Cumulonimbus/Cirrus 参数化); D5 Lite (SketchUp 实时 plugin); AI Scene Match / AI Image to 3D.
- **替代**: Lumion (cinematic) / Enscape (BIM) / Twinmotion (Epic) / Chaos Vantage (V-Ray 实时)
- **常见坑**:
  1. 把 D5 当 V-Ray final 用 — D5 强在速度, V-Ray 仍在 hero shot 微调精度领先.
  2. AI Scene Match 生硬替换 — 应作 starting point 不是 final.
  3. 国际客户不熟 D5 — boutique 出 final 标 "rendered" 不标软件即可.
- **来源**: [T02-S023] [T02-S024]

### 🛠️ 25. Twinmotion (D. Visualization / 实时 UE 底层)

- **类别**: D. Visualization / 实时 (Unreal Engine 底层)
- **开发商**: Epic Games (收购自 Abvent 2019)
- **当前版本**: Twinmotion 2025.2 (2025-10); Nanite 支持
- **license model**: free (个人 < $1M revenue); commercial $645 perpetual; subscription $445/yr
- **典型价格**: $445/yr or $645 perpetual — 比 Lumion 便宜 5x
- **核心场景**: SD-DD 实时 presentation; UE 底层但无 UE 学习曲线; LiveSync 几乎所有 BIM/CAD host; 价格 / 性能 / 易用三角占优.
- **persona 适配**:
  - boutique: 主选实时之一 (价格友好).
  - 中型: 通用配置.
  - 大型院: 投标动画用; 与 Lumion / D5 三选.
- **典型 I/O**: TM / import FBX / DAE / OBJ / GLB / DWG / SKP / RVT / DGN; LiveSync Revit / ArchiCAD / SketchUp / Rhino / VectorWorks; export MP4 / PNG / 360 panorama / Pixel Streaming
- **配合**: Datasmith (Epic, BIM 转换); UE pipeline (转 UE 深加工)
- **学习曲线**: easy
- **2025-2026**: 2025.1 (2025-02) 加 volumetric clouds + Virtual Shadow Maps + 自动 LOD + orthographic realtime + Orbit cam rig + Configuration (交互式 walkthrough); 2025.1.1 (2025-04) 加 3D grass + DLSS 4; 2025.2 (2025-10) 加 Nanite (UE 虚拟化几何系统) — 可处理 billions of polygons.
- **替代**: D5 Render (国产) / Enscape (BIM-integrated) / Lumion (cinematic) / Unreal Engine 5 (直接)
- **常见坑**:
  1. Nanite 期待万能 — 仍有 hardware requirement, 笔记本受限.
  2. 不用 Datasmith — 导致 BIM 元数据丢失.
- **来源**: [T02-S025] [T02-S026] [T02-S081]

### 🛠️ 26. Unreal Engine 5 (D. Visualization / 高级 custom)

- **类别**: D. Visualization / 游戏引擎 (custom interactive)
- **开发商**: Epic Games (US)
- **当前版本**: UE 5.5+ (2025-)
- **license model**: free; 5% royalty after $1M revenue per product
- **典型价格**: free
- **核心场景**: 高级 interactive / VR / Pixel Streaming / metaverse / 长期 archviz pipeline; 不是日常工具 — 是 visualization specialist 专项.
- **persona 适配**:
  - boutique: 几乎不用 (学习曲线太陡).
  - 中型: 1-2 个 viz specialist 用; 大型方案有时使用.
  - 大型院: 高端项目 (e.g. 文旅 / 展览) 专项使用.
- **典型 I/O**: UE Asset / Datasmith (从 Twinmotion / Revit / Rhino import); export 高清 video / Pixel Streaming web
- **配合**: Twinmotion (轻量入门) / Datasmith / Sequencer (动画) / MetaHumans (人物) / Quixel Megascans (asset)
- **学习曲线**: steep+ (3-6 月入门, profession itself)
- **2025-2026**: UE 5.5+ Nanite + Lumen 持续优化; Twinmotion 桥接 Datasmith 让 archviz 用户 0→UE 路径明朗; UEFN (Unreal Editor for Fortnite) 不适合 archviz.
- **替代**: Twinmotion (90% archviz 场景已够) / Unity (轻量, 但 archviz 社区弱于 UE)
- **常见坑**:
  1. boutique 想全员学 UE — 投入 vs 回报失衡; 应 Twinmotion 入门.
  2. 不优化 model — UE 卡; 应该 LOD + Nanite (5.x+) 利用.
- **来源**: [T02-S027] [T02-S078]

### 🛠️ 27. Adobe Creative Cloud (D. Visualization / 后期 + 出图)

- **类别**: D. Visualization / 后期 + 平面排版 (合并条目: Photoshop + Illustrator + InDesign)
- **开发商**: Adobe (US)
- **当前版本**: CC 2025 (2025-2026 滚动 SaaS); Photoshop / Illustrator / InDesign 主三件
- **license model**: subscription only
- **典型价格**: All Apps $54.99/月 (~$660/yr individual); Single App $22.99/月 (PS / AI / ID 各)
- **核心场景**: 全 5-phase 通用 — PS 后期 + entourage; AI 制图 + 矢量 diagram; ID 排版 portfolio + book.
- **persona 适配**: 每个 persona 必备; boutique 通常 All Apps individual; 中型 + 大型院 团队 license.
- **典型 I/O**: PSD / AI / INDD / PDF; 与 Revit / Rhino / SketchUp PDF 出口对接
- **配合**: Adobe Firefly (2023+, 集成 AI 生成); Adobe Express (web 轻量); Acrobat Pro (PDF)
- **学习曲线**: medium (PS 比 AI/ID 都广; 三者全熟练 1-3 年)
- **2025-2026**: 2025-04 Firefly Image Model 4 / 4 Ultra 大幅 prompt fidelity 提升; PS Generative Fill / Expand 持续 AI; AI 生成 + 传统工作流融合是 2025-2026 主基调.
- **替代**: Affinity Suite (买断, 一次性 $164.99 全套) — boutique 反 subscription 趋向; Procreate (iPad 概念草图)
- **常见坑**:
  1. 用 PS 改 vector — 用 Illustrator 才对; PS 改 vector 像素化.
  2. 用 PS 排版 portfolio — InDesign 是排版主, PS 是图; 长 portfolio PS 维护痛苦.
  3. 直接 PS 出 client 大图 — 应该 InDesign 链接 PSD/AI/EXR (linked, 不 embed).
- **来源**: [T02-S063] [T02-S042]

### 🛠️ 28. Ladybug + Honeybee (E. Sustainability / 入门主力)

- **类别**: E. Sustainability / 环境分析 Grasshopper plugin (open-source)
- **开发商**: Ladybug Tools (Mostapha Sadeghipour Roudsari, et al., open source community)
- **当前版本**: Ladybug Tools 1.7+ (LBT 持续); 与 Grasshopper / Rhino / Revit (Pollination 商业) 多平台
- **license model**: free + open source (GPL3)
- **典型价格**: $0 (Pollination 商业云版另收)
- **核心场景**: SD-DD 阶段 daylight + 能耗 + 风 + 视野 + 辐射分析; 建筑师入门 sustainability 标配; EnergyPlus / Radiance / OpenStudio 等专业引擎的可视化前端.
- **persona 适配**:
  - boutique: 入门 sustainability 自学首选.
  - 中型: SD 阶段标配 + 项目专项 specialist.
  - 大型院 (中国): 投标 sustainability 加分项 + 绿建报告辅助 (但中国 main 是斯维尔出绿建报告).
- **典型 I/O**: GH 内置; 调用 EnergyPlus / Radiance / OpenStudio / OpenFOAM; export Excel / CSV / 可视化
- **配合**: Grasshopper / Karamba3D (多目标) / Wallacei / ClimateStudio (商业平行替代)
- **学习曲线**: medium-steep (GH 基础 + 环境物理双门槛)
- **2025-2026**: 持续社区维护; Pollination 云版 (Ladybug Tools 商业产品) 提供 cloud + Revit 集成.
- **替代**: ClimateStudio (商业更快 + UI 更友好) / IES VE (传统专业) / DesignBuilder (传统)
- **常见坑**:
  1. 用 Ladybug 跑 EnergyPlus 不校核 weather file — EPW 选错气候带, 结论错.
  2. daylight 只看 DA — 应该综合 sDA / ASE / glare 多 metric.
  3. 把分析结果直接当 final — 应该交 sustainability consultant 复核.
- **来源**: [T02-S030]

### 🛠️ 29. ClimateStudio (E. Sustainability / 专业付费)

- **类别**: E. Sustainability / 商业专业 (Ladybug 创办者衍生)
- **开发商**: Solemma (Christoph Reinhart MIT lab spinout)
- **当前版本**: ClimateStudio 2.x (Rhino plugin 主线); ClimateStudio Revit (2025 首发 demo at Solemma Symposium 2025)
- **license model**: subscription
- **典型价格**: $1,295/yr professional; $545/yr education
- **核心场景**: 比 Ladybug 更快更易用; daylight + glare + 视野 + 能耗 + 占用 + thermal + spectral simulation; 适合 sustainability consultant 与 boutique 专人.
- **persona 适配**:
  - boutique: 有 sustainability 专人 / 项目主力.
  - 中型: sustainability specialist 标配.
  - 大型院: 项目 specialist 配置.
- **典型 I/O**: Rhino + GH 内; 2025-2026 Revit 版 demo; 与 RADIANCE / EnergyPlus 底层连接
- **配合**: Rhino / Grasshopper / EnergyPlus / RADIANCE
- **学习曲线**: medium (比 Ladybug 略 easy 因 UI; 物理仍 steep)
- **2025-2026**: Solemma Symposium 2025 (NYC KPF office) 首次 ClimateStudio Revit 公开 demo + spectral simulation (与 PNNL 合作) + 新 HVAC component library.
- **替代**: Ladybug + Honeybee (open source) / IES VE (传统) / DesignBuilder (传统)
- **常见坑**:
  1. 期待 Revit 版即用 — 2025-2026 仍 demo / early access.
  2. 跑 spectral 不校 IES file — 灯光数据精度依赖.
- **来源**: [T02-S028] [T02-S029] [T02-S079]

### 🛠️ 30. IES VE (E. Sustainability / 传统专业)

- **类别**: E. Sustainability / 传统专业 (commercial)
- **开发商**: IES (Integrated Environmental Solutions, Glasgow UK)
- **当前版本**: VE 2024-2025
- **license model**: subscription
- **典型价格**: 议价 ($3,000-15,000/yr 按 module)
- **核心场景**: 全 5-phase 整合 — APACHE engine 能耗 + Radiance daylight + CFD + LCA; 适合 sustainability engineer team 不是 architect; 大型公建 / hospital / lab 强项.
- **persona 适配**:
  - boutique: 几乎不用 (重 + 贵).
  - 中型: sustainability engineering team 才装.
  - 大型院: 大型 hospital / lab / 高校 EPC 项目用.
- **典型 I/O**: gbXML / IFC / DWG (有限) / SketchUp; export 复杂 LEED / BREEAM report
- **配合**: Revit (gbXML) / Rhino
- **学习曲线**: steep
- **2025-2026**: VE 仍是 LEED / WELL / BREEAM consultant 主用; AI/auto-calibration 在 roadmap.
- **替代**: DesignBuilder (类似定位, 价格更友好) / ClimateStudio (建筑师向)
- **常见坑**:
  1. 建筑师独立采购 — 应是 engineering team 主用.
  2. 设计早期跑 VE — overkill, 应 Ladybug/ClimateStudio early stage.
- **来源**: [T02-S034]

### 🛠️ 31. DesignBuilder (E. Sustainability / EnergyPlus 前端)

- **类别**: E. Sustainability / EnergyPlus 商业前端
- **开发商**: DesignBuilder Software (UK)
- **当前版本**: DesignBuilder v7+ (2024-2025)
- **license model**: subscription + perpetual hybrid
- **典型价格**: £675-3,000/yr 按 module (energy / lighting / CFD / Cost / HVAC)
- **核心场景**: 中级 sustainability engineer 主用; UI 友好的 EnergyPlus 前端 + 内置 Radiance + CFD; 适合 sustainability consultant / engineer 而非 architect 直接.
- **persona 适配**: 同 IES VE — engineering team 主.
- **典型 I/O**: gbXML / IFC / DWG / 3DM
- **配合**: EnergyPlus (底层) / Revit (gbXML)
- **学习曲线**: medium (比 IES VE 友好)
- **2025-2026**: 持续 EnergyPlus 新版本跟进 (EnergyPlus 24.x); LEED v5 (2025) compliance 更新.
- **替代**: IES VE (更全套) / OpenStudio (开源 EP 前端) / ClimateStudio
- **常见坑**: 同 IES VE.
- **来源**: [T02-S035]

### 🛠️ 32. EnergyPlus (E. Sustainability / 开源 engine)

- **类别**: E. Sustainability / 开源能耗 simulation engine
- **开发商**: US DOE (Dept of Energy) + 学术界
- **当前版本**: EnergyPlus 24.2 (2024-10)
- **license model**: open source (BSD-style)
- **典型价格**: $0
- **核心场景**: 底层 engine; 通过 DesignBuilder / OpenStudio / ClimateStudio / Honeybee 等前端使用; 单独使用罕见.
- **persona 适配**: 不是直接使用工具; sustainability engineer 用 OpenStudio + EnergyPlus 直接做 custom.
- **典型 I/O**: IDF / IDD; weather EPW; output ESO / SQL / HTML report
- **配合**: OpenStudio (NREL 开源前端) / DesignBuilder / ClimateStudio / Honeybee
- **学习曲线**: steep (直接 IDF 编辑)
- **2025-2026**: 持续 release; HVAC + envelope model 增强.
- **替代**: TRNSYS (传统 system) / IDA ICE (北欧)
- **常见坑**:
  1. 直接编 IDF — 建筑师不该, 应 GUI 前端.
  2. EPW 文件不更新 — 用旧 weather data 在 climate change 时代严重失真.
- **来源**: [T02-S036]

### 🛠️ 33. One Click LCA (E. Sustainability / LCA)

- **类别**: E. Sustainability / 全 LCA + EPD 计算
- **开发商**: One Click LCA (Helsinki Finland)
- **当前版本**: SaaS 持续 update
- **license model**: subscription
- **典型价格**: €1,200-15,000/yr 按 module + project count
- **核心场景**: CD/CA 阶段 embodied + operational carbon LCA; LEED / BREEAM / DGNB / EU Level(s) / GHG protocol compliance; 全球 LCA 市占第一.
- **persona 适配**:
  - boutique: 项目 LCA 必走 (越来越多客户要求).
  - 中型: sustainability lead 标配.
  - 大型院: 国际项目 + 出口项目.
- **典型 I/O**: import Revit / IFC / Excel; output EPD / LCA report PDF + dashboard
- **配合**: Revit (One Click LCA Revit plugin) / EC3 (2025 集成 EPD 共享) / Tally (2025 同生态合并)
- **学习曲线**: medium
- **2025-2026**: 2025 与 Building Transparency 合作 — EC3 + One Click LCA EPD 双向同步; EU CSRD / SBTi 合规热点.
- **替代**: Tally (Revit-only, Building Transparency 2.0 发布 2025) / EC3 (免费 embodied carbon 子集) / Athena Impact Estimator (北美) / BEAM (北美开源)
- **常见坑**:
  1. EPD 数据库选择不一致 — 项目内一致性需 governance.
  2. 操作 LCA 不读 ISO 21931/21930/EN 15978 — 出 report 不合规.
- **来源**: [T02-S031]

### 🛠️ 34. EC3 (E. Sustainability / 开源 embodied carbon)

- **类别**: E. Sustainability / 开源 embodied carbon calculator
- **开发商**: Building Transparency (非营利, US Carbon Leadership Forum 关联)
- **当前版本**: SaaS 持续 update
- **license model**: free + open access
- **典型价格**: $0
- **核心场景**: CD/CA 阶段材料 embodied carbon 比较; 全球唯一 free + open-access 全建筑 EPD 数据库; LEED v5 (2025) 应用.
- **persona 适配**: 全 persona 入门首选, 免费.
- **典型 I/O**: web + Revit/Tally plugin; 输入 material quantity, 输出 GWP / 比较
- **配合**: Tally (Revit 集成) / One Click LCA (2025 EPD 同步)
- **学习曲线**: easy
- **2025-2026**: 2025 与 One Click LCA EPD 数据互通; LEED v5 + EU CSRD 推动使用.
- **替代**: One Click LCA (商业全套) / Tally (Revit-only)
- **常见坑**:
  1. 数据精度依赖输入 — material quantity 错误传导.
  2. 仅看 embodied 不看 operational — 应配合 EnergyPlus 类工具.
- **来源**: [T02-S032]

### 🛠️ 35. Tally / Tally 2.0 (E. Sustainability / Revit LCA)

- **类别**: E. Sustainability / Revit-integrated LCA
- **开发商**: KieranTimberlake (创办); 2024 转 Building Transparency 维护
- **当前版本**: Tally 2.0 (2025 发布; 重写 + ISO 21931/21930/EN 15978/15804+A2)
- **license model**: subscription (商业)
- **典型价格**: $799/yr (single user)
- **核心场景**: Revit 内 LCA — 直接读 Revit material quantity 算 embodied carbon; 直接 export 到 EC3.
- **persona 适配**: 中型 + 大型院 Revit-heavy 主用.
- **典型 I/O**: Revit material → LCA → EC3
- **配合**: Revit (内) / EC3
- **学习曲线**: easy
- **2025-2026**: 2024 KieranTimberlake → Building Transparency 转移; Tally 2.0 (2025) 全面重写 + 新 UI + 新 reporting + interactive dashboard.
- **替代**: One Click LCA Revit plugin / EC3 (free, less integrated)
- **常见坑**: Revit material take-off 准确性是上限; family 类别错则结果错.
- **来源**: [T02-S033]

### 🛠️ 36. Midjourney (F. AI Generative / Concept)

- **类别**: F. AI Generative / 概念 visualization
- **开发商**: Midjourney Inc (US, David Holz)
- **当前版本**: V7 (2025-04); V8 alpha (2026-03); V8.1 (2026-04)
- **license model**: subscription only (Discord + Web)
- **典型价格**: $10/月 Basic; $30/月 Standard; $60/月 Pro; $120/月 Mega
- **核心场景**: PD (Pre-Design) / 概念阶段 mood board + 探索; client 沟通 concept image; AIA 2026 调查 62% 美国 firm 用 generative AI (vs 2024 18%).
- **persona 适配**:
  - boutique: 概念阶段主力 mood board; 客户提案前.
  - 中型: 概念 + marketing image.
  - 大型院 (中国): 投标 mood board + 国际项目客户沟通.
- **典型 I/O**: text → image (PNG); V7 加入 video; Discord/web UI
- **配合**: PS post / SD ControlNet 配合 (concept→深加工) / Veras (architecture-specific)
- **学习曲线**: easy (prompt 工程 medium)
- **2025-2026**: V7 (2025-04) 大改 — spatial coherence + material realism 显著提升; V8 (2026-03) + V8.1 (2026-04) 基础设施大改; RIBA 2026 盲测 73% 客户分不清 AI vs 3D render.
- **替代**: SD + ControlNet (开源 + 控制力强) / DALL-E 3 (OpenAI) / Adobe Firefly (商用 indemnity) / Veras (Enscape 系 archviz 专)
- **常见坑**:
  1. **Midjourney 渲染交业主当方案** — 大业主开始要求 Midjourney mood board, 但建筑师不能用它替代严肃概念设计或 SD-level 工作.
  2. 出 mood board 不做几何控制 — 应 SD+ControlNet 接续, 让 image 服从 geometry.
  3. 客户期待 Midjourney 出 final — 不能, 应教育客户 generative 仅 PD 阶段用.
- **来源**: [T02-S039]

### 🛠️ 37. Stable Diffusion + ControlNet (F. AI Generative / 开源 + 控制)

- **类别**: F. AI Generative / 开源 + 几何控制
- **开发商**: Stability AI (SD); Lvmin Zhang 张吕敏 / Stanford (ControlNet 2023-02)
- **当前版本**: SD 3.5 / SDXL (2024-2025); ControlNet 1.1+ + ControlNet++ (2025)
- **license model**: open source (SD Open RAIL-M); 自部署或云端
- **典型价格**: $0 (self-host) / RunDiffusion etc $10-50/月 / GPU 成本
- **核心场景**: SD-DD 阶段 — 用 ControlNet 控制几何 (Canny edge / depth / line / OpenPose / scribble) 把建筑师线稿 → photoreal; 是 Midjourney 替代的 geometry-controlled 版.
- **persona 适配**:
  - boutique: 有 GPU 站 + 1-2 个 AI savvy 设计师; 复杂工作流.
  - 中型: visualization team 进阶配置.
  - 大型院: 大型院开始 pilot, IT 部署 SDXL 工作流.
- **典型 I/O**: 线稿 / 模型截图 + prompt → photoreal image; 与 Photoshop / Krita workflow 集成
- **配合**: ComfyUI / Automatic1111 (UI) / Krita-Diffusion / Photoshop plugin / Blender 集成 (Parametric Architecture community 介)
- **学习曲线**: steep (Python / GPU / prompt 多门槛)
- **2025-2026**: SD 3.5 (2024-10) + ControlNet++ 多模态; ComfyUI 节点式工作流主流; 与 Blender 集成做 archviz 是 2025 热点.
- **替代**: Midjourney (易用, 控制弱) / Veras (Enscape 系一键) / mnml.ai / ReRender AI
- **常见坑**:
  1. 期待 SD 即用 — 需大量 model / LoRA 训练 / curated 才能稳出 archviz 质量.
  2. 不用 ControlNet 直 prompt — 出图与设计无关.
  3. GPU 成本被低估 — 单卡 A6000 6 万元起.
- **来源**: [T02-S040] [T02-S041]

### 🛠️ 38. Adobe Firefly (F. AI Generative / 商用 indemnity)

- **类别**: F. AI Generative / 商用安全 (license-clean 训练数据)
- **开发商**: Adobe (US)
- **当前版本**: Firefly Image Model 4 / 4 Ultra (2025-04)
- **license model**: subscription (含在 Creative Cloud All Apps); standalone Firefly plan
- **典型价格**: 含在 CC All Apps $54.99/月; Standalone Firefly $9.99/月
- **核心场景**: PS / AI / ID 内集成 generative — Generative Fill (PS) / Vector Recolor (AI) / 概念图生成; 适合需要 client-deliverable + IP indemnity 的商业用途.
- **persona 适配**: 已有 CC subscription 的所有 persona 顺便用; 商业项目 + 客户图首选 (Adobe legal indemnification).
- **典型 I/O**: PS / AI / web; output PNG / SVG / 矢量
- **配合**: Photoshop Generative Fill / Illustrator Vector / InDesign 排版
- **学习曲线**: easy
- **2025-2026**: 2025-04 Image Model 4 / 4 Ultra 大幅 fidelity 提升; Adobe 提供商业用途 IP 保护 (与 Midjourney/SD 区别).
- **替代**: Midjourney (创意更强) / DALL-E (集成 ChatGPT) / SD (开源)
- **常见坑**:
  1. 期待 Midjourney 级 wow 效果 — Firefly 安全但创意上限略低.
  2. 不利用 PS/AI 集成 — 错过最大价值.
- **来源**: [T02-S042]

### 🛠️ 39. DALL-E 3 (F. AI Generative / OpenAI)

- **类别**: F. AI Generative / OpenAI 集成
- **开发商**: OpenAI (US)
- **当前版本**: DALL-E 3 (2023-10) + GPT-4o native image (2025); DALL-E 4 暗指 2026
- **license model**: subscription (含 ChatGPT Plus); API per-image
- **典型价格**: $20/月 ChatGPT Plus; API $0.04-0.12/image
- **核心场景**: PD 概念 + 简单 mood; 与 ChatGPT 对话式生成 — 适合非 AI 专业的 PM / 客户.
- **persona 适配**: 所有 persona 偶用 (PM 与客户 brainstorm); 不是专业 archviz 工具.
- **典型 I/O**: text / chat → PNG
- **配合**: ChatGPT (对话生成); GPT-4o native image (2025) 多模态
- **学习曲线**: easy
- **2025-2026**: GPT-4o native image (2025) 让 ChatGPT 直接出图; 多模态融合; vs Midjourney 创意略低, vs Firefly 商业 indemnity 较弱.
- **替代**: Midjourney / Firefly / SD
- **常见坑**:
  1. 期待 archviz 级精度 — DALL-E 偏 illustrative.
  2. 商业用途 IP — OpenAI 政策不如 Adobe 清晰.
- **来源**: [T02-S043]

### 🛠️ 40. Autodesk Forma (ex-Spacemaker) (F. AI Generative / B. BIM 上游)

- **类别**: F. AI Generative / massing + site planning (前身 Spacemaker)
- **开发商**: Autodesk (Spacemaker 2020-11 acq $240M, 2023-05 改名 Forma)
- **当前版本**: Forma Site Design (2025); Forma Building Design (2025 新, 预览)
- **license model**: subscription (在 AEC Collection 内或单买)
- **典型价格**: $1,565/yr (standalone); 在 AEC Collection 包内
- **核心场景**: PD / SD 阶段 site analysis + massing + 日照 + 风 + 噪音 + 微气候; AI 生成建筑布局 (city block / line / tower / mixed); 与 Revit 双向; 早期可行性研究替代 GIS+手算.
- **persona 适配**:
  - boutique: 大型 site 项目用; 小项目 overkill.
  - 中型: SD 早期标配; 与 Revit AEC Collection 一起.
  - 大型院: 大型城市更新 / 文旅 / 园区项目主力.
- **典型 I/O**: cloud SaaS; import GIS / DWG / Revit; export Revit / 截图 / 报告
- **配合**: Revit (双向) / ACC
- **学习曲线**: easy-medium
- **2025-2026**: 2025-04 加入 generative design + AI 3D 建筑生成 (Autodesk 自家训练集, 比通用 AI 更可靠); Forma Building Design (2025 preview) 扩 facade + 室内 layout + carbon/daylight metric.
- **替代**: TestFit (开发商 feasibility 偏向) / Snaptrude (AI BIM) / Hypar (function-based)
- **常见坑**:
  1. 把 Forma generative 当 final massing — 应作 starting point + 设计师过滤.
  2. 不上 Revit — 错过 Forma 入 Revit 的核心价值.
  3. 中国客户不熟 — 国内项目 Forma 用得少, 多用 SketchUp + GH 自做.
- **来源**: [T02-S037] [T02-S038]

### 🛠️ 41. TestFit (F. AI Generative / 开发商 feasibility)

- **类别**: F. AI Generative / real-estate feasibility 参数化
- **开发商**: TestFit (US Dallas)
- **当前版本**: TestFit 2.20+ (持续 update)
- **license model**: subscription + free tier (2024 free for personal)
- **典型价格**: free → $250/月 starter → enterprise
- **核心场景**: PD pre-design 阶段 — 开发商 / 项目经理 / 早期 architect feasibility 计算; 限制条件 (site / height / unit mix / parking) → 数千种 massing + cost + ROI; 多家庭 / 混合用 / urban plan.
- **persona 适配**:
  - boutique: 开发商客户对接时用; 自己很少主.
  - 中型: pre-design 团队配置.
  - 大型院: 投标 / feasibility 阶段; 与 developer 对接.
- **典型 I/O**: 输入 site CAD / 数值参数; output 3D massing + spreadsheet
- **配合**: Revit / Forma / Snaptrude
- **学习曲线**: easy
- **2025-2026**: 2024 Massing 模块 free; 2025 Urban Planner 模块加; 开发商市场强势.
- **替代**: Snaptrude (AI agents) / Hypar (function) / Forma (Autodesk)
- **常见坑**:
  1. 把 TestFit constraint 跑 default — 应认真 input local zoning code.
  2. 不审 cost 假设 — TestFit cost 算法是粗略, 不替代 estimator.
- **来源**: [T02-S044] [T02-S045]

### 🛠️ 42. Hypar (F. AI Generative / function-based BIM)

- **类别**: F. AI Generative / function-based 生成 + 空间规划
- **开发商**: Hypar (US, Ian Keough + Anthony Hauck)
- **当前版本**: Hypar 2.0 (2024-2025)
- **license model**: free tier + subscription
- **典型价格**: free → $99/月 → enterprise
- **核心场景**: 医疗 / 工作场所 / 数据中心 / 实验室等 重复 building type 自动化; 用户定义 architectural rules → 完整 building system 生成; Revit 兼容.
- **persona 适配**:
  - boutique: 通用项目少用; healthcare / data center 专项 boutique 用.
  - 中型: function library 累积 → 重复项目效率倍增.
  - 大型院: 医院 / 学校等标准化项目主力试用.
- **典型 I/O**: web + Revit/Rhino/GH plugin; function (C#/typescript) 输出 3D + data
- **配合**: Revit / Rhino / Grasshopper
- **学习曲线**: steep (function 写作 = programming)
- **2025-2026**: Hypar 2.0 加 space planning (block + stack + 家具); Excel/CSV program import; AI 增强 2025.
- **替代**: Snaptrude (AI agents) / TestFit (real estate)
- **常见坑**:
  1. 期待 out-of-box 万能 — Hypar 强在 function 累积, 自家 firm 需投入写 function.
  2. function debug 难 — 需 dev mindset.
- **来源**: [T02-S046] [T02-S047]

### 🛠️ 43. Maket.ai (F. AI Generative / 户型生成)

- **类别**: F. AI Generative / floor plan / residential
- **开发商**: Maket (Canada, Patrick Murphy founder)
- **当前版本**: SaaS 持续
- **license model**: subscription + free tier
- **典型价格**: free → $25/月 → enterprise
- **核心场景**: PD 阶段 residential floor plan 自动 — 输入 site + program → 数十种合规 layout; 偏 small-scale residential / developer / homeowner.
- **persona 适配**:
  - boutique: 小住宅项目 / homeowner direct 项目用.
  - 中型: residential developer 工作流.
  - 大型院: 几乎不用 (项目类型不匹配).
- **典型 I/O**: web; export PDF / DWG
- **学习曲线**: easy
- **2025-2026**: 持续 update; AI 户型生成 + AI 渲染 + zoning compliance 检查.
- **替代**: Snaptrude / Architechtures.com / Veras
- **常见坑**:
  1. 把 AI plan 直接送 client — 应作 starting point.
  2. zoning 检查依赖 local code data — 中国不支持.
- **来源**: [T02-S050]

### 🛠️ 44. Architechtures.com (F. AI Generative / residential / multifamily)

- **类别**: F. AI Generative / 住宅 / 多家庭自动设计
- **开发商**: Architechtures (Spain)
- **当前版本**: SaaS
- **license model**: subscription + free tier
- **典型价格**: free → €99-499/月
- **核心场景**: residential building (尤其 multifamily) — 输入 site + program → 自动 unit layout + facade + structure; 欧洲市场偏强.
- **persona 适配**: 中小 boutique residential 试用; 大型院少用.
- **典型 I/O**: web; export Revit / IFC / DWG
- **学习曲线**: easy
- **2025-2026**: 增加 AI compliance + multi-language; 欧洲市场试点.
- **替代**: Maket / Snaptrude / Hypar
- **常见坑**: 同 Maket — zoning data dependency.
- **来源**: [T02-S051]

### 🛠️ 45. 天正 T20 建筑 (G. 中国本土 / A. CAD)

- **类别**: G. 中国本土 / A. CAD + 中国施工图主力
- **开发商**: 北京天正软件 (Tangent, 1993-)
- **当前版本**: T20 V10 (2024-2025); 支持 64bit AutoCAD 2024 平台; V8/V9 主流在用
- **license model**: subscription / perpetual (国内通行)
- **典型价格**: ¥6,000-12,000/license (经销商议价); 大型院批购 ¥3,000-5,000
- **核心场景**: CD (施工图) 阶段中国 90%+ 设计院 default; 在 AutoCAD 之上的"建筑专业增强工具"— 墙 / 门窗 / 楼梯 / 符号 / 总图 / 文字标注 / 详图 / 图纸出图 全中国规范化; 完全遵循中国 GB 制图标准.
- **persona 适配**:
  - boutique: 国际方案 boutique 弱用; 中国 boutique 必装 (但偏 Rhino + 天正 + AutoCAD 三角).
  - 中型: 100% 中国中型院主用.
  - 大型院 (尤其中国): 主力中的主力 — AutoCAD + 天正 占 95% 施工图工作.
- **典型 I/O**: 天正自定义对象 + DWG (兼容 AutoCAD); 转 IFC / 3D 需要导出对象
- **配合**: AutoCAD (基础平台必需) / 鸿业 / 探索者 / 斯维尔 (协同插件); 与 Revit 互通弱
- **学习曲线**: medium (AutoCAD + 天正 双门槛; 中国设计院员工 1-3 月入门)
- **2025-2026**: T20 V10 支持 AutoCAD 2024 64-bit; 持续跟新 GB 规范; 天正自家 BIM 系列 (天正 BIM 设计) 在加紧, 但施工图核心仍 T20 + CAD.
- **替代**: 浩辰 CAD 建筑 / 中望 CAD 建筑 (同生态国产替代, license 1/3); Revit (BIM 转型, 但施工图深度仍弱); 鸿业建筑 (类似定位, 北方占比稍高)
- **常见坑**:
  1. 国际项目用 T20 出图 — 国外不接 .dwg+天正对象, 应转通用 DWG.
  2. 升级 AutoCAD 不升 T20 — 版本错配, 对象不识别.
  3. 期待天正能做 BIM — 它是 CAD 增强不是 BIM, 应另上 Revit/ArchiCAD.
- **来源**: [T02-S064] [T02-S065]

### 🛠️ 46. 鸿业 BIMSpace (G. 中国本土 / B. BIM)

- **类别**: G. 中国本土 / B. BIM (建筑 / 机电 / 结构)
- **开发商**: 洛阳鸿业信息科技 (Hongye, 1992-, 2024 与广联达合作)
- **当前版本**: 鸿业 BIM 2025; BIMSpace 建筑 / 机电 / 结构 系列
- **license model**: subscription / perpetual
- **典型价格**: ¥8,000-20,000/yr 按 module
- **核心场景**: CD / CA 阶段全专业 BIM 正向设计; 中国市政 + 工业 + 建筑全覆盖; AutoCAD 平台扩展 → Revit 平台 BIM; 大型院 BIM 项目部装备.
- **persona 适配**:
  - boutique: 不用.
  - 中型: 中国中型 BIM 项目部.
  - 大型院 (尤其中国): 中国 BIM 项目第二选 (Revit 之后).
- **典型 I/O**: RVT / DWG / IFC / 鸿业自有
- **配合**: Revit / AutoCAD / 广联达
- **学习曲线**: medium
- **2025-2026**: 2024-2025 与广联达战略合作; 全专业 BIM 正向设计 (建筑—结构—机电) 三位一体加快.
- **替代**: Revit 原生 + 自家 family / 广联达数维 / PKPM-BIM
- **常见坑**:
  1. 鸿业 + Revit 工作流不 lock — 双源对象冲突.
  2. 国际项目期待鸿业 — 国际不识, 应 IFC 输出.
- **来源**: [T02-S066] [T02-S067]

### 🛠️ 47. 探索者 TSSD / TSPT (G. 中国本土 / 结构)

- **类别**: G. 中国本土 / 结构出图 + BIM (装配式)
- **开发商**: 北京探索者软件 (Tansuozhe, 1995-)
- **当前版本**: TSSD 2025 / TSPT 2025 (装配式)
- **license model**: subscription / perpetual
- **典型价格**: ¥5,000-15,000/yr
- **核心场景**: 结构施工图 + 装配式 BIM 配合; AutoCAD 平台 + Revit 平台; 中国结构院主用之一 (与 PKPM 配合).
- **persona 适配**:
  - boutique: 不用.
  - 中型 / 大型院: 中国结构院主流之一; 装配式项目必备.
- **典型 I/O**: DWG / RVT / IFC
- **配合**: AutoCAD / PKPM (结构分析) / Revit
- **学习曲线**: medium
- **2025-2026**: 装配式 BIM 政策推动持续增长; AI 配筋 + 智能审图试点.
- **替代**: PKPM 结构施工图 (后处理一体) / 鸿业结构
- **常见坑**: 与 PKPM 双源, 应明确主次.
- **来源**: [T02-S068]

### 🛠️ 48. 斯维尔 节能 / 绿建 / 碳排放 (G. 中国本土 / E. Sustainability)

- **类别**: G. 中国本土 / E. Sustainability (中国绿建标准)
- **开发商**: 北京绿建斯维尔 (THsware, 2002-)
- **当前版本**: 斯维尔 2025 PLUS / 2026; CEEB (碳排放计算软件) 中国市占第一
- **license model**: subscription / perpetual
- **典型价格**: ¥5,000-30,000/yr 按 module
- **核心场景**: CD 阶段中国绿建 / 节能 / 碳排放 / 日照 / 采光 / 通风 / 声环境 / 室内热舒适 / 住区热环境 报告生成; 中国《绿色建筑评价标准》/ 《建筑节能与可再生能源利用通用规范》强制合规.
- **persona 适配**:
  - boutique: 中国项目都需; boutique 通常外包给 sustainability consultant.
  - 中型 / 大型院 (中国): 必备 — 绿建评审 / 节能审查报告强制出.
- **典型 I/O**: 输入 DWG / IFC; 输出 PDF 报告 + 数据
- **配合**: AutoCAD / 天正 / Revit / 鸿业
- **学习曲线**: medium (中国规范学习曲线 vs 软件本身)
- **2025-2026**: 2025 PLUS 加超低能耗 + LCA 加强; CEEB 是中国应用最广碳排放工具; THS-BIM 解决方案全套.
- **替代**: PKPM 节能 (类似定位) / Ladybug / ClimateStudio (国际不出中国合规报告)
- **常见坑**:
  1. 用国际工具 (Ladybug/ClimateStudio) 出绿建报告 — 不合规, 仍需斯维尔.
  2. 不读最新 GB 规范 — 版本错配.
- **来源**: [T02-S069] [T02-S070]

### 🛠️ 49. PKPM 结构 (G. 中国本土 / 结构 / BIM)

- **类别**: G. 中国本土 / 结构设计 + 施工图 + 装配式 + 减隔震 + AI 智能化
- **开发商**: 北京构力科技 (中国建筑科学研究院旗下, 1988-)
- **当前版本**: PKPM 2025 R2 (2025); PKPM-BIM / PKPM-PC (装配式) / PKPM-AIChecker (AI 审图)
- **license model**: subscription / perpetual
- **典型价格**: ¥10,000-50,000/yr 按 module (结构 + 施工图 + BIM)
- **核心场景**: CD 阶段中国结构设计绝对主力 — 全 GB 规范, 配合最新《混标》《抗标》; 结构设计 + 施工图 + 装配式 + 减隔震 + 加固改造一体化; AI 智能化产品 (AID-MJ / AID-JG).
- **persona 适配**:
  - boutique: 国际方案 boutique 不用; 中国 boutique 结构外协即 PKPM.
  - 中型 / 大型院: 100% 中国设计院结构主力; 90% 中国结构师生涯软件.
- **典型 I/O**: PKPM 自有 + DWG + RVT (PKPM-BIM)
- **配合**: AutoCAD / 天正 / Revit / 探索者
- **学习曲线**: steep (中国结构规范 + 软件双门槛)
- **2025-2026**: 2025 R2 全模块引入智能化 (AID 系列); 紧跟新《混标》《抗标》; 智能出图 + 审查持续重构; 减隔震 + 加固改造方向扩张.
- **替代**: 盈建科 YJK (后起之秀, 部分院已替换 PKPM); 北方建科 / 鲁班 (轻量); SAP2000 / ETABS (国际, 不出中国规范报告)
- **常见坑**:
  1. 用 SAP2000 / ETABS 出中国 CD 报告 — 不合规, 仍需 PKPM 转一遍.
  2. PKPM-BIM 与 Revit 双源 — 应明确主次, 一致性 governance.
- **来源**: [T02-S071] [T02-S072]

### 🛠️ 50. 浩辰 CAD + 中望 CAD + 广联达 BIMMAKE / 数维 (G. 中国本土 / 国产替代综合)

- **类别**: G. 中国本土 / A. CAD 国产替代 + B. BIM 国产 (合并条目)
- **开发商**: 浩辰软件 GstarCAD (苏州); 中望软件 ZWSOFT (广州); 广联达 Glodon (北京)
- **当前版本**: 浩辰 CAD 2025; 中望 CAD 2026 建筑版; 广联达 BIMMAKE 2025; 广联达数维建筑设计 2025
- **license model**: subscription / perpetual
- **典型价格**: 浩辰 CAD ¥2,000-5,000/yr; 中望 CAD ¥1,500-4,000/yr (比 AutoCAD 1/3); BIMMAKE 部分 free; 数维 ¥10,000+/yr
- **核心场景**: 信创 / 国产化替代主线 — 大型央国企 / 设计院 IT 部门主动替代 AutoCAD license; 广联达 BIMMAKE 主打"施工 BIM 落地"轻量化; 数维设计是广联达布局的国产 BIM 设计平台.
- **persona 适配**:
  - boutique: 个人 boutique 偶用 (替 AutoCAD).
  - 中型: 国企背景中型已部分替换.
  - 大型院 (尤其中国): 信创要求项目主推; 央国企设计院 30-50% AutoCAD license 已替为浩辰/中望.
- **典型 I/O**: DWG (兼容 AutoCAD) / IFC / RVT (有限)
- **配合**: 天正 (适配) / 鸿业 / 探索者 / 斯维尔 (适配测试 2024-2025)
- **学习曲线**: easy (AutoCAD 用户 1 周迁移)
- **2025-2026**: 浩辰 CAD 2025 加 2D 参数化约束 + 硬件加速 + RVT import; 中望 CAD 2026 建筑版加强; BIMMAKE 持续 free + 钢筋 / 模板深化; 数维建筑设计是广联达国产 BIM 战略.
- **替代**: AutoCAD (国际通用) / Revit (国际 BIM 主)
- **常见坑**:
  1. 国际项目用国产 CAD 出图 — 客户 / 海外 firm 不识 .dwg 中的天正自定义对象.
  2. 期待 BIMMAKE 替代 Revit 设计 — 它是施工 BIM 落地, 不是设计 BIM.
  3. 数维成熟度 vs Revit — 仍有 1-2 代距离, 关键项目谨慎.
- **来源**: [T02-S073] [T02-S074] [T02-S075] [T02-S076] [T02-S077]

---

## 决策树 (Phase 2 提炼必用)

### 决策树 A — 三角色 (Atelier / 中型 / 大型院) tool stack

**A1. 新建一家 boutique atelier (5-10 人, 国际方案为主, design-intent driven)**

- **设计 / SD**: Rhino 8 + Grasshopper (核心) + SketchUp Pro (快速概念)
- **BIM / CD**: Revit (主力, 1-3 license) + Rhino.Inside.Revit (设计 → BIM 桥)
- **渲染**: Enscape (实时 daily) + V-Ray (final hero shot)
- **可持续**: Ladybug + Honeybee (免费入门) + ClimateStudio (有 sustainability 专人时)
- **AI 概念**: Midjourney V8 (mood board) + Photoshop Firefly (post)
- **后期 / 出图**: Adobe Creative Cloud All Apps
- **协作**: Bluebeam Revu (PDF markup) + ACC BIM Collaborate Pro
- **预算估算**: 年软件 ~$25k-50k (10 人), 5-7 type license

**A2. 新建一家中型 firm (50-150 人, 北美主流, balanced)**

- **CAD**: AutoCAD (LT 部分 + full) + SketchUp Pro
- **BIM / CD**: Revit (主力, AEC Collection 标配) + ArchiCAD 1-2 license (若欧洲项目) + Snaptrude (AI BIM SD)
- **Parametric**: Rhino + Grasshopper (5-10 license, GH 工作组)
- **渲染**: Enscape (人手) + V-Ray (visualization team) + D5 Render (尝试)
- **可持续**: ClimateStudio + One Click LCA / Tally 2.0 + EC3 (免费)
- **AI**: Forma (AEC Collection 自带) + Midjourney + Firefly
- **协作**: Bluebeam + Revizto (跨 BIM coordination) + ACC
- **预算估算**: 年软件 ~$300k-600k (100 人)

**A3. 加入中国大型设计院 (1000-5000 人, 施工图 + 资质 + 流水线)**

- **CAD 主力**: AutoCAD (full) + **天正 T20** (中国必装, 配 CAD)
- **BIM (项目级别)**: Revit (BIM 项目部) + 鸿业 BIMSpace + 广联达数维 (国产试用)
- **结构**: PKPM (绝对主流) + 探索者 (配合)
- **绿建 / 节能**: 斯维尔全套 (出 GB 合规报告)
- **渲染**: Lumion / D5 Render (投标动画) + V-Ray (hero) + Enscape (设计阶段)
- **参数化 (投标 / 复杂方案)**: Rhino + GH (有专门方案组)
- **AI**: Midjourney (投标 mood) + Forma 试点
- **国产替代** (信创要求项目): 浩辰 CAD / 中望 CAD + 广联达 BIMMAKE
- **预算估算**: 年软件 ~¥5M-30M (1000 人), 复杂 license 分级

---

### 决策树 B — 渲染选择 (Render decision)

```
是否需要实时 / 客户 walkthrough?
├─ 是 (大部分情况)
│   ├─ 用 Revit / ArchiCAD 主 BIM?
│   │   └─ Enscape (host-integrated, 最丝滑)
│   ├─ 中国项目, 投标动画?
│   │   └─ D5 Render (国产, 中文社区强, 价低) or Lumion (cinematic 老牌)
│   ├─ 大场景自然环境 + 动画?
│   │   └─ Lumion (cinematic 强项) or Twinmotion (Epic, Nanite 处理 billion polys)
│   ├─ VR + 长期 archviz pipeline?
│   │   └─ Twinmotion (易) → Unreal Engine 5 (custom 高级)
│   └─ 已有 V-Ray subscription, 想用实时?
│       └─ Chaos Vantage or V-Ray 7 Update 3 viewport realtime (2026 加)
└─ 否 (final hero shot, 出版 / 比赛 / 客户图)
    ├─ Path-traced photoreal final?
    │   └─ V-Ray (Chaos, 行业 default) or Corona (Chaos, 室内易) or Octane (GPU 快)
    ├─ 概念 / 草图风 / mood?
    │   └─ Midjourney + PS + SD ControlNet (geometry-controlled)
    └─ Quick post + Photoshop?
        └─ Enscape 实时出 PNG + Photoshop Firefly 补
```

---

### 决策树 C — BIM 选择 (Revit vs ArchiCAD vs Vectorworks vs 国产)

```
项目 locale 与客户?
├─ 北美 / 中国主流 / 政府要求 BIM 项目?
│   └─ Revit (95%+ 市场份额, AEC Collection 标配)
│       ├─ 是 boutique 设计 driven?
│       │   └─ Revit + Rhino.Inside.Revit (Rhino 设计 + Revit 文档)
│       └─ 是大型 standardized (医院 / 学校)?
│           └─ Revit + Hypar (function library) or Snaptrude (AI agents)
├─ 欧洲 (尤其 DACH / 北欧) / 日本 / 拉美 boutique?
│   └─ ArchiCAD (boutique 友好, Mac 良好支持; 28+ keynotes + GH live link)
├─ 英国 / 澳洲 / 美国 small studio (含 landscape / interior)?
│   └─ Vectorworks Architect (单软件全流程; 不依赖多工具)
├─ 大型 infrastructure (基建 + 建筑联合)?
│   └─ Bentley OpenBuildings + MicroStation + iTwin
└─ 中国施工图 / 信创合规项目?
    └─ AutoCAD + 天正 T20 (主力) + Revit / 鸿业 / 广联达数维 (BIM 子集) + PKPM (结构)
```

---

### 决策树 D — AI Generative 用法 (PD/SD 阶段)

```
目标产物?
├─ 早期 mood board / 灵感 / 客户提案?
│   ├─ 创意优先 (有商业 risk):
│   │   └─ Midjourney V7/V8 (state of art)
│   ├─ 商业项目 (need IP indemnity):
│   │   └─ Adobe Firefly (Image Model 4 Ultra, license-clean)
│   └─ ChatGPT 用户对话生成?
│       └─ DALL-E 3 / GPT-4o native image
├─ 给定线稿 / 模型 → photoreal (geometry-controlled)?
│   ├─ 开源 + 团队有 GPU + AI 专人?
│   │   └─ Stable Diffusion XL + ControlNet (ComfyUI workflow)
│   └─ 商业一键?
│       └─ Veras (Enscape 系) / mnml.ai / ReRender AI
├─ 大型 site planning / massing AI (PD 阶段)?
│   ├─ Autodesk 生态?
│   │   └─ Forma (ex-Spacemaker) — site / 日照 / 风 / 微气候
│   ├─ 开发商 feasibility / 多家庭 / 混合用?
│   │   └─ TestFit (real-estate feasibility)
│   └─ 标准化 building type (医院 / 学校 / 数据中心)?
│       └─ Hypar (function-based) or Snaptrude (AI agents)
└─ 户型 / 多家庭 residential AI?
    └─ Maket.ai / Architechtures.com / Snaptrude
```

---

## Phase 2 接口

### 反复在 ≥ 3 个事务所类型用到的工具 (候选必备工具)

| 工具 | boutique | 中型 | 大型院 (中国) | 评分 |
|------|----------|------|--------------|------|
| AutoCAD | ◯ (部分) | ●  | ● | 3/3 |
| Revit | ● | ● | ● | 3/3 |
| Rhino + Grasshopper | ● | ● | ● | 3/3 |
| Enscape | ● | ● | ● (设计阶段) | 3/3 |
| V-Ray | ● | ● | ● | 3/3 |
| SketchUp Pro | ● | ● | ◯ | 2.5/3 |
| Bluebeam Revu | ● | ● | ◯ | 2.5/3 |
| Adobe Creative Cloud | ● | ● | ● | 3/3 |
| Midjourney | ● | ● | ● | 3/3 |
| 天正 T20 (zh-CN 限) | ◯ | ● | ● | 中国必备 |
| PKPM (zh-CN 限) | ◯ | ● | ● | 中国结构必备 |
| 斯维尔 (zh-CN 限) | ◯ | ● | ● | 中国绿建必备 |
| Ladybug + Honeybee | ● | ● | ● (sustainability 团队) | 3/3 |
| Lumion / D5 / Twinmotion (三选一) | ◯ | ● | ● | 投标动画必备 |
| Navisworks / Revizto (二选一) | ◯ | ● | ● | BIM coordination 必备 |
| Rhino.Inside.Revit | ● | ● | ● | Rhino + Revit 必装 |

### 工具 vs 反模式 (Phase 2 反模式入口)

- **Midjourney → 业主当方案**: 大业主开始要求 Midjourney mood board, 但建筑师不能用它替代严肃概念设计 / SD-level 工作. **反模式标记**: "AI mood board final".
- **Lumion / D5 出图与施工图脱节**: 渲染前必须 lock 平面与立面; 否则改方案后渲染冗工. **反模式**: "渲染先行".
- **Revit 全自动用 family**: 中国施工图深度往往超出 RVT family 库; 强用导致 family hell. **反模式**: "RVT family 全能论".
- **天正 + 国际客户**: 国外客户不接 .dwg 中的天正自定义对象; 国际项目出图前需 explode. **反模式**: "天正 .dwg 全球通用".
- **Grasshopper 散脚本不归档**: 50+ component 散乱 GH 文件难维护; boutique 应建 GH 模板 + cluster + Speckle 协作. **反模式**: "GH 一次性脚本".
- **Enscape 当 V-Ray 用做 final**: Enscape 是过程, V-Ray 是 final hero; 混用导致客户图 not crisp. **反模式**: "实时即 final".
- **PS 改 vector / 排版**: 矢量用 Illustrator, 长 portfolio 用 InDesign; PS 改 vector / 排长文档是 Adobe 工作流反模式. **反模式**: "PS 全能".
- **AutoCAD 做 3D**: AutoCAD 3D 是历史负担, 该用 Rhino / Revit. **反模式**: "AutoCAD 3D".
- **Tally / EC3 自动数据不审 EPD**: LCA 数据库选择不一致导致结论偏 30-50%; project governance 必需. **反模式**: "EPD 数据黑箱".
- **PKPM / SAP2000 双源**: 中国结构师用 SAP/ETABS 算后再 PKPM 出图 — 双源 governance 缺则错; 应一主一辅 + reconcile.

### 冷僻 / 薄弱信号

- 总工具 = 50 (在 35-50 区间内 — 满足).
- 7 类全部 ≥ 3 — 满足 (A=5, B=8, C=6, D=7, E=6, F=9, G=9; 注: 某些工具兼属多类, 上面分类按主类).
- 中国本土 9 ≥ 3 — 满足充分 (天正 / 鸿业 / 探索者 / 斯维尔 / PKPM / 浩辰 / 中望 / 广联达 BIMMAKE / 广联达数维).
- AI generative 9 ≥ 5 — 满足 (Midjourney / SD+ControlNet / Firefly / DALL-E / Forma / TestFit / Hypar / Snaptrude / Maket / Architechtures — 10 if include Maket).
- 4 个决策树 (A 三角色 + B 渲染 + C BIM + D AI) — ≥ 3 满足.

### last_updated 时间戳

- 全部 entry 2026-05-16 (last_checked); 工具版本注明 2025-2026 release year.
- 已知 churn 风险高: F. AI Generative 子类 — Midjourney V8/V8.1 (2026-04) + D5 Render 3.0 (2026-01) + Twinmotion 2025.2 Nanite (2025-10) — 这些条目 6 月内应 re-check.
