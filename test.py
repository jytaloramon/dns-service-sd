def _show_services() -> None:

    data = {
        'cpfservice': {
            'status': True,
            'host': 'locahost',
            'port': 4444,
            'history': []
        },
        'nameservice': {
            'status': False,
            'host': 'locahost',
            'port': 5556,
            'history': ['localost/5663', 'localost/5663', 'localost/5663', ]
        }
    }

    char_div = '-'
    h = ['Service', 'Status', 'Host/port', 'History']

    print(f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')
    print(f'|{h[0]:^19}|{h[1]:^9}|{h[2]:^24}|{h[3]:^24}|')
    print(f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')

    for s, d in data.items():
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

        print(f'+{char_div:-^19}+{char_div:-^9}+{char_div:-^24}+{char_div:-^24}+')


_show_services()
