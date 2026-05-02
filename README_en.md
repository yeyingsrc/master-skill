<div align="center">

# 🎓 master-skill

### *Stop hunting for the right skill.*
### *Tell us your industry — we hand you the only skill you'll need.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-v1.1-brightgreen)]()
[![Stars](https://img.shields.io/github/stars/voidborne-d/master-skill?style=social)](https://github.com/voidborne-d/master-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://github.com/voidborne-d/master-skill)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/voidborne-d/master-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/voidborne-d/master-skill)

<br>

<table>
<tr><td align="left">

🎯 &nbsp;**Switched industries** and don't know where to start? The senior practitioners' tacit knowledge isn't in any README.<br>
📰 &nbsp;**Information scattered** across 12 newsletters / 30 podcasts / 5 Discords, perpetually playing catch-up?<br>
🤖 &nbsp;**Stuffed an AI agent** with every PDF in the field — and it still sounds like an outsider, because "wiki ≠ how this field thinks"?

</td></tr>
</table>

### ✨ master-skill solves all three.

<br>

Not a Wikipedia stuffed into a prompt. **The cognitive operating system of "the senior practitioner sitting next to you, right now"** — mental models, decision heuristics, tool selection trees, current workflows, expression DNA, anti-patterns, honest boundaries.

**Tell it your sub-niche. 30-60 minutes later, you get an installable `{industry}-master.skill`.**

<br>

[🚀 Install](#-install) · [✨ Demo](#-demo) · [🛠️ Not just talk](#️-not-just-talk--cli-tool-stream-v06) · [🧬 Lineage](#-lineage) · [⭐ Distilled industries](#-distilled-industries-prototypes)

[**中文 README →**](README.md)

[![Star History Chart](https://api.star-history.com/svg?repos=voidborne-d/master-skill&type=Date)](https://star-history.com/#voidborne-d/master-skill&Date)

</div>

---

> 📢 **2026.05.02 — v1.1 ship** · CLI tool stream + cross-skill composition + incremental refresh.
> Generated skills aren't just conversational advisors — they ship with a bash command suite. [Release notes →](https://github.com/voidborne-d/master-skill/releases/tag/v1.1)

> 🔥 **2026.05.02 — v1.0 public** · LLM agent infra prototype runs end-to-end (Phase 4 PASS — 10 mech / 1 partial / 0 fail), repo public.

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

## 🛠️ Not just talk — CLI tool stream (v0.6+)

> "master-skill doesn't just tell you what to do — it ships a bash toolkit to help you do it."

Every generated `{industry}-master.skill` includes a `cli/` subtree — the cognitive OS materialized as command-line tools:

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

Pure bash 4 + POSIX coreutils — **zero external deps** (no jq, no Python). Auto-generated by [`tools/cli_writer.py`](tools/cli_writer.py) from synthesis. Full spec: [`references/cli-spec.md`](references/cli-spec.md).

---

## 🌐 Cross-skill composition (v1.1+)

> "master-skill doesn't reinvent the wheel. Phase 3 auto-invokes nuwa-skill to distill top 3 figures into sub-skills/."

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

Industry OS, not industry wiki. master-skill extracts 7 layers:

| Layer | What it is |
|---|---|
| **How they judge** | Mental models — the field's lens |
| **How they decide** | Standard playbooks — "if X, then Y" heuristics |
| **What they use** | Tool stack + selection tree |
| **How they work** | Workflows / SOPs marked with "Apr 2026 onward this step changes to Y" timestamps |
| **How they speak** | Expression DNA — jargon, register, outsider giveaways |
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

## ⭐ Distilled industries (Prototypes)

End-to-end sample skills, each with full research data + generated SKILL.md + executable cli/ tool stream:

| Industry | Locale | Phase 4 | CLI scripts | Path |
|------|--------|---------|-------------|------|
| 🔥 **LLM agent infra** | en (global) | ✅ PASS (10/12 mech) | 11 (1+6+3+lib+README) | [prototypes/llm-agent-infra-master/](prototypes/llm-agent-infra-master/) |
| ✅ **Cross-border e-commerce** | zh-CN | mini scope | 5 (1+1+2+lib+README) | [prototypes/cross-border-ecommerce-master/](prototypes/cross-border-ecommerce-master/) |
| 🔲 Short-video paid ads | zh-CN | planned | — | (v1.x) |
| 🔲 Foot-and-ankle surgery | zh-CN | planned | — | (v1.x) |

Research process is **fully transparent** — every prototype includes complete 6-track research notes + synthesis.md, traceable per mental model / playbook rule.

Want to distill an industry not on the list? Install master-skill, say "build a master skill for XXX".

---

## 🔬 How it works

After you input a sub-niche, master-skill does **5 things**:

```
Phase 0    Industry intake          ← Push back when granularity is bad ("AI" → "LLM agent infra")
Phase 0.5  Create skill directory   ← Self-contained, all artifacts inside
Phase 1    6-track parallel research ← 6 subagents: figures / tools / workflows / canon / sources / glossary
Phase 1.5  Research review gate     ← User confirms quality before continuing
Phase 2    Framework synthesis      ← Triple-gate validation blocks generic platitudes
Phase 2.5  Synthesis review gate    ← User confirms the OS before generation
Phase 3    Skill writeout           ← skill_writer emits full directory (auto-invokes nuwa for sub-skills + auto-emits cli/)
Phase 4    Three-test verification  ← Known / edge / voice blind tests
Phase 5    Two-agent refinement     ← Optimize "activates and acts"
```

Full spec in [SKILL.md](SKILL.md) — 524 lines of agent-loadable workflow.
Methodology in [references/extraction-framework.md](references/extraction-framework.md) — triple-gate validation, 3-tier tool extraction, school-of-thought handling, decay-rate table.

---

## 🧬 Lineage

master-skill stands on two shoulders:

```
🧬 colleague-skill   distills one specific person          scope: 1 person
🌟 nuwa-skill        distills a way of thinking            scope: anyone alive or historical
🎓 master-skill      distills an industry's OS             scope: an entire sub-niche
```

- **[colleague-skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — proved "distill a person" works. Source of the meta-skill pattern: intake → multi-source collect → analyze → write.
- **[nuwa-skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — proved "distill a way of thinking" beats "distill words." Source of the 6-agent parallel swarm + triple quality gates + Agentic Protocol. **master-skill calls nuwa-skill in Phase 3 to distill top 3 figures as sub-skills.**

Three of one lineage, scaling outward — distill someone you know → anyone alive or dead → an entire field of human knowledge.

---

## 📜 License

MIT — use it, fork it, ship with it.

<div align="center">

<br>

**🧬 colleague-skill** distilled what **one person** does.<br>
**🌟 nuwa-skill** distilled how **anyone** thinks.<br>
**🎓 master-skill** distills an **entire industry's** cognitive OS.<br>

<br>

*Stop hunting for the right skill.*<br>
*Tell us your industry — we hand you the only skill you'll need.*

<br>

MIT License © [voidborne-d](https://github.com/voidborne-d) · [中文 README](README.md) · English README

</div>
