from pydantic import BaseSettings


class Settings(BaseSettings):
    MANIPULATOR_HOST: str = "localhost"
    MANIPULATOR_PORT: int = 5000
