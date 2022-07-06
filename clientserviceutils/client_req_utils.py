import json
from socket import AF_INET, socket
from typing import Any, Dict


def get_servname_service_info(
        servname_host: str,
        servname_port: int,
        service_name: str,
        len_buffer: int = 1024
) -> Dict[str, Any]:

    s = socket(AF_INET)
    s.connect((servname_host, servname_port))

    data_n = {'type': 'get', 'service': service_name}

    s.send(bytes(json.dumps(data_n), 'utf-8'))

    data_sn_raw = s.recv(len_buffer)
    s.close()

    if len(data_sn_raw) == 0:
        return None

    return json.loads(data_sn_raw)


def get_service_operation(
    host: str,
    port: int,
    data: Dict[str, any],
    len_buffer: int = 1024
) -> Dict[str, Any]:

    s = socket(AF_INET)
    s.connect((host, port))

    s.send(bytes(json.dumps(data), 'utf-8'))
    data_raw = s.recv(len_buffer)

    s.close()

    return json.loads(data_raw)
