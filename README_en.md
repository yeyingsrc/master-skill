<div align="center">

# 🎓 master-skill

> *"Why stop at distilling people? Distill an entire industry."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**master-skill distills an entire industry into one skill — the senior practitioner's judgment + the current best workflows + tool selection trees, packaged with an auto-generated bash command suite.**

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) proved that distilling one specific person is viable.
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) extended distillation from one person to anyone.
**master-skill pushes distillation to an entire industry — not just cognition, but workflows and runnable tools.**

Tell it your sub-niche. 30-60 minutes later, the full pipeline runs automatically: research, synthesis, skill generation, plus the bash tool suite. Drop into any AI agent — instantly enter "the senior practitioner of that field" mode.

<br>

[🚀 Install](#-install) · [✨ Demo](#-demo) · [🛠️ Auto-distilled bash tools](#️-auto-distilled-bash-command-suite) · [🧬 Lineage](#-lineage) · [⭐ Distilled industries](#-distilled-industries)

[**中文 README →**](README.md)

</div>

---

> 📢 &nbsp;**2026.05.02 release** — generated skills don't just talk; they ship with a bash command suite. [Release notes →](https://github.com/voidborne-d/master-skill/releases/tag/v1.1)
>
> 🔥 &nbsp;**2026.05.02 public** — first complete industry (LLM agent infrastructure) verified end-to-end.

---

## 🎯 What it does

[colleague-skill](https://github.com/titanwings/colleague-skill) distills **one specific person** into a skill (a coworker / friend / idol).
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) distills **anyone's way of thinking** (Jobs / Munger / Musk / Naval...).
**master-skill** distills **an entire sub-niche industry's cognitive OS** into a skill.

Each is a **10× leap**:

| | Scope | Output |
|---|---|---|
| 🧬 colleague-skill | **One** specific person | Skill that mimics work + persona of one person |
| 🌟 nuwa-skill | **Anyone** alive or historical | Skill that judges using their cognitive frame |
| 🎓 **master-skill** | **An entire** sub-niche field | Skill that turns the agent into "the senior practitioner of that field" |

---

## ✨ Demo

> Not a search engine. **The senior practitioner of this field, sitting next to you, right now.**

#### 🤖 Demo · LLM agent infrastructure

```
You    ❯ Should we migrate this RAG system to Vespa?

Master ❯ This is a "scaffolding vs. concrete" judgment.

         First check whether the retrieval bottleneck actually
         lives at the vector index, or upstream in the embedding
         model. If it's the embedding model, migrating is pouring
         concrete around scaffolding — six months of model churn
         will make you want to swap again.

         If retrieval is genuinely the wall: Vespa beats Pinecone
         on native hybrid-search, but has your ops stack already
         absorbed its ZooKeeper / Tensor complexity? The senior
         take here — Filtering speed × Index size × Team Op
         overhead, you pick two. Where's your pain?

         Production cases: [3-4 real migration writeups + links]
```

#### 🛒 Demo · Cross-border e-commerce (Amazon EU)

```
You    ❯ Launching a new category on Amazon Germany — where do I start?

Master ❯ Three things on DE differ completely from US — answer first:

         1) VAT one-stop reporting: OSS or per-country?
            This decides whether you can use Pan-EU FBA.
         2) Packaging law (VerpackG) + WEEE/battery registration?
            Without it, your listing gets reported and pulled day 1.
         3) GS vs CE certification — is your category GS-mandatory?
            This decides whether you can hit Idealo / price-comparison traffic.

         These aren't compliance checklists — they're hard gates
         on whether you can sell at all. Once cleared, do keyword
         research with Helium 10's German pack — don't translate from
         US wordbanks; German search has much higher long-tail density.
```

**This isn't stuffing wiki into a prompt** — it's giving you judgment using **the field's mental models + playbook**.

Every generated skill ships with an **Agentic Protocol** — when faced with a new problem, the agent first researches it the way a senior practitioner would, then applies the OS to deliver judgment. **Not just sounding like a pro. Acting like one.**

---

## 🛠️ Auto-distilled bash command suite

> This is what sets master-skill apart from colleague / nuwa — what gets distilled isn't just "how to talk", it's "how to do".

Every generated skill **includes a `cli/` subtree by default** — the cognitive OS materialized as runnable command-line tools:

```
{industry}-master/
└── cli/
    ├── protocol/agentic.sh        # New problem → walk N research dimensions → output markdown report
    ├── decision/{cluster}.sh      # Interactive decision tree from clustered playbook rules
    └── workflow/{slug}.sh         # SOP walkthrough + failure-mode self-check
```

Every script supports `--help` / `--explain` / `--dry-run` / `--json`. One command, structured output:

```bash
# New problem: "should we migrate the RAG system to Vespa"
$ ./cli/protocol/agentic.sh
# → walks 5 research dimensions → generates agentic-protocol-{date}.md

$ ./cli/decision/framework-select.sh
$ ./cli/workflow/build-rag-agent.sh

# See backing mental models / playbook (no interaction)
$ ./cli/decision/framework-select.sh --explain
```

Pure bash + POSIX coreutils — **zero external dependencies** (no jq, no Python). Auto-generated by [`tools/cli_writer.py`](tools/cli_writer.py) from the distilled synthesis — you don't write a line of code; the tools **grow directly out of** the industry's workflows and decision rules.

Full spec: [`references/cli-spec.md`](references/cli-spec.md).

---

## 🌐 Auto-invoke nuwa to distill top figures

> master-skill doesn't reinvent the wheel. The job of distilling industry top figures gets outsourced to nuwa-skill, results embed straight into `sub-skills/`.

```
{industry}-master/
├── SKILL.md
└── sub-skills/                       ← person sub-skills distilled by nuwa
    ├── {figure-1}/SKILL.md           ← e.g. Karpathy
    ├── {figure-2}/SKILL.md           ← e.g. Hamel Husain
    └── {figure-3}/SKILL.md           ← e.g. Eugene Yan
```

Master spawns **3 parallel subagents**, each running nuwa-skill's full 5-phase pipeline on one figure → person sub-skill embeds in.

When the user's question needs a specific figure's perspective, the agent loads the matching sub-skill — no full re-trigger.

See [SKILL.md Phase 3.3-3.5](SKILL.md) + [`prompts/sub-skill-figures.md`](prompts/sub-skill-figures.md).

---

## 📦 What gets distilled

Industry's cognitive operating system, not industry's encyclopedia. One skill packs four things:

- 🧠 &nbsp;**How they judge** — mental models + decision rules
- ⚙️ &nbsp;**How they work** — current best-practice workflows, each step marked with decay timestamps
- 🛠️ &nbsp;**What they use** — tool selection trees + anti-pattern checklists + **auto-generated bash command suite**
- 💬 &nbsp;**How they speak** — industry expression + outsider giveaways

The 7 specific layers extracted:

| Layer | What it is |
|---|---|
| **How they judge** | Mental models — the field's lens |
| **How they decide** | Standard decision rules — "if X, then Y" heuristics |
| **What they use** | Tool stack + selection tree + anti-pattern checklist |
| **How they work** | Workflows, each step marked with "Apr 2026 onward this step changes to Y" timestamps |
| **How they speak** | Industry expression — jargon, cadence, outsider giveaways |
| **What they avoid** | Anti-patterns — only outsiders make these mistakes |
| **What they don't know** | Honest boundaries — info cutoff, fastest-decaying modules |

### Honest boundaries

Every skill explicitly states what it can't do:

- **Tools / workflows** decay fastest (refresh every 3-6 months)
- **Regulation / standards** modules decay even faster (must update within 12 months)
- master-skill **can't replace real production debugging experience** — it gives cognitive frameworks, not incident response

**A skill that won't tell you its limits doesn't deserve trust.**

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

In a host with master-skill installed:

```
> Build me a master skill for LLM agent infra
> I work in cross-border e-commerce, distill it for me
> I do foot-and-ankle surgery, give me a master OS

> update master LLM-agent-infra      # incremental refresh after 6 months
```

master-skill confirms 6 dimensions with you (industry / sub-niche / region / role / local materials / new vs update), then launches a **6-track parallel research swarm**: figures / tools / workflows / canon / sources / glossary.

30-60 minutes later you get an `{industry}-master.skill` directory installable into any Claude Code / OpenClaw / Codex / Hermes agent — instantly turning it into "the senior practitioner of that field."

### 💻 CLI pipeline (5 commands end-to-end)

```bash
python3 tools/research/merge_research.py merge --skill-dir ./prototype/      # Phase 1.5
python3 tools/skill_writer.py create --skill-dir ./output ...                # Phase 3
python3 tools/research/quality_check.py check --skill-dir ./output           # Phase 4.4
python3 tools/install.py install --host claude --source ./output             # Deploy

# Incremental refresh (v1.1)
python3 tools/update_skill.py plan --skill-dir <existing-skill>
python3 tools/update_skill.py archive --skill-dir <skill>
python3 tools/update_skill.py mark-in-progress --tracks tools,workflows
# (agent re-runs selected tracks)
python3 tools/update_skill.py finalize --skill-dir <skill>
```

---

## ⭐ Distilled industries

Each is end-to-end runnable, with full research data + generated SKILL.md + executable bash tool suite:

| Industry | Language | Validation | bash scripts | Path |
|------|------|---------|-------------|------|
| 🔥 **LLM agent infrastructure** | English | 10 of 12 checks passed | 11 scripts | [llm-agent-infra-master/](prototypes/llm-agent-infra-master/) |
| ✅ **Cross-border e-commerce** | Chinese | mini scope (validation run) | 5 scripts | [cross-border-ecommerce-master/](prototypes/cross-border-ecommerce-master/) |
| 🔲 Short-video paid ads | Chinese | planned | — | (v1.x) |
| 🔲 Foot-and-ankle surgery | Chinese | planned | — | (v1.x) |

Research process is **fully transparent** — every prototype includes complete six-track research notes + the synthesis document, every mental model and decision rule traceable to its sources.

Want an industry not on the list? Install master-skill, say "build a master skill for XXX".

---

## 🔬 How it works

After you input a sub-niche, master-skill does these things:

```
1. Industry intake          ← Push back when granularity is bad ("AI" → "LLM agent infra")
2. Create skill directory   ← Self-contained, all artifacts inside
3. 6-track parallel research ← 6 subagents: figures / tools / workflows / canon / sources / glossary
   ─ Research review gate   ← User confirms quality before continuing
4. Framework synthesis      ← Triple-gate validation blocks generic platitudes
   ─ Synthesis review gate  ← User confirms the cognitive frame before generation
5. Write the skill          ← Generate full directory, invoke nuwa for sub-skills, emit bash tools
6. Three-test verification  ← Known / edge / voice blind tests
7. Two-agent refinement     ← Optimize "activates and acts"
```

Full spec in [SKILL.md](SKILL.md) — 524 lines of agent-loadable workflow. Methodology in [references/extraction-framework.md](references/extraction-framework.md) — triple-gate validation, three-tier tool extraction, school-of-thought handling, decay-rate table.

---

## 🧬 Lineage

master-skill stands on two shoulders:

```
🧬 colleague-skill   distills one specific person      scope: 1 person
🌟 nuwa-skill        distills a way of thinking        scope: anyone alive or historical
🎓 master-skill      distills an entire industry       scope: a sub-niche field
```

- **[colleague-skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — proved "distill a person" works. Source of the meta-skill pattern: intake → multi-source collect → analyze → write.
- **[nuwa-skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — proved "distill a way of thinking" beats "distill words." Source of the 6-agent parallel research + triple quality gates + research protocol architecture. **master-skill calls nuwa in Phase 3 to distill the top 3 figures of the industry as sub-skills.**

Three of one lineage, scaling outward — one person you know → anyone alive or dead → an entire field of human knowledge.

---

## 📜 License

MIT — use it, fork it, ship with it.

<div align="center">

<br>

**🧬 colleague-skill** distills what **one person** does.<br>
**🌟 nuwa-skill** distills how **anyone** thinks.<br>
**🎓 master-skill** distills an **entire industry** — cognition + workflows + tools.<br>

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
