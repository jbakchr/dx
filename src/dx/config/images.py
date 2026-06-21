# src/dx/config/images.py

IMAGE_PROFILES = {
    "nginx": {
        "container_port": 80,
        "prompts": ["port", "container_port"],
    },
    "postgres": {
        "container_port": 5432,
        "prompts": ["env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
    },
    "redis": {
        "container_port": 6379,
        "prompts": ["port"],
    },
}