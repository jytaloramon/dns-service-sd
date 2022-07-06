from clientserviceutils.client_req_utils import get_servname_service_info, get_service_operation


def main():

    BUFFER_LEN = 1024
    HOST_SERVER_NAME = 'localhost'
    PORT_SERVER_NAME = 20467

    print('-------- IMC CALCULADORA --------\n')

    while True:

        weight = float(input('Digite seu peso (Kg): '))
        height = float(input('Digite sua altura (m): '))

        data_res = get_servname_service_info(
            HOST_SERVER_NAME, PORT_SERVER_NAME, 'imcservice')

        if data_res is None:
            print(f' - Servidor não encontrado ou Inativo\n')
            continue

        host_service, port_service = data_res['host'], data_res['port']

        print('\nDados:')
        print(
            f' - Info. Servidor da Requisição: host({host_service}) / port({port_service})')

        data_imc = {'weight': weight, 'height': height}

        data_imc_res = get_service_operation(
            host_service, port_service, data_imc)

        print(' - Resultado')
        print(f'   - imc: {data_imc_res["imc"]}')
        print(f'   - classe: {data_imc_res["class"]}')

        print('\n')


if __name__ == '__main__':
    main()
