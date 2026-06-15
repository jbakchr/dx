## 🐳 dx — Roadmap

> Build dx slowly.  
> Each step should be small, useful, and testable.

---

## 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Always prefer working software over ideas
- Each phase should feel like:  
  → "Ahh… this is already useful"

---

## ✅ CURRENT STATE (Milestone reached)

dx now has:

- ✅ Installable Typer CLI
- ✅ `dx run <image>`
- ✅ Interactive prompts
- ✅ Real Docker execution
- ✅ Command generation + explanation
- ✅ Image-aware behavior via `IMAGE_PROFILES`
- ✅ Basic support for:
  - nginx (ports)
  - postgres (env variables)

👉 This is the **first real version of dx as a learning tool**

---

## ⚡ Phase 0 — Setup ✅ DONE

Goal:
→ Have a runnable CLI

---

## ⚡ Phase 1 — Basic run command ✅ DONE

Goal:
→ Introduce Docker command execution

---

## ⚡ Phase 2 — Interactive run ✅ DONE

Goal:
→ Build commands step-by-step

---

## ⚡ Phase 3 — Explanation layer ✅ DONE

Goal:
→ Show meaning of flags

---

## ⚡ Phase 4 — Image-aware prompts ✅ DONE (NEW CORE)

Goal:
→ Adapt prompts based on image

### ✅ Implemented

- Introduced `IMAGE_PROFILES`
- nginx → port + container port
- postgres → environment variables

### 🧠 Insight

This is the core of dx:
→ guided, context-aware Docker learning

---

## ⚡ Next Phase — Expand image profiles (HIGH VALUE)

Goal:
→ Cover more real-world use cases

### Steps

- [ ] Add `redis`
  - no env
  - default port 6379

- [ ] Add `mysql`
  - MYSQL_ROOT_PASSWORD
  - port 3306

- [ ] Add `node`
  - optional volume mount

- [ ] Add `python`
  - optional script execution

Success =

```

dx run redis
dx run mysql
dx run node

```

feel natural and useful

---

## ⚡ Phase — Improve explanations (learning depth)

Goal:
→ Move from “what” → “why”

### Steps

- [ ] Improve `-p` explanation  
      → “makes service доступable via host port”

- [ ] Improve `-e` explanation  
      → show purpose of env vars

- [ ] Optionally add short hints

Success =

User not only sees the command  
→ but understands _why it matters_

---

## ⚡ Phase — Dry-run mode

Goal:
→ Separate learning from execution

### Steps

- [ ] Add:

```

dx run nginx --dry-run

```

- [ ] Skip Docker execution

Success =

User can experiment safely

---

## ⚡ Phase — `dx explain`

Goal:
→ Explain existing commands

### Steps

- [ ] Add:

```

dx explain "docker run -d -p 8080:80 nginx"

```

- [ ] Reuse existing explanation logic

Success =

dx helps even without generating commands

---

## ⚡ Phase — `dx learn run`

Goal:
→ Build mental model of commands

### Steps

- [ ] Show progression:

```

docker run nginx
docker run -p 8080:80 nginx
docker run -d nginx
docker run --name web nginx

```

Success =

User sees patterns clearly

---

## ⚡ Phase — Prompt improvements

Goal:
→ Better UX without adding complexity

### Steps

- [ ] Improve wording
- [ ] Improve ordering consistency
- [ ] Reduce friction

Success =

dx feels fast and intuitive

---

## ⚡ Phase — Refactor (lightweight)

Goal:
→ Keep code clean as complexity grows

### Steps

- [ ] Keep separation:
  - commands/
  - ui/
  - config/

- [ ] Avoid duplication
- [ ] Keep functions small

Success =

Code remains simple and readable

---

## ⚡ Phase — Personal patterns

Goal:
→ Match your real workflow

### Ideas

- [ ] auto `--rm` for temporary runs
- [ ] common container presets
- [ ] project-specific defaults

Success =

dx reflects how _you_ actually use Docker

---

## 🔮 Later (optional)

Only after everything above works:

- smarter image detection
- volumes & mounts
- docker-compose support
- templates ("run a database")
- shareable command recipes

---

## 🧠 Final rule

If something feels:

- too complex
- too abstract
- too “big”

→ skip it.

---

## 🏁 Definition of success

You gradually move from:

```

"I don't remember docker commands"
↓
"I recognize patterns"
↓
"I don't need dx anymore"

```
