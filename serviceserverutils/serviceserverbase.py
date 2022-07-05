from socket import AF_INET, socket
from tkinter import E


class ServiceServerBase:

    def __init__(self, service_name, host: str, port: int, bacKlog: int = 50) -> None:

        self._service_name = service_name
        self._host = host
        self._port = port
        self._backlog = bacKlog
        self._len_buffer = 1024

        self._socket = socket(AF_INET)
        self._socket.bind((host, port))
        self._socket.listen(bacKlog)

        print(f'Service (UP): {self._service_name} ')
        print(f'- Host: {self._host}')
        print(f'- Port: {self._port}')
        print('--------+--------+--------+--------', end='\n\n')

    def _run_recv_requests(self) -> None:
        pass

    def _register_server_name(self) -> None:
        pass

    def _has_service_up(self, host: str, port: int) -> bool:

        s = socket(AF_INET)

        try:
            s.connect((host, port))
            s.close()
            return True
        except ConnectionRefusedError as e:
            pass

        return False
