# src/dx/commands/reset.py

import subprocess


def reset():
    print()
    print("♻️ Resetting container state:\n")

    stop_cmd = "docker stop $(docker ps -q)"
    rm_cmd = "docker rm $(docker ps -a -q)"

    print(stop_cmd)
    print("→ stop all running containers\n")

    print(rm_cmd)
    print("→ remove all containers\n")

    confirm = input("Run? (Y/n) ").strip().lower()

    if confirm == "n":
        print("\nAborted ❌\n")
        return

    print("\nExecuting Docker commands...\n")
    print("--- Docker output ---\n")

    # Run stop first, then remove
    subprocess.run(stop_cmd, shell=True)
    subprocess.run(rm_cmd, shell=True)

    print("\n✅ Reset complete\n")