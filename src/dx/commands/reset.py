# src/dx/commands/reset.py

import subprocess

from dx.ui.output import separator, show_header


def reset() -> None:
    """
    Reset Docker container state.

    Stops all running containers and then removes all containers.
    The generated Docker commands are displayed and must be
    confirmed before execution.

    Returns:
        None.
    """

    show_header("♻️  Resetting container state")

    stop_cmd = "docker stop $(docker ps -q)"
    rm_cmd = "docker rm $(docker ps -a -q)"

    print("Generated Docker commands:\n")

    print(f"👉  {stop_cmd}")
    print("    → stop all running containers\n")

    print(f"👉  {rm_cmd}")
    print("    → remove all containers")

    separator()
    confirm = input("Run? (Y/n) ").strip().lower()
    separator()

    if confirm == "n":
        print("Aborted ❌\n")
        return

    print("Executing: Generated Docker commands...\n")
    print("--- Docker output ---\n")

    # Run stop first, then remove
    subprocess.run(stop_cmd, shell=True)
    subprocess.run(rm_cmd, shell=True)

    print("\n✅ Reset complete\n")