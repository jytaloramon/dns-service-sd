import json
from socket import socket, AF_INET
from time import sleep
from typing import Dict
from serviceserverutils.serviceserverbase import ServiceServerBase


class NameServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        self._services: Dict[str, Dict[str, any]] = {}

        super().__init__('nameservice', host, port)

    def add_service(self, name: str, host: str, port: int) -> None:

        service = self.get_service(name)

        if service is None:
            self._services[name] = {
                'host': host, 'port': port, 'active': True, 'history': []
            }

            return

        service['host'] = host
        service['port'] = port
        service['status'] = True

    def get_service(self, name: str) -> Dict[str, any]:

        return self._services.get(name)

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data_raw = cli.recv(self._len_buffer)

            data = json.loads(data_raw)
            #imc_pred = imc_predict(data['weight'], data['height'])

            #data_send = {'imc': imc_pred[0], 'class': imc_pred[1]}

            #cli.send(bytes(json.dumps(data_send), 'utf-8'))
            cli.close()

    def _check_server_status(self) -> None:

        has_update = False
        status = True

        while status:
            has_update = False

            for k, d in self._services.values():
                status_service = self._has_service_up(d['host'], d['port'])

                if not(status_service):
                    d['status'] = False
                    d['history'].append(f'{d["host"]}/{d["port"]}')
                    d['host'], d['port'] = '', 0
                    has_update = True

            if has_update:
                pass

            sleep(5)

    def _show_services(self) -> None:

        char_div = '-'
        h = ['Service', 'Status', 'Host/port', 'History']

        print(f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')
        print(f'|{h[0]:^19}|{h[1]:^9}|{h[2]:^24}|{h[3]:^24}|')
        print(f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')

        for s, d in self._services.items():
            n = s
            st = d['status']
            hp = d['host'] + '/' + str(d['port'])
            h = d['history']

            print(f'|{n:^19}|{st:^9}|{hp:^24}|', end='')

            if len(h) == 0:
                m = 'n/d'
                print(f'{m:^24}|')
            else:
                m = ''
                print(f'{h[0]:^24}|')

                for i in h[1:]:
                    print(f'|{m:<19}|{m:<9}|{m:<24}|{i:^24}|')

            print(
                f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')
