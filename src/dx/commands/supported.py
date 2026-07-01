from dx.config.images import IMAGE_PROFILES
from dx.ui.output import separator


def supports_dockerfile(profile) -> bool:
    dockerfile = profile.get("dockerfile")

    return bool(
        dockerfile
        and (
            dockerfile.get("base")
            or dockerfile.get("workdir")
            or dockerfile.get("cmd")
        )
    )


def supported():
    separator()
    print("Supported images")
    separator()

    for name, profile in IMAGE_PROFILES.items():
        purpose = profile.get("purpose", "")
        concepts = " + ".join(profile.get("concepts", []))

        marker = " [dockerfile]" if supports_dockerfile(profile) else ""

        print(
            f"  {name:<10} {purpose:<15} → ({concepts}){marker}"
        )

    print()