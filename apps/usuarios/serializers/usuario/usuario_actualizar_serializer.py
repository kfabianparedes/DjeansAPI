from rest_framework import serializers
from rest_framework.serializers import Serializer

from apps.usuarios.models import Usuario


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
    is_employee = serializers.BooleanField(required=True,
                                           error_messages={
                                               "required": "El estado del usuario empleado es requerido.",
                                               "blank": "El estado del usuario empleado no debe estar vacío.",
                                               "invalid": "El estado del usuario empleado debe ser válido.",
                                           })
    is_staff = serializers.BooleanField(required=True,
                                        error_messages={
                                            "required": "El estado del usuario administrador es requerido.",
                                            "blank": "El estado del usuario administrador no debe estar vacío.",
                                            "invalid": "El estado del usuario administrador debe ser válido.",
                                        })
    is_superuser = serializers.BooleanField(required=True,
                                            error_messages={
                                                "required": "El estado de super usuario es requerido.",
                                                "blank": "El estado de super usuario no debe estar vacío.",
                                                "invalid": "El estado de super usuario debe ser válido.",
                                            })

    def validate_username(self, value):
        if len(str.strip(value)) >= 0:
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

    def update(self, instance, data):
        instance.is_superuser = data.get('is_superuser', instance.is_superuser)
        if instance.is_superuser:
            instance.is_employee = True
            instance.is_staff = True
        else:
            instance.is_employee = data.get('is_employee', instance.is_employee)
            instance.is_staff = data.get('is_staff', instance.is_staff)
        instance.username = data.get('username', instance.username)
        instance.is_active = data.get('is_active', instance.is_active)
        return instance.save()
