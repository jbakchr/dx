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
→ hide complexity

dx does something else:  
→ **reveal complexity — step by step**

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

```
? Expose port? (default: 8080)
? Container port? (default: 80)
? Run in background? (Y/n)
? Name container? → web
```

Which gives you:

```
👉  docker run -d -p 8080:80 --name web nginx
```

With explanation:

```
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

```
dx run → experiment → dx reset → repeat
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

dx teaches both sides of Docker:

### 🔹 Run containers

```bash
dx run nginx
```

### 🔹 Build Dockerfiles

```bash
dx dockerfile python
```

Example flow:

```
? Base image (python:3.11) →
👉  FROM python:3.11

? Working directory (/app) →
👉  WORKDIR /app

? Copy files? →
👉  COPY . .

? Command? →
👉  CMD ["python", "app.py"]
```

👉 Learn Dockerfile syntax through repetition

---

## 🔹 Example: running code in a container

```bash
dx run python
```

```
? Run in background? (Y/n)
? Mount current directory? (Y/n)
? Container working directory? (default: /app)
? Python file to run (leave empty to skip)
? Name container?
```

Result:

```
👉 docker run -d -v $(pwd):/app -w /app --name python python
```

Explanation:

```
-v         → mount current directory
             (so your local files are available inside the container)

-w         → set working directory to /app
             (so commands run where your files are mounted)
```

👉 Learn how `-v` and `-w` work together

---

## ✅ Commands

### 🔹 dx run

Run a container with guided prompts:

```bash
dx run nginx
```

If unsupported:

```
❌ Unknown image: foo
💡 Tip: run `dx supported`
```

---

### 🔹 dx dockerfile

Build a Dockerfile step by step:

```bash
dx dockerfile python
```

---

### 🔹 dx supported

```
nginx      → web server (ports)
postgres   → database (ports + env)
mysql      → database (ports + env)
redis      → cache (ports)
node       → development (volume)
python     → development (volume + command)
```

---

### 🔹 dx reset

```bash
docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
```

👉 Enables repetition

---

## 🧠 Core concept

```
IMAGE_PROFILES
```

Example:

```
nginx     → ports
python    → volume + command
postgres  → ports + env
```

👉 One system powers:

- prompts
- defaults
- explanations
- Dockerfile generation

---

## ✅ Real Docker execution

dx does NOT simulate anything.

It runs:

```
--- Docker output ---
<container id / logs>

✅ Container started — ID shown in Docker output above
```

---

## 🧱 Core principle

Always show:

```bash
docker ...
```

Because:

👉 If you don’t see the real command, you don’t learn it

---

## 🧠 Philosophy

This is NOT:

- a Docker replacement
- a production tool
- a full abstraction layer

This IS:

✅ a learning-first CLI

Designed to take you from:

```
"I copy Docker commands"
↓
"I recognize patterns"
↓
"I understand what I’m doing"
↓
"I can write them myself"
```

---

## 🏗️ Architecture

```
src/
└── dx/
    ├── cli.py
    ├── commands/
    ├── config/
    └── ui/
```

👉 Flat structure  
👉 IMAGE_PROFILES drives behavior

---

## 📚 Documentation

See the `docs/` folder for:

- project context
- roadmap
- design principles
- prompt and output guidelines

---

## 🔧 Installation

### Requirements

- Python 3.10+
- Docker installed and running

### Install

```bash
git clone <https://github.com/dx.git>
cd dx
pip install -e .
```

### Verify

```bash
dx --help
```

---

## 📄 License

MIT
