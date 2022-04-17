from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.usuarios.models import Usuario
from core.assets.validations.obtener_error_serializer import validarEsNumerico


class UsuarioActualizarSerializer(Serializer):
    username = serializers.CharField(required=True,
                                     error_messages={
                                         'required': 'El nombre de usuario es requerido.',
                                         'blank': 'El nombre de usuario no debe estar vacío.',
                                         'invalid': 'El nombre de usuario debe ser válido.',

                                     })

    is_active = serializers.BooleanField(required=True,
                                         error_messages={
                                             "required": "El estado del usuario es requerido.",
                                             "blank": "El estado del usuario no debe estar vacío.",
                                             "invalid": "El estado del usuario debe ser válido.",
                                         })

    rol = serializers.IntegerField(required=True,
                                   error_messages={
                                       'required': 'El rol es requerido',
                                       'null': 'El rol no debe ser estar vacío.',
                                       'invalid': 'El rol debe ser un número entero.',
                                   })

    def validate_username(self, value):
        if len(str.strip(value)) >= 5:
            if len(str.strip(value)) <= 50:
                if str(value).isalpha():
                    username = Usuario.objects.filter(username=value).exclude(id=self.instance.id)
                    if not username.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El nombre de usuario ya le pertenece a una cuenta.')
                else:
                    raise serializers.ValidationError("El nombre de usuario solo acepta caracteres alfabéticos.")
            else:
                raise serializers.ValidationError("El nombre de usuario debe tener máximo 50 caracteres.")
        else:
            raise serializers.ValidationError("El nombre de usuario debe tener mínimo 5 caracteres.")

    def validate_is_active(self, value):
        print(type(value), ' estado')
        print(value)
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de usuario solo puede ser Verdadero o Falso")

    def validate_rol(self, value):
        if validarEsNumerico(value):
            if 0 < value < 4:
                return value
            raise serializers.ValidationError("El rol debe ser un número entero entre 1 y 3.")
        raise serializers.ValidationError("El rol debe ser un número entero.")

    def save(self, **kwargs):
        print(self.data)
        print(self.instance)
        # self.instance.is_active = self.data.get('is_active', self.instance.is_active)
        # self.instance.username = str.strip(self.data.get('username', self.instance.username))
        # rol = self.data.get('rol', 0)
        # if rol == 1:
        #     self.instance.is_superuser = True
        #     self.instance.is_employee = True
        #     self.instance.is_staff = True
        # elif rol == 2:
        #     self.instance.is_superuser = False
        #     self.instance.is_employee = False
        #     self.instance.is_staff = True
        # elif rol == 3:
        #     self.instance.is_superuser = False
        #     self.instance.is_employee = True
        #     self.instance.is_staff = False
        # else:
        #     raise serializers.ValidationError("El rol debe ser un número entero.")
        # return self.instance.save()
