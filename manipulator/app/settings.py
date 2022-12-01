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
                "format": "{message}",
                "level": os.getenv("LOGGING_LEVEL", "INFO").upper(),
            },
        ]
    }
)


class Settings(BaseSettings):
    HOST: str
    PORT: int


settings = Settings()
