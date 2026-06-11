# src/dx/ui/output.py

def separator():
    print("\n" + "-" * 50 + "\n")


def show_command(cmd: str):
    print("Generated command:\n")
    print(cmd)


def explain(detached, port, name):
    print("\nExplanation:\n")

    if detached:
        print("-d       → run in background")

    if port:
        print(f"-p       → map port {port} → 80")

    if name:
        print(f'--name   → name the container "{name}"')

    print()


def execution_header():
    print("Executing Docker command...\n")
    print("--- Docker output ---\n")


def execution_done():
    print("\n📦 Container ID shown above")
    print("\n✅ Container started (see Docker output above)")