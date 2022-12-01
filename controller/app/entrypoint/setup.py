import socket
from fastapi import FastAPI

from router import sensors_handler
from settings import settings

app = FastAPI()

app.include_router(sensors_handler)

manipulator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
manipulator_socket.connect((settings.MANIPULATOR_HOST, settings.MANIPULATOR_PORT))


def get_socket() -> socket:
    return manipulator_socket
