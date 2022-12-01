import socket
from datetime import datetime
from fastapi import Depends

from entrypoint.setup import get_socket


def decision(data, m_socket=Depends(get_socket)):
    dec = {'datetime': datetime.now().strftime('%Y%m%dT%H%M%S'), 'status': 'on'}
    m_socket.sendall(bytes(data, 'utf-8'))
