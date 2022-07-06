import json
from socket import socket, AF_INET


def main():

    BUFFER_LEN = 1024
    HOST_SERVER_NAME = 'localhost'
    PORT_SERVER_NAME = 20467

    print('-------- IMC CALCULADORA --------\n')

    while True:

        weight = float(input('Digite seu peso (Kg): '))
        height = float(input('Digite sua altura (m): '))

        sn = socket(AF_INET)
        sn.connect((HOST_SERVER_NAME, PORT_SERVER_NAME))

        data_sn = {'type': 'get', 'service': 'imcservice'}

        sn.send(bytes(json.dumps(data_sn), 'utf-8'))
        data_sn_raw = sn.recv(BUFFER_LEN)
        sn.close()

        if len(data_sn_raw) == 0:
            print(f' - Servidor não encontrado ou Inativo')
            continue

        data_res = json.loads(data_sn_raw)

        host_service, port_service = data_res['host'], data_res['port']

        print('\nDados:')
        print(
            f' - Info. Servidor da Requisição: host({host_service}) / port({port_service})')

        s_simc = socket(AF_INET)
        s_simc.connect((host_service, port_service))

        data_imc = {'weight': weight, 'height': height}

        s_simc.send(bytes(json.dumps(data_imc), 'utf-8'))
        data_imc_raw = s_simc.recv(BUFFER_LEN)
        s_simc.close()

        data_imc_res = json.loads(data_imc_raw)

        print(' - Resultado')
        print(f'   - imc: {data_imc_res["imc"]}')
        print(f'   - classe: {data_imc_res["class"]}')

        print('\n')


if __name__ == '__main__':
    main()
