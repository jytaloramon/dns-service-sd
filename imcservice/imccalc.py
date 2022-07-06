from typing import Tuple


def imc_calculate(weight: float, height: float) -> float:

    return weight / (height ** 2)


def imc_class_predict(imc: float) -> str:

    labels = [
        (17.0, 'Abaixo de 17'),
        (18.5, 'Abaixo do peso'),
        (25, 'Peso normal'),
        (30, 'Acima do peso'),
        (35, 'Obesidade I'),
        (40, 'Obesidade II (severa)'),
    ]

    for v, t in labels:
        if imc < v:
            return t

    return 'Obesidade III (mórbida)'


def imc_predict(weight: float, height: float) -> Tuple[float, str]:

    imc = imc_calculate(weight, height)
    imc_class = imc_class_predict(imc)

    return (imc, imc_class)
