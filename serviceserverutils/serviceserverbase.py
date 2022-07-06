import json
from socket import AF_INET, socket
from time import sleep

from serviceserverutils.logger import LoggerService


class ServiceServerBase:

    def __init__(self, service_name, host: str, port: int, bacKlog: int = 50) -> None:

        self._service_name = service_name
        self._host = host
        self._port = port
        self._backlog = bacKlog
        self._len_buffer = 1024

        self._count_event = 1
        self._logger = LoggerService()

        self._socket = socket(AF_INET)
        self._socket.bind((host, port))
        self._socket.listen(bacKlog)

        self._show_info_service()

    def _run_recv_requests(self) -> None:
        pass

    def _register_server_name(self, host: str, port: int) -> None:

        data = {'type': 'register', 'name': self._service_name,
                'host': self._host, 'port': self._port}

        s = socket(AF_INET)
        s.connect((host, port))

        s.send(bytes(json.dumps(data), 'utf-8'))
        s.close()

    def _has_service_up(self, host: str, port: int) -> bool:

        s = socket(AF_INET)

        try:
            s.connect((host, port))
            s.close()
            return True
        except ConnectionRefusedError as e:
            pass

        return False

    def _show_info_service(self) -> None:

        print(f'Service (UP): {self._service_name} ')
        print(f'- Host: {self._host}')
        print(f'- Port: {self._port}')
        print('--------+--------+--------+--------', end='\n\n')
