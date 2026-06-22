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
    "mysql": {
        "container_port": 3306,
        "prompts": ["port", "env"],
        "env": {
            "MYSQL_ROOT_PASSWORD": "password",
        },
    },
}