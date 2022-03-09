def obtenerErrorSerializer(value):
    return list(value.errors.values())[0][0]


def validarEsNumerico(value):
    if value.isnumeric():
        return True
    return False


def validarEsMayorQueCero(value):
    if validarEsNumerico(value):
        if int(value) > 0:
            return True
    return False
