# 🐳 dx — Roadmap

Build dx slowly.
Each step should be small, useful, and testable.

---

## 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Prefer working software over ideas

Each phase should feel like:
→ "Ahh… this is already useful"

---

## ✅ CURRENT STATE (IMPORTANT)

dx is now a **learning-first Docker system** with a **complete, repeatable workflow**.

---

### ✅ Core capabilities

- ✅ Installable CLI (pip install -e .)
- ✅ dx run
- ✅ dx dockerfile
- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation (with “why”)
- ✅ Image-aware behavior via IMAGE_PROFILES
- ✅ Guardrails for unsupported images
- ✅ Discoverability via dx supported

---

## ✅ Learning model (important)

dx teaches Docker across **two connected layers**:

---

### 🔹 Build (Dockerfile)

- ✅ FROM → base image
- ✅ WORKDIR → working directory
- ✅ COPY → add files
- ✅ CMD → default command
- ✅ Image-aware defaults

👉 Guided construction through repetition  
👉 No need to revisit docs

---

### 🔹 Run (Container lifecycle)

- ✅ docker run
- ✅ -d → background
- ✅ -p → ports
- ✅ -e → environment variables
- ✅ -v → volumes
- ✅ -w → working directory
- ✅ command execution (python)

👉 Full command is always visible

---

### 🔹 Stop

- ✅ docker stop $(docker ps -q)

---

### 🔹 Remove

- ✅ docker rm $(docker ps -a -q)

---

### 🔹 Reset (core loop)

```

dx run → experiment → dx reset → repeat

```

👉 This loop is the **core learning mechanic**

---

### 🔹 Extended learning loop

```

dx dockerfile → understand build
→ dx run → experiment
→ dx reset → repeat

```

👉 Covers **build + run lifecycle**

---

## ✅ UX (current experience)

dx now provides a **tight, structured learning flow**:

- ✅ Minimal header (single-line context)
- ✅ Consistent prompt structure:
  - global → image-specific → name
- ✅ Clear focus on real syntax:
  👉 docker run ...
  👉 FROM python:3.11
- ✅ Layered explanations (short + why)
- ✅ Only relevant flags are shown
- ✅ Real Docker output always visible
- ✅ Clean execution feedback

👉 UX is part of the learning system

---

## ✅ Prompt structure (important)

dx now follows a **consistent mental model**:

```

\[GLOBAL DOCKER FLAGS]
→ ports (-p)
→ detached (-d)

\[IMAGE-SPECIFIC CONFIG]
→ env (-e)
→ volume (-v)
→ working directory (-w)
→ command

\[METADATA]
→ name (--name)

```

👉 Same entry pattern for all images
👉 Builds strong repetition + pattern recognition

---

## ✅ Core system (important)

The central concept in dx:

```

IMAGE_PROFILES

```

Used for:

- prompting ✅
- defaults ✅
- runtime behavior ✅
- Dockerfile behavior ✅

Example:

```

nginx → ports
python → volume + command + working directory
postgres → ports + env

```

👉 One system → multiple learning paths

---

## 🧠 Key insight

dx has evolved from:

```

command generator

```

to:

```

guided Docker learning system

```

Now covering:

```

build → run → stop → remove → reset → repeat

```

👉 A complete, repeatable learning workflow

---

## 🎯 CURRENT FOCUS

dx is now in:

👉 **polish + friction reduction phase**

NOT a feature-building phase.

---

## ⚡ Phase — Friction reduction (highest value)

Goal:
→ Make repeated usage feel effortless

Focus:

- Reduce prompt friction
- Improve defaults (IMAGE_PROFILES-driven)
- Remove unnecessary prompts
- Keep flow fast and obvious

Rule:

If something:

- slows you down
- feels repetitive
- breaks flow

→ simplify it

---

## ⚡ Phase — Prompt UX tightening

Goal:
→ Make prompts feel natural and predictable

Current direction:

- ✅ Consistent prompt order across images
- ✅ Clear dependencies (e.g. -v → -w)
- ✅ Minimal branching in flows

Next:

- Improve wording clarity
- Improve defaults
- Remove low-value prompts

---

## ⚡ Phase — Micro learning improvements

Goal:
→ Increase understanding without adding complexity

Focus:

- Improve explanation wording
- Strengthen "why" clarity
- Show relationships (e.g. -v ↔ -w)

Rule:

- Keep explanations short
- Keep explanations practical
- No “teaching mode”

---

## ⚡ Phase — Workflow alignment

Goal:
→ Make dx feel like a natural part of Docker usage

Ideas:

- Smarter defaults
- Reduce repetition
- Improve flow transitions

Success:

```

dx feels like a natural extension of Docker

```

---

## ⏳ Later (only if still simple)

Not priorities:

- dx explain
- dry-run mode
- dx learn
- recipes / presets
- advanced Docker features

👉 Only revisit if:

- dx remains simple
- real need appears

---

## ⚠️ Things to AVOID (very important)

- ❌ Becoming a full Docker abstraction layer
- ❌ Mirroring the full Docker CLI
- ❌ Supporting everything
- ❌ Adding complex config systems
- ❌ Hiding real Docker commands

👉 Simplicity is the product

---

## 🧠 Final rule

If something feels:

- too complex
- too abstract
- too big

→ skip it

---

## 🏁 Definition of success

You move from:

```

"I copy Docker commands"
↓
"I recognize patterns"
↓
"I understand what I’m doing"
↓
"I can write them myself"
↓
"I don’t need dx anymore"

```
