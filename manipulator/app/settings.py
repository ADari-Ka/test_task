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
                "format": "{time:%Y%m%dT%H%M%S} - {message}",
                "level": os.getenv("LOGGING_LEVEL", "INFO").upper(),
            },
        ]
    }
)


class Settings(BaseSettings):
    HOST: str
    PORT: int


settings = Settings()
