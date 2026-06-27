# dx – Project Context

---

## 🧠 What this project is

dx is a small CLI tool that helps me learn Docker by actively using it.

The focus is NOT:

- to abstract Docker
- to simplify everything away

The focus is:

✅ learning Docker through guided repetition

---

## 🎯 Core philosophy

The goal is not:

- to hide complexity
- to create shortcuts
- to be faster than Docker

The goal is:

✅ to make Docker understandable through use

Success is measured by:

- Do I recognize patterns in Docker commands?
- Can I start writing commands myself?
- Do I need dx less over time?

---

## ⚡ Key realization (important)

dx should NOT replace Docker.

Instead, it should:

✅ expose the real Docker command  
✅ explain it  
✅ reinforce it through repetition

The biggest risk is not:

❌ missing features

The biggest risk is:

❗ overengineering and losing simplicity

---

## 🔁 Current learning loops

dx now supports **two connected learning loops**:

---

### 🔹 Run loop (container lifecycle)

```

dx run → experiment → dx reset → repeat

```

What happens:

```

dx run <image>
→ answer prompts
→ see generated command
→ understand flags
→ run real Docker
→ observe real output

```

Then:

```

dx reset
→ stop containers
→ remove containers
→ start fresh

```

---

### 🔹 Build loop (Dockerfile)

```

dx dockerfile <image>
→ answer prompts
→ see instructions
→ understand Dockerfile syntax
→ build mental model

```

What happens:

```

dx dockerfile python
→ FROM
→ WORKDIR
→ COPY
→ CMD
→ final Dockerfile

```

---

### 🔹 Combined loop (full learning system)

```

dx dockerfile → understand build
→ dx run → experiment
→ dx reset → repeat

```

👉 dx now teaches **build + run together**

---

## 🧪 Current state

dx currently supports:

- ✅ dx run
- ✅ dx dockerfile
- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset

- ✅ interactive prompts
- ✅ real Docker execution
- ✅ command + instruction explanation (“why”)
- ✅ image-aware behavior via IMAGE_PROFILES
- ✅ guardrails for unsupported images

---

## ✅ UX (important)

The experience is structured to reinforce learning:

- ✅ Context header before flows
- ✅ Clear focus on real syntax:

```

👉 docker run ...
👉 FROM python:3.11

```

- ✅ Layered explanations:

```

-d → run in background
so your terminal stays free

```

- ✅ Real Docker output is always visible

👉 UX is part of the learning system

---

## 🏗️ Current architecture (important)

CLI (Typer)  
→ commands/run/  
→ commands/dockerfile/  
→ commands/stop.py  
→ commands/rm.py  
→ commands/reset.py  
→ commands/supported.py  
→ ui/prompt.py (input)  
→ ui/output.py (display + explanation)  
→ config/images.py (IMAGE_PROFILES)  
→ subprocess (Docker CLI)

### Principles:

- CLI stays simple and predictable
- Commands remain flat (no deep nesting)
- UI logic is separate from command logic
- Image-specific behavior lives in config
- Docker is always visible (never hidden)

---

## 🧠 Core concept (important)

The most important idea in dx:

```

IMAGE\_PROFILES

```

Example:

```

nginx  → ports
postgres → env variables
python → volume + command + dockerfile defaults

```

IMAGE_PROFILES powers:

✅ runtime prompts  
✅ defaults  
✅ Dockerfile generation  
✅ learning context

👉 One system → multiple learning paths

---

## 🔍 Key insights so far

- ✅ Seeing the real syntax is critical for learning
- ✅ Explaining flags/instructions reinforces understanding
- ✅ Prompts must be relevant (image-aware)
- ✅ Too many prompts = friction
- ✅ Simplicity beats completeness
- ✅ Real Docker output is valuable (do not hide it)
- ✅ Repetition builds intuition
- ✅ Build + run together deepen understanding
- ✅ UX structure directly impacts learning

---

## 🧭 Intended direction (high level)

dx evolves from:

```

"generate a command"

```

to:

```

"guide the user through real Docker workflows"

```

Now extended to:

```

build → run → stop → remove → reset → repeat

```

👉 A complete, repeatable learning system

---

## 🧱 Near-term evolution priorities

### 1. Reduce friction (highest value)

- Remove unnecessary prompts
- Improve prompt wording
- Improve defaults (IMAGE_PROFILES-driven)
- Keep flow fast and obvious

---

### 2. Improve learning clarity

- Refine explanations slightly
- Improve “why” statements
- Keep explanations:
  - short
  - practical
  - consistent

---

### 3. Maintain simplicity

- Avoid adding too many commands
- Avoid abstraction layers
- Keep everything predictable

---

## 🔄 Structural direction (important)

From:

```

"generate a command"

```

To:

```

"guide real workflows step-by-step"

```

This is the shift from:

a tool

to:

✅ a learning system

---

## 🚫 Non-goals

- Not a full Docker abstraction layer
- Not a replacement for Docker CLI
- Not a feature-complete tool
- Not optimized for all use cases
- Not an automation system

---

## ✅ What makes this project different

This is not:

- a wrapper CLI
- a shortcut tool
- a productivity optimizer

This is:

✅ a learning-first system

Designed to:

- expose real commands
- reinforce understanding
- reduce cognitive friction
- build confidence over time

---

## 🧠 Why this matters (personally)

This project helps:

- reduce friction when using Docker
- move from copying → understanding
- build confidence with CLI tools
- avoid repeatedly returning to docs

It is both:

- a technical experiment
- a personal learning tool

---

## 🚀 What I want help with in a new chat

- Continue evolving dx step-by-step
- Keep everything minimal and focused
- Improve real-world workflow experience
- Reduce friction without adding complexity
- Strengthen learning through repetition

---

## 💡 How to use this context

When starting a new chat, say:

```

I’m working on this project:
\[paste PROJECT\_CONTEXT.md]

I want help evolving it step-by-step without overengineering.
Let’s start with \[X]

```
