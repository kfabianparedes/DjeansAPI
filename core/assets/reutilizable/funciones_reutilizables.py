from rest_framework.response import Response


def respuestaJson(code, message, data=None):
    respuesta = {'code': code, 'message': message, 'data': data}
    return Response(respuesta, status=code)
