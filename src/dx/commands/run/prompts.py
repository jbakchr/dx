from dx.ui.prompt import ask_port


def handle_port(profile):
    default_host = str(
        profile.get("default_host_port")
        or profile.get("container_port", "8080")
    )
    host_port = ask_port(default_host)

    if "container_port" in profile.get("prompts", []):
        default = profile.get("container_port", "")
        value = input(f"? Container port (default: {default}) → ").strip()
        container_port = value if value else str(default)
    else:
        container_port = str(profile.get("container_port"))

    return host_port, container_port


def handle_env(profile):
    env_vars = {}

    print("\nℹ️ Configure environment variables:\n")

    for key, default in profile.get("env", {}).items():
        value = input(f"? {key} (default: {default}) → ").strip()
        env_vars[key] = value if value else default

    return env_vars



def handle_volume():
    choice = input("? Mount current directory? (Y/n) → ").strip().lower()

    if choice == "n":
        return None

    return "$(pwd):/app"


def handle_command():
    cmd = input("? Python file to run (leave empty to skip) → ").strip()

    if not cmd:
        return None

    return f"python {cmd}"

def collect_inputs(profile):
    host_port = None
    container_port = None
    env_vars = {}
    volume = None
    command = None

    prompts = profile.get("prompts", [])

    if "port" in prompts:
        host_port, container_port = handle_port(profile)

    if "env" in prompts:
        env_vars = handle_env(profile)

    if "volume" in prompts:
        volume = handle_volume()

    if "command" in prompts:
        command = handle_command()

    return host_port, container_port, env_vars, volume, command