import json
from serviceserverutils.serviceserverbase import ServiceServerBase
from imcservice.imccalc import imc_predict


class ImcServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        super().__init__('imcservice', host, port)

        self._register_server_name('localhost', 20467)

        self._run_recv_requests()

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data_raw = cli.recv(self._len_buffer)

            if len(data_raw) > 0:
                data = json.loads(data_raw)

                imc_pred = imc_predict(data['weight'], data['height'])

                data_send = {'imc': imc_pred[0], 'class': imc_pred[1]}

                cli.send(bytes(json.dumps(data_send), 'utf-8'))

                event_id = self._get_logger_id()
                self._logger.push_event(event_id, 'Request', data)
                self._logger.push_event(event_id, 'Reponse', data_send)
                self._logger.pop_show_event(event_id)

            cli.close()
