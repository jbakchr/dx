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

dx is now a **learning-first Docker CLI** with a **complete learning loop**.

---

### ✅ Core capabilities

- ✅ Installable CLI (`pip install -e .`)
- ✅ `dx run`
- ✅ `dx stop --all`
- ✅ `dx rm --all`
- ✅ `dx reset`
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation (with “why”)
- ✅ Image-aware behavior via `IMAGE_PROFILES`
- ✅ Guardrails for unsupported images
- ✅ Discoverability via `dx supported`

---

### ✅ Learning model (important)

dx teaches the **core Docker container lifecycle**:

#### 🔹 Run

- ✅ `docker run`
- ✅ `-d` → background
- ✅ `-p` → ports
- ✅ `-e` → environment variables
- ✅ `-v` → volumes
- ✅ `-w` → working directory
- ✅ command execution

#### 🔹 Stop

- ✅ `docker stop $(docker ps -q)`

#### 🔹 Remove

- ✅ `docker rm $(docker ps -a -q)`

#### 🔹 Reset (core loop)

```

dx run → experiment → dx reset → repeat

```

👉 This loop is now the **core learning mechanic**

- ✅ Stops + removes containers
- ✅ Shows real commands before execution
- ✅ Encourages repetition
- ✅ Enables fast iteration

---

### ✅ UX (current experience)

dx now has a **clear and structured learning flow**:

- ✅ Context-setting header before prompts
- ✅ Focused command display:

```

👉  docker run ...

```

- ✅ Layered explanations:

```

-d        → run in background
so your terminal stays free

```

- ✅ Consistent and scannable output
- ✅ Real Docker output always visible

👉 UX now reinforces learning at every step

---

### ✅ Supported images

#### 🌐 Web

- nginx (ports)

#### 🗄️ Databases

- postgres (ports + env)
- mysql (ports + env)
- redis (ports)

#### 💻 Development

- node (volume)
- python (volume + command)

---

### 🧠 Key insight

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

run → stop → remove → reset → repeat

```

👉 A complete, repeatable workflow

---

## 🎯 CURRENT FOCUS

dx is now in a:

👉 **polish + friction reduction phase**

NOT a feature-building phase.

---

## ⚡ Phase — Friction reduction (highest value)

Goal:
→ Make repeated usage feel effortless

Focus areas:

- Remove unnecessary friction
- Optimize run → reset flow
- Improve clarity and feedback
- Tighten interaction speed

Rule:
If something:

- slows you down
- feels repetitive
- breaks flow  
  → simplify it

---

## ⚡ Phase — Prompt UX tightening

Goal:
→ Make prompts feel obvious and natural

Ideas:

- Improve wording clarity
- Improve ordering
- Remove unnecessary prompts

Rule:
If a prompt does not provide learning value  
→ remove or simplify it

---

## ⚡ Phase — Micro learning improvements

Goal:
→ Increase understanding without adding complexity

Ideas:

- Refine explanations slightly
- Improve “why it matters”
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

- small defaults that reduce friction
- lightweight workflow helpers (like `reset`)
- remove unnecessary repetition

Success:
dx feels like:

→ a natural extension of how you use Docker

---

## ⏳ Later (only if still simple)

Not priorities:

- dx explain
- dry-run mode
- dx learn (pattern training)
- recipes / presets

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
"I don’t need dx anymore"

```
