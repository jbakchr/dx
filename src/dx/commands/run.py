import subprocess


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

    print("\nGenerated command:\n")
    print(cmd)

    # ---- confirmation ----

    confirm = input("\nRun? (Y/n) ").strip().lower()

    if confirm == "n":
        print("\nAborted ❌")
        return

    print("\nExecuting Docker command...\n")
    print("--- Docker output ---\n")
    subprocess.run(cmd, shell=True)