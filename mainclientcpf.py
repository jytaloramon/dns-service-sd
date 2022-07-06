from clientserviceutils.client_req_utils import get_servname_service_info, get_service_operation


def main():

    BUFFER_LEN = 1024
    HOST_SERVER_NAME = 'localhost'
    PORT_SERVER_NAME = 20467

    print('-------- CPF VALIDADOR --------\n')

    while True:

        try:
            cpf = input('Digite o CPF: ')

            data_res = get_servname_service_info(
                HOST_SERVER_NAME, PORT_SERVER_NAME, 'cpfservice')

            if data_res is None:
                print(f' - Servidor não encontrado ou Inativo\n')
                continue

            host_service, port_service = data_res['host'], data_res['port']

            print('\nDados:')
            print(
                f' - Info. Servidor da Requisição: host({host_service}) / port({port_service})')

            data_cpf = {'cpf': cpf}

            data_cpf_res = get_service_operation(
                host_service, port_service, data_cpf)

            print(' - Resultado')
            print(f'   - {cpf}: {data_cpf_res["res"]}')
            
        except Exception as e:
            print(f' - @Error: {e.args}')

        print('\n')


if __name__ == '__main__':
    main()
