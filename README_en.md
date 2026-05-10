<div align="center">

# 🎓 master-skill &nbsp;[![Tweet](https://img.shields.io/badge/share%20on-Twitter%2FX-000000?style=flat-square&logo=x)](https://twitter.com/intent/tweet?text=master-skill%20%E2%80%94%20give%20it%20an%20industry%2C%2030-60%20min%20later%20it%20auto-distills%20a%20loadable%20Master%20OS%20skill.%20Plug%20into%20any%20AI%20agent%2C%20instantly%20become%20%22the%20senior%20practitioner%20of%20that%20field.%22&url=https%3A%2F%2Fgithub.com%2Fvoidborne-d%2Fmaster-skill&hashtags=ClaudeCode%2CAIAgent%2CMasterSkill%2COpenSource)

> *"Next step — don't just distill a person. Distill an entire industry."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) distills **one person** into AI.<br>
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) distills **anyone's way of thinking** into AI.<br>

But some things are bigger than one person —<br>
**an entire industry's senior judgment, workflows, and tool stack.**

<br>

master-skill doesn't distill a single person.<br>
It distills **the cognitive operating system of a whole industry.**

<br>

Tell it the sub-niche you work in,<br>
and 30-60 minutes later, it auto-runs research, distillation, skill generation, plus a bash command suite.<br>

Drop into any AI agent — from that moment on,<br>
**it is the most senior practitioner in that field.**

<br>

> **With master-skill, you don't need to install any other skill —**<br>
> **it auto-distills the right one for your industry.**

<br>

[🚀 Install](#-install) · [✨ Demos](#-demos) · [🛠️ Auto-distilled bash tools](#️-auto-distilled-bash-command-suite) · [🧬 Lineage](#-three-generation-lineage) · [⭐ Distilled industries](#-distilled-industries)

[**中文 README →**](README.md)

</div>

---

> 🆕 &nbsp;**2026.05.10 — 12th industry: iOS App Store launch** — the first **platform-specific + dual-compliance + 12-month-mandatory-deadline** industry. Apple App Review is a black box (industry estimate 20-40% rejection rate), so this skill distills **how to reduce rejection rate + recover fast** instead of "guaranteed approval." Overseas Apple-only review vs mainland China's 4-step (ICP + Algorithm + Game-license + 8-10 domestic marketplaces) is non-fungible. **Skips person sub-skills** per user direction (validates the skip_sub_skills flag).
>
> 🆕 &nbsp;**2026.05.09 — 11th industry: Monetizing AI agents** — distilled the emerging commercial niche (high volume but terrible signal-to-noise; 90% is hype). 5 schools openly contradict each other (B2B SaaS / Indie hacker / Consulting / VC observer / China) — distillation preserves disagreement, doesn't average. 3 cross-school person sub-skills: **Bret Taylor** (Sierra B2B) + **Pieter Levels** (Indie extreme) + **Hamel Husain** (Consulting + evals).
>
> 🆕 &nbsp;**2026.05.08 — 10th industry: Bazi metaphysics / Chinese fortune-telling** — the first **semi-sensitive + school-divergent** industry distilled. Five schools (子平派 Ziping / 盲派 Mangpai / 五术派 Wushu / 新派 Newschool / 学院派 Academic) give different readings of the same chart, and the skill **preserves disagreement instead of averaging**. The 2026-01-01 amendment to China's Public Security Administration Punishment Law (Article 27, business-side compliance) is baked into the decision rules. 3 cross-school person sub-skills shipped: **段建业** (mainland Mangpai) + **倪海厦** (Hong Kong/Taiwan five-arts) + **梁湘润** (子平 academic-track).
>
> 🔥 &nbsp;**2026.05.05 — v1.4 quality upgrade** — before, when an agent claimed "86% of my sources are first-hand," it was self-grading on the honor system. Now every URL is auto-classified, every skill must clear 16 quality checks, and known content farms (Zhihu / WeChat blogs / G2 / Capterra etc.) are hard-blocked at intake. **You can't distill garbage anymore.** Plus a 9th end-to-end industry — **insurance brokers / agents (China)**.
>
> 📢 &nbsp;**2026.05.02 release** — generated skills don't just talk; they ship with a bash command suite. [Release notes →](https://github.com/voidborne-d/master-skill/releases/tag/v1.1)
>
> 🔥 &nbsp;**2026.05.02 public** — first complete industry (LLM agent infrastructure) verified end-to-end.

---

## ✨ Demos

> Not a search engine. **The senior practitioner of this field, sitting next to you, right now.**

#### 🤖 Demo 1 · LLM agent infrastructure

```
You    ❯ Should we migrate this RAG system to Vespa?

Master ❯ This is a "framework as scaffolding vs. concrete" judgment.

         First check whether the retrieval bottleneck actually
         lives at Vespa, or upstream in the embedding model. If
         it's the embedding model, migrating is pouring concrete
         around scaffolding — six months of model churn will make
         you want to swap again.

         If retrieval is genuinely the wall: Vespa beats Pinecone
         on native hybrid-search support, but has your ops stack
         already absorbed its ZooKeeper / Tensor complexity? The
         senior take here — Filtering speed × Index size × Team Op
         overhead, you pick two. Where's your bottleneck?

         Production cases: [3-4 real migration writeups + links]
```

#### 🛒 Demo 2 · Cross-border e-commerce (Amazon DE)

```
You    ❯ Launching a new category on Amazon Germany — where do I start?

Master ❯ Three things on DE differ completely from US — answer first:

         1) VAT one-stop reporting: OSS or per-country?
            This decides whether you can use Pan-EU FBA.
         2) Packaging law (VerpackG) + WEEE/battery registration?
            Without it, your listing gets reported and pulled day 1.
         3) GS vs CE — is your category GS-mandatory?
            This decides whether you reach Idealo / price-comparison flow.

         These aren't compliance checklists — they're hard gates on
         "can you sell at all". Once cleared, do keyword research with
         Helium 10's German pack — don't translate from US wordbanks;
         German search has much higher long-tail density.
```

#### 🎬 Demo 3 · Short-video paid ads

```
You    ❯ ROAS just won't go up — is it the bidding strategy?

Master ❯ Bidding is the consequence, not the cause. Creative first:

         What's your 3-second hold rate on cold audience? Below 35%
         and tweaking bids does nothing — the platform's exploration
         budget won't push volume to a creative that won't hold.

         Once creative is clean, look at targeting. The senior take
         here — "good creative × right targeting × bidding", get the
         order wrong and the last two just burn budget. Show me your
         creative-asset curve from the last 7 days.
```

**This isn't stuffing wiki into a prompt** — it's giving you judgment using **the field's mental models + decision rules**.

Every generated skill ships with an **Agentic Protocol** — when faced with a new problem, the agent first researches it the way a senior practitioner would, then applies the OS to deliver judgment. **Not just sounding like a pro. Acting like one.**

---

## 🛠️ Auto-distilled bash command suite

> This is what sets master-skill apart from colleague / nuwa — what gets distilled isn't just "how to talk", it's "how to do".

Every generated skill **includes a `cli/` subtree by default** — the cognitive OS materialized as runnable command-line tools:

```
{industry}-master/
└── cli/
    ├── protocol/agentic.sh        # New problem → walk N research dimensions → output report
    ├── decision/{topic}.sh        # Decision tree (clustered playbook rules)
    └── workflow/{slug}.sh         # SOP walkthrough + failure-mode self-check
```

Every script supports four standard flags: `--help` / `--explain` (show the backing mental model) / `--dry-run` / `--json` (machine-readable output).

```bash
# New problem: "should we migrate the RAG system to Vespa"
$ ./cli/protocol/agentic.sh
# → walks 5 research dimensions → generates report

# Selection decision
$ ./cli/decision/framework-select.sh

# Walk a full workflow + self-check failure modes
$ ./cli/workflow/build-rag-agent.sh

# Show the backing mental model (no interaction, just print)
$ ./cli/decision/framework-select.sh --explain
```

**Pure bash + system commands, zero external dependencies** (no jq, no Python). Auto-generated by [`tools/cli_writer.py`](tools/cli_writer.py) from the distilled synthesis — you don't write a line of code; the tools **grow directly out of** the industry's workflows and decision rules.

Full spec: [`references/cli-spec.md`](references/cli-spec.md).

---

## 🌐 Auto-invoke nuwa to distill the industry's top figures

> master-skill doesn't reinvent the wheel. The job of distilling top figures gets outsourced to nuwa-skill, results embed straight into `sub-skills/`.

```
{industry}-master/
├── SKILL.md
└── sub-skills/                       ← person sub-skills distilled by nuwa
    ├── {figure-1}/SKILL.md           ← e.g. Karpathy
    ├── {figure-2}/SKILL.md           ← e.g. Hamel Husain
    └── {figure-3}/SKILL.md           ← e.g. Eugene Yan
```

master-skill spawns 3 parallel subagents, each running nuwa-skill's full pipeline to produce one person sub-skill.

When the user later asks something that needs a specific figure's perspective, the agent loads the matching sub-skill — no full re-trigger of master.

See [SKILL.md Phase 3.3-3.5](SKILL.md) + [`prompts/sub-skill-figures.md`](prompts/sub-skill-figures.md).

---

## 📦 What gets distilled

The industry's cognitive operating system, not its encyclopedia. One skill packs four things:

- 🧠 &nbsp;**How a senior practitioner thinks** — mental models + decision rules
- ⚙️ &nbsp;**How they work** — current best-practice workflows, each step marked with decay timestamps
- 🛠️ &nbsp;**What tools they pick** — selection decision trees + anti-pattern checklists + **auto-generated bash command suite**
- 💬 &nbsp;**How they speak** — industry expression + outsider giveaways

The 7 layers extracted:

| Layer | What it is |
|---|---|
| **How they judge** | Mental models — the field's lens |
| **How they decide** | Standard decision rules — fast "if X, then Y" heuristics |
| **What they use** | Tool stack + selection tree + anti-pattern checklist |
| **How they work** | Workflows, each step marked with "from 2026-04 onward this step changes to Y" timestamps |
| **How they speak** | Industry expression — jargon, cadence, outsider giveaways |
| **What they avoid** | Anti-patterns — the mistakes only outsiders make |
| **What they don't know** | Honest boundaries — info cutoff, fastest-decaying modules |

### Honest boundaries

Every skill explicitly states what it can't do:

- Tools and workflows decay fastest — refresh every 3-6 months
- Regulation and standards decay even faster — must update within 12 months
- master-skill **can't replace real production experience** — it gives cognitive frameworks, not incident response runbooks

**A skill that won't tell you its limits doesn't deserve trust.**

---

## 🔍 Why trust what it distills

> A new skill comes online — how do I know it isn't making stuff up?

**16 automatic checks. No pass, no ship.** Every generated skill must answer:

- ✅ **Are the sources really first-hand?** — every URL is auto-classified (academic papers / official docs / authors' own blogs / vendor docs count as first-hand; news coverage / second-hand summaries count as secondary; Zhihu / WeChat blogs / Baidu Baike / CSDN / G2 / Capterra / content farms are **rejected outright**)
- ✅ **Can the "this company is a big deal" claims be cross-referenced?** — every backbone conclusion needs ≥ 2 independent sources (different person / different platform); single-source claims are auto-demoted to a "fast rules" section, never enter the core mental models
- ✅ **Are the sources recent enough?** — every source carries a date; anything over 18 months gets auto-half-discounted
- ✅ **Did the mental models really appear in the source material?** — after the skill is written, the tool greps back through the research notes; any conclusion that can't be traced to original wording gets flagged
- ✅ **What if the industry is too obscure for public sources?** — auto-detects "public material is too thin" and switches to deep-research mode: asks you for internal materials + auto-pulls from industry associations / regulator filings / job descriptions / university course syllabi as multi-source backup, instead of bluffing

**Result**: the insurance broker prototype — 73 sources, 67 first-hand (91.8%), 0 blacklisted, 0 self-grading; 16 checks → 14 perfect + 1 partial pass + 0 fails.

---

## ⚡ Install

```bash
# Claude Code
git clone https://github.com/voidborne-d/master-skill.git ~/.claude/skills/master-skill
```

<details>
<summary><b>🛠️ Other host paths</b></summary>

<br>

```bash
git clone https://github.com/voidborne-d/master-skill.git <TARGET>
```

| Host | `<TARGET>` path |
|------|-----------------|
| 🟣 Claude Code | `~/.claude/skills/master-skill` |
| 🔵 OpenClaw | `~/.openclaw/skills/master-skill` |
| ⚫ Codex | `~/.codex/skills/master-skill` |
| 🟠 Hermes | after clone, `python3 tools/install.py install --host hermes` |

Install to all hosts at once: `python3 tools/install.py install --host all`

</details>

---

## 🚀 Usage

In an agent with master-skill installed, just say:

```
> Build me a master skill for LLM agent infra
> I work in cross-border e-commerce, distill it for me
> I do foot-and-ankle surgery, give me a master OS

> update master LLM-agent-infra      # incremental refresh after 6 months
```

master-skill confirms 6 things with you (industry / sub-niche / region / your role / any first-hand materials / new vs update), then launches **6-track parallel research**: industry figures / tool map / workflows / canon / sources / glossary.

30-60 minutes later you get an `{industry}-master` directory. Drop it into any agent — it instantly enters "the senior practitioner of that field" mode.

### 🎛️ Calling the generated skill

```
> Use llm-agent-infra-master to evaluate this framework choice
> Use cross-border-ecommerce-master to look at my Amazon listing
> Run llm-agent-infra-master's framework-select decision tree
```

### 💻 CLI pipeline

```bash
# End-to-end: research → cold-detect → write skill → quality check → install
python3 tools/research/merge_research.py merge --skill-dir ./prototype/
python3 tools/research/cold_detector.py --skill-dir ./prototype --stage wave1
python3 tools/skill_writer.py create --skill-dir ./output ...
python3 tools/research/quality_check.py check --skill-dir ./output
python3 tools/install.py install --host claude --source ./output

# 6 months later, incremental refresh
python3 tools/update_skill.py plan --skill-dir <existing-skill>
# (agent re-runs the marked tracks)
python3 tools/update_skill.py finalize --skill-dir <skill>
```

---

## ⭐ Distilled industries

Every one is end-to-end runnable, with full research data + generated SKILL.md + a working bash tool suite:

| Industry | Category | Language | Path |
|------|------|------|------|
| 🔥 **LLM agent infrastructure** | Technical | English | [llm-agent-infra-master/](prototypes/llm-agent-infra-master/) |
| ✅ **Cross-border e-commerce** | Commercial | Chinese | [cross-border-ecommerce-master/](prototypes/cross-border-ecommerce-master/) |
| ✅ **Xiaohongshu operations** | Content ops | Chinese | [xiaohongshu-ops-master/](prototypes/xiaohongshu-ops-master/) |
| ✅ **Short-video paid ads** | Commercial + algo | Chinese | [short-video-ads-master/](prototypes/short-video-ads-master/) |
| ✅ **SEO expert** | Semi-technical | Chinese | [seo-master/](prototypes/seo-master/) |
| ✅ **Love coach** | Soft skills | Chinese | [love-coach-master/](prototypes/love-coach-master/) |
| ✅ **Foot-and-ankle surgery** | Medical (regulated) | Chinese | [foot-ankle-surgery-master/](prototypes/foot-ankle-surgery-master/) |
| ✅ **Chinese law practice** | Legal (regulated) | Chinese | [china-law-master/](prototypes/china-law-master/) |
| ✅ **Insurance broker / agent** | Finance (regulated) | Chinese | [insurance-broker-cn-master/](prototypes/insurance-broker-cn-master/) |
| ✅ **Bazi metaphysics / fortune-telling** | Traditional culture (semi-sensitive) | Chinese | [bazi-metaphysics-master/](prototypes/bazi-metaphysics-master/) |
| ✅ **Monetizing AI agents** | Emerging commercial | Global | [monetize-agents-master/](prototypes/monetize-agents-master/) |
| 🆕 **iOS App Store launch** | Platform-specific (high policy churn) | Global + Chinese | [ios-app-launch-master/](prototypes/ios-app-launch-master/) |

12 industries cross-cutting technical / commercial / content ops / soft skills / medical / legal / finance / traditional culture / emerging commercial / platform-specific — master-skill handles even cases where five schools openly disagree (emerging commercial) or where 12-month policy deadlines are enforced (platform-specific).

**What's inside the latest "iOS App Store launch" deliverable**:

- 169 sources, 70.4% first-hand, 0 blacklisted
- 6 core mental models (**Apple App Review is a black box** / **Dual compliance is non-fungible** (overseas vs mainland China) / **Policy decay is fast** / **ASO data-driven vs Indie audience-first** / **30% Apple Tax is a fact** / **Rejection is daily**)
- 10 decision rules, including a dedicated path for the China 4-step compliance: ICP filing + Algorithm filing + Game license number + 8-10 domestic Android marketplaces' separate review
- 12 real-industry dialogue samples (4 registers: peer / user-education / anti-Apple / counter-example × 6 schools covered)
- 5 ready-to-run bash decision scripts (rejection handling / ASO choice / region strategy / monetization model / China compliance)
- A complete **6-school comparison matrix** (Apple official / Overseas Indie / Big-co release engineering / ASO optimization / Anti-Apple antitrust / China compliance)

**User directive**: this iOS deliverable **skips person sub-skill distillation** (saves 1 cron cycle), while keeping the 16-figure landscape research as part of the industry's cognitive map. This validates master-skill's `skip_sub_skills` flag — the deliverable is still complete (research + synthesis + SKILL.md + cli + full QC suite).

All four QC checks PASS:
- mechanical rubric: 13 perfect + 1 partial + 0 fail (16 items)
- claim verifier: 16 supported / 0 weak / 0 unsupported
- source manifest: 0 violation
- cross-prototype regression: 0 issue across all 12 skills

**Sensitivity note**: iOS App Store launch is a black-box review industry (industry estimate 20-40% rejection rate). Any "guarantee approval / proxy submission" service is a scam. What this skill distills is **the cognitive framework for reducing rejection rate + recovering quickly + multi-region compliance** — not "guaranteed approval" promises. Six honest-boundary clauses include "no fraudulent shortcuts" (no fake reviews / no using TestFlight public links as a release / no Chinese license-number gray market / no protesting the 30% tax instead of accepting it).

The research process is **fully transparent** — every prototype includes complete six-track research notes + the synthesis document, every mental model and decision rule traceable to its sources.

Want an industry not on the list? Install master-skill, say "build a master skill for XXX".

---

## 🔬 How it works

You give it a sub-niche, master-skill does the following:

```
1. Industry intake          ← Pushes back when granularity is bad ("AI" → "LLM agent infra")
2. Create skill directory   ← All artifacts inside, self-contained
3. 6-track parallel research ← 6 subagents: figures / tools / workflows / canon / sources / glossary
   ─ Research review gate   ← You confirm research quality before continuing — bad input doesn't poison downstream
4. Framework synthesis      ← Triple-gate validation (cross-scenario / generative power / exclusivity) blocks generic platitudes
   ─ Synthesis review gate  ← You confirm the cognitive frame before generation
5. Write the skill          ← Generate full directory, invoke nuwa for sub-skills, emit bash tools
6. Three-test verification  ← Known-question / edge-case / voice blind tests
7. Two-agent refinement     ← Optimize the "activates and acts" quality
```

Full spec in [SKILL.md](SKILL.md) — 524 lines of agent-loadable workflow. Methodology in [references/extraction-framework.md](references/extraction-framework.md) — triple-gate validation, three-tier tool extraction, school-of-thought handling, decay-rate table.

---

## 🧬 Three-generation lineage

master-skill stands on two shoulders:

- **[colleague-skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — gave us the meta-skill pattern: intake → multi-source collect → analyze → write.
- **[nuwa-skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — gave us 6-agent parallel research + triple quality gates. **master-skill calls nuwa in Phase 3 to distill the top 3 figures of the industry as sub-skills.**

Three of one lineage, scaling outward.

---

## 📂 Project structure

```
master-skill/
├── SKILL.md                          # the master itself (core workflow spec)
├── prompts/                          # prompt system
│   ├── intake.md                     #   industry intake + cold-niche deep-mode 2nd intake
│   ├── synthesis.md                  #   distillation guide (incl. Step 5b dialogue sample library)
│   ├── quality_check.md              #   16-item mechanical rubric
│   ├── sub-skill-figures.md          #   subagent template for invoking nuwa
│   └── research/
│       ├── _source_id_manifest.md    #   global source-ID convention + Surrogate Sources Policy
│       └── 01-06.md                  #   six-track research prompts (incl. voice_samples field)
├── tools/                            # Python tooling
│   ├── skill_writer.py               #   generate skill directory
│   ├── cli_writer.py                 #   generate bash tool subtree
│   ├── update_skill.py               #   incremental refresh
│   ├── install.py                    #   four-host installer
│   ├── self_test.py                  #   regression tests across all prototypes + tools
│   ├── research/                     # quality guardrails (new in v1.4)
│   │   ├── source_verifier.py        #   per-URL auto-classify + black/whitelist
│   │   ├── source_manifest.py        #   source ledger + consistency enforcement
│   │   ├── claim_verifier.py         #   reverse-check every SKILL.md conclusion against source notes
│   │   ├── cold_detector.py          #   obscure-industry auto-fallback (deep-research mode)
│   │   ├── refresh_sources.py        #   periodic source-liveness check
│   │   ├── quality_check.py          #   16 automatic checks
│   │   └── merge_research.py         #   research review aggregator
│   ├── collectors/                   # auto-pull industry seed material
│   │   ├── github / arxiv / RSS / podcast (4 collectors)
│   │   └── regulator / association / job-desc / syllabus (cold-niche fallback, 4 collectors)
│   ├── ingest/                       # parse industry reports / papers / course slides
│   │   └── PDF / EPUB / PPTX one-shot ingest
│   └── transcribe/                   # video / podcast transcription
│       ├── youtube.sh / local_video.sh   # caption pull + local-video transcription
│       └── caption cleaning / signal-density scoring / mention extraction
├── references/
│   ├── skill-template.md             #   standard structure for generated skills
│   ├── extraction-framework.md       #   distillation methodology (triple-gate / decay table / schools)
│   └── cli-spec.md                   #   bash tool design spec
└── prototypes/
    └── 9 complete industry samples   #   see "Distilled industries" above
```

---

## ⚠️ Notes

**Research material quality = skill quality**. Different research dimensions have different source priorities:

| Dimension | Source priority (high → low) |
|------|------|
| 🌟 Industry figures | Long-form by the figure themselves (book / long interview / blog series) **›** decision records (public commits / public statements) **›** secondary summaries |
| 🛠️ Tool map | Official docs **›** engineer-written production cases **›** training tutorials / SEO content |
| 📋 Workflows | Real flows on company engineering blogs **›** senior practitioner long interviews **›** training-org curricula |
| 📚 Canon | Reading lists from industry people (≥ 3 independent recommenders) **›** academic surveys **›** secondary book reviews |
| 📰 Sources | Industry-people subscription lists **›** mainstream long-form journalism **›** content farms |

- In Chinese-language environments, Zhihu / WeChat blogs / Baidu Baike / CSDN are auto-excluded (unless author-original)
- The earlier the info cutoff, the faster the tools/workflows modules decay — use `update master X` to incrementally refresh
- This is v1.1 and still iterating fast. Found a bug? Open an issue.

---

## 📄 Roadmap

| Version | Content | Status |
|------|------|------|
| v0.1-0.4 | Workflow spec + prompts + tooling + polish | ✅ |
| v1.0 | First complete sample (LLM agent infra), public repo | ✅ |
| v0.6 | Bash tool pipeline — generated skills ship with command suite | ✅ |
| v1.1 | Cross-skill calls + incremental refresh + Chinese samples | ✅ |
| v1.2 | Auto-clustered decision-tree topics + scheduled refresh + 5 industry samples (incl. Xiaohongshu / SEO / love coach) | ✅ |
| v1.3 | Short-video paid ads / foot-and-ankle surgery / law = 8 industries cross-cutting coverage | ✅ |
| v1.4 | **Quality guardrails + 9th industry** — auto-run 16 quality checks + URL verification + blacklist hard-block + cold-niche fallback (auto-pull from associations / regulators / job descs / course syllabi) + new **insurance broker / agent** sample | ✅ |
| v1.5 | **10th industry — Bazi metaphysics / fortune-telling** — first semi-sensitive + school-divergent industry; preserves disagreement instead of averaging when 5 schools give different readings; source_verifier extended with 4 zh-CN classical archives (ctext / guoxuedashi / wikisource / archive.org), benefiting all metaphysics + TCM + history canon work going forward | ✅ |
| v1.6 | **11th + 12th industries — Monetizing AI agents + iOS App Store launch** — emerging commercial (high volume but terrible signal-to-noise, 5 schools openly contradicting) + platform-specific (12-month mandatory deadlines + dual compliance overseas vs mainland China). Validates `skip_sub_skills` flag (iOS launch skips person distillation per user, saves 1 cron cycle); iOS launch ships a 6-school comparison matrix (Apple / Indie / Big-co release engineering / ASO / Anti-Apple / China compliance) | ✅ |
| v2.x | PyPI packaging / GitHub Action auto-update / multi-language docs / tool marketplace | 🔲 |

See [ROADMAP.md](ROADMAP.md).

---

## 📜 License

MIT — use it, fork it, ship with it.

<div align="center">

<br>

**🧬 colleague-skill** distills what **one specific person** does.<br>
**🌟 nuwa-skill** distills how **anyone** thinks.<br>
**🎓 master-skill** distills **an entire industry's** cognition + workflows + tools.<br>

<br>

*Distill an entire industry's senior expertise into one skill.*

<br>

MIT License © [voidborne-d](https://github.com/voidborne-d) · [中文 README](README.md) · English README

</div>

---

## ⭐ Star History

<a href="https://www.star-history.com/?repos=voidborne-d%2Fmaster-skill&type=date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=voidborne-d/master-skill&type=date" />
 </picture>
</a>
