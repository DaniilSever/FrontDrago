from pydantic_settings import BaseSettings

class Config(BaseSettings):
    # какой-то конфиг для приложения
    APP_ENV: str
    # ------------------------------
    POSTGRES_DBN: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = "5432"


def get_config():
    return Config()  # pragma: no cover
