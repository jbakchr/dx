# 🐳 dx

A CLI that helps you _learn Docker by using it_

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

---

### 1. Clone the repository

```

git clone https://github.com/dx.git
cd dx

```

---

### 2. Install locally (editable mode)

```

pip install -e .

```

This installs `dx` as a CLI command on your system.

---

### 3. Verify installation

```

dx --help

```

If everything works, you should see the CLI help output.

---

### ✅ Try it

```

dx run nginx
dx run redis
dx run python

```

---

### ⚠️ Notes

- Docker must already be installed and running
- `dx` simply calls the Docker CLI

---

## 🎯 The goal

Most tools do this:  
_→ Hide complexity_

`dx` does something else:  
_→ Reveal complexity — step by step_

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

? Expose port? (default 8080) →
? Container port? (default 80) →
? Run in background? (Y/n) →
? Name container? → web

***

Generated command:

docker run -d -p 8080:80 --name web nginx

Explanation:

-d        → run in background
-p        → map port 8080 → 80
\--name    → name container "web"

***

```

---

## 🔁 The learning loop

Every time you use `dx`:

- You answer simple prompts
- A real Docker command is generated
- You see how it is constructed
- You run it
- You observe the result

👉 Over time, you stop needing `dx`

---

## 🔁 How `dx` works (at a glance)

```

input → guided prompts → docker command → explanation → execution → learning

```

Example:

```

dx run nginx
    ↓
answer prompts
    ↓
see generated command
    ↓
understand flags
    ↓
run real Docker
    ↓
repeat → build intuition

```

---

## 🧩 Current features

### ✅ `dx run <image>`

Interactive Docker runner.

---

### 🧠 Image-aware prompts (core concept)

dx adapts prompts based on the image you run.

---

### ✅ Supported images

#### 🌐 Web

**nginx**

- port mapping (default: 8080 → 80)

---

#### 🗄️ Databases

**postgres**

- port mapping (5432)
- environment variables

**mysql**

- port mapping (3306)
- environment variables

**redis**

- port mapping (6379)

---

#### 💻 Development containers

**node**

- optional volume mount (`-v`)
- working directory (`-w`)

**python**

- optional volume mount (`-v`)
- working directory (`-w`)
- optional command (run a script)

Example:

```

dx run python

? Mount current directory? (Y/n) →
? Python file to run (leave empty to skip) → app.py
? Run in background? (Y/n) →
? Name container? →

***

Generated command:

docker run -v $(pwd):/app -w /app python python app.py

Explanation:

-v        → mount current directory into container
-w        → set working directory inside container

***

```

---

### ✅ Explanation layer

After generating a command, `dx` explains:

- `-d` → run in background
- `-p` → map ports
- `-e` → set environment variables
- `-v` → mount files into container
- `-w` → set working directory
- `--name` → name the container

---

### ✅ Real Docker execution

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

docker run ...

```

Because:

> If you don’t see the real command, you don’t learn it.

---

## 🧠 Philosophy

This is NOT:

- a Docker replacement
- a production tool
- a full abstraction layer

This IS:

> A learning-first CLI

Designed to take you from:

```

"I copy commands from Google"

```

to:

```

"I understand and write them myself"

```

---

## 🏗️ Architecture (simple by design)

```

src/
└── dx/
    ├── __init__.py
    ├── cli.py
    ├── commands/
    │   ├── __init__.py
    │   ├── run.py           # orchestration
    │   ├── run_exec.py      # execution layer
    │   └── run_prompts.py   # prompt handling
    ├── config/
    │   └── images.py        # image profiles
    └── ui/
        ├── output.py        # display + explanations
        └── prompt.py        # basic prompts

```

---

## 🔧 Image profiles (core concept)

`dx` uses small profiles to define behavior:

```python
IMAGE_PROFILES = {
    "nginx": {
        "container_port": 80,
        "default_host_port": 8080,
        "prompts": ["port", "container_port"],
    },

    "postgres": {
        "container_port": 5432,
        "default_host_port": 5432,
        "prompts": ["port", "env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
    },

    "node": {
        "prompts": ["volume"],
    },

    "python": {
        "prompts": ["volume", "command"],
    },
}
```

👉 Behavior is driven by data — not hardcoded logic.

---

## 🧠 Why this exists

Learning Docker is hard not because of concepts, but because of:

- remembering syntax
- remembering flags
- remembering combinations

Example:

```
docker run [OPTIONS] IMAGE [COMMAND]
```

👉 Simple, but hard to internalize.

---

## 🧠 Summary

`dx` is not trying to replace Docker.

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
`dx` simply calls the Docker CLI.

---

## 📄 License

MIT
