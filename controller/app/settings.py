from pydantic import BaseSettings

from datetime import datetime

current_time: datetime = datetime.now()

current_data = []


class Settings(BaseSettings):
    MANIPULATOR_HOST: str
    MANIPULATOR_PORT: int


settings = Settings()
