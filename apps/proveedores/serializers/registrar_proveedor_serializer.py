from shutil import register_unpack_format
from sqlite3 import enable_shared_cache
from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.proveedores.models import Proveedor
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios,    \
                                                    validarEsNumerico, validarCaracteresAlfabeticoConEspaciosPuntos, validarEmail,validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos


class ProveedorCrearSerializer(Serializer):
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
                                          error_messages={"required": "El ESTADO del proveedor es requerido.",
                                                          "blank": "El ESTADO del proveedor no debe estar vacio",
                                                          "invalid": "El ESTADO del proveedordebe ser valido.",
                                                          })

    def validate_pro_ruc(self, value):
        if len(value) == 11:
            if validarEsNumerico(value):
                ruc_proveedor = Proveedor.objects.filter(pro_ruc=value)
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
                    nombre_proveedor = Proveedor.objects.filter(pro_nombre=value)
                    if not nombre_proveedor.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El nombre del proveedor ingresado ya existe.')
                else:
                    raise serializers.ValidationError('El nombre del proveedor solo permite caracteres alfabéticos y puntos.')
            else:
                raise serializers.ValidationError("El nombre del proveedor no debe superar los 50 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del provedor debe tener mas de 3 caracteres.")

    def validate_pro_razon_social(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 50:
                if validarCaracteresAlfabeticoConEspaciosPuntos(value):
                    razon_social = Proveedor.objects.filter(pro_razon_social=value)
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
                    if Proveedor.objects.filter(pro_email=value).exists():
                        raise serializers.ValidationError("El email ya se encuntra Registrado")
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
                return value
            else:
                raise serializers.ValidationError('El teléfono 2 del proveedor debe tener valores numericos.')
        else:
            raise serializers.ValidationError("El teléfono 2 del proveedor no debe tener mas de 9 caracteres.")

    def validate_pro_direccion1(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlnumconEspaciosGuionesNumeralesPuntos(value):
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

    def create(self, data):
        codigo = '+51'
        pro_ruc = str(data['pro_ruc']).upper()
        pro_nom = str(data['pro_nombre']).upper()
        pro_raz_so = str(data['pro_razon_social']).upper()
        pro_email = str(data['pro_email']).upper()
        pro_tel1 = str(codigo + data['pro_telefono1']).upper()
        pro_tel2 = str(codigo + data['pro_telefono2']).upper()
        pro_dir1 = str(data['pro_direccion1']).upper()
        pro_dir2 = str(data['pro_direccion2']).upper()
        proveedor_nuevo = Proveedor(pro_ruc=pro_ruc, pro_nombre=pro_nom, pro_razon_social=pro_raz_so, pro_email=pro_email, pro_telefono1=pro_tel1,
                                    pro_telefono2=pro_tel2, pro_direccion1=pro_dir1, pro_direccion2=pro_dir2,
                                    pro_estado=True)
        proveedor_nuevo.save()
