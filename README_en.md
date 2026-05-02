<div align="center">

# master-skill

### *Stop hunting for the right skill.*
### *Tell us your industry — we hand you the only skill you'll need.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-teal)](https://github.com/voidborne-d/master-skill)
[![Codex](https://img.shields.io/badge/Codex-Skill-black)](https://github.com/voidborne-d/master-skill)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://github.com/voidborne-d/master-skill)
[![Status](https://img.shields.io/badge/status-v1.0-brightgreen)]()

</div>

---

## In one line

[colleague-skill](https://github.com/titanwings/colleague-skill) distills **a person** into a skill.
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) distills **anyone's way of thinking** into a skill.
**master-skill** distills **an entire industry's cognitive operating system** into a skill.

Each is a 10× leap: one person you know → anyone alive or dead → an entire field of human knowledge.

> **Stop scrolling awesome-skill lists. Stop asking Reddit which framework to pick. Stop subscribing to 12 newsletters because you might miss something.
> Tell master-skill what you do. It hands back what a senior practitioner of that field has in their head — distilled into one skill you can load.**

---

## What it actually does

> Not a search engine. **The senior practitioner sitting next to you, right now.**

#### Demo · LLM agent infrastructure

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

This is **not** a Wikipedia stuffed into a prompt. master-skill captures **how senior practitioners think**:

| Layer | What it is |
|---|---|
| **How they judge** | Mental models — the lens this field uses |
| **How they decide** | Standard playbooks — "if X, then Y" heuristics |
| **What they use** | Tool stack + selection trees |
| **How they work** | Workflows / SOPs, marked with "this step changes Apr 2026" timestamps |
| **How they speak** | Expression DNA — jargon, register, the giveaways of an outsider |
| **What they avoid** | Anti-patterns — only outsiders make these mistakes |
| **What they don't know** | Honest boundaries — info cutoff, fastest-decaying modules |

Every generated skill ships with an **Agentic Protocol** — when handed a new problem, it first researches along the dimensions a senior practitioner would, then applies the OS above to deliver judgment. **Not sounding like a pro. Acting like one.**

---

## Install

```bash
# Claude Code
git clone https://github.com/voidborne-d/master-skill.git ~/.claude/skills/master-skill
```

```bash
# OpenClaw / Codex / Hermes — clone into the corresponding skills directory
```

---

## Usage

```
> Build me a master skill for LLM agent infra
> I work in cross-border e-commerce, distill it for me
> I do foot-and-ankle surgery, give me a master OS

> update master LLM-agent-infra    # incremental refresh after 6 months
```

master-skill confirms 6 dimensions with you (industry / sub-niche / region / your role / local materials / new vs update), then launches a 6-track parallel research swarm: industry figures / tool map / workflows / canonical knowledge / information sources / glossary. 30-60 minutes later you get an `{industry}-master.skill` directory installable into any Claude Code / OpenClaw / Codex / Hermes agent — instantly turning it into "the senior practitioner of that field."

---

## Quickstart — 5-command pipeline

```bash
# 1. Phase 1.5 — review research quality once 6 research files are ready
python3 tools/research/merge_research.py merge --skill-dir ./prototype/

# 2. Phase 2 — Agent synthesizes per prompts/synthesis.md → references/synthesis.md

# 3. Phase 3 — generate the skill directory
python3 tools/skill_writer.py create \
  --skill-dir ./output \
  --intake ./prototype/intake.json \
  --synthesis ./prototype/references/synthesis.md \
  --template references/skill-template.md \
  --research-dir ./prototype/references/research

# 4. Phase 4.4 — mechanical rubric verification
python3 tools/research/quality_check.py check --skill-dir ./output

# 5. Install into any host (claude / openclaw / codex / hermes / all)
python3 tools/install.py install --host claude --source ./output
```

A complete prototype run lives at [prototypes/llm-agent-infra-master/](prototypes/llm-agent-infra-master/) — the LLM agent infra industry, end-to-end Phase 0 → 4 verified (10 pass / 1 partial / 0 fail).

---

## How it works

5 phases + 3 quality gates, every step interceptable:

```
Phase 0   Industry intake          ← push back when granularity is too broad
Phase 0.5 Create skill directory   ← self-contained, all artifacts inside
Phase 1   6-track parallel research ← agent swarm, one subagent per track
Phase 1.5 Research review gate     ← user confirms quality before continuing
Phase 2   Framework synthesis      ← triple-gate validation blocks generic platitudes
Phase 2.5 Synthesis review gate    ← user confirms the OS before generation
Phase 3   Skill writeout           ← skill_writer emits the full directory
Phase 4   Three-test verification  ← known / edge / voice blind tests
Phase 5   Two-agent refinement     ← optimize "activates and acts"
```

Full spec in [SKILL.md](SKILL.md) — 524 lines of agent-loadable workflow.
Methodology in [references/extraction-framework.md](references/extraction-framework.md) — triple-gate validation, 3-tier tool extraction, school-of-thought handling, decay-rate table.

---

## Roadmap

| Version | Content | Status |
|---|---|---|
| v0.1 | SKILL.md + README + ROADMAP | ✅ |
| v0.2 | Templates + prompts (intake / research × 6 / synthesis / quality-check) | ✅ |
| v0.3 | Tools: skill_writer / merge_research / quality_check / yt-dlp pipeline / 4-host installers | ✅ |
| v0.4 | Polish + adaptive cold-floor + cross-track contradiction + voice surrogate + multi-host install | ✅ |
| v1.0 | LLM agent infra prototype Phase 0→4 verified, repo public | ✅ |
| v1.x | Cross-skill composition: Phase 3 auto-invokes nuwa-skill to distill top 3 figures as sub-skills | 🔲 |
| v1.x | Incremental refresh: `update master X` follows decay table, only refreshes tools/workflows | 🔲 |
| v0.6 | CLI output: generated industry skill ships with bash-callable scripts | 🔲 |

Details in [ROADMAP.md](ROADMAP.md).

---

## Acknowledgments & lineage

master-skill stands on two shoulders:

- **[colleague-skill (titanwings/colleague-skill)](https://github.com/titanwings/colleague-skill)** — proved "distill a person" works. Source of the meta-skill pattern: intake → multi-source collect → analyze → write.
- **[nuwa-skill (alchaincyf/nuwa-skill)](https://github.com/alchaincyf/nuwa-skill)** — proved "distill a way of thinking" beats "distill words." Source of the 6-agent parallel swarm + triple quality gates + Agentic Protocol idea. **master-skill calls nuwa-skill in Phase 3 to distill top 3 figures as sub-skills.**

Three of one lineage, scaling outward:

```
colleague-skill    distills a specific person       scope: 1 person
nuwa-skill         distills a way of thinking       scope: any living/historical figure
master-skill       distills an industry's OS        scope: an entire sub-niche
```

---

## License

MIT · 中文 README → [README.md](README.md)
