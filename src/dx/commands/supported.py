# src/dx/commands/supported.py

from dx.config.images import IMAGE_PROFILES


DESCRIPTIONS = {
    "nginx": "web server (ports)",
    "postgres": "database (ports + env)",
    "mysql": "database (ports + env)",
    "redis": "cache (ports)",
    "node": "development (volume)",
    "python": "development (volume + command)",
}


def supported():
    print("\nSupported images:\n")

    for name in IMAGE_PROFILES.keys():
        description = DESCRIPTIONS.get(name, "")
        print(f"{name:<10} → {description}")

    print()