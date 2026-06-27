from dx.ui.output import print_header, print_instruction
from dx.ui.prompt import input_prompt


def run():
    print_header("Dockerfile Builder")

    # Step 1 — Base image
    base_image = input_prompt("Base image", default="python:3.11")

    instruction = f"FROM {base_image}"

    print_instruction(instruction)

    print(
        """
FROM → defines the base image
everything builds on top of this
""".strip()
    )