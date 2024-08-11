from typing import Annotated
from fastapi import Depends
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    # какой-то конфиг для приложения
    APP_ENV: str = "development"
    # ------------------------------
    POSTGRES_DBN: str = "my_app_db"
    POSTGRES_USER: str = "my_app_user"
    POSTGRES_PASSWORD: str = "my_app_password"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"


def get_config():
    return Config()  # pragma: no cover


AConfig = Annotated[Config, Depends(get_config)]