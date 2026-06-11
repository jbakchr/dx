# src/dx/commands/run.py

import subprocess
from dx.ui.prompt import ask_port, ask_detached, ask_name, confirm_run
from dx.ui.output import (
    separator,
    show_command,
    explain,
    execution_header,
    execution_done,
)


def build_command(image, detached, port, name):
    parts = ["docker", "run"]

    if detached:
        parts.append("-d")

    if port:
        parts.extend(["-p", f"{port}:80"])

    if name:
        parts.extend(["--name", name])

    parts.append(image)

    return " ".join(parts)


def run(image: str):
    """Interactive run command"""

    print()

    # ---- input ----
    port = ask_port()
    detached = ask_detached()
    name = ask_name()

    # ---- build ----
    cmd = build_command(image, detached, port, name)

    # ---- output ----
    separator()
    show_command(cmd)
    explain(detached, port, name)
    separator()

    # ---- confirm ----
    if not confirm_run():
        print("\nAborted ❌")
        return

    separator()

    # ---- execute ----
    execution_header()
    subprocess.run(cmd, shell=True)
    execution_done()

    separator()