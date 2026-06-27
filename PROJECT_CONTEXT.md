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

## 🔁 Current behavior loop

The core experience in dx is now a **complete learning loop**:

```

dx run → experiment → dx reset → repeat

```

This is not just a workflow — it is:

✅ the core learning mechanic

What happens in each cycle:

```

dx run <image>
→ answer prompts
→ see generated command (clearly highlighted)
→ understand flags (short + “why”)
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

The tool is now:

✅ a guided learning loop  
(not just a CLI wrapper)

---

## 🧪 Current state

dx currently supports:

- ✅ dx run
- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset

- ✅ interactive prompts
- ✅ real Docker execution
- ✅ command generation + explanation (with “why”)
- ✅ image-aware behavior via profiles

### ✅ UX (important)

The experience is now structured to reinforce learning:

- ✅ Context header before prompts
- ✅ Clear command focus:

```

👉  docker run ...

```

- ✅ Layered explanations:

```

-d        → run in background
so your terminal stays free

```

- ✅ Real Docker output is always visible

👉 UX is part of the learning system

---

## 🏗️ Current architecture (important)

CLI (Typer)  
→ commands/run/ (orchestration, prompts, execution)  
→ commands/stop.py  
→ commands/rm.py  
→ commands/reset.py  
→ commands/supported.py  
→ ui/prompt.py (input)  
→ ui/output.py (display + explanation)  
→ config/images.py (image profiles)  
→ subprocess (Docker CLI)

### Principles:

- CLI should remain simple and predictable
- Complex commands can be grouped (run/)
- Simple commands stay flat
- UI logic is separated from command logic
- Image-specific behavior lives in config
- Docker is always visible (never hidden)

---

## 🔍 Key insights so far

- ✅ Seeing the real command is critical for learning
- ✅ Explaining flags reinforces understanding
- ✅ Prompts must be relevant (image-aware)
- ✅ Too many prompts = friction
- ✅ Simplicity beats completeness
- ✅ Real Docker output is valuable (do not hide it)
- ✅ Showing lifecycle commands deepens learning
- ✅ Repetition (run → reset → repeat) builds intuition
- ✅ UX structure directly impacts learning

---

## 🧠 Core concept (important)

The most important idea in dx:

```

IMAGE\_PROFILES

```

Example:

```

nginx → ports
postgres → environment variables

```

This allows dx to:

✅ adapt behavior  
✅ stay simple  
✅ guide correct usage

---

## 🧭 Intended direction (high level)

dx evolves from:

```

run command generator

```

to:

```

guided Docker learning system

```

Now extended to:

```

run → stop → remove → reset → repeat

```

👉 A complete, repeatable workflow

---

## 🧱 Near-term evolution priorities

### 1. Reduce friction (highest value)

- Remove unnecessary prompts
- Improve prompt wording
- Keep flow fast and obvious

---

### 2. Improve learning clarity

- Refine explanations slightly
- Improve “why” statements
- Keep explanations short and practical

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

"guide the user through real Docker workflows"

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

- a wrapper tool
- a shortcut CLI
- a productivity tool

This is:

✅ a learning-first CLI

It is designed to:

- expose real commands
- reinforce understanding
- reduce cognitive friction
- build confidence over time

---

## 🧠 Why this matters (personally)

This project helps:

- reduce friction when using Docker
- move from copying commands → understanding them
- build confidence with CLI tools
- create a better learning experience

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
