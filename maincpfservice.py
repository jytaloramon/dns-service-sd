from random import randint
from cpfservice.cpfserviceserver import CpfServiceServer


def main():

    HOST = 'localhost'
    PORT = randint(33000, 33999)

    cpf_server = CpfServiceServer(HOST, PORT)


if __name__ == '__main__':
    main()
