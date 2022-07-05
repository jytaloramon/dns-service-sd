import json
from socket import socket, AF_INET
from cpfservice.cfpvalidation import is_valid_cpf
from serviceserverutils.serviceserverbase import ServiceServerBase


class CpfServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        super().__init__('cpfservice', host, port)

        self._register_server_name()

        self._run_recv_requests()

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data = cli.recv(self._len_buffer)

            cpf = str(data, 'utf-8')
            cpf_is_valid = is_valid_cpf(cpf)

            cli.send(bytes(cpf_is_valid))
            cli.close()

    def _register_server_name(self) -> None:

        host = ''
        port = 6666

        data = {'name': self._service_name,
                'host': self._host, 'port': self._port}

        s = socket(AF_INET)
        s.connect((host, port))

        s.send(bytes(json.dumps(data), 'utf-8'))

        data_res = s.recv(self._len_buffer)