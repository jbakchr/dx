# 🧭 dx — Output Layout

This file defines how CLI output in dx should be structured.

The goal is NOT to make output visually complex.

The goal is to:

✅ make output easy to scan  
✅ reinforce learning through structure  
✅ create a consistent terminal experience

---

## 🧠 Core principle

Output is part of the learning loop.

Good output should:

- guide attention
- separate concepts clearly
- reinforce patterns visually

---

## 🧱 Standard layout (run command)

All `dx run` flows must follow this structure:

```

***

<header>
------------------------------------------------------------

<prompts>

***

Generated command:

👉  docker run ...

Explanation:

<flag explanations>

***

Run? (Y/n)

***

Executing Docker command...

\--- Docker output ---

<real docker output>

✅ Container started — ID shown in Docker output above

```

---

## 🔹 Section rules

### 1. Header

```

***

## Build a real Docker run command step by step.

```

Rules:

- Always one line
- Always short
- No extra explanation

---

### 2. Prompts

```

? Expose port? (default: 8080)
? Container port? (default: 80)
? Run in background? (Y/n)

? Name container?

```

Rules:

- One prompt per line
- Empty line before metadata section (`name`)
- No explanations here

---

### 3. Separator usage

Use:

```

***

```

Rules:

- Separate major sections only
- Never stack multiple separators
- Always leave one empty line after

---

### 4. Command display

```

Generated command:

👉  docker run -d -p 8080:80 --name web nginx

```

Rules:

- Always include `👉`
- Always include real command
- No wrapping or splitting

---

### 5. Explanation section

```

Explanation:

-d         → run in background
(so your terminal stays free)

-p         → map port 8080 → 80
(so you can access the service from your machine)

```

Rules:

- Only show used flags
- Follow EXPLANATION_PATTERNS.md strictly
- Keep vertical spacing tight

---

### 6. Confirmation

```

Run? (Y/n)

```

Rules:

- Always before execution
- No extra text
- One line only

---

### 7. Execution phase

```

Executing Docker command...

\--- Docker output ---

<real output>
```

Rules:

- Always show real Docker output
- Never hide or parse output
- Keep raw format

---

### 8. Final feedback

```
✅ Container started — ID shown in Docker output above
```

Rules:

- Single line only
- No duplicate information
- No extra explanation

---

## 🔁 Consistency rules

All commands must:

- follow same section ordering
- use same separators
- use same spacing
- use same phrasing

👉 Output should feel identical across images

---

## ⚡ Spacing rules

Use spacing intentionally:

✅ Good:

```
Section

Content
```

❌ Bad:

```
Section


Content
```

Rules:

- One empty line between sections
- No extra vertical spacing
- Keep output compact

---

## 🔗 Visual hierarchy

Use formatting to guide attention:

- `👉` → highlights command
- `?` → input prompt
- `✅` → success state
- `--- Docker output ---` → raw system output

👉 Users should scan without reading everything

---

## 🚫 What to avoid

- ❌ Long paragraphs
- ❌ Multiple headers
- ❌ Decorative formatting
- ❌ Inconsistent spacing
- ❌ Mixing explanation into prompts
- ❌ Hiding Docker output

---

## 🏁 Success criteria

Output is successful when:

- user can scan quickly
- user recognizes structure instantly
- user focuses on the command
- user understands flags without re-reading

```
structure → clarity → repetition → intuition
```

---

## 🧠 Final rule

If output feels:

- cluttered
- inconsistent
- slow to scan

→ simplify it

👉 Structure is part of the learning system
