# 🐳 dx — Roadmap

Build dx slowly.  
Each step should be small, useful, and testable.

---

## 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Prefer working software over ideas
- Each phase should feel like:
  → "Ahh… this is already useful"

---

## ✅ CURRENT STATE (IMPORTANT)

dx is now a **learning-first Docker system** with a **complete learning loop**.

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

dx now teaches Docker across **two levels**:

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
- ✅ command execution

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

dx dockerfile → build understanding
→ dx run → experiment
→ dx reset → repeat

```

👉 Covers **build + run lifecycle**

---

## ✅ UX (current experience)

dx now provides a **structured learning flow**:

- ✅ Context headers before flows
- ✅ Focused instruction display:

```

👉 docker run ...
👉 FROM python:3.11

```

- ✅ Layered explanations (short + why)
- ✅ Consistent, scannable output
- ✅ Real Docker output always visible

👉 UX reinforces learning at every step

---

## ✅ Core system (important)

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

nginx  → ports
python → volume + command + dockerfile defaults
postgres → ports + env + dockerfile defaults

```

👉 One system → multiple learning flows

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

Focus areas:

- Reduce prompt friction
- Improve defaults
- Avoid unnecessary questions
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
→ Make prompts feel natural and obvious

Ideas:

- Improve wording clarity
- Improve order of prompts
- Remove unnecessary prompts

Rule:
If a prompt does not provide learning value  
→ remove or simplify it

---

## ⚡ Phase — Micro learning improvements

Goal:
→ Increase understanding without adding complexity

Ideas:

- Slightly refine explanations
- Improve “why this matters”
- Keep explanations:
  - short
  - practical
  - consistent

Rule:
No long explanations. No teaching mode.

---

## ⚡ Phase — Workflow alignment

Goal:
→ Make dx feel like a natural part of Docker usage

Ideas:

- Smarter defaults
- Lightweight helpers
- Reduce repetition

Success:
dx feels like:
→ a natural extension of Docker usage

---

## ⏳ Later (only if still simple)

Not priorities:

- dx explain
- dry-run mode
- dx learn (pattern training)
- recipes / presets
- Docker build integration

👉 Only revisit if:

- dx remains simple
- and real need appears

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
