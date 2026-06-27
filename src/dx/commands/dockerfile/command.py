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