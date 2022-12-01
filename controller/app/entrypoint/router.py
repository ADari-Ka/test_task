from datetime import datetime
from fastapi import APIRouter

from settings import logger, current_data
from service import decision

sensors_handler = APIRouter()

current_time = datetime.now()


@sensors_handler.post("/data")
async def post_data(data: dict):
    global current_time, current_data

    current_data.append(data)

    if (datetime.now() - current_time).seconds >= 5:
        decision(current_data)

        current_time = datetime.now()
        current_data.clear()

