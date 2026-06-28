# src/dx/commands/run.py

from dx.ui.prompt import ask_name, confirm_run
from dx.ui.output import separator, show_command, explain, show_run_header
from dx.commands.run.prompts import collect_image_inputs, collect_common_inputs
from dx.commands.run.exec import execute

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

    # ---- input ----
    
    image_name = get_image_name(image)
    profile = get_profile(image_name)

    if image_name not in IMAGE_PROFILES:
        print(f"\n❌ Unknown image: {image_name}\n")
        print("💡 Tip: run `dx supported` to see available images\n")
        return


    # ---- header ----
    show_run_header()

    # ---- prompts ----
    host_port, container_port, detached = collect_common_inputs(profile)

    env_vars, volume, command = collect_image_inputs(profile)

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
