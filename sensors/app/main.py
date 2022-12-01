import sys

from asyncio import get_event_loop

from settings import settings
from model.sensor import SensorFactory

from service import data_generation_task


if __name__ == '__main__':
    arg = sys.argv[1]

    loop = get_event_loop()

    sensor = SensorFactory.get_sensor(arg, settings)

    loop.run_until_complete(data_generation_task(sensor))

