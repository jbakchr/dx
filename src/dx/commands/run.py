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

from dx.config.images import IMAGE_PROFILES


WEB_IMAGES = {"nginx", "httpd", "apache"}
DB_IMAGES = {"postgres", "mysql", "mongo", "redis"}


def get_image_name(image: str):
    return image.split(":")[0]


def get_profile(image_name: str):
    return IMAGE_PROFILES.get(image_name, {})



def build_command(image, detached, host_port, container_port, name, env_vars):
    parts = ["docker", "run"]

    if detached:
        parts.append("-d")

    if host_port and container_port:
        parts.extend(["-p", f"{host_port}:{container_port}"])

    for key, value in env_vars.items():
        parts.extend(["-e", f"{key}={value}"])

    if name:
        parts.extend(["--name", name])

    parts.append(image)

    return " ".join(parts)


def run(image: str):
    """Interactive run command"""

    print()

    # ---- input ----
    
    image_name = get_image_name(image)
    profile = get_profile(image_name)

    # ---- prompts ----

    host_port = None
    container_port = None
    env_vars = {}

    # PORT handling (nginx case)
    if "port" in profile.get("prompts", []):
        host_port = ask_port()

        default_container_port = profile.get("container_port", "")
        container_port_input = input(
            f"? Container port? (default {default_container_port}) → "
        ).strip()

        container_port = (
            container_port_input if container_port_input else str(default_container_port)
        )

    # ENV handling (postgres case)
    if "env" in profile.get("prompts", []):
        print("\nℹ️ Configure environment variables:\n")

        for key, default in profile.get("env", {}).items():
            value = input(f"? {key}? (default {default}) → ").strip()
            env_vars[key] = value if value else default

    # always ask these
    detached = ask_detached()
    name = ask_name()

    # ---- build ----
    cmd = build_command(
        image=image,
        detached=detached,
        host_port=host_port,
        container_port=container_port,
        name=name,
        env_vars=env_vars,
)

    # ---- output ----
    separator()
    show_command(cmd)
    explain(detached, host_port, container_port, name, env_vars)
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