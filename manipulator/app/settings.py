import sys
import os

from pydantic import BaseSettings
from loguru import logger


logger.configure(
    **{
        "handlers": [
            {
                "sink": sys.stdout,
                "serialize": False,
                "colorize": True,
                "format": "[<level>{level}</level>] {message}",
                "level": os.getenv("LOGGING_LEVEL", "INFO").upper(),
            },
        ]
    }
)


class Settings(BaseSettings):
    CONTROLLER_HOST: str
    CONTROLLER_PORT: int


settings = Settings()
