from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.roles.models import Rol
from apps.usuarios.models import Usuario
from core.assets.validations.obtener_error_serializer import validarEsNumerico, validarCaracteresAlfabeticoConEspacios


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
                if validarCaracteresAlfabeticoConEspacios(value):
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
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado de usuario solo puede ser Verdadero o Falso")

    def validate_rol(self, value):
        if validarEsNumerico(value):
            rol = Rol.objects.filter(rol_id=value)
            if rol.exists():
                return value
            else:
                raise serializers.ValidationError("El rol no está registrado.")
        else:
            raise serializers.ValidationError("El rol debe ser un número entero.")

    def update(self, instance, data):
        instance.is_active = data.get('is_active', instance.is_active)
        instance.username = str.strip(data.get('username', instance.username)).upper()
        instance.rol = data.get('rol', instance.rol)
        role = Rol.objects.filter(rol_id=instance.rol, rol_tipo='SUPERUSUARIO')
        if role.exists():
            print('Existe')
            instance.is_superuser = True
        else:
            print('No existe')
            instance.is_superuser = False
        return instance.save()
