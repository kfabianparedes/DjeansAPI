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
    if re.match(r"^[a-zñáéíóúA-ZÑÁÉÍÓÚ' ]+$", str(value)):
        return True
    return False

def validarCaracteresAlfabeticoConEspaciosPuntos(value):
    if re.match(r"^[a-zñáéíóúA-ZÑÁÉÍÓÚ. ]+$", str(value)):
        return True
    return False

def validarEmail(value):
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", str(value)):
        return True
    return False

def validarCaracteresAlfaNumericos(value):
    if re.match(r"^[a-zñáéíóúA-ZÑÁÉÍÓÚ 0-9]+$", str(value)):
        return True
    return False


def validarCaracteresAlfabeticoConEspaciosNumerosGuiones(value):
    if re.match(r"[a-zñáéíóú\- A-ZÑÁÉÍÓÚ 0-9]+$", str(value)):
        return True
    return False

def validarCaracteresAlfanumericosGuiones(value):
    if re.match(r"[a-zñáéíóú\- A-ZÑÁÉÍÓÚ0-9]+$", str(value)):
        return True
    return False

def validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
    if re.match(r"[a-zñáéíóú\-.# A-ZÑÁÉÍÓÚ 0-9]+$", str(value)):
        return True
    return False

def validarNumeroSerie(value):
    if re.match(r"^[BbFf]\d{3}", str(value)):
        return True
    return False

