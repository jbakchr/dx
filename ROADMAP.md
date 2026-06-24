# 🐳 dx — Roadmap
  
Build dx slowly.  
Each step should be small, useful, and testable.

---

## 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Always prefer working software over ideas
- Each phase should feel like:
→ "Ahh… this is already useful"

---

## ✅ CURRENT STATE (IMPORTANT)

dx is now a **learning-first Docker CLI** with a strong, polished learning loop.

---

### ✅ Core capabilities

- ✅ Installable CLI (pip install -e .)
- ✅ dx run <image>
- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation (with “why”)
- ✅ Image-aware behavior via IMAGE_PROFILES
- ✅ Guardrails for unsupported images
- ✅ Discoverability via `dx supported`

---

### ✅ Learning model (important)

dx now teaches the **core Docker container lifecycle**:

#### 🔹 Run
- ✅ docker run
- ✅ -d → run in background
- ✅ -p → ports
- ✅ -e → environment variables
- ✅ -v → volumes
- ✅ -w → working directory
- ✅ command execution (e.g. python app.py)

#### 🔹 Stop
- ✅ docker stop $(docker ps -q)

#### 🔹 Remove
- ✅ docker rm $(docker ps -a -q)

#### 🔹 Reset (workflow loop)
- ✅ run → reset → run → repeat

👉 All commands are **shown before execution**  
👉 Explanations include **“why this matters”**

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

### ✅ UX improvements (recent)

- ✅ Explanations include real-world purpose
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

- ✅ Lifecycle commands show real Docker usage:

```

dx stop --all
→ docker stop $(docker ps -q)

dx rm --all
→ docker rm $(docker ps -a -q)

dx reset
→ docker stop $(docker ps -q)
→ docker rm $(docker ps -a -q)

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

Now covering:

```

run → stop → remove → reset → repeat

```

The core loop is:

```

input → prompts → command → explanation → execution → learning

```

👉 This loop is now **complete for real-world container usage**

---

## 🎯 CURRENT FOCUS

👉 dx is now in a **polish + friction reduction phase**  
NOT a feature-building phase

---

## ⚡ Next Phase — Real-world friction reduction

Goal:
→ Make repeated usage feel effortless

#### Focus areas

- Improve small UX details
- Reduce unnecessary repetition
- Improve feedback (empty states, clarity)
- Optimize the run → reset loop

#### Rule

If something:
- slows you down
- feels repetitive
- breaks flow  

→ simplify it

---

## ⚡ Phase — Prompt UX tightening

Goal:
→ Make prompts feel natural and obvious

#### Ideas

- Improve wording clarity
- Improve ordering
- Remove unnecessary prompts

#### Rule

If a prompt:
- doesn’t provide learning value  
→ remove or simplify it

---

## ⚡ Phase — Micro learning improvements

Goal:
→ Increase understanding without adding complexity

#### Ideas

- Slightly refine explanations
- Improve clarity of “why” statements
- Keep explanations:
  - short
  - practical
  - consistent

#### Rule

No long explanations. No theory. No teaching modes.

---

## ⚡ Phase — Personal workflow patterns (lightweight)

Goal:
→ Align dx with real usage patterns

#### Ideas

- auto `--rm` for temporary runs
- small defaults that reduce friction
- tiny workflow shortcuts (like `reset`)

#### Success

dx feels like:
→ a natural extension of how you use Docker

---

## ⏳ Later (only if still simple)

Not priorities right now:

- dx explain
- dry-run mode
- dx learn (pattern training)
- small “recipes”

👉 Only revisit if:
- dx stays simple
- and a real need appears

---

## ⚠️ Things to AVOID (very important)

- ❌ Do NOT turn dx into a full Docker abstraction layer
- ❌ Do NOT mirror large parts of Docker CLI
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
