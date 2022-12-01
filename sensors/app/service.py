from requests import post
from datetime import datetime

from settings import logger, settings

from model.sensor import AbstractSensor


async def data_generation_task(sensor: AbstractSensor):
    logger.info(f'Generating data for {sensor}')
    return post(settings.CONTROLLER_URI + '/data',
                json={'datetime': datetime.now().strftime('%Y%m%dT%H%M%S'), 'payload': await sensor.get_data()})
