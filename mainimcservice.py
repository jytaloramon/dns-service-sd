from imcservice.imcserviceserver import ImcServiceServer
from random import randint


def main():

    HOST = 'localhost'
    PORT = randint(34000, 34999)

    imc_server = ImcServiceServer(HOST, PORT)


if __name__ == '__main__':
    main()
