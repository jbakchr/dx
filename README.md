# 🐳 dx

> A CLI that helps you _learn Docker by using it_

---

## 🧠 What is this?

`dx` is a small, personal CLI that sits on top of Docker.

But unlike most wrappers, it does **not try to hide Docker**.

Instead, it helps you:

- use Docker without friction ✅
- understand what you are doing ✅
- gradually learn the real Docker CLI ✅

---

## 🎯 The goal

Most Docker tools do this:

> Hide complexity

`dx` does something else:

> Reveal complexity — but in small, manageable steps

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

And get:

```
? Expose port? (default 8080) → 3000
? Run in background? (Y/n) → Y
? Name container? → web

Generated command:

docker run -d -p 3000:80 --name web nginx

Run? (Y/n)
```

---

## 🧠 Why this exists

When learning Docker, the hardest part is not _what Docker is_ —  
it's remembering:

- command syntax
- flags (`-d`, `-p`, `--name`)
- argument order
- when and why to use what

For example:

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

This structure is powerful but hard to internalize at first [\[forums.docker.com\]](https://forums.docker.com/t/command-line-documentation-where-is-the-order-of-flags-arguments-specified/119438)

---

### `dx` helps by:

- breaking commands into **small decisions**
- showing you the **final Docker command**
- reinforcing patterns through repetition

---

## 🔁 The learning loop

Every time you use `dx`:

1. You answer a few simple prompts
2. A real `docker` command is generated
3. You see exactly how it is constructed
4. You run it
5. Repeat

Over time, you stop needing `dx`

---

## 🧩 Two modes

### ✅ 1. Do (use Docker)

```bash
dx run nginx
dx ps
dx logs web
```

→ helps you _do things quickly_

---

### ✅ 2. Learn (understand Docker)

```bash
dx learn run
dx explain "docker run -d -p 8080:80 nginx"
```

→ helps you _understand what’s happening_

---

## 🧠 Philosophy

This is not:

- a full Docker replacement
- a feature-complete CLI
- a production-grade tool

This is:

> A tool designed to help one person (me) go from  
> “I copy Docker commands from Google”  
> → to  
> “I understand and write them myself”

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

## 🚀 Initial scope (very small)

The first version will only focus on:

- `dx run` → interactive container runner
- `dx explain` → explain Docker commands
- `dx learn run` → quick patterns for `docker run`

---

## 🔮 Future ideas

- smarter prompts (volumes, env vars, networks)
- dry-run mode (show without executing)
- progressive learning steps
- personal command patterns ("recipes")

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

`dx` simply wraps and calls the existing Docker CLI,  
which provides the actual container functionality [\[bing.com\]](https://bing.com/search?q=what+is+docker+CLI+wrapper+simple+explanation)
