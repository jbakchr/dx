import subprocess


def separator():
    print("\n" + "-" * 50 + "\n")


def run(image: str):
    """Interactive run command"""

    # ---- prompts ----

    port_input = input("? Expose port? (default 8080) → ").strip()
    port = port_input if port_input else "8080"

    detached_input = input("? Run in background? (Y/n) → ").strip().lower()
    detached = detached_input != "n"

    name = input("? Name container? → ").strip()

    # ---- build command ----

    parts = ["docker", "run"]

    if detached:
        parts.append("-d")

    if port:
        parts.extend(["-p", f"{port}:80"])

    if name:
        parts.extend(["--name", name])

    parts.append(image)

    cmd = " ".join(parts)

    # ---- output ----

    separator()
    print("Generated command:\n")
    print(cmd)

    print("\nExplanation:\n")

    if detached:
        print("-d       → run in background")

    if port:
        print(f"-p       → map port {port} → 80")

    if name:
        print(f'--name   → name the container "{name}"')

    separator()

    # ---- confirmation ----

    confirm = input("Run? (Y/n) ").strip().lower()

    separator()

    if confirm == "n":
        print("\nAborted ❌")
        return

    print("Executing Docker command...\n")
    print("--- Docker output ---\n")

    subprocess.run(cmd, shell=True)

    print("\n📦 Container ID shown above")

    separator()
