from dx.ui.output import print_header, print_instruction
from dx.ui.prompt import input_prompt


DOCKERFILE_DEFAULTS = {
    "python": {
        "base": "python:3.11",
        "workdir": "/app",
        "cmd": "python app.py",
    },
    "node": {
        "base": "node:18",
        "workdir": "/app",
        "cmd": "npm start",
    },
    "nginx": {
        "base": "nginx:latest",
        "workdir": None,
        "cmd": None,
    },
}


def run(image: str = None):
    print_header("Dockerfile Builder")

    # Guard: require supported image
    if not image:
        print("❌ You must provide an image.")
        print("\nExample:")
        print("  dx dockerfile python\n")
        print("Run 'dx supported' to see available images.\n")
        return

    if image not in DOCKERFILE_DEFAULTS:
        print(f"❌ Unsupported image: {image}")
        print("\nSupported images:")

        for name in DOCKERFILE_DEFAULTS:
            print(f"  - {name}")

        print("\nExample:")
        print(f"  dx dockerfile {list(DOCKERFILE_DEFAULTS.keys())[0]}\n")

        return

    # Optional: show which defaults are used
    if image:
        print(f"Using defaults for: {image}\n")

    defaults = DOCKERFILE_DEFAULTS.get(image, {})

    default_base = defaults.get("base", "python:3.11")
    default_workdir = defaults.get("workdir", "/app")
    default_cmd = defaults.get("cmd", "python app.py")

    dockerfile_lines = []

    # Step 1 — Base image
    base_image = input_prompt("Base image", default=default_base)

    from_line = f"FROM {base_image}"
    dockerfile_lines.append(from_line)

    print_instruction(from_line)

    print(
        """
FROM → defines the base image
everything builds on top of this
""".strip()
    )

    # Step 2 — Working directory (optional)
    if default_workdir:
        workdir = input_prompt("Working directory", default=default_workdir)

        workdir_line = f"WORKDIR {workdir}"
        dockerfile_lines.append(workdir_line)

        print_instruction(workdir_line)

        print(
            """
WORKDIR → sets the directory inside the container
where commands will run
""".strip()
        )

    # Step 3 — Copy files (optional)
    copy = input("? Copy current directory into container? (Y/n) → ").strip().lower()

    if copy != "n":
        copy_line = "COPY . ."
        dockerfile_lines.append(copy_line)

        print_instruction(copy_line)

        print(
            """
COPY → adds files from your machine into the image
so your code is available inside the container
""".strip()
        )

    # Step 4 — Command (optional)
    if default_cmd:
        cmd = input_prompt(
            "Command to run (e.g. python app.py)",
            default=default_cmd
        )

        cmd_parts = cmd.split() if cmd else default_cmd.split()
        cmd_as_list = ", ".join(f'"{part}"' for part in cmd_parts)

        cmd_line = f"CMD [{cmd_as_list}]"
        dockerfile_lines.append(cmd_line)

        print_instruction(cmd_line)

        print(
            """
CMD → defines the default command to run
when the container starts
""".strip()
        )

    # Final output
    print("\n" + "-" * 60)
    print("\nYour Dockerfile:\n")

    for line in dockerfile_lines:
        print(line)

    print("\n" + "-" * 60)

    print("\n👉 Copy this into a file named 'Dockerfile'\n")