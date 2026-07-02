# 🐳 dx — Roadmap

Build dx slowly.

Each step should be:

- small
- useful
- testable

Every phase should feel like:

```text
"Ahh... this is already useful."
```

---

## 🧠 Guiding principles

### Keep things minimal

Build only what is needed right now.

Avoid:

- abstractions
- configuration systems
- feature creep

Prefer:

- clear workflows
- real Docker usage
- repetition

---

### Reveal Docker, don't hide it

dx exists to teach Docker.

It should never become:

```text
Docker but easier
```

Instead:

```text
Docker but easier to understand
```

The real command should always remain visible.

---

### Learning over convenience

The goal is not:

- fewer commands
- maximum automation
- productivity optimization

The goal is:

- understanding
- confidence
- pattern recognition

---

## ✅ CURRENT STATE

dx is now a **learning-first Docker system** with a complete build → run → reset workflow.

---

### ✅ Core capabilities

#### Runtime

- ✅ `dx run`
- ✅ guided prompts
- ✅ image-aware behavior
- ✅ real Docker execution
- ✅ command explanations

##### Dockerfiles

- ✅ `dx dockerfile`
- ✅ image-aware defaults
- ✅ FROM
- ✅ WORKDIR
- ✅ COPY
- ✅ CMD

##### Container lifecycle

- ✅ `dx stop --all`
- ✅ `dx rm --all`
- ✅ `dx reset`

##### Discovery

- ✅ `dx supported`
- ✅ image descriptions
- ✅ concept visibility
- ✅ Dockerfile support indicators

---

## ✅ Learning model

dx teaches Docker through connected learning loops.

---

#### 🔹 Build loop

```text
dx dockerfile
→ understand image construction
```

Concepts:

- FROM
- WORKDIR
- COPY
- CMD

Goal:

```text
Understand how images are built.
```

---

#### 🔹 Run loop

```text
dx run
→ understand container execution
```

Concepts:

- ports
- detached mode
- environment variables
- volumes
- working directories
- commands

Goal:

```text
Understand how containers run.
```

---

#### 🔹 Reset loop

```text
dx run
→ experiment

dx reset
→ clean environment

repeat
```

Goal:

```text
Encourage repetition.
```

---

#### 🔹 Complete workflow

```text
dx dockerfile
→ build understanding

dx run
→ runtime understanding

dx reset
→ clean slate

repeat
```

Goal:

```text
Build and run become connected ideas.
```

---

## ✅ Learning concepts

Current learning paths:

| Image | Purpose | Concepts |
|---------|---------|---------|
| nginx | web server | ports |
| redis | cache | ports |
| postgres | database | ports, environment variables |
| mysql | database | ports, environment variables |
| node | development | volumes |
| python | development | volumes, commands |

Each image teaches only a few Docker concepts.

This keeps learning focused.

---

## ✅ UX

Current UX goals:

- ✅ minimal headers
- ✅ predictable prompts
- ✅ real Docker syntax
- ✅ concise explanations
- ✅ visible command output
- ✅ low friction

Example:

```text
👉 docker run ...
```

Not:

```text
Magic hidden abstraction
```

---

## ✅ Prompt model

All runtime flows follow the same structure:

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
- pattern recognition
- consistency

---

## ✅ Core system

The heart of dx:

```python
IMAGE_PROFILES
```

Current responsibilities:

- prompts
- defaults
- supported output
- explanations
- runtime behavior
- Dockerfile behavior

Example:

```python
{
    "purpose": "database",
    "concepts": ["ports", "env"]
}
```

One configuration drives multiple learning paths.

---

## 🧠 Key insight

dx started as:

```text
command generator
```

dx evolved into:

```text
guided Docker learning system
```

The project is no longer about generating commands.

The project is about helping users internalize Docker.

---

## 🎯 CURRENT FOCUS

dx is firmly in:

```text
POLISH MODE
```

Not:

```text
FEATURE MODE
```

---

## ⚡ Priority 1 — Friction reduction

Goal:

```text
Make repeated usage feel effortless.
```

Focus:

- improve defaults
- remove unnecessary prompts
- reduce repetition
- tighten wording

Rule:

If something slows learning down:

```text
simplify it
```

---

## ⚡ Priority 2 — Learning clarity

Goal:

```text
Improve understanding without adding complexity.
```

Focus:

- explanation wording
- concise "why" statements
- concept relationships

Examples:

```text
-v → mount files

-w → run commands where files are mounted
```

Show relationships.

Avoid lengthy teaching.

---

## ⚡ Priority 3 — IMAGE_PROFILES cleanup

Goal:

```text
Keep image knowledge centralized.
```

Current direction:

```python
{
    "purpose": "development",
    "concepts": ["volume", "command"]
}
```

Benefits:

- cleaner supported output
- cleaner explanations
- cleaner future extensions

Rule:

Keep IMAGE_PROFILES as the single source of truth.

---

## ⚡ Priority 4 — Workflow refinement

Goal:

```text
Make dx feel closer to normal Docker usage.
```

Focus:

- better defaults
- less typing
- smoother flows

Success looks like:

```text
I stop thinking about dx.

I start thinking about Docker.
```

---

## ✅ Recently completed

### Learning improvements

- ✅ Dockerfile workflow
- ✅ build + run integration
- ✅ concept-focused image descriptions
- ✅ improved supported output

### UX improvements

- ✅ consistent prompt ordering
- ✅ cleaner command displays
- ✅ image-aware prompts
- ✅ concept visibility

### Code quality

- ✅ type hints
- ✅ Google-style docstrings
- ✅ helper extraction
- ✅ improved readability

---

## ⏳ Later (only if still simple)

Potential future ideas:

- dx explain
- dry-run mode
- image learning recommendations
- recipe examples

These are not priorities.

Only revisit them if:

- a real learning problem appears
- simplicity is preserved

---

## ⚠️ Things to avoid

Do NOT become:

- ❌ a Docker replacement
- ❌ a Docker abstraction layer
- ❌ a feature-complete wrapper
- ❌ a productivity framework
- ❌ a configuration-heavy tool

Do NOT:

- ❌ hide Docker commands
- ❌ mirror the full Docker CLI
- ❌ optimize for every use case

---

## 🧠 Final rule

If a feature feels:

- too big
- too abstract
- too clever
- too configurable

skip it.

Simplicity is the product.

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

The end goal is not:

```text
Dependency on dx
```

The end goal is:

```text
Confidence with Docker
```