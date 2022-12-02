import ast
import socket

from settings import settings, logger

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((settings.HOST, settings.PORT))


sock.listen()
conn, addr = sock.accept()

with conn:
    while True:
        raw_data = conn.recv(1024)

        if not raw_data:
            logger.info('No data received')

        data: dict = ast.literal_eval(raw_data.decode('utf-8'))

        logger.info(f"status: {data['status']}", time=data['datetime'])
