# 🧭 dx — Anti Patterns

These are common mistakes when evolving dx.

If you see these → stop and fix it.

---

## 1. Hidden behavior

❌ Example:

docker run -d nginx

(where -d was not prompted)

Problem:

- user does not know where it came from
- breaks learning loop

✅ Fix:

- every flag must come from a prompt

👉 No magic. No hidden defaults.

---

## 2. Grouped prompts

❌ Example:

? Configure ports?

Problem:

- hides real Docker structure
- combines multiple concepts

✅ Fix:

? Expose port?
? Container port?

👉 One concept = one prompt

---

## 3. Inconsistent flows

❌ Example:

nginx:
ports → name → detached

postgres:
ports → env → detached → name

Problem:

- user must “re-learn” flow per image
- breaks pattern recognition

✅ Fix:

```

GLOBAL → IMAGE → NAME

```

👉 Same flow everywhere

---

## 4. Explaining inside prompts

❌ Example:

? Run in background (this prevents blocking the terminal)?

Problem:

- makes prompts long
- mixes input + learning

✅ Fix:

Prompt:
? Run in background? (Y/n)

Explanation:
-d → run in background
(so your terminal stays free)

👉 Prompts ask  
👉 Output teaches

---

## 5. Too many prompts

❌ Example:

? Expose port?
? Container port?
? Confirm port?
? Confirm mapping?

Problem:

- slows flow
- adds no learning value

✅ Fix:

- ask once
- trust defaults

👉 Fewer decisions = better learning

---

## 6. Showing unused flags

❌ Example:

Explanation:

-d ...
-p ...
-e ...

(but command only used -d)

Problem:

- noise
- weakens signal

✅ Fix:

Only show:

-d → run in background

👉 Only show what is used

---

## 7. Smart but inconsistent logic

❌ Example:

If image == nginx:
skip detached prompt

Problem:

- breaks repetition
- unpredictable behavior

✅ Fix:

- same prompts for all images (when applicable)

👉 Consistency > cleverness

---

## 8. Over-specific defaults

❌ Example:

python → /usr/src/app  
node → /workspace  
nginx → /usr/share/nginx/html

Problem:

- hard to remember
- breaks learning pattern

✅ Fix:

(default: /app)

👉 Consistency > realism

---

## 9. Long explanations

❌ Example:

-d → run in detached mode which means the container will run in the background and you can continue interacting with the terminal...

Problem:

- too much cognitive load
- slows scanning

✅ Fix:

-d → run in background
(so your terminal stays free)

👉 Short = memorable

---

## 10. Decorative output

❌ Example:

==== Setup Phase ==== \***\* Configuring Container \*\***

Problem:

- noise
- not aligned with CLI norms

✅ Fix:

Use:

---

👉 Structure through simplicity

---

## 11. Breaking command visibility

❌ Example:

Running container...

(no docker command shown)

Problem:

- removes learning core

✅ Fix:

Always show:

👉 docker run ...

👉 This is the most important output

---

## 12. Feature creep

❌ Example:

- adding flags not needed for learning
- adding complex configuration layers
- adding automation features

Problem:

- turns dx into a tool
- moves away from learning system

✅ Fix:

Ask:

→ does this improve learning?

If not:
→ don’t add it

---

## 🧠 Detection rule

If something feels:

- “smart”
- “helpful”
- “efficient”

But:

- reduces repetition
- hides complexity
- adds abstraction

→ it's probably an anti-pattern

---

## 🧠 Final rule

dx should feel like:

→ guided repetition of real Docker usage

NOT:

→ a smarter Docker CLI
