def handle_port(profile):
    from dx.ui.prompt import ask_port

    default = str(profile.get("container_port", "8080"))
    host_port = ask_port(default)

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


def collect_inputs(profile):
    host_port = None
    container_port = None
    env_vars = {}

    prompts = profile.get("prompts", [])

    if "port" in prompts:
        host_port, container_port = handle_port(profile)

    if "env" in prompts:
        env_vars = handle_env(profile)

    return host_port, container_port, env_vars