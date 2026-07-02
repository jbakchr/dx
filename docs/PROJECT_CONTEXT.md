# dx – Project Context

---

## 🧠 What this project is

dx is a small CLI tool that helps me learn Docker by actively using it.

The focus is NOT:

- to abstract Docker
- to simplify everything away
- to replace Docker

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

- Do I recognize Docker patterns?
- Do I understand what Docker commands do?
- Can I start writing commands myself?
- Do I need dx less over time?

---

## ⚡ Key realization (important)

dx should NOT replace Docker.

Instead, it should:

✅ expose the real Docker command

✅ explain the command

✅ reinforce it through repetition

The biggest risk is not:

❌ missing features

The biggest risk is:

❗ overengineering and losing simplicity

---

## 🔁 Current learning system

dx now teaches Docker through multiple connected workflows.

---

### 🔹 Build loop

```text
dx dockerfile
→ understand image construction
```

What happens:

```text
dx dockerfile python

→ FROM
→ WORKDIR
→ COPY
→ CMD
→ final Dockerfile
```

Purpose:

```text
Understand how images are built.
```

---

### 🔹 Run loop

```text
dx run
→ understand container execution
```

What happens:

```text
dx run <image>

→ answer prompts
→ see generated command
→ understand flags
→ run real Docker
→ observe real output
```

Purpose:

```text
Understand how containers run.
```

---

### 🔹 Reset loop

```text
dx reset

→ stop containers
→ remove containers
→ start clean
```

Purpose:

```text
Encourage rapid repetition.
```

---

### 🔹 Complete workflow

```text
dx dockerfile
→ understand build

dx run
→ understand runtime

dx reset
→ return to a clean state

repeat
```

👉 dx teaches build + run together

---

## 🧪 Current state

dx currently supports:

### Runtime

- ✅ dx run
- ✅ image-aware prompts
- ✅ command generation
- ✅ command explanations
- ✅ real Docker execution

### Dockerfiles

- ✅ dx dockerfile
- ✅ image-aware defaults
- ✅ FROM
- ✅ WORKDIR
- ✅ COPY
- ✅ CMD

### Container lifecycle

- ✅ dx stop --all
- ✅ dx rm --all
- ✅ dx reset

### Discovery

- ✅ dx supported
- ✅ concept-aware image listing
- ✅ Dockerfile support indicators

### Quality

- ✅ type hints
- ✅ Google-style docstrings
- ✅ helper extraction
- ✅ improved readability

---

## ✅ UX principles

The experience is structured to reinforce learning.

### Real syntax first

Always show:

```text
docker run ...

FROM python:3.11
```

The learner should always see the actual Docker syntax.

---

### Consistent prompt structure

```text
GLOBAL
→ IMAGE
→ NAME
```

This structure should be repeated across images.

---

### Short explanations

Example:

```text
-d → run in background

(so your terminal stays free)
```

Keep explanations:

- short
- practical
- predictable

---

### Relationships matter

Example:

```text
-v → mount files

-w → run commands where files are mounted
```

Understanding relationships is more valuable than memorizing flags.

---

### Real output matters

Do not hide:

- Docker output
- container IDs
- runtime behavior

Learning happens through exposure.

---

## 🧠 Core concept

The most important idea in dx is:

```python
IMAGE_PROFILES
```

Example:

```python
"nginx": {
    "purpose": "web server",
    "concepts": ["ports"]
}

"postgres": {
    "purpose": "database",
    "concepts": ["ports", "env"]
}

"python": {
    "purpose": "development",
    "concepts": ["volume", "command"]
}
```

IMAGE_PROFILES powers:

✅ prompts

✅ defaults

✅ explanations

✅ supported output

✅ Dockerfile generation

✅ learning context

👉 One system → multiple learning paths

---

## 🧠 Learning concepts

Each image teaches a small set of Docker concepts.

| Image | Purpose | Concepts |
|---------|---------|---------|
| nginx | web server | ports |
| redis | cache | ports |
| postgres | database | ports, environment variables |
| mysql | database | ports, environment variables |
| node | development | volumes |
| python | development | volumes, commands |

This is intentional.

The goal is not:

```text
teach everything
```

The goal is:

```text
teach a few concepts well
```

---

## 🧠 Core learning model

All runtime workflows follow the same structure:

```text
[GLOBAL]

→ ports (-p)
→ detached (-d)

[IMAGE]

→ env (-e)
→ volume (-v)
→ working directory (-w)
→ command

[METADATA]

→ name (--name)
```

Benefits:

- repetition
- consistency
- pattern recognition

---

## 🔍 Key insights so far

- ✅ Seeing the real command is critical
- ✅ Repetition builds intuition
- ✅ Explanations reinforce understanding
- ✅ Prompts must be relevant
- ✅ Too many prompts create friction
- ✅ Build + run together deepen learning
- ✅ Consistency improves retention
- ✅ Relationships between concepts matter
- ✅ Simplicity beats completeness
- ✅ UX directly affects learning outcomes

---

## 🎯 Current phase

dx is currently in:

```text
POLISH + FRICTION REDUCTION
```

Not:

```text
FEATURE EXPANSION
```

Focus areas:

### Reduce friction

- improve defaults
- remove low-value prompts
- tighten wording
- simplify flows

### Improve clarity

- improve explanations
- strengthen "why"
- highlight concept relationships

### Maintain simplicity

- avoid unnecessary commands
- avoid abstraction layers
- avoid configuration systems

---

## 🔄 Structural direction

From:

```text
generate a command
```

To:

```text
guide real Docker workflows
```

This is the shift from:

```text
tool
```

to:

```text
learning system
```

---

## 🚫 Non-goals

dx is NOT:

- a Docker replacement
- a full Docker abstraction
- a feature-complete wrapper
- a productivity optimizer
- an automation platform

---

## ✅ What makes this project different

This is not:

- a wrapper CLI
- a shortcut tool
- a productivity tool

This is:

✅ a learning-first system

Designed to:

- expose real commands
- reinforce understanding
- reduce cognitive friction
- build confidence
- make itself unnecessary over time

---

## 🧠 Why this matters (personally)

This project helps me:

- reduce friction when using Docker
- move from copying → understanding
- build confidence with CLI tools
- avoid repeatedly searching documentation

It is both:

- a technical experiment
- a personal learning tool

---

## 🏁 Definition of success

```text
I copy Docker commands
```

↓

```text
I recognize patterns
```

↓

```text
I understand what I'm doing
```

↓

```text
I can write them myself
```

↓

```text
I don't need dx anymore
```

The goal is not dependency.

The goal is confidence.

---

## 🚀 What I want help with in a new chat

- Continue evolving dx step-by-step
- Keep everything minimal and focused
- Improve learning outcomes
- Improve real-world workflow experience
- Reduce friction without adding complexity
- Protect the core philosophy

---

## 💡 How to use this context

When starting a new chat:

```text
I'm working on this project:

[paste PROJECT_CONTEXT.md]

Help me evolve it without overengineering.
Let's work on:
[X]
```

The most important thing to remember:

```text
dx is a learning system.

Not a Docker abstraction layer.
```
