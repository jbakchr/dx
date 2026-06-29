# 🧭 dx — Laws

These are the non-negotiable rules for dx.

If something conflicts with these → it’s wrong.

---

## 1. Show the real command

Always show:

👉 docker ...

Never hide it.  
Never abstract it.

👉 If you don’t see it, you don’t learn it.

---

## 2. One concept = one prompt

Each prompt must map to:

→ one Docker flag or concept

No grouping.  
No abstraction.

👉 Clarity beats cleverness.

---

## 3. Same structure everywhere

All flows follow:

```

GLOBAL → IMAGE → NAME

```

Never reorder.  
Never customize per image.

👉 Repetition builds intuition.

---

## 4. No unused behavior

If something appears in the command:

→ it must come from a prompt

No hidden defaults.  
No magic values.

👉 Everything must be explainable.

---

## 5. Only show what is used

Only show:

- prompts that matter
- flags that are used
- explanations that apply

👉 No noise. No extras.

---

## 6. Prefer defaults over questions

If something is predictable:

→ give a default  
→ allow override

Do not ask unless needed.

👉 Fewer decisions = better flow.

---

## 7. Learning > convenience

Do not optimize for:

- speed
- shortcuts
- fewer steps

Optimize for:

👉 understanding  
👉 pattern recognition  
👉 repetition

---

## 🧠 Final test

Before adding anything, ask:

- Does this help me understand Docker?
- Does this keep the system simple?
- Does this reinforce patterns?

If not:

👉 don’t add it
