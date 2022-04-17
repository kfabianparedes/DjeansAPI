import re


def obtenerErrorSerializer(value):
    return list(value.errors.values())[0][0]


def validarEsNumerico(value):
    if str(value).isnumeric():
        return True
    return False


def validarEsMayorQueCero(value):
    if validarEsNumerico(value):
        if int(value) > 0:
            return True
    return False


def validarCaracteresAlfabeticoConEspacios(value):
    if re.match(r"[a-zA-Z ]+$", str(value)):
        return True
    return False
