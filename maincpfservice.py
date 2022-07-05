from cpfservice.cpfserviceserver import CpfServiceServer


def main():

    HOST = 'localhost'
    PORT = 35750

    cpf_server = CpfServiceServer(HOST, PORT)


if __name__ == '__main__':
    main()
