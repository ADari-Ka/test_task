import json
from datetime import datetime
from asyncio import sleep, create_task

from settings import manipulator_socket, logger, current_data

time = datetime.now()


async def decision(dt: datetime, data=current_data, m_socket=manipulator_socket):
    # up when the average value is less than "middle possible value"
    status = True if sum(data) // (len(data) + 1) < 6200 else False

    dec = {'datetime': dt.strftime('%Y%m%dT%H%M%S'), 'status': 'up' if status else 'down'}
    logger.info(f"Status: {dec['status']}, datetime: {dec['datetime']}")

    m_socket.sendall(bytes(json.dumps(dec), 'utf-8'))

    data.clear()


async def change_data(data, c_data=current_data, c_time=time):
    # don't take into account the outdated data
    if datetime.strptime(data.datetime, '%Y%m%dT%H%M%S') < c_time:
        return

    c_data.append(data.payload)


async def timer_handler(data, c_time=time):
    """
    The function is called every 5 seconds and sends a decision to the manipulator

    :param data: list of received payload values
    :param c_time: last time when the decision was sent
    :return:
    """
    while True:
        await sleep(5)

        c_time = datetime.now()
        create_task(decision(c_time, data))  # send data to manipulator


create_task(timer_handler(current_data))


