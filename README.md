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

```

docker run -d -p 8080:80 --name web nginx

```

You can do:

```

dx run nginx

```

And go through a guided flow:

```

? Expose port? (default 8080)
? Container port? (default 80)
? Run in background? (Y/n)
? Name container? → web

```

Which gives you:

```

Generated command:

👉  docker run -d -p 8080:80 --name web nginx

```

With explanation:

```

-d        → run in background  
so your terminal stays free and non-blocked

-p        → map port 8080 → 80  
so you can access the service from your machine

\--name    → name container "web"  
so you can reference it later

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
- see the Docker command  
- understand the flags  
- run it  
- observe the result  

👉 Over time, you stop needing dx

---

## ✅ Commands

### 🔹 dx run

Run a container with guided prompts.

```

dx run nginx

```

If the image is unsupported:

```

dx run foo

Unknown image: foo
Tip: run `dx supported`

```

---

### 🔹 dx supported

Show supported images:

```

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

docker stop $(docker ps -q)
→ stop all running containers

```

---

### 🔹 dx rm --all

Remove all containers:

```

docker rm $(docker ps -a -q)
→ remove all containers

```

---

### 🔹 dx reset

Reset your environment (fresh start):

```

docker stop $(docker ps -q)
docker rm $(docker ps -a -q)

```

👉 Combines stop + remove  
👉 Shows real commands  
👉 Encourages repetition  

---

## 🧩 Supported concepts

dx teaches core Docker usage:

### Container lifecycle
- docker run  
- docker stop  
- docker rm  

### Flags
- `-d` → run in background  
- `-p` → map ports  
- `-e` → environment variables  
- `-v` → mount files  
- `-w` → working directory  

---

## 🧠 Image-aware prompts

dx adapts based on the image:

- nginx → ports  
- postgres → ports + env  
- python → volume + command  

### Example

```

dx run python

```
```

? Mount current directory? (Y/n)
? Python file to run → app.py

```
```

👉  docker run -v $(pwd):/app -w /app python python app.py

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
👉 Learning stays the focus  

---

## 🧠 Why this exists

Docker isn’t hard because of concepts.

It’s hard because:
- remembering syntax  
- remembering flags  
- remembering combinations  

dx helps you build that **through repetition**.

---

## 🔧 Installation

### Requirements
- Python 3.10+
- Docker installed and running

### Install

```

git clone <https://github.com/dx.git>
cd dx
pip install -e .

```

### Verify

```

dx --help

```

---

## 📄 License

MIT
