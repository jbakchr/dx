# 🧭 dx — Explanation Patterns

This file defines how explanations in dx should be written.

The goal is NOT to fully teach Docker.

The goal is to:

✅ reinforce understanding through repetition  
✅ connect flags to real behavior  
✅ keep explanations minimal and consistent

---

## 🧠 Core principle

Explanations are not documentation.

They are:

✅ quick reinforcement of meaning

Every explanation should:

- explain what the flag does
- explain why it matters
- connect to real usage

---

## 🧱 Explanation format (strict)

All explanations must follow this format:

```

<flag> → <what it does>
(so <why it matters>)

```

Example:

```

-d → run in background
(so your terminal stays free)

```

Rules:

- Always 2 lines (max)
- First line = what
- Second line = why
- Always aligned formatting

---

## 🔁 Consistency rule

The same flag must ALWAYS have the same explanation.

Example:

```

-d → run in background
(so your terminal stays free)

```

Rules:

- Never reword explanations
- Never shorten randomly
- Never expand randomly

👉 Repetition builds memory

---

## ✅ Standard flag explanations

### -d (detached)

```

-d → run in background
(so your terminal stays free)

```

---

### -p (ports)

```

-p → map port <host> → <container>
(so you can access the service from your machine)

```

---

### -e (environment variables)

```

-e → set environment variable '<key>=<value>'
(used to configure the container)

```

---

### -v (volume)

```

-v → mount current directory
(so your local files are available inside the container)

```

---

### -w (working directory)

```

-w → set working directory to <dir>
(so commands run where your files are)

```

---

### --name (container name)

```

\--name → name container "<name>"
(so you can reference it later)

```

---

## 🔗 Relationship rule (important)

If flags are related, explanations should reflect that.

Example:

```

-v → mount current directory
(so your local files are available inside the container)

-w → set working directory to /app
(so commands run where your files are mounted)

```

👉 Reinforce mental model:
mount → location → execution

---

## ⚡ Dynamic values

Explanations must reflect real values when relevant.

Example:

```

-p → map port 8080 → 80

```

```

-w → set working directory to /app

```

Rules:

- Always show actual values
- Never use placeholders in runtime output

---

## 🚫 What to avoid

- ❌ Long explanations
- ❌ Multi-paragraph output
- ❌ Abstract wording
- ❌ Inconsistent phrasing
- ❌ Explaining inside prompts (belongs here)
- ❌ Explaining concepts not used in the command

---

## ✅ When to show explanations

Only show explanations for:

- flags actually used in the command ✅

Do NOT show:

- unused flags
- possible flags
- future flags

---

## 🧠 Tone and wording

Keep language:

- simple
- direct
- concrete

✅ Good:

```

so your terminal stays free

```

❌ Bad:

```

so that the execution is non-blocking with respect to the terminal session

```

---

## 🏁 Success criteria

Explanations are successful when:

- User recognizes the flag instantly
- User remembers what it does
- User can predict behavior before running

```

command → explanation → recognition → intuition

```

---

## 🧠 Final rule

If an explanation feels:

- too long
- inconsistent
- unnecessary

→ simplify it

👉 Clarity comes from repetition, not detail
