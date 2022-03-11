from rest_framework.response import Response


def respuestaJson(code, message, data=None, success=False):
    respuesta = {
        'code': code,
        'success': success,
        'message': message,
        'data': data
    }
    return Response(respuesta, status=code)
