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
    if re.match(r"^[a-zñáéíóúA-ZÑÁÉÍÓÚ ]+$", str(value)):
        return True
    return False

def validarCaracteresAlfabeticoConEspaciosNumerosGuiones(value):
    if re.match(r"[a-zñáéíóú\- A-ZÑÁÉÍÓÚ 0-9]+$", str(value)):
        return True
    return False

def validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
    if re.match(r"[a-zñáéíóú\-.# A-ZÑÁÉÍÓÚ 0-9]+$", str(value)):
        return True
    return False
