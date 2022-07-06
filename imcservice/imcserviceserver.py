import json
from socket import socket, AF_INET
from serviceserverutils.serviceserverbase import ServiceServerBase
from imcservice.imccalc import imc_predict


class ImcServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        super().__init__('imcservice', host, port)

        self._register_server_name('localhost', 35750)

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
