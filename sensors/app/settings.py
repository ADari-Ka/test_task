import sys

from pydantic import BaseSettings
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")


class Settings(BaseSettings):
    CONTROLLER_URL: str

    class Config:
        env_prefix = ""


settings = Settings()
