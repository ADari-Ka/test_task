import json
from datetime import datetime
from asyncio import sleep, create_task

from settings import manipulator_socket, logger, current_data

time = datetime.now()


async def decision(dt: datetime, data=current_data, m_socket=manipulator_socket):
    status = True if sum(data) // (len(data) + 1) < 6100 else False
    dec = {'datetime': dt.strftime('%Y%m%dT%H%M%S'), 'status': 'up' if status else 'down'}

    logger.info(f"Status: {dec['status']}, datetime: {dec['datetime']}")

    m_socket.sendall(bytes(json.dumps(dec), 'utf-8'))

    data.clear()


async def change_data(data, c_data=current_data, c_time=time):
    if datetime.strptime(data['datetime'], '%Y%m%dT%H%M%S') < c_time:
        return

    c_data.append(data['payload'])


async def timer_handler(data, c_time=time):
    while True:
        await sleep(5)

        await decision(datetime.now())

        c_time = datetime.now()


create_task(timer_handler(current_data))


