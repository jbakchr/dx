# src/dx/commands/run.py

from dx.ui.prompt import ask_detached, ask_name, confirm_run
from dx.ui.output import separator, show_command, explain
from dx.commands.run_prompts import collect_inputs
from dx.commands.run_exec import execute

from dx.config.images import IMAGE_PROFILES


def get_image_name(image: str):
    return image.split(":")[0]


def get_profile(image_name: str):
    return IMAGE_PROFILES.get(image_name, {})



def build_command(image, detached, host_port, container_port, name, env_vars, volume, command):
    parts = ["docker", "run"]

    if detached:
        parts.append("-d")

    if host_port and container_port:
        parts.extend(["-p", f"{host_port}:{container_port}"])

    for key, value in env_vars.items():
        parts.extend(["-e", f"{key}={value}"])
    
    if volume:
        parts.extend(["-v", volume])
        parts.extend(["-w", "/app"])

    if name:
        parts.extend(["--name", name])

    parts.append(image)

    if command:
        parts.extend(command.split())

    return " ".join(parts)


def run(image: str):
    """Interactive run command"""

    print()

    # ---- input ----
    
    image_name = get_image_name(image)
    profile = get_profile(image_name)

    # ---- prompts ----
    host_port, container_port, env_vars, volume, command = collect_inputs(profile)

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
        volume=volume,
        command=command
    )

    # ---- output ----
    separator()
    show_command(cmd)
    explain(detached, host_port, container_port, name, env_vars, volume)
    separator()

    # ---- confirm ----
    if not confirm_run():
        print("\nAborted ❌")
        return

    separator()

    # ---- execute ----
    execute(cmd)
