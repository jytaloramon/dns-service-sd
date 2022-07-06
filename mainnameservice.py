from nameservice.nameserviceserver import NameServiceServer


def main():

    HOST = 'localhost'
    PORT = 35750

    name_server = NameServiceServer(HOST, PORT)


if __name__ == '__main__':
    main()
