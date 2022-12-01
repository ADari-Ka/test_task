import sys
import os

import loguru
import pydantic

# Logging
logger = loguru.logger
logger.configure(
    **{
        "handlers": [
            {
                "sink": sys.stdout,
                "serialize": False,
                "colorize": True,
                "format": "{file}:{line} [<level>{level}</level>] {time:%Y%m%dT%H%M%S} {message}",
                "level": os.getenv("LOGGING_LEVEL", "INFO").upper(),
            },
        ]
    }
)


class Settings(pydantic.BaseSettings):
    CONTROLLER_URL: str

    class Config:
        env_prefix = ""


settings = Settings()
