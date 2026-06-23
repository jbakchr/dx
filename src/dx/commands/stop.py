# src/dx/commands/stop.py

import subprocess


def stop(all: bool = False):
    if not all:
        print("\nOnly `--all` is supported for now.\n")
        return

    print()
    print("🛑 Stopping all running containers:\n")

    command = "docker stop $(docker ps -q)"

    print(command)
    print("→ stop all running containers\n")

    confirm = input("Run? (Y/n) ").strip().lower()

    if confirm == "n":
        print("\nAborted ❌\n")
        return

    print("\nExecuting Docker command...\n")
    print("--- Docker output ---\n")

    subprocess.run(command, shell=True)

    print("\n✅ Done\n")
