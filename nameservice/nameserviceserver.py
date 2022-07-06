import json
from threading import Thread
from time import sleep
from typing import Dict
from serviceserverutils.serviceserverbase import ServiceServerBase


class NameServiceServer(ServiceServerBase):

    def __init__(self, host: str, port: int, bacKlog: int = 50) -> None:

        self._services: Dict[str, Dict[str, any]] = {}

        super().__init__('nameservice', host, port)

        t_recv = Thread(target=self._run_recv_requests)
        t_recv.start()
        self._check_server_status()

    def add_service(self, name: str, host: str, port: int, status: bool = True) -> None:

        service = self.get_service(name)

        if not(service is None):
            service['history'].append(f'{service["host"]}/{service["port"]}')
            service['host'] = host
            service['port'] = port
            service['status'] = status

            return

        self._services[name] = {'host': host,
                                'port': port, 'status': status, 'history': []}

    def get_service(self, name: str) -> Dict[str, any]:

        return self._services.get(name)

    def _run_recv_requests(self) -> None:
        while True:
            cli, _ = self._socket.accept()
            data_raw = cli.recv(self._len_buffer)

            data = json.loads(data_raw)
            self.add_service(data['name'], data['host'], data['port'])

            cli.close()

            self._show_services()

    def _check_server_status(self) -> None:

        has_update = False
        status = True

        while status:
            has_update = False

            for k, d in self._services.items():

                if d['status'] and not(self._has_service_up(d['host'], d['port'])):
                    self.add_service(k, '', 0, False)
                    has_update = True

            if has_update:
                self._show_services()

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
