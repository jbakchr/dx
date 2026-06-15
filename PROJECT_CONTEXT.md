## dx – Project Context

---

### 🧠 What this project is

dx is a small CLI tool that helps me learn Docker by actively using it.

The focus is NOT:

- to abstract Docker
- to simplify everything away

The focus is:
✅ learning Docker through guided repetition

---

### 🎯 Core philosophy

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

### ⚡ Key realization (important)

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

### 🔁 Current behavior loop

What happens when using dx:

```

dx run <image>
→ answer prompts
→ see generated command
→ understand flags
→ run real Docker
→ observe output

```

The tool is becoming:

✅ a guided learning loop  
(not just a CLI wrapper)

---

### 🧪 Current state

dx currently supports:

- ✅ `dx run <image>`
- ✅ interactive prompts
- ✅ real Docker execution
- ✅ explanation of flags
- ✅ image-aware behavior via profiles

Current image support:

- nginx  
  → port + container port

- postgres  
  → environment variables

---

### 🏗️ Current architecture (important)

```

CLI (Typer)
→ commands/run.py (orchestration)
→ ui/prompt.py (input)
→ ui/output.py (display + explanation)
→ config/images.py (image profiles)
→ subprocess (Docker CLI)

```

Principles:

- CLI should remain simple and predictable
- UI logic is separated from command logic
- Image-specific behavior lives in config
- Docker is always visible (never hidden)

---

### 🔍 Key insights so far

- ✅ Seeing the real command is critical for learning
- ✅ Explaining flags reinforces understanding
- ✅ Prompts must be relevant (image-aware)
- ✅ Too many prompts = friction
- ✅ Simplicity beats completeness
- ✅ Real Docker output is valuable (do not hide it)

---

### 🧠 Core concept (important)

The most important idea in dx:

> IMAGE_PROFILES

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

### 🧭 Intended direction (high level)

dx evolves from:

```

run command generator

```

to:

```

guided Docker learning system

```

Future direction:

```

input → guided prompts → command → explanation → execution → learning

```

---

### 🧱 Near-term evolution priorities

#### 1. Expand image profiles (highest value)

- Add redis
- Add mysql
- Add node
- Add python

Goal:
→ cover common real-world use cases

---

#### 2. Improve explanations

- Explain more flags when needed
- Slightly improve clarity (but stay short)
- Start introducing "why this matters"

Important:

- no long descriptions
- no walls of text

---

#### 3. Maintain simplicity

- Avoid adding too many prompts
- Avoid trying to support all Docker features
- Keep everything predictable

---

### 🔄 Structural direction (important)

From:

```

"generate a command"

```

To:

```

"guide the user toward correct command usage"

```

This is the shift from:

a tool

to:

✅ a learning system

---

### 🚫 Non-goals

- Not a full Docker abstraction layer
- Not a replacement for Docker CLI
- Not a feature-complete tool
- Not optimized for all use cases
- Not an automation system

---

### ✅ What makes this project different

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

### 🧠 Why this matters (personally)

This project helps:

- reduce friction when using Docker
- move from copying commands → understanding them
- build confidence with CLI tools
- create a better learning experience

It is both:

- a technical experiment
- a personal learning tool

---

### 🚀 What I want help with in a new chat

- Continue evolving dx step-by-step
- Keep everything minimal and focused
- Expand image profiles cleanly
- Improve UX without overcomplicating
- Design learning-oriented improvements

---

### 💡 How to use this context

When starting a new chat, say:

I’m working on this project:
\[paste PROJECT_CONTEXT.md\]

I want help evolving it step-by-step without overengineering.

Let’s start with \[X\]
