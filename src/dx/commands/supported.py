# src/dx/commands/supported.py

from dx.config.images import IMAGE_PROFILES
from dx.ui.output import separator


def supported():
    separator()
    print("Supported images")
    separator()

    for name, profile in IMAGE_PROFILES.items():
        description = profile.get("description", "")

        # Check if dockerfile support exists
        dockerfile_defaults = profile.get("dockerfile")
        has_dockerfile = bool(dockerfile_defaults and (
            dockerfile_defaults.get("base") or
            dockerfile_defaults.get("workdir") or
            dockerfile_defaults.get("cmd")
        ))

        marker = " [dockerfile]" if has_dockerfile else ""

        if description:
            print(f"  {name:<10} → {description}{marker}")
        else:
            print(f"  {name}{marker}")
    
    print()