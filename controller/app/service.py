import socket
import json
from datetime import datetime
from fastapi import Depends

from settings import manipulator_socket


def decision(data, m_socket=manipulator_socket):
    dec = {'datetime': datetime.now().strftime('%Y%m%dT%H%M%S'), 'status': 'on'}

    m_socket.sendall(bytes(json.dumps(dec), 'utf-8'))
