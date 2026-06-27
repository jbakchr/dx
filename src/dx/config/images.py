IMAGE_PROFILES = {
    "nginx": {
        "container_port": 80,
        "default_host_port": 8080,
        "prompts": ["port", "container_port"],
        "description": "web server (ports)",
        "dockerfile": {
            "base": "nginx:latest",
            "workdir": None,
            "cmd": None,
        },
    },
    "postgres": {
        "container_port": 5432,
        "default_host_port": 5432,
        "prompts": ["port", "container_port", "env"],
        "description": "database (ports + env)",
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
        "dockerfile": {
            "base": "postgres:15",
            "workdir": None,
            "cmd": None,
        },
    },
    "redis": {
        "container_port": 6379,
        "default_host_port": 6379,
        "prompts": ["port", "container_port"],
        "description": "cache (ports)",
        "dockerfile": {
            "base": "redis:latest",
            "workdir": None,
            "cmd": None,
        },
    },
    "mysql": {
        "container_port": 3306,
        "default_host_port": 3306,
        "prompts": ["port", "container_port", "env"],
        "description": "database (ports + env)",
        "env": {
            "MYSQL_ROOT_PASSWORD": "password",
        },
        "dockerfile": {
            "base": "mysql:8",
            "workdir": None,
            "cmd": None,
        },
    },
    "node": {
        "prompts": ["volume"],
        "description": "development (volume)",
        "dockerfile": {
            "base": "node:18",
            "workdir": "/app",
            "cmd": "npm start",
        },
    },
    "python": {
        "prompts": ["volume", "command"],
        "description": "development (volume + command)",
        "dockerfile": {
            "base": "python:3.11",
            "workdir": "/app",
            "cmd": "python app.py",
        },
    },
}