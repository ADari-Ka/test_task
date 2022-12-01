import sys

from asyncio import sleep, get_event_loop, wait

from settings import logger
from model.sensor import AbstractSensor, RandomSensor

from service import data_generation_task


if __name__ == '__main__':
    arg = sys.argv[1]

    loop = get_event_loop()

    if arg == '-r':
        logger.info('Starting random sensor')
        sensor = RandomSensor()
    else:
        sensor = AbstractSensor()

    loop.run_until_complete(data_generation_task(sensor))

