from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.proveedores.models import Proveedor
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios,    \
                                                    validarEsNumerico, validarCaracteresAlfabeticoConEspaciosPuntos, validarEmail,validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos


class ProveedorActualizarSerializer(Serializer):
    pro_id = serializers.IntegerField(required=True,
                                      error_messages={
                                          "required": "El ID del color es requerido",
                                          "blank": "El ID del color no debe estar vacío",
                                          "invalid": "El ID del color debe ser válido",
                                      })
    pro_ruc = serializers.CharField(required=True,
                                    error_messages={"required": "El RUC del proveedor es requerido.",
                                                    "blank": "El RUC del proveedor no debe estar vacio",
                                                    "invalid": "El RUC del proveedor debe ser valido.",
                                                    })
    pro_nombre = serializers.CharField(required=True,
                                       error_messages={"required": "El nombre del proveedor es requerido.",
                                                       "blank": "El nombre del proveedor no debe estar vacio",
                                                       "invalid": "El nombre del proveedor debe ser valido.",
                                                       })
    pro_razon_social = serializers.CharField(required=True,
                                            error_messages={"required": "La razón social del proveedor es requerido.",
                                                            "blank": "La razón social del proveedor no debe estar vacio",
                                                            "invalid": "La razón social del proveedor debe ser valido.",
                                                            })
    pro_email = serializers.EmailField(required=True,
                                       error_messages={"required": "El email del proveedor es requerido.",
                                                       "blank": "El email del proveedor no debe estar vacio",
                                                       "invalid": "El email del proveedor debe ser valido.",
                                                       })
    pro_telefono1 = serializers.CharField(required=True,
                                          error_messages={"required": "El teléfono 1 del proveedor es requerido.",
                                                          "blank": "El teléfono 1 del proveedor no debe estar vacio",
                                                          "invalid": "El teléfono 1 del proveedor debe ser valido.",
                                                          })
    pro_telefono2 = serializers.CharField(required=True,allow_blank=True,
                                          error_messages={"required": "El teléfono 2 del proveedor es requerido.",
                                                          "blank": "El teléfono 2 del proveedor no debe estar vacio",
                                                          "invalid": "El teléfono 2 del proveedor debe ser valido.",
                                                          })
    pro_direccion1 = serializers.CharField(required=True,
                                           error_messages={"required": "La dirección 1 del proveedor es requerido.",
                                                           "blank": "La dirección 1 del proveedor no debe estar vacio",
                                                           "invalid": "La dirección 1 del proveedor debe ser valido.",
                                                           })
    pro_direccion2 = serializers.CharField(required=True,allow_blank=True,
                                           error_messages={"required": "La dirección 2 del proveedor es requerido.",
                                                           "blank": "La dirección 2 del proveedor no debe estar vacio",
                                                           "invalid": "La dirección 2 del proveedor debe ser valido.",
                                                           })
    pro_estado = serializers.BooleanField(required=True,
                                          error_messages={"required": "El estado del proveedor es requerido.",
                                                          "blank": "El estado del proveedor no debe estar vacio",
                                                          "invalid": "El estado del proveedordebe ser valido.",
                                                          })

    def validate_pro_ruc(self, value):
        if len(value) == 11:
            if validarEsNumerico(value):
                ruc_proveedor = Proveedor.objects.filter(pro_ruc=value).exclude(
                        pro_id=self.instance.pro_id)
                if not ruc_proveedor.exists():
                    return value
                else:
                    raise serializers.ValidationError('El RUC del proveedor ingresado ya existe.')
            else:
                raise serializers.ValidationError('El RUC del proveedor debe tener valores numericos.')
        else:
            raise serializers.ValidationError("El RUC del proveedor debe tener 11 caracteres.")

    def validate_pro_nombre(self, value):
        if len(str.strip(value)) > 3:
            if len(value) <= 50:
                if validarCaracteresAlfabeticoConEspaciosPuntos(value):
                    nombre_proveedor = Proveedor.objects.filter(pro_nombre=value).exclude(
                        pro_id=self.instance.pro_id)
                    if not nombre_proveedor.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El nombre del proveedor ingresado ya existe.')
                else:
                    raise serializers.ValidationError(
                        'El nombre del proveedor solo permite caracteres alfabéticos y puntos.')
            else:
                raise serializers.ValidationError("El nombre del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del provedor debe tener mas de 3 caracteres.")

    def validate_pro_razon_social(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 50:
                if validarCaracteresAlfabeticoConEspaciosPuntos(value):
                    razon_social = Proveedor.objects.filter(pro_razon_social=value).exclude(
                        pro_id=self.instance.pro_id)
                    if not razon_social.exists():
                        return value
                    else:
                        raise serializers.ValidationError('La razón social del proveedor ya existe.')
                else:
                    raise serializers.ValidationError('La razón social del proveedor solo permite caracteres alfabéticos y puntos.')
            else:
                raise serializers.ValidationError("La razón social del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("La razón social del provedor debe tener mas de 4 caracteres.")

    def validate_pro_email(self, value):
        if len(str.strip(value)) > 10:
            if len(value) <= 50:
                if validarEmail(value):
                    email = Proveedor.objects.filter(pro_email=value).exclude(
                        pro_id=self.instance.pro_id)
                    if email.exists():
                        raise serializers.ValidationError("El email ya se encunetra Registrado")
                    else:
                        return value
                else:
                    raise serializers.ValidationError('El email del proveedor no tiene el formato correcto.')
            else:
                raise serializers.ValidationError("El email del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("El email del provedor debe tener mas de 10 caracteres.")

    def validate_pro_telefono1(self, value):
        if len(value) == 9:
            if validarEsNumerico(value):
                codigo = "+51"
                if Proveedor.objects.filter(pro_telefono1=codigo + value).exclude(pro_id=self.instance.pro_id).exists() or Proveedor.objects.filter(
                        pro_telefono2=codigo + value).exclude(pro_id=self.instance.pro_id).exists():
                    raise serializers.ValidationError("El teléfono 1 ingresado ya es utilizado por otro proveedor.")
                else:
                    return value
            else:
                raise serializers.ValidationError('El teléfono 1 del proveedor debe tener valores numericos.')
        else:
            raise serializers.ValidationError("El teléfono 1 del proveedor debe tener 9 caracteres.")

    def validate_pro_telefono2(self, value):
        if len(value) == 0:
            return value
        if len(value) == 9:
            if validarEsNumerico(value):
                codigo = "+51"
                if Proveedor.objects.filter(pro_telefono1=codigo + value).exclude(
                        pro_id=self.instance.pro_id).exists() or Proveedor.objects.filter(
                        pro_telefono2=codigo + value).exclude(pro_id=self.instance.pro_id).exists():
                    raise serializers.ValidationError("El teléfono 2 ingresado ya es utilizado por otro proveedor.")
                else:
                    return value
            else:
                raise serializers.ValidationError('El teléfono 2 del proveedor debe tener valores numericos.')
        else:
            raise serializers.ValidationError("El teléfono 2 del proveedor no debe tener mas de 9 caracteres.")

    def validate_pro_direccion1(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
                    if Proveedor.objects.filter(pro_direccion1=value).exclude(
                            pro_id=self.instance.pro_id).exists() or Proveedor.objects.filter(
                            pro_direccion2=value).exclude(pro_id=self.instance.pro_id).exists():
                        raise serializers.ValidationError("La direccion 1 ingresada ya es utilizada por otro proveedor.")
                    else:
                        return value
                else:
                    raise serializers.ValidationError('La dirección 1 del proveedor tiene el formato incorrecto.')
            else:
                raise serializers.ValidationError("La dirección 1 del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("La dirección 1 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_direccion2(self, value):
        if len(value) == 0:
            return value
        if len(str.strip(value)) > 4:
            if len(value) <= 50:
                if validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
                    if Proveedor.objects.filter(pro_direccion1=value).exclude(
                            pro_id=self.instance.pro_id).exists() or Proveedor.objects.filter(
                                pro_direccion2=value).exclude(pro_id=self.instance.pro_id).exists():
                        raise serializers.ValidationError(
                            "La direccion 2 ingresada ya es utilizada por otro proveedor.")
                    else:
                        return value
                else:
                    raise serializers.ValidationError('La dirección 2 del proveedor tiene el formato incorrecto.')
            else:
                raise serializers.ValidationError("La dirección 2 del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("La dirección 2 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado del proveedor solo puede ser Verdadero o Falso")

    def validate(self, data):

        if data['pro_direccion2'] != '':
            if data['pro_direccion1'] == data['pro_direccion2']:
                raise serializers.ValidationError("La dirección 2 no puede ser igual a la dirección 1.")
            else:
                if data['pro_telefono2'] != '':
                    if data['pro_telefono1'] == data['pro_telefono2']:
                        raise serializers.ValidationError("El teléfono 2 no puede ser igual al teléfono 1")

        return data

    def update(self, instance, data):
        codigo = '+51'

        instance.pro_ruc = str(data.get('pro_ruc', instance.pro_ruc))
        instance.pro_nombre = str(data.get('pro_nombre', instance.pro_nombre)).upper()
        instance.pro_razon_social = str(data.get('pro_razon_social', instance.pro_razon_social)).upper()
        instance.pro_email = str(data.get('pro_email', instance.pro_email)).upper()
        instance.pro_telefono1 = str(data.get('pro_telefono1', instance.pro_telefono1))
        instance.pro_telefono2 = str(data.get('pro_telefono2', instance.pro_telefono2))
        instance.pro_direccion1 = str(data.get('pro_direccion1', instance.pro_direccion1)).upper()
        instance.pro_direccion2 = str(data.get('pro_direccion2', instance.pro_direccion2)).upper()
        instance.pro_estado = data.get('pro_estado', instance.pro_estado)
        instance.pro_telefono1 = codigo + instance.pro_telefono1
        if instance.pro_telefono2 != '':
            instance.pro_telefono2 = codigo + instance.pro_telefono2
        return instance.save()
