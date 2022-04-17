from shutil import register_unpack_format
from sqlite3 import enable_shared_cache
from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.proveedores.models import Proveedor
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios, validarEsNumerico


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
    pro_telefono2 = serializers.CharField(required=True,
                                          error_messages={"required": "El teléfono 2 del proveedor es requerido.",
                                                          "blank": "El teléfono 2 del proveedor no debe estar vacio",
                                                          "invalid": "El teléfono 2 del proveedor debe ser valido.",
                                                          })
    pro_direccion1 = serializers.CharField(required=True,
                                           error_messages={"required": "La dirección 1 del proveedor es requerido.",
                                                           "blank": "La dirección 1 del proveedor no debe estar vacio",
                                                           "invalid": "La dirección 1 del proveedor debe ser valido.",
                                                           })
    pro_direccion2 = serializers.CharField(required=True,
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
        if len(str.strip(value)) > 0:
            if len(value) <= 11:
                if validarEsNumerico(value):
                    ruc_proveedor = Proveedor.objects.filter(pro_ruc=value)
                    if not ruc_proveedor.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El proveedor ya existe.')
                else:
                    raise serializers.ValidationError('El RUC del proveedor debe tener valores numericos.')
            else:
                raise serializers.ValidationError("El RUC del proveedor no debe tener mas de 11 caracteres.")
        else:
            raise serializers.ValidationError("El RUC del provedor es un campo OBLIGATORIO.")

    def validate_pro_nombre(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_proveedor = Proveedor.objects.filter(pro_nombre=value)
                    if not nombre_proveedor.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El proveedor ya existe.')
                else:
                    raise serializers.ValidationError('El nombre del proveedor solo permite caracteres alfabéticos.')
            else:
                raise serializers.ValidationError("El nombre del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El nombre del provedor debe tener mas de 4 caracteres.")

    def validate_pro_email(self, value):
        if len(str.strip(value)) > 10:
            if len(value) <= 30:
                if Proveedor.objects.filter(pro_email=value).exists():
                    raise serializers.ValidationError("El email ya se encuntra Registrado")
                else:
                    return value
            else:
                raise serializers.ValidationError("El email del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El email del provedor debe tener mas de 10 caracteres.")

    def validate_pro_telefono1(self, value):
        if len(str.strip(value)) >= 4:
            if len(value) < 10:
                if validarEsNumerico(value):
                    return value
                else:
                    raise serializers.ValidationError('El teléfono 1 del proveedor debe tener valores numericos.')
            else:
                raise serializers.ValidationError("El teléfono 1 del proveedor no debe tener mas de 10 caracteres.")
        else:
            raise serializers.ValidationError("El teléfono 1 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_telefono2(self, value):
        if len(str.strip(value)) > 4:
            if len(value) < 10:
                if validarEsNumerico(value):
                    return value
                else:
                    raise serializers.ValidationError('El teléfono 2 del proveedor debe tener valores numericos.')
            else:
                raise serializers.ValidationError("El teléfono 2 del proveedor no debe tener mas de 10 caracteres.")
        else:
            raise serializers.ValidationError("El teléfono 2 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_direccion1(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    return value
                else:
                    raise serializers.ValidationError('La dirección 1 del proveedor solo permite Letras.')
            else:
                raise serializers.ValidationError("La dirección 1 del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("La dirección 1 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_direccion2(self, value):
        if len(str.strip(value)) > 4:
            if len(value) <= 30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    return value
                else:
                    raise serializers.ValidationError('La dirección 2 del proveedor solo permite Letras.')
            else:
                raise serializers.ValidationError("La dirección 2 del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("La dirección 2 del provedor debe tener mas de 4 caracteres.")

    def validate_pro_estado(self, value):
        if type(value) == bool:
            return value
        else:
            raise serializers.ValidationError("El estado del proveedor solo puede ser Verdadero o Falso")

    def create(self, data):
        pro_ruc = str(data['pro_ruc']).upper()
        pro_nom = str(data['pro_nombre']).upper()
        pro_email = str(data['pro_email']).upper()
        pro_tel1 = str(data['pro_telefono1']).upper()
        pro_tel2 = str(data['pro_telefono2']).upper()
        pro_dir1 = str(data['pro_direccion1']).upper()
        pro_dir2 = str(data['pro_direccion2']).upper()
        proveedor_nuevo = Proveedor(pro_ruc=pro_ruc, pro_nombre=pro_nom, pro_email=pro_email, pro_telefono1=pro_tel1,
                                    pro_telefono2=pro_tel2, pro_direccion1=pro_dir1, pro_direccion2=pro_dir2,
                                    pro_estado=True)
        proveedor_nuevo.save()
