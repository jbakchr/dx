# 🐳 dx

**Learn Docker by using it — not memorizing it**

A CLI that helps you _learn Docker by using it_.

---

## 🧠 What is this?
  
dx is a small CLI that sits on top of Docker.  
But unlike most tools, it does **not try to hide Docker**.

Instead, it helps you:

- use Docker without friction ✅
- understand what you are doing ✅
- gradually learn the real Docker CLI ✅

---

## 🔧 Installation

### Requirements
- Python 3.10+
- Docker installed and working

### 1. Clone the repository
  
git clone https://github.com/dx.git  
cd dx

### 2. Install locally (editable mode)
  
pip install -e .

### 3. Verify installation
  
dx --help

---

## ✅ Try it
  
dx run nginx  
dx run redis  
dx run python  

To see supported images:
```

dx supported

```

---

## ⚠️ Notes
- Docker must already be installed and running
- dx simply calls the Docker CLI

---

## 🎯 The goal
  
Most tools do this:  
→ Hide complexity  

dx does something else:  
→ Reveal complexity — step by step  

---

## ⚡ The idea
  
Instead of writing:

```

docker run -d -p 8080:80 --name web nginx

```

You can do:

```

dx run nginx

```

And get a guided flow:

```

? Expose port? (default 8080)
? Container port? (default 80)
? Run in background? (Y/n)
? Name container? → web

```

Generated command:

```

docker run -d -p 8080:80 --name web nginx

```

Explanation:

```

-d        → run in background (so your terminal stays free)
-p        → map port 8080 → 80 (so you can access the service from your machine)
\--name    → name container "web" (so you can reference it later)

```

---

## 🔁 The learning loop
  
Every time you use dx:

- Answer prompts  
- See the real Docker command  
- Understand the flags  
- Run it  
- Observe the result  

👉 Over time, you stop needing dx  

---

## 🔁 How dx works (at a glance)

```

input → prompts → command → explanation → execution → learning

```

---

## ✅ Commands

---

### 🔹 dx run <image>

Run a container with guided prompts.

If you try an unsupported image:

```

dx run foo

Unknown image: foo

Tip: run `dx supported` to see available images

```

---

### 🔹 dx supported

Show supported images:

```

Supported images:

nginx     → web server (ports)
postgres  → database (ports + env)
mysql     → database (ports + env)
redis     → cache (ports)
node      → development (volume)
python    → development (volume + command)

```

---

### 🔹 dx stop --all

Stop all running containers:

```

dx stop --all

docker stop $(docker ps -q)
→ stop all running containers

Run? (Y/n)

```

---

### 🔹 dx rm --all

Remove all containers:

```

dx rm --all

docker rm $(docker ps -a -q)
→ remove all containers

Run? (Y/n)

```

---

### 🔹 dx reset

Stop and remove all containers (fresh start):

```

dx reset

docker stop $(docker ps -q)
→ stop all running containers

docker rm $(docker ps -a -q)
→ remove all containers

Run? (Y/n)

```

👉 Combines stop + remove into a single step  
👉 Shows the real Docker commands before running  
👉 Reinforces container lifecycle usage  

---

## 🧩 Supported concepts

dx teaches the core Docker workflow:

### Container lifecycle
- docker run  
- docker stop  
- docker rm  

### Flags and concepts
- -d → run in background  
- -p → map ports  
- -e → environment variables  
- -v → mount files into container  
- -w → working directory  
- command execution (e.g. python app.py)

---

## 🧠 Image-aware prompts (core concept)

dx adapts behavior based on the image.

Examples:

- nginx → ports  
- postgres → ports + env  
- python → volume + command  

---

### ✅ Example: python

```

dx run python

```
```

? Mount current directory? (Y/n)
? Python file to run (leave empty to skip) → app.py
? Run in background? (Y/n)
? Name container?

```

Generated command:

```

docker run -v $(pwd):/app -w /app python python app.py

```

Explanation:

```

-v        → mount current directory (so your local files are available inside the container)
-w        → set working directory (so commands run in the correct folder)

```

---

## ✅ Real Docker execution

dx does NOT simulate anything.  
It runs the real Docker command and shows real output:

```

\--- Docker output ---
\<container id / logs>

```

---

## 🧱 Core principle

Always show:

```

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

✅ A learning-first CLI  

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

## 🏗️ Architecture (simple by design)

```

src/
└── dx/
├── cli.py
├── commands/
│   ├── run/
│   │   ├── run.py
│   │   ├── exec.py
│   │   └── prompts.py
│   ├── stop.py
│   ├── rm.py
│   ├── reset.py
│   └── supported.py
├── config/
│   └── images.py
└── ui/
├── output.py
└── prompt.py

```

👉 Structure follows complexity  
👉 Simple commands stay simple  
👉 Complex commands get grouped  

---

## 🧠 Why this exists

Learning Docker is hard not because of concepts, but because of:

- remembering syntax  
- remembering flags  
- remembering combinations  

Example:

```

docker run \[OPTIONS] IMAGE \[COMMAND]

```

👉 Simple, but hard to internalize  

---

## 🧠 Summary
  
dx is not trying to replace Docker.  
It is trying to make this transition easier:

```

"I don’t understand this command"
↓
"I recognize parts of it"
↓
"I can write it myself"

```

---

## ⚠️ Note
  
Docker must already be installed.  
dx simply calls the Docker CLI.

---

## 📄 License
  
MIT
