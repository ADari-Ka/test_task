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
                "format": "{file}:{line} [<level>{level}</level>] {time:YYYY-MM-DDTHH:mm:ssZ} {message}",
                "level": os.getenv("LOGGING_LEVEL", "INFO").upper(),
            },
        ]
    }
)


class Settings(pydantic.BaseSettings):
    CONTROLLER_URI: str = "http://localhost:5000"

    class Config:
        env_file = ".env"


settings = Settings()
