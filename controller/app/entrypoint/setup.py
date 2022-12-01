import socket
from fastapi import FastAPI

from router import sensors_handler
from settings import settings

app = FastAPI()

app.include_router(sensors_handler)
