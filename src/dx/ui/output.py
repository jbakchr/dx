# src/dx/ui/output.py

def separator():
    print("\n" + "-" * 50 + "\n")


def show_command(cmd: str):
    print("Generated command:\n")
    print(cmd)


def explain(detached, host_port, container_port, name, env_vars):
    print("\nExplanation:\n")

    if detached:
        print("-d        → run in background")

    if host_port and container_port:
        print(f"-p        → map port {host_port} → {container_port}")

    for key, value in env_vars.items():
        print(f"-e {key}={value} → set environment variable inside container")

    if name:
        print(f'--name    → name container "{name}"')

    print()


def execution_header():
    print("Executing Docker command...\n")
    print("--- Docker output ---\n")


def execution_done():
    print("\n📦 Container ID (from Docker output above)")
    print("\n✅ Container started (see Docker output above)")