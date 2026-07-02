# 🐳 dx

**Learn Docker by using it — not memorizing it**

A small CLI that helps you learn Docker through real usage.

---

## 🧠 What is this?

dx is a CLI that sits on top of Docker.

But unlike most tools, it does **not hide Docker**.

Instead, it helps you:

- use Docker without friction ✅
- understand what you're doing ✅
- gradually learn the real Docker CLI ✅

---

## 🎯 The goal

Most tools do this:

```text
hide complexity
```

dx does something else:

```text
reveal complexity — step by step
```

Success is not measured by:

- how many commands dx supports
- how much Docker it hides

Success is measured by:

- recognizing Docker patterns
- understanding Docker concepts
- becoming confident writing commands yourself

---

## ⚡ The idea

Instead of writing:

```bash
docker run -d -p 8080:80 --name web nginx
```

You can do:

```bash
dx run nginx
```

And go through a guided flow:

```text
? Expose port? (default: 8080)
? Container port? (default: 80)
? Run in background? (Y/n)
? Name container? → web
```

Which gives you:

```bash
docker run -d -p 8080:80 --name web nginx
```

With explanation:

```text
-d         → run in background
             (so your terminal stays free)

-p         → map port 8080 → 80
             (so you can access it locally)

--name     → name container "web"
             (so you can reference it later)
```

👉 You always see the real Docker command

👉 You always understand what it does

---

## 🔁 The learning loop

dx is built around repetition:

```text
dx run
→ experiment
→ dx reset
→ repeat
```

Each time you:

- answer prompts
- see the command
- understand the flags
- run it
- observe the result

👉 Over time, you stop needing dx

---

## 🧩 Build + Run

dx teaches both sides of Docker.

### 🔹 Run containers

```bash
dx run nginx
```

### 🔹 Build Dockerfiles

```bash
dx dockerfile python
```

Example flow:

```text
? Base image (python:3.11)
→ FROM python:3.11

? Working directory (/app)
→ WORKDIR /app

? Copy current directory?
→ COPY . .

? Command?
→ CMD ["python", "app.py"]
```

👉 Learn Dockerfile syntax through repetition

---

## 🔄 Complete workflow

dx is designed around a repeatable workflow:

```text
dx dockerfile
→ understand image construction

dx run
→ understand container execution

dx reset
→ return to a clean state

repeat
```

This reinforces both:

- Dockerfile concepts
- Runtime concepts

through repetition.

---

## 🔹 Example: running code in a container

```bash
dx run python
```

```text
? Run in background? (Y/n)
? Mount current directory? (Y/n)
? Container working directory? (default: /app)
? Python file to run (leave empty to skip)
? Name container?
```

Result:

```bash
docker run -v $(pwd):/app -w /app python python app.py
```

Explanation:

```text
-v         → mount current directory
             (so your local files are available inside the container)

-w         → set working directory to /app
             (so commands run where your files are mounted)
```

👉 Learn how `-v` and `-w` work together

---

# ✅ Commands

## 🔹 dx run

Run a container with guided prompts:

```bash
dx run nginx
```

If unsupported:

```text
❌ Unknown image: foo

💡 Tip: run `dx supported`
```

---

## 🔹 dx dockerfile

Build a Dockerfile step-by-step:

```bash
dx dockerfile python
```

---

## 🔹 dx supported

Displays all supported images and the Docker concepts they teach:

```text
------------------------------------------------------------
Supported images
------------------------------------------------------------

nginx      web server      → (ports) [dockerfile]
redis      cache           → (ports) [dockerfile]

postgres   database        → (ports + env) [dockerfile]
mysql      database        → (ports + env) [dockerfile]

node       development     → (volume) [dockerfile]
python     development     → (volume + command) [dockerfile]
```

---

## 🔹 dx stop

Stop all running containers:

```bash
dx stop --all
```

---

## 🔹 dx rm

Remove all containers:

```bash
dx rm --all
```

---

## 🔹 dx reset

Reset Docker container state:

```bash
dx reset
```

Runs:

```bash
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
```

👉 Enables fast repetition

---

# 🎓 Learning concepts

Each image introduces a small set of Docker concepts.

| Image | Purpose | Concepts |
|---------|---------|---------|
| nginx | web server | ports |
| redis | cache | ports |
| postgres | database | ports, environment variables |
| mysql | database | ports, environment variables |
| node | development | volumes |
| python | development | volumes, commands |

The goal is not to learn every Docker feature at once.

Instead, each image teaches a few concepts that can be practiced repeatedly.

---

# 🧠 Core concept

The heart of dx is:

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

One system powers:

- prompts
- defaults
- explanations
- supported output
- Dockerfile generation

👉 One configuration → multiple learning paths

---

# 🚀 Real execution

dx does **not** simulate Docker commands.

Every command shown by dx is a real Docker command.

Example:

```bash
docker run ...
```

is the actual command that will execute.

This is intentional.

👉 If you don't see the real command, you don't learn the real command.

---

# 🧱 Core principle

Always show:

```bash
docker ...
```

Because:

```text
Seeing the command
→ builds familiarity

Understanding the command
→ builds confidence

Repeating the command
→ builds intuition
```

---

# 🧠 Philosophy

This is NOT:

- a Docker replacement
- a production management tool
- a full abstraction layer
- a feature-complete Docker wrapper

This IS:

✅ a learning-first CLI

Designed to take you from:

```text
"I copy Docker commands"
```

↓

```text
"I recognize patterns"
```

↓

```text
"I understand what I'm doing"
```

↓

```text
"I can write them myself"
```

↓

```text
"I don't need dx anymore"
```

---

# 🏗️ Architecture

```text
src/
└── dx/
    ├── cli.py
    ├── commands/
    ├── config/
    │   └── images.py
    └── ui/
```

The central design idea is:

```python
IMAGE_PROFILES
```

Each profile defines:

- purpose
- concepts
- prompts
- defaults
- Dockerfile behavior

👉 IMAGE_PROFILES drives behavior across the entire application

---

# 📚 Documentation

The project documentation includes:

- project context
- roadmap
- design principles
- learning philosophy
- prompt guidelines
- output guidelines

---

# 🔧 Installation

## Requirements

- Python 3.10+
- Docker installed and running

## Install

```bash
git clone https://github.com/dx.git
cd dx
pip install -e .
```

## Verify

```bash
dx --help
```

---

# 📄 License

MIT