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

dx is now a **learning-first Docker system**  
with a **complete, repeatable workflow**.

---

### ✅ Core capabilities

- ✅ Installable CLI (`pip install -e .`)
- ✅ dx run
- ✅ dx dockerfile
- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset

- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation (with “why”)
- ✅ Image-aware behavior via `IMAGE_PROFILES`
- ✅ Guardrails for unsupported images
- ✅ Discoverability via `dx supported`

---

## ✅ Learning model

dx teaches Docker across **two connected layers**:

---

### 🔹 Build (Dockerfile)

- ✅ FROM → base image
- ✅ WORKDIR → working directory
- ✅ COPY → add files
- ✅ CMD → default command
- ✅ Image-aware defaults

👉 Guided construction through repetition

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

### 🔹 Reset loop (core mechanic)

```

dx run → experiment → dx reset → repeat

```

👉 This is the **core learning loop**

---

### 🔹 Extended loop

```

dx dockerfile → understand build
→ dx run → experiment
→ dx reset → repeat

```

👉 Covers **build + run lifecycle**

---

## ✅ UX (current experience)

dx now provides a **tight, structured flow**:

- ✅ Minimal header (single line)
- ✅ Consistent prompt structure:

```

GLOBAL → IMAGE → NAME

```

- ✅ Clear focus on real syntax:

```

👉 docker run ...
👉 FROM python:3.11

```

- ✅ Layered explanations (short + why)
- ✅ Only relevant flags shown
- ✅ Real Docker output always visible
- ✅ Clean execution feedback

👉 UX is part of the learning system

---

## ✅ Prompt model (important)

All flows follow:

```

\[GLOBAL]
→ ports (-p)
→ detached (-d)

\[IMAGE]
→ env (-e)
→ volume (-v)
→ working directory (-w)
→ command

\[METADATA]
→ name (--name)

```

👉 Same structure across all images  
👉 Builds pattern recognition through repetition

---

## ✅ Core system

The central concept in dx:

```

IMAGE\_PROFILES

```

Used for:

- prompting ✅
- defaults ✅
- runtime behavior ✅
- Dockerfile behavior ✅

Example:

```

nginx    → ports
python   → volume + command + working directory
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

👉 A complete learning workflow

---

## 🎯 CURRENT FOCUS

dx is in:

👉 **polish + friction reduction phase**

NOT a feature-building phase.

---

## ⚡ Friction reduction (highest priority)

Goal:

→ Make repeated usage feel effortless

Focus:

- Reduce prompt friction
- Improve defaults (`IMAGE_PROFILES`)
- Remove unnecessary prompts
- Keep flow fast and obvious

Rule:

If something:

- slows usage
- feels repetitive
- breaks flow

→ simplify it

---

## ⚡ Prompt UX tightening

Goal:

→ Make prompts feel natural and predictable

Current state:

- ✅ Consistent ordering
- ✅ Clear dependencies (`-v → -w`)
- ✅ Minimal branching

Next:

- Improve wording clarity
- Improve defaults
- Remove low-value prompts

---

## ⚡ Micro learning improvements

Goal:

→ Improve understanding without adding complexity

Focus:

- Improve explanation wording
- Strengthen “why”
- Show relationships (e.g. `-v ↔ -w`)

Rule:

- keep it short
- keep it practical
- no “teaching mode”

---

## ⚡ Workflow alignment

Goal:

→ Make dx feel like a natural extension of Docker

Focus:

- smarter defaults
- reduced repetition
- smoother flow

Success:

```

dx feels like normal Docker usage

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

- dx stays simple
- real need appears

---

## ⚠️ Things to avoid

- ❌ Becoming a full Docker abstraction
- ❌ Mirroring the full Docker CLI
- ❌ Supporting everything
- ❌ Complex config systems
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
