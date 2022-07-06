import re


def is_valid_cpf(cpf: str) -> bool:

    if not(len(cpf) == 14):
        return False

    reg_exp = '^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'

    m = re.match(reg_exp, cpf)

    if m is None:
        return False

    cpf_a = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:]

    cpf_s = cpf_a[0]

    if len(list(filter(lambda x: x == cpf_s, cpf_a))) == 11:
        return False

    s1 = sum(map(lambda x, y: int(x) * y, cpf_a[:9], list(range(10, 1, -1))))
    res1 = s1 % 11
    d1 = 0 if res1 < 2 else 11 - res1

    if not(int(cpf_a[9]) == d1):
        return False

    s2 = sum(map(lambda x, y: int(x) * y, cpf_a[:10], list(range(11, 1, -1))))
    res2 = s2 % 11
    d2 = 0 if res2 < 2 else 11 - res2

    return int(cpf_a[10]) == d2
