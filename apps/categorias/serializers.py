from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Categoria


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

        if len(str.strip(value)) > 4:
            if len(str.strip(value)) <= 30:
                if str(value).isalpha():
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
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("La estado de la categoría solo puede ser Verdadero o Falso")

    def create(self, data):
        descripcion = str(data['cat_descripcion']).upper()
        categoria_nueva = Categoria(cat_descripcion=descripcion, cat_estado=True)
        categoria_nueva.save()


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['cat_id', 'cat_descripcion', 'cat_estado']

    def update(self, instance, data):
        print(instance)
        instance.cat_descripcion = data.get('cat_descripcion', instance.cat_descripcion)
        instance.cat_estado = data.get('cat_estado', instance.cat_estado)
        instance.save()
        return instance

    def validate_cat_descripcion(self, value):

        if len(str.strip(value)) > 4:
            if len(str.strip(value)) <= 30:
                if str(value).isalpha():
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
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("La estado de la categoría solo puede ser Verdadero o Falso")
