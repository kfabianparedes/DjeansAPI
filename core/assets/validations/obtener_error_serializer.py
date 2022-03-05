def obtenerErrorSerializer(serializer):
    return list(serializer.errors.values())[0][0]
