import json
from cpfservice.cfpvalidation import is_valid_cpf
from serviceserverutils.serviceserverbase import ServiceServerBase


class CpfServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        super().__init__('cpfservice', host, port)

        self._register_server_name('localhost', 35750)

        self._run_recv_requests()

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data_raw = cli.recv(self._len_buffer)

            data = json.loads(data_raw)
            cpf_is_valid = is_valid_cpf(data['cpf'])
            cpf_result_text = 'CPF VÁLIDO' if cpf_is_valid else "CPF INVÁLIDO"

            data_send = {'res': cpf_result_text}

            cli.send(bytes(json.dumps(data_send), 'utf-8'))
            cli.close()
