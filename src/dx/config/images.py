IMAGE_PROFILES = {
    "nginx": {
        "purpose": "web server",
        "concepts": ["ports"],
        "container_port": 80,
        "default_host_port": 8080,
        "prompts": ["port", "container_port"],
        "dockerfile": {
            "base": "nginx:latest",
            "workdir": None,
            "cmd": None,
        },
    },

    "redis": {
        "purpose": "cache",
        "concepts": ["ports"],
        "container_port": 6379,
        "default_host_port": 6379,
        "prompts": ["port", "container_port"],
        "dockerfile": {
            "base": "redis:latest",
            "workdir": None,
            "cmd": None,
        },
    },

    "postgres": {
        "purpose": "database",
        "concepts": ["ports", "env"],
        "container_port": 5432,
        "default_host_port": 5432,
        "prompts": ["port", "container_port", "env"],
        "env": {
            "POSTGRES_PASSWORD": "password",
        },
        "dockerfile": {
            "base": "postgres:15",
            "workdir": None,
            "cmd": None,
        },
    },

    "mysql": {
        "purpose": "database",
        "concepts": ["ports", "env"],
        "container_port": 3306,
        "default_host_port": 3306,
        "prompts": ["port", "container_port", "env"],
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
        "purpose": "development",
        "concepts": ["volume"],
        "prompts": ["volume"],
        "dockerfile": {
            "base": "node:18",
            "workdir": "/app",
            "cmd": "npm start",
        },
    },

    "python": {
        "purpose": "development",
        "concepts": ["volume", "command"],
        "prompts": ["volume", "command"],
        "dockerfile": {
            "base": "python:3.11",
            "workdir": "/app",
            "cmd": "python app.py",
        },
    },
}