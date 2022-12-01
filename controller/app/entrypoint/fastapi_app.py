from fastapi import FastAPI

from router import sensors_handler

app = FastAPI()

app.include_router(sensors_handler)
