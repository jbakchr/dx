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

    def line(flag: str, short: str, long: str):
        print(f"{flag:<10} → {short}")
        print(f"{'':<10}   {long}\n")

    if detached:
        line(
            "-d",
            "run in background",
            "(so your terminal stays free and non-blocked)"
        )

    if host_port and container_port:
        line(
            "-p",
            f"map port {host_port} → {container_port}",
            "(so you can access the service from your machine)"
        )

    for key, value in env_vars.items():
        line(
            "-e",
            f"set environment variable '{key}={value}'",
            "(used to set things like passwords and config inside the container)"
        )

    if name:
        line(
            "--name",
            f'name container "{name}"',
            "(so you can reference it later)"
        )

    if volume:
        line(
            "-v",
            "mount current directory",
            "(so your local files are available inside the container)"
        )
        line(
            "-w",
            "set working directory",
            "(so commands run in the correct folder)"
        )



def execution_header():
    print("Executing Docker command...\n")
    print("--- Docker output ---\n")


def execution_done():
    print("\n📦 Container ID (from Docker output above)")
    print("\n✅ Container started (see Docker output above)")


def print_header(title: str):
    separator()
    print(f"{title}")
    separator()


def print_instruction(line: str):
    print(f"👉  {line}")