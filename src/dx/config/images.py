# src/dx/config/images.py

IMAGE_PROFILES = {
    "nginx": {
        "type": "web",
        "container_port": 80,
        "prompts": ["port", "container_port"],
    },
    "postgres": {
        "type": "db",
        "container_port": 5432,
        "prompts": ["env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
    },
}