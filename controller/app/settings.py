import socket
import sys

from pydantic import BaseSettings
from loguru import logger

logger.configure(
    **{
        "handlers": [
            {
                "sink": sys.stdout,
                "serialize": False,
                "format": "{message}",
            },
        ]
    }
)

current_data = []


class Settings(BaseSettings):
    MANIPULATOR_HOST: str
    MANIPULATOR_PORT: int


settings = Settings()


# setup and connect socket to manipulator
manipulator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manipulator_socket.connect((settings.MANIPULATOR_HOST, settings.MANIPULATOR_PORT))

