from dx.ui.output import print_header, print_instruction, show_header
from dx.ui.prompt import input_prompt
from dx.config.images import IMAGE_PROFILES


def run(image: str | None = None) -> None:
    """
    Build a Dockerfile through an interactive workflow.

    Guides the user through common Dockerfile instructions,
    applies image-specific defaults, and generates a Dockerfile
    that can be copied into a project.

    Args:
        image: Name of the image profile to use.

    Returns:
        None.
    """

    show_header("🧱 Dockerfile Builder")

    # Guard: require image
    if not image:
        print("❌ You must provide an image.\n")
        print("Example:")
        print("  dx dockerfile python\n")
        print("Run 'dx supported' to see available images.\n")
        return

    # Guard: supported images
    if image not in IMAGE_PROFILES:
        print(f"❌ Unsupported image: {image}\n")
        print("Supported images:")

        for name in IMAGE_PROFILES:
            print(f"  - {name}")

        print("\nExample:")
        print("  dx dockerfile python\n")
        return

    print(f"Using defaults for: {image}\n")

    # Get profile
    profile = IMAGE_PROFILES.get(image, {})
    dockerfile_defaults = profile.get("dockerfile", {})

    default_base = dockerfile_defaults.get("base", "python:3.11")
    default_workdir = dockerfile_defaults.get("workdir")
    default_cmd = dockerfile_defaults.get("cmd")

    dockerfile_lines: list[str] = []

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
        workdir = input_prompt(
            "Working directory",
            default=default_workdir,
        )

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
    copy = input(
        "? Copy current directory into container? (Y/n) → "
    ).strip().lower()

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
            default=default_cmd,
        )

        cmd_parts = cmd.split() if cmd else default_cmd.split()
        cmd_as_list = ", ".join(
            f'"{part}"' for part in cmd_parts
        )

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