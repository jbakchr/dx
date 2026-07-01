from dx.ui.prompt import ask_port, ask_detached



def handle_port(profile: dict) -> tuple[str, str]:
    """
    Collect port mapping inputs for an image profile.

    Prompts the user for a host port and, when applicable,
    a container port.

    Args:
        profile: The image profile configuration.

    Returns:
        A tuple containing the host port and container port.
    """

    default_host = str(
        profile.get("default_host_port")
        or profile.get("container_port", "8080")
    )
    host_port = ask_port(default_host)

    if "container_port" in profile.get("prompts", []):
        default = profile.get("container_port", "")
        value = input(f"? Container port? (default: {default}) → ").strip()
        container_port = value if value else str(default)
    else:
        container_port = str(profile.get("container_port"))

    return host_port, container_port



def handle_env(profile: dict) -> dict[str, str]:
    """
    Collect environment variable inputs for an image profile.

    Prompts the user for each configured environment variable
    and falls back to default values when no input is provided.

    Args:
        profile: The image profile configuration.

    Returns:
        A dictionary of environment variable names and values.
    """

    env_vars = {}

    print("\nℹ️ Configure environment variables:\n")

    for key, default in profile.get("env", {}).items():
        value = input(f"? {key} (default: {default}) → ").strip()
        env_vars[key] = value if value else default

    return env_vars




def handle_volume() -> tuple[str | None, str | None]:
    """
    Collect volume and working directory inputs.

    Prompts the user to optionally mount the current directory
    and configure the container working directory.

    Returns:
        A tuple containing the volume mapping and working
        directory. Returns (None, None) if mounting is skipped.
    """

    choice = input("? Mount current directory? (Y/n) → ").strip().lower()

    if choice == "n":
        return None, None

    volume = "$(pwd):/app"

    workdir = input("? Container working directory? (default: /app) → ").strip()
    workdir = workdir if workdir else "/app"

    return volume, workdir


def handle_command() -> str | None:
    """
    Collect a Python command to run inside the container.

    Returns:
        A Python command string, or None if no command
        was provided.
    """

    cmd = input("? Python file to run (leave empty to skip) → ").strip()

    if not cmd:
        return None

    return f"python {cmd}"



def collect_common_inputs(
    profile: dict,
) -> tuple[str | None, str | None, bool]:
    """
    Collect Docker inputs common to multiple image profiles.

    Currently includes port configuration and detached mode.

    Args:
        profile: The image profile configuration.

    Returns:
        A tuple containing the host port, container port,
        and detached mode flag.
    """

    host_port = None
    container_port = None
    detached = False

    prompts = profile.get("prompts", [])

    if "port" in prompts:
        host_port, container_port = handle_port(profile)

    detached = ask_detached()

    return host_port, container_port, detached



def collect_image_inputs(
    profile: dict,
) -> tuple[
    dict[str, str],
    str | None,
    str | None,
    str | None,
]:
    """
    Collect image-specific Docker inputs.

    Prompts are determined by the image profile and may
    include environment variables, volume mounting,
    working directory configuration, and commands.

    Args:
        profile: The image profile configuration.

    Returns:
        A tuple containing:
            - environment variables
            - volume mapping
            - working directory
            - command
    """

    env_vars = {}
    volume = None
    workdir = None   # ✅ ADD THIS
    command = None

    prompts = profile.get("prompts", [])

    if "env" in prompts:
        env_vars = handle_env(profile)

    if "volume" in prompts:
        volume, workdir = handle_volume()

    if "command" in prompts:
        command = handle_command()

    return env_vars, volume, workdir, command


