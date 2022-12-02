from requests import post
from datetime import datetime

from settings import settings, logger

from model.sensor import AbstractSensor


async def data_generation_task(sensor: AbstractSensor):
    while True:
        try:
            post(
                settings.CONTROLLER_URL,
                json={
                    'datetime': datetime.now().strftime('%Y%m%dT%H%M%S'),
                    'payload': await sensor.get_payload()
                }
            )
        except Exception as e:
            logger.error('Error while sending data to controller: {}'.format(e))
