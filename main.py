from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config.app import AppConfig
from src.config.container import Container
from src.routers.user import user_router


def create_app() -> FastAPI:
    container = Container()

    api = FastAPI(title="Social Media APP")
    api.container = container
    api.include_router(user_router)
    return api


app = create_app()
config = AppConfig()

TORTOISE_ORM = {
    "connections": {
        "default": config.db_url
    },
    "apps": {
        "models": {
            "models": ["src.models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)
