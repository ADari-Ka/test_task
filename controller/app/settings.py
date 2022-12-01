import sys
import os
import socket

from pydantic import BaseSettings
from loguru import logger

current_data = []

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
    MANIPULATOR_HOST: str
    MANIPULATOR_PORT: int


settings = Settings()


manipulator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manipulator_socket.connect((settings.MANIPULATOR_HOST, settings.MANIPULATOR_PORT))

