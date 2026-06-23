## 🐳 dx — Roadmap

Build dx slowly.  
Each step should be small, useful, and testable.

---

### 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Always prefer working software over ideas
- Each phase should feel like:
  → "Ahh… this is already useful"

---

## ✅ CURRENT STATE (IMPORTANT)

dx is now a **learning-first Docker CLI** with a strong, polished core loop.

---

### ✅ Core capabilities

- ✅ Installable CLI (pip install -e .)
- ✅ dx run <image>
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation (with “why”)
- ✅ Image-aware behavior via IMAGE_PROFILES
- ✅ Guardrails for unsupported images
- ✅ Discoverability via `dx supported`

---

### ✅ Learning model (important)

dx now teaches the **core mental model of `docker run`:**

- ✅ -d → run in background
- ✅ -p → ports
- ✅ -e → environment variables
- ✅ -v → volumes
- ✅ -w → working directory
- ✅ command execution (e.g. python app.py)

👉 Explanations now include **“why this matters”**  
(not just what the flags do)

---

### ✅ Supported images

##### 🌐 Web

- nginx (ports)

##### 🗄️ Databases

- postgres (ports + env)
- mysql (ports + env)
- redis (ports)

##### 💻 Development

- node (volume)
- python (volume + command)

---

### ✅ UX improvements (recent)

- ✅ Explanations now include **real-world purpose**
- ✅ Output formatting is consistent and aligned
- ✅ Environment variables no longer break alignment
- ✅ Clear error for unknown images:

```

Unknown image: foo

Tip: run `dx supported` to see available images

```

- ✅ `dx supported` command for discoverability:

```

Supported images:

nginx     → web server (ports)
postgres  → database (ports + env)
mysql     → database (ports + env)
redis     → cache (ports)
node      → development (volume)
python    → development (volume + command)

```

---

### 🧠 Key insight (where dx is now)

dx has evolved from:

```

command generator

```

to:

```

guided Docker learning system

```

The core loop is now:

```

input → prompts → command → explanation → execution → learning

```

👉 This loop is now **complete and coherent**

---

## 🎯 CURRENT FOCUS

👉 dx is now in a **polish + friction reduction phase**

NOT a feature-building phase.

---

## ⚡ Next Phase — Prompt UX tightening (highest value)

Goal:  
→ Reduce friction without adding complexity

#### Things to improve

- Improve wording (clearer prompts)
- Improve ordering (more natural flow)
- Remove unnecessary prompts
- Reduce repetition

#### Rule

If a prompt:

- feels unnecessary
- slows you down
- adds no learning value

→ simplify or remove it

#### Success

Prompts feel:

- obvious
- fast
- frictionless

---

## ⚡ Phase — Micro learning improvements

Goal:  
→ Slightly improve learning without adding systems

#### Ideas

- Small refinements to explanations (if something feels unclear)
- Slightly better phrasing of “why” explanations
- Keep explanations:
  - short
  - practical
  - consistent

#### Rule

No long text. No theory. No teaching mode.

---

## ⚡ Phase — Personal workflow patterns (lightweight)

Goal:  
→ Better reflect real-world Docker usage

#### Ideas

- auto `--rm` for temporary runs (optional default)
- small convenience improvements that reduce friction
- minimal, practical defaults

#### Success

dx feels like:
→ a natural extension of how you use Docker

---

## ⏳ Later (only if still simple)

These are **not priorities right now**:

- dx explain (explain existing commands)
- dry-run mode
- dx learn (pattern training)
- small “recipes”

👉 Only revisit if:

- dx remains simple
- and a real need appears

---

## ⚠️ Things to AVOID (very important)

- ❌ Do NOT turn dx into a Docker abstraction layer
- ❌ Do NOT mirror Docker CLI commands (e.g. dx images → docker images)
- ❌ Do NOT support all Docker features
- ❌ Do NOT introduce complex config systems
- ❌ Do NOT hide real Docker commands

👉 Simplicity is the product

---

## 🧠 Final rule

If something feels:

- too complex
- too abstract
- too “big”

→ skip it

---

## 🏁 Definition of success

You move from:

"I copy Docker commands"  
↓  
"I recognize patterns"  
↓  
"I understand what I am doing"  
↓  
"I don’t need dx anymore"
