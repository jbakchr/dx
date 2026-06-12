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


WEB_IMAGES = {"nginx", "httpd", "apache"}
DB_IMAGES = {"postgres", "mysql", "mongo", "redis"}


def get_image_name(image: str):
    return image.split(":")[0]


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
    
    image_name = get_image_name(image)

    # conditional prompt
    if image_name in WEB_IMAGES:
        port = ask_port()
    else:
        port = None

    # always ask these
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