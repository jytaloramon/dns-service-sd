from imcservice.imcserviceserver import ImcServiceServer


def main():

    HOST = 'localhost'
    PORT = 35752

    imc_server = ImcServiceServer(HOST, PORT)


if __name__ == '__main__':
    main()
