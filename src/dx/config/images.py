IMAGE_PROFILES = {
    "nginx": {
        "container_port": 80,
        "default_host_port": 8080,
        "prompts": ["port", "container_port"],
    },
    "postgres": {
        "container_port": 5432,
        "default_host_port": 5432,
        "prompts": ["port", "container_port", "env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
    },
    "redis": {
        "container_port": 6379,
        "default_host_port": 6379,
        "prompts": ["port", "container_port"],
    },
    "mysql": {
        "container_port": 3306,
        "default_host_port": 3306,
        "prompts": ["port", "container_port", "env"],
        "env": {
            "MYSQL_ROOT_PASSWORD": "password",
        },
    },
    "node": {
        "prompts": ["volume"],
    },
}