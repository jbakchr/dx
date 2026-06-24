# src/dx/ui/output.py


def show_run_header() -> None:
    separator()
    print("You're about to run a real Docker container.\n")
    print("Answer a few prompts to build the command step by step.")
    separator()


def separator():
    print("\n" + "-" * 60 + "\n")


def show_command(cmd: str):
    print("Generated command:\n")
    print(f"👉  {cmd}")


def explain(detached, host_port, container_port, name, env_vars, volume):
    print("\nExplanation:\n")

    if detached:
        print("-d        → run in background (so your terminal stays free and non-blocked)")

    if host_port and container_port:
        print(f"-p        → map port {host_port} → {container_port} (so you can access the service from your machine)")

    for key, value in env_vars.items():
        print(f"-e        → set environment variable '{key}={value}' (used to set things like passwords and config inside the container)")

    if name:
        print(f'--name    → name container "{name}" (so you can reference it later)')
    
    if volume:
        print("-v        → mount current directory (so your local files are available inside the container)")
        print("-w        → set working directory (so commands run in the correct folder)")

    print()


def execution_header():
    print("Executing Docker command...\n")
    print("--- Docker output ---\n")


def execution_done():
    print("\n📦 Container ID (from Docker output above)")
    print("\n✅ Container started (see Docker output above)")