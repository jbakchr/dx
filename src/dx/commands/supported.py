# src/dx/commands/supported.py

from dx.config.images import IMAGE_PROFILES
from dx.ui.output import separator


def supported():
    separator()
    print("Supported images")
    separator()

    for name, profile in IMAGE_PROFILES.items():
        description = profile.get("description", "")

        purpose = description
        concepts = ""

        if "(" in description and ")" in description:
            purpose = description.split("(")[0].strip()
            concepts = description.split("(")[1].replace(")", "").strip()

        dockerfile_defaults = profile.get("dockerfile")
        has_dockerfile = bool(
            dockerfile_defaults
            and (
                dockerfile_defaults.get("base")
                or dockerfile_defaults.get("workdir")
                or dockerfile_defaults.get("cmd")
            )
        )

        marker = " [dockerfile]" if has_dockerfile else ""

        print(
            f"  {name:<14} {purpose:<14} → ({concepts}){marker}"
        )

    print()