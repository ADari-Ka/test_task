from datetime import datetime
from fastapi import APIRouter

from settings import logger, current_time, current_data
from service import decision

sensors_handler = APIRouter()


@sensors_handler.post("/data")
async def post_data(data: dict):
    current_data.append(data)
    if (datetime.now() - current_time).second > 5:
        logger.info(f'decision')

        current_time = datetime.now()

        decision(current_data)

        current_data.clear()

