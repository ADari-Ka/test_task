import socket

from settings import settings, logger

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 5000))

logger.info('Socket bind complete')

sock.listen()
conn, addr = sock.accept()

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        logger.info(data.decode('utf-8'))
