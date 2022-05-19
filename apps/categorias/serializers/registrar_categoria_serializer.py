from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.categorias.models import Categoria
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios


class CategoriaCrearSerializer(Serializer):
    cat_descripcion = serializers.CharField(required=True,
                                            error_messages={
                                                "required": "El nombre de la categoría es requerido.",
                                                "blank": "El nombre de la categoría no debe estar vacío.",
                                                "invalid": "El nombre de la categoría debe ser válido.",
                                            })
    cat_estado = serializers.BooleanField(required=True,
                                          error_messages={
                                              "required": "El estado de la categoría es requerido.",
                                              "blank": "El estado de la categoría no debe estar vacío.",
                                              "invalid": "El estado de la categoría debe ser válido.",
                                          })

    def validate_cat_descripcion(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_categoria = Categoria.objects.filter(cat_descripcion=value)
                    if not nombre_categoria.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La categoría ya existe.')
                else:
                    raise serializers.ValidationError('La categoría debe contener caracteres alfabéticos.')

            else:
                raise serializers.ValidationError("El nombre de la categoría no debe tener más de 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de la categoría no debe tener menos de 4 caracteres.")

    def validate_cat_estado(self, value):
        if bool(value):
            return value
        else:
            raise serializers.ValidationError("El estado de la categoría solo puede ser Verdadero")

    def create(self, data):
        descripcion = str(data['cat_descripcion']).upper()
        categoria_nueva = Categoria(cat_descripcion=descripcion, cat_estado=True)
        categoria_nueva.save()
