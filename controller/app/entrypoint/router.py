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
    logger.info((datetime.now() - current_time).seconds)

    if (datetime.now() - current_time).seconds >= 5:
        logger.info(f'decision')

        current_time = datetime.now()

        decision(current_data)

        current_data.clear()

