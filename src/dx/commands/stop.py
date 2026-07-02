# src/dx/commands/stop.py

import subprocess

from dx.ui.output import separator, show_command, show_header


def stop(all: bool = False) -> None:
    """
    Stop running Docker containers.

    Currently, only the ``--all`` option is supported. When enabled,
    the user is shown the generated Docker command and asked for
    confirmation before execution.

    Args:
        all: Whether to stop all running containers.

    Returns:
        None.
    """

    if not all:
        print("\nOnly `--all` is supported for now.\n")
        return

    show_header("🛑 Stopping all running containers")

    command = "docker stop $(docker ps -q)"

    show_command(command)

    separator()
    confirm = input("Run? (Y/n) ").strip().lower()
    separator()

    if confirm == "n":
        print("\nAborted ❌\n")
        separator()
        return

    print("Executing Docker command...\n")
    print("--- Docker output ---\n")

    subprocess.run(command, shell=True)

    print("\n✅ Done\n")