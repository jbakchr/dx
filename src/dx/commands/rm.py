# src/dx/commands/rm.py

import subprocess

from dx.ui.output import separator, show_command, show_header


def rm(all: bool = False) -> None:
    """
    Remove Docker containers.

    Currently, only the ``--all`` option is supported. When enabled,
    the user is shown the generated Docker command and asked for
    confirmation before execution.

    Args:
        all: Whether to remove all containers.

    Returns:
        None.
    """

    if not all:
        print("\nOnly `--all` is supported for now.\n")
        return

    show_header("🧹 Removing all containers")

    command = "docker rm $(docker ps -a -q)"

    show_command(command)

    separator()
    confirm = input("Run? (Y/n) ").strip().lower()
    separator()

    if confirm == "n":
        print("\nAborted ❌\n")
        return

    print("Executing Docker command...\n")
    print("--- Docker output ---\n")

    subprocess.run(command, shell=True)

    print("\n✅ Done\n")