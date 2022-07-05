import json
from socket import socket, AF_INET
from serviceserverutils.serviceserverbase import ServiceServerBase
from imcservice.imccalc import imc_predict


class ImcServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        super().__init__('imcservice', host, port)

        self._register_server_name()

        self._run_recv_requests()

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data_raw = cli.recv(self._len_buffer)

            data = json.loads(data_raw)
            imc_pred = imc_predict(data['weight'], data['height'])

            data_send = {'imc': imc_pred[0], 'class': imc_pred[1]}

            cli.send(bytes(json.dumps(data_send), 'utf-8'))
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
