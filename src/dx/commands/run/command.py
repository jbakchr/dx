# src/dx/commands/run.py

from dx.ui.prompt import ask_name, confirm_run
from dx.ui.output import separator, show_command, explain, show_header, show_run_header
from dx.commands.run.prompts import collect_image_inputs, collect_common_inputs
from dx.commands.run.exec import execute

from dx.config.images import IMAGE_PROFILES


def get_image_name(image: str) -> str:
    """
    Extract the base image name from an image reference.

    Args:
        image: Docker image name, optionally including a tag.

    Returns:
        The image name without its tag.
    """
    return image.split(":")[0]


def get_profile(image_name: str) -> dict:
    """
    Retrieve the image profile for a supported image.

    Args:
        image_name: Name of the Docker image.

    Returns:
        The matching image profile, or an empty dictionary if
        the image is not supported.
    """
    return IMAGE_PROFILES.get(image_name, {})


def build_command(
    image: str,
    detached: bool,
    host_port: str | None,
    container_port: str | None,
    name: str | None,
    env_vars: dict,
    volume: str | None,
    workdir: str | None,
    command: str | None,
) -> str:
    """
    Build a docker run command from user inputs.

    Args:
        image: Docker image to run.
        detached: Whether to run the container in the background.
        host_port: Host port to expose.
        container_port: Container port to expose.
        name: Container name.
        env_vars: Environment variables to inject.
        volume: Volume mapping specification.
        workdir: Working directory inside the container.
        command: Command to execute inside the container.

    Returns:
        A complete docker run command.
    """
    parts = ["docker", "run"]

    if detached:
        parts.append("-d")

    if host_port and container_port:
        parts.extend(["-p", f"{host_port}:{container_port}"])

    for key, value in env_vars.items():
        parts.extend(["-e", f"{key}={value}"])

    if volume:
        parts.extend(["-v", volume])

    if workdir:
        parts.extend(["-w", workdir])

    if name:
        parts.extend(["--name", name])

    parts.append(image)

    if command:
        parts.extend(command.split())

    return " ".join(parts)


def run(image: str) -> None:
    """
    Run a container through the interactive dx workflow.

    Guides the user through image-specific prompts,
    builds the corresponding docker run command,
    explains the selected options, and optionally
    executes the command.

    Args:
        image: Docker image to run.

    Returns:
        None.
    """
    # ---- input ----

    image_name = get_image_name(image)
    profile = get_profile(image_name)

    if image_name not in IMAGE_PROFILES:
        print(f"\n❌ Unknown image: {image_name}\n")
        print("💡 Tip: run `dx supported` to see available images\n")
        return

    # ---- header ----

    # show_run_header()
    show_header(f"Build a real Docker run command step by step.")

    # ---- prompts ----

    host_port, container_port, detached = collect_common_inputs(profile)

    env_vars, volume, workdir, command = collect_image_inputs(profile)

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
        workdir=workdir,
        command=command,
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