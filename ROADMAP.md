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

dx is now a **learning-first Docker CLI** with a complete basic feature set.

### ✅ Core capabilities

- ✅ Installable CLI (`pip install -e .`)
- ✅ `dx run <image>`
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation
- ✅ Image-aware behavior via `IMAGE_PROFILES`

---

### ✅ Supported concepts (learning model)

dx now covers the **core mental model of `docker run`:**

- ✅ `-p` → ports
- ✅ `-e` → environment variables
- ✅ `-v` → volumes
- ✅ `-w` → working directory
- ✅ command execution (e.g. `python app.py`)

👉 This is a major milestone:
dx now teaches **how Docker actually works**

---

### ✅ Supported images

#### 🌐 Web

- nginx (port + container port)

#### 🗄️ Databases

- postgres (port + env)
- mysql (port + env)
- redis (port)

#### 💻 Development

- node (volume)
- python (volume + command)

---

### ✅ Internal structure (refactored)

- ✅ `run.py` → orchestration
- ✅ `run_prompts.py` → prompt logic
- ✅ `run_exec.py` → execution
- ✅ `ui/` → input/output separation
- ✅ `config/images.py` → behavior via profiles

👉 Code is now clean, composable, and aligned with the learning model

---

## 🧠 Key insight (where dx is now)

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

---

## ⚡ Next Phase — Improve explanations (HIGH VALUE)

Goal:
→ Move from “what” → “why”

### Steps

- Improve `-p` explanation  
  → “so you can access the service from your browser”

- Improve `-v` explanation  
  → “so your local files are available inside the container”

- Improve `-w` explanation  
  → “so commands run in the correct directory”

- Keep explanations:
  - short
  - practical
  - non-verbose

### Success

User not only sees commands  
→ but understands why each part matters

---

## ⚡ Phase — Dry-run mode

Goal:
→ Separate learning from execution

### Steps

- Add:

```

dx run nginx --dry-run

```

- Skip actual Docker execution

### Success

- User can experiment safely
- Faster learning loop

---

## ⚡ Phase — dx explain

Goal:

→ Explain existing Docker commands

### Steps

- Add:

```

dx explain "docker run -d -p 8080:80 nginx"

```

- Reuse existing explanation logic

### Success

dx becomes useful even without generating commands

---

## ⚡ Phase — dx learn

Goal:

→ Strengthen pattern recognition

### Idea

Show progressive examples:

```

docker run nginx
docker run -p 8080:80 nginx
docker run -d nginx
docker run --name web nginx

```

### Success

User starts recognizing patterns naturally

---

## ⚡ Phase — Prompt UX improvements

Goal:

→ Improve flow without adding complexity

### Steps

- Slightly improve wording
- Make prompt order consistent
- Reduce unnecessary prompts

### Rule

If a prompt adds friction → remove or simplify it

---

## ⚡ Phase — Personal workflow patterns

Goal:

→ Reflect real usage patterns

### Ideas

- auto `--rm` for temporary runs
- common presets (e.g. quick nginx)
- small defaults for dev workflows

### Success

dx feels like a natural extension of how you actually use Docker

---

## ⚠️ Things to AVOID (very important)

- ❌ Do NOT turn dx into a Docker abstraction layer
- ❌ Do NOT try to support all Docker features
- ❌ Do NOT introduce complex config systems
- ❌ Do NOT hide real Docker commands

👉 Simplicity is the product

---

## 🔮 Later (only if still simple)

- Better command explanations
- Small learning modes
- Volumes/mount edge cases
- Very small “recipes”

---

## 🧠 Final rule

If something feels:

- too complex
- too abstract
- too “big”

→ skip it.

---

## 🏁 Definition of success

You move from:

```

"I copy Docker commands"

↓

"I recognize patterns"

↓

"I understand what I am doing"

↓

"I don’t need dx anymore"

```
