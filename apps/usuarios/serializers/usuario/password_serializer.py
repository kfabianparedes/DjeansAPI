from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.serializers import Serializer


class PasswordSerializer(Serializer):
    new_password = serializers.CharField(required=True,
                                         error_messages={
                                             'required': 'La contraseña nueva es requerida.',
                                             'null': 'La contraseña nueva no debe estar vacía.',
                                             'invalid': 'La contraseña nueva debe ser válida.',
                                         })

    old_password = serializers.CharField(required=True,
                                         error_messages={
                                             'required': 'La contraseña antigua es requerida.',
                                             'null': 'La contraseña antigua no debe estar vacía.',
                                             'invalid': 'La contraseña antigua debe ser válida.',
                                         })

    def validate(self, data):
        if data.get('new_password') != data.get('old_password'):
            return data
        else:
            raise serializers.ValidationError('Las contraseñas no deben ser iguales.')

    def validate_password(self, value):
        if len(str.strip(value)) >= 8:
            if len(str.strip(value)) <= 50:
                return value
            else:
                raise serializers.ValidationError("La contraseña debe tener máximo 50 caracteres.")
        else:
            raise serializers.ValidationError("La contraseña debe tener mínimo 8 caracteres.")

    def validate_old_password(self, value):
        if len(str.strip(value)) >= 8:
            if len(str.strip(value)) <= 50:
                return value
            else:
                raise serializers.ValidationError("La contraseña debe tener máximo 50 caracteres.")
        else:
            raise serializers.ValidationError("La contraseña debe tener mínimo 8 caracteres.")

    def update(self, instance, data):
        password = data.get('new_password')
        instance.set_password(password)
        instance.save()
