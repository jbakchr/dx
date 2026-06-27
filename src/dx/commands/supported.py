# src/dx/commands/supported.py

from dx.config.images import IMAGE_PROFILES


def supported():
    print("\nSupported images:\n")

    for name, profile in IMAGE_PROFILES.items():
        description = profile.get("description")

        # If description exists → show it
        if description:
            print(f"{name:<10} → {description}")
        else:
            print(f"{name}")
    
    print()