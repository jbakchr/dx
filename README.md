# 🐳 dx

> A CLI that helps you _learn Docker by using it_

---

## 🧠 What is this?

`dx` is a small CLI that sits on top of Docker.

But unlike most wrappers, it does **not try to hide Docker**.

Instead, it helps you:

- use Docker without friction ✅
- understand what you are doing ✅
- gradually learn the real Docker CLI ✅

---

## 🎯 The goal

Most tools do this:

> Hide complexity

`dx` does something else:

> Reveal complexity — step by step

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

And get an interactive flow:

```
? Expose port? (default 8080) →
? Container port? (default 80) →
? Run in background? (Y/n) →
? Name container? → web

--------------------------------------------------

Generated command:

docker run -d -p 8080:80 --name web nginx

Explanation:

-d        → run in background
-p        → map port 8080 → 80
--name    → name container "web"

--------------------------------------------------
```

---

## 🧠 What makes dx different

Most Docker tools:

- hide the underlying command
- optimize for speed

`dx` is different:

- always shows the real command ✅
- explains the flags ✅
- adapts prompts based on the image ✅

---

## 🔁 The learning loop

Every time you use `dx`:

1. You answer simple prompts
2. A real Docker command is generated
3. You see how it is constructed
4. You run it
5. Repeat

👉 Over time, you stop needing `dx`

---

## 🧩 Current features

### ✅ `dx run <image>`

Interactive Docker runner.

---

### 🧠 Image-aware prompts

`dx` adapts to the image you're running:

#### nginx (web)

```
- asks for port mapping
- asks for container port (default 80)
```

#### postgres (database)

```
- asks for environment variables (e.g. password)
```

Example:

```
dx run postgres

ℹ️ Configure environment variables:

? POSTGRES_PASSWORD (default: password) →

? Run in background? (Y/n) →
? Name container? → db

--------------------------------------------------

Generated command:

docker run -d -e POSTGRES_PASSWORD=password --name db postgres

Explanation:

-d        → run in background
-e POSTGRES_PASSWORD=password → set environment variable inside container
--name    → name container "db"
```

---

### ✅ Explanation layer

After generating a command, `dx` explains:

- what each flag does
- why it is used

---

### ✅ Real Docker execution

`dx` does NOT simulate execution.

It runs the real Docker command and shows real output:

```
--- Docker output ---
<actual docker logs / container id>
```

---

## 🧠 Why this exists

Learning Docker is hard not because of concepts, but because of:

- remembering syntax
- remembering flags
- remembering combinations

Example:

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

👉 Simple, but difficult to internalize.

---

## 🧠 Philosophy

This is not:

- a Docker replacement
- a production tool
- a full abstraction

This is:

> A tool designed to help one person go from

```
"I copy Docker commands from Google"
```

to:

```
"I understand and write them myself"
```

---

## 🧱 Core principle

Always show:

```
Generated command:
docker run ...
```

Because:

> If you don’t see the real command, you don’t learn it

---

## 🏗️ Architecture (simple by design)

```
src/dx/
├── cli.py             # Typer CLI entrypoint
├── commands/
│   └── run.py        # run command (orchestrator)
├── ui/
│   ├── prompt.py     # input handling
│   └── output.py     # display / formatting
├── config/
│   └── images.py     # image-specific profiles
```

---

## 🔧 Image profiles (core concept)

`dx` uses small profiles to define:

- default container ports
- required environment variables
- which prompts to show

Example:

```python
IMAGE_PROFILES = {
    "nginx": {
        "container_port": 80,
        "prompts": ["port", "container_port"],
    },
    "postgres": {
        "container_port": 5432,
        "prompts": ["env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
    },
}
```

---

## 🔮 Future ideas

- more image profiles (redis, node, python)
- volumes & file mounts
- smarter explanations ("why this matters")
- `dx explain` command
- `dx learn` command
- dry-run mode
- reusable "recipes"

---

## 🧠 Summary

`dx` is not trying to replace Docker.

It is trying to make this transition easier:

```
"I have no idea what this command means"
            ↓
"I recognize some of it"
            ↓
"I can write it myself"
```

---

## ⚠️ Note

Docker must already be installed.

`dx` simply wraps and calls the existing Docker CLI.

## 📄 License

MIT