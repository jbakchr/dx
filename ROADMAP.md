# 🐳 dx — Roadmap

> Build dx slowly.
> Each step should be small, useful, and testable.

---

# 🧠 Guiding principles

- Keep things minimal
- Build only what is needed right now
- Always prefer working software over ideas
- Each phase should feel like:
  → "Ahh… this is already useful"

---

# ⚡ Phase 0 — Setup (very small)

Goal:
→ Have a runnable CLI

### Steps

- [ ] Create basic project structure
- [ ] Create `dx/cli.py`
- [ ] Add simple `main()` function
- [ ] Make `dx` runnable via:

```bash
python -m dx
```

Success =

```bash
dx
→ prints "dx is working"
```

---

# ⚡ Phase 1 — First real command (`dx run` skeleton)

Goal:
→ Introduce the idea of dx wrapping docker

### Steps

- [ ] Add `dx run <image>`
- [ ] Build a very simple command:

```bash
docker run <image>
```

- [ ] Print the command before running it
- [ ] Execute it via `subprocess`

Success =

```bash
dx run nginx
→ prints docker command
→ runs container
```

---

# ⚡ Phase 2 — Interactive run (core idea!)

Goal:
→ Start building the _learning experience_

### Steps

- [ ] Add prompt for port

```
Expose port? (default 8080)
```

- [ ] Add prompt for background mode

```
Run in background? (Y/n)
```

- [ ] Add prompt for container name

```
Name container?
```

- [ ] Build final command dynamically
- [ ] Print:

```
Generated command:
docker run ...
```

- [ ] Ask for confirmation before running

Success =

User can “build” a docker run command step-by-step

---

# ⚡ Phase 3 — Explanation (learning layer)

Goal:
→ Help understand what the command means

### Steps

- [ ] After generating command, add explanation:

```
-d → run in background
-p → port mapping
--name → container name
```

- [ ] Keep explanations very short

Success =

User sees:

- command
- meaning of flags

---

# ⚡ Phase 4 — Dry-run mode

Goal:
→ Separate learning from execution

### Steps

- [ ] Add flag:

```bash
dx run nginx --dry-run
```

- [ ] Skip execution
- [ ] Only print command + explanation

Success =

User can explore without running containers

---

# ⚡ Phase 5 — `dx explain`

Goal:
→ Understand existing docker commands

### Steps

- [ ] Add:

```bash
dx explain "<docker command>"
```

- [ ] Parse basic flags:
  - `-d`
  - `-p`
  - `--name`
  - `-v`

- [ ] Print explanations

Success =

```bash
dx explain "docker run -d -p 8080:80 nginx"
→ prints meaning of flags
```

---

# ⚡ Phase 6 — `dx learn run`

Goal:
→ Build mental model of docker run

### Steps

- [ ] Add:

```bash
dx learn run
```

- [ ] Show progression:

```
Basic:
docker run nginx

With port:
docker run -p 8080:80 nginx

Detached:
docker run -d nginx

Named:
docker run --name web nginx
```

Success =

User sees how command evolves step-by-step

---

# ⚡ Phase 7 — Basic helper commands

Goal:
→ Make dx slightly useful day-to-day

### Steps

- [ ] Add:

```bash
dx ps
dx logs <container>
dx stop <container>
```

- [ ] Always print underlying docker command

Success =

dx becomes usable for simple workflows

---

# ⚡ Phase 8 — Refactor (important!)

Goal:
→ Avoid mess before growing

### Steps

- [ ] Move commands into separate modules
- [ ] Introduce simple command dispatcher
- [ ] Remove duplication
- [ ] Keep code readable and small

Success =

Code feels clean and extendable

---

# ⚡ Phase 9 — Improve prompts

Goal:
→ Better UX

### Steps

- [ ] Add defaults
- [ ] Allow skipping prompts
- [ ] Improve wording
- [ ] Reduce friction

Success =

Using `dx` feels fast and natural

---

# ⚡ Phase 10 — Personal patterns

Goal:
→ Encode your real usage

### Ideas

- [ ] `dx run python`
- [ ] `dx run node`
- [ ] auto-mount current directory
- [ ] auto `--rm` when appropriate

Success =

dx reflects how _you_ actually use Docker

---

# 🔮 Later (optional)

Only consider AFTER everything above works:

- smarter flag parsing
- volumes + env prompts
- docker-compose support
- templates ("run a database")
- export / share commands

---

# 🧠 Final note

Do NOT jump ahead.

If something feels:

- too complex
- too abstract
- too "future"

→ skip it.

---

# 🏁 Definition of success

You gradually move from:

"I don't remember docker commands"

to:

"I recognize patterns"

to:

"I don't need dx anymore"
