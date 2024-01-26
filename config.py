from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    TOKEN_OPEN_AI: str = ""

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()

    print(f"Loading settings from the file .env")
    return settings


env = get_settings()
