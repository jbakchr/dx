# src/dx/commands/rm.py

import subprocess


def rm(all: bool = False):
    if not all:
        print("\nOnly `--all` is supported for now.\n")
        return

    print()
    print("🧹 Removing all containers:\n")

    command = "docker rm $(docker ps -a -q)"

    print(command)
    print("→ remove all containers\n")

    confirm = input("Run? (Y/n) ").strip().lower()

    if confirm == "n":
        print("\nAborted ❌\n")
        return

    print("\nExecuting Docker command...\n")
    print("--- Docker output ---\n")

    subprocess.run(command, shell=True)

    print("\n✅ Done\n")