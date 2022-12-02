from requests import post
from datetime import datetime

from settings import logger, settings

from model.sensor import AbstractSensor


async def data_generation_task(sensor: AbstractSensor):
    while True:
        post(
            settings.CONTROLLER_URL,
            json={
                'datetime': datetime.now().strftime('%Y%m%dT%H%M%S'),
                'payload': await sensor.get_payload()
            }
        )
