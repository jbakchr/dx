# 📚 dx — Documentation

This folder contains the design and thinking behind dx.

These files are not required to use dx.  
They exist to:

- explain how dx works
- keep the system consistent
- guide future decisions

---

## 🧠 How to read this

Start here:

1. PROJECT_CONTEXT.md → what dx is and why it exists
2. ROADMAP.md → where dx is going
3. philosophy/ → rules and constraints
4. learning-system/ → how prompts and output are designed

---

## 🧱 Structure

### Top-level

#### 📄 PROJECT_CONTEXT.md

The core description of the project.

- What dx is
- Why it exists
- Core philosophy
- Learning model

👉 This is the **source of truth for intent**

---

#### 📄 ROADMAP.md

Current state and direction.

- What is already built
- What is being improved now
- What to avoid

👉 This is the **source of truth for decisions over time**

---

## 🧭 philosophy/

Rules that protect the identity of dx.

---

### 📄 DX_LAWS.md

Short, non-negotiable rules.

Examples:

- always show real Docker commands
- consistency over cleverness
- learning > convenience

👉 Use this when making decisions quickly

---

### 📄 ANTI_PATTERNS.md

Common mistakes to avoid.

Examples:

- hidden behavior
- inconsistent prompts
- feature creep

👉 Use this when something “feels off”

---

## 🧩 learning-system/

How dx teaches through prompts and output.

---

### 📄 PROMPT_GUIDELINES.md

Rules for designing prompts.

- one concept per prompt
- consistent order across flows
- no unnecessary questions

👉 Defines **how input works**

---

### 📄 EXPLANATION_PATTERNS.md

Rules for explaining Docker flags.

- short (2 lines max)
- consistent wording
- explain “what” + “why”

👉 Defines **how learning is reinforced**

---

### 📄 OUTPUT_LAYOUT.md

Rules for structuring CLI output.

- section layout
- separators
- spacing and flow

👉 Defines **how output feels**

---

## 🧠 How everything fits together

dx is a small system with clear layers:

```

DX\_LAWS → decisions
ANTI\_PATTERNS → guardrails
PROMPT\_GUIDELINES → input
EXPLANATION\_PATTERNS → learning
OUTPUT\_LAYOUT → structure
PROJECT\_CONTEXT → vision
ROADMAP → direction

```

👉 Together, this creates a **consistent learning experience**

---

## 🏁 Why this exists

Without these files:

- prompts drift
- output becomes inconsistent
- features become unclear
- complexity increases

With these files:

👉 dx stays simple  
👉 dx stays focused  
👉 dx stays a learning system

---

## 🧠 Final note

If you are unsure about a change:

1. Check DX_LAWS.md
2. Check ANTI_PATTERNS.md
3. Keep it simple

👉 Simplicity is part of the product
