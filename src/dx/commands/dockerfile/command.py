from dx.ui.output import print_header, print_instruction
from dx.ui.prompt import input_prompt


def run():
    print_header("Dockerfile Builder")

    dockerfile_lines = []

    # Step 1 — Base image
    base_image = input_prompt("Base image", default="python:3.11")

    from_line = f"FROM {base_image}"
    dockerfile_lines.append(from_line)

    print_instruction(from_line)

    print(
        """
FROM → defines the base image
everything builds on top of this
""".strip()
    )

    # Step 2 — Working directory
    workdir = input_prompt("Working directory", default="/app")

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

    # Step 4 — Command
    # Step 4 — Command
    cmd = input_prompt("Command to run (e.g. python app.py)", default="python app.py")

    # Convert string → JSON array style
    cmd_parts = cmd.split() if cmd else ["python", "app.py"]
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