from typing import Any

from dx.ui.output import separator, show_header
from dx.config.images import IMAGE_PROFILES


def supports_dockerfile(profile: dict[str, Any]) -> bool:
    """
    Determine whether an image profile supports dx dockerfile.

    Dockerfile support exists when at least one Dockerfile-related
    setting is defined in the image profile.

    Args:
        profile: An image profile from IMAGE_PROFILES.

    Returns:
        True if Dockerfile generation is supported, otherwise False.
    """
    dockerfile = profile.get("dockerfile")

    return bool(
        dockerfile
        and (
            dockerfile.get("base")
            or dockerfile.get("workdir")
            or dockerfile.get("cmd")
        )
    )



def supported() -> None:
    """
    Display the images supported by dx.

    Lists each supported image together with its purpose,
    Docker concepts, and Dockerfile support indicator.

    Returns:
        None.
    """
    show_header("Supported images")

    for name, profile in IMAGE_PROFILES.items():
        purpose = profile.get("purpose", "")
        concepts = " + ".join(profile.get("concepts", []))

        marker = " [dockerfile]" if supports_dockerfile(profile) else ""

        print(
            f"  {name:<10} {purpose:<15} → ({concepts}){marker}"
        )

    print()