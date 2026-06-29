# 🧭 dx — Prompt Guidelines

This file defines how prompts in dx should behave.

The goal is NOT to make prompts “nice”.  
The goal is to:

✅ reinforce Docker understanding  
✅ build pattern recognition through repetition  
✅ minimize cognitive friction

---

## 🧠 Core principle

Prompts are not input helpers.

Prompts are:

✅ part of the learning system

Every prompt should:

- teach a real Docker concept
- map to a real flag/instruction
- reinforce a repeated pattern

---

## 🧱 Prompt structure (critical)

ALL flows must follow this structure:

```

\[GLOBAL DOCKER FLAGS]
→ ports (-p)
→ detached (-d)

\[IMAGE-SPECIFIC]
→ env (-e)
→ volume (-v)
→ working directory (-w)
→ command

\[METADATA]
→ name (--name)

```

Rules:

- Always keep this order
- Never mix sections
- Never reorder for specific images

👉 Consistency builds intuition

---

## 🔁 Repetition rule

The same concept must always appear the same way.

Examples:

- `? Run in background? (Y/n)`
- `? Name container?`
- `? Container working directory? (default: /app)`

Rules:

- Same wording across all commands
- Same order across all images
- Same defaults when possible

👉 Repetition > flexibility

---

## ⚡ Prompt design rules

### 1. One concept per prompt

✅ Good:

```

? Expose port?
? Container port?

```

❌ Bad:

```

? Configure ports?

```

---

### 2. Mirror real Docker concepts

Prompts should map directly to Docker:

- `-p` → port prompts
- `-d` → background prompt
- `-v` → volume prompt
- `-w` → working directory prompt

👉 If a flag appears in output, it must come from a prompt

---

### 3. Respect dependencies

Only ask prompts when they are relevant.

Example:

```

? Mount current directory? → Y
? Container working directory? → (ask only now)

```

Rules:

- No irrelevant prompts
- No “future” prompts
- No unused values

---

### 4. Prefer defaults over questions

If something is predictable:

- provide a default
- allow override
- avoid extra prompts

Example:

```

(default: 8080)
(default: /app)
(default: password)

```

---

### 5. Keep prompts short

✅ Good:

```

? Run in background? (Y/n)

```

❌ Bad:

```

? Do you want to run the container in detached mode so the terminal is not blocked?

```

👉 Explanation belongs in output, not prompts

---

## 🧠 Explanation rules (important)

Prompts collect input
Explanations teach meaning

Rules:

- Short (1–2 lines max)
- Always include “why”
- Show real effect

Example:

```

-d → run in background
(so your terminal stays free)

```

---

## 🔗 Relationship rule (important)

When concepts are connected, show it.

Example:

```

-v → mount files
-w → run commands where your files are mounted

```

👉 Teach systems, not isolated flags

---

## 🚫 What to avoid

- ❌ Too many prompts
- ❌ Prompts without learning value
- ❌ Different flows per image
- ❌ Hidden defaults (must be visible)
- ❌ Explaining inside prompts
- ❌ “Smart” logic that breaks repetition

---

## ✅ When to add a prompt

Only add a prompt if:

- it maps to a real Docker concept ✅
- it improves understanding ✅
- it does not break flow ✅

Otherwise:

👉 skip it

---

## 🏁 Success criteria

Prompt system is successful when:

- User recognizes patterns quickly
- User remembers flag meanings
- User predicts the command before seeing it
- User needs dx less over time

```

Prompt → Pattern → Recognition → Intuition

```

---

## 🧠 Final rule

If a prompt feels:

- unnecessary
- inconsistent
- confusing

→ remove or simplify it

👉 Simplicity is part of the learning system
