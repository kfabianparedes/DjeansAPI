from shutil import register_unpack_format
from sqlite3 import enable_shared_cache
from rest_framework import serializers
from rest_framework.serializers import Serializer
from apps.proveedores.models import PROVEEDORES
from core.assets.validations.obtener_error_serializer import validarCaracteresAlfabeticoConEspacios, validarEsNumerico

class ProveedorCrearSerializer(Serializer):
    PRO_RUC=serializers.CharField(required=True,
                                    error_messages={"required":"El RUC del proveedor es requerido.",
                                                    "blank":"El RUC del proveedor no debe estar vacio",
                                                    "invalid": "El RUC del proveedor debe ser valido.",
                                                    })
    PRO_NOMBRE=serializers.CharField(required=True,
                                    error_messages={"required":"El NOMBRE del proveedor es requerido.",
                                                    "blank":"El NOMBRE del proveedor no debe estar vacio",
                                                    "invalid": "El NOMBRE del proveedor debe ser valido.",
                                                    })
    PRO_EMAIL=serializers.EmailField(required=True,
                                    error_messages={"required":"El EMAIL del proveedor es requerido.",
                                                    "blank":"El EMAIL del proveedor no debe estar vacio",
                                                    "invalid": "El EMAIL del proveedor debe ser valido.",
                                                    })
    PRO_TELEFONO1=serializers.CharField(required=True,
                                    error_messages={"required":"El TELEFONO 1 del proveedor es requerido.",
                                                    "blank":"El TELEFONO 1 del proveedor no debe estar vacio",
                                                    "invalid": "El TELEFONO 1 del proveedor debe ser valido.",
                                                    })
    PRO_TELEFONO2=serializers.CharField(required=True,
                                    error_messages={"required":"El TELEFONO 2 del proveedor es requerido.",
                                                    "blank":"El TELEFONO 2 del proveedor no debe estar vacio",
                                                    "invalid": "El TELEFONO 2 del proveedor debe ser valido.",
                                                    })
    PRO_DIRECCION1=serializers.CharField(required=True,
                                    error_messages={"required":"La DIRECCION 1 del proveedor es requerido.",
                                                    "blank":"La DIRECCION 1 del proveedor no debe estar vacio",
                                                    "invalid": "La DIRECCION 1 del proveedor debe ser valido.",
                                                    })
    PRO_DIRECCION2=serializers.CharField(required=True,
                                    error_messages={"required":"La DIRECCION 2 del proveedor es requerido.",
                                                    "blank":"La DIRECCION 2 del proveedor no debe estar vacio",
                                                    "invalid": "La DIRECCION 2 del proveedor debe ser valido.",
                                                    })                                                                                                                                                                                                                                                 
    PRO_ESTADO=serializers.BooleanField(required=True,
                                        error_messages={"required":"El ESTADO del proveedor es requerido.",
                                                        "blank":"El ESTADO del proveedor no debe estar vacio",
                                                        "invalid": "El ESTADO del proveedordebe ser valido.",
                                                        })

    def validate_PRO_RUC(self, value):
            if len(str.strip(value)) > 0:
                if len(value) <= 11:
                    if validarEsNumerico(value):
                        ruc_proveedor= PROVEEDORES.objects.filter(PRO_RUC=value)
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

    def validate_PRO_NOMBRE(self, value):
        if len(str.strip(value)) > 4:
            if len(value)<=30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    nombre_proveedor=PROVEEDORES.objects.filter(PRO_NOMBRE=value)
                    if not nombre_proveedor.exists():
                        return value
                    else:
                        raise serializers.ValidationError('El proveedor ya existe.')
                else:
                    raise serializers.ValidationError('El NOMBRE del proveedor solo permite Letras.')   
            else:
                raise serializers.ValidationError("El NOMBRE del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El NOMBRE del provedor debe tener mas de 4 caracteres.")

    def validate_PRO_EMAIL(self,value):
        if len(str.strip(value))>10:
            if len(value)<=30:
                if PROVEEDORES.objects.filter(PRO_EMAIL=value).exists():
                    raise serializers.ValidationError("El Email ya se encuntra Registrado")
                else:
                    return value
            else:
                raise serializers.ValidationError("El EMAIL del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El EMAIL del provedor debe tener mas de 10 caracteres.")
    
    def validate_PRO_TELEFONO1(self, value):
        if len(str.strip(value))>4:
            if len(value)<10:
                if validarEsNumerico(value):
                    return value
                else:
                    raise serializers.ValidationError('El TELEFONO 1 del proveedor debe tener valores numericos.')
            else:
                raise serializers.ValidationError("El TELEFONO 1 del proveedor no debe tener mas de 10 caracteres.")
        else:
            raise serializers.ValidationError("El TELEFONO 1 del provedor debe tener mas de 4 caracteres.")

    def validate_PRO_TELEFONO2(self, value):
        if len(str.strip(value))>4:
            if len(value)<10:
                if validarEsNumerico(value):
                    return value
                else:
                    raise serializers.ValidationError('El TELEFONO 2 del proveedor debe tener valores numericos.')
            else:
                raise serializers.ValidationError("El TELEFONO 2 del proveedor no debe tener mas de 10 caracteres.")
        else:
            raise serializers.ValidationError("El TELEFONO 2 del provedor debe tener mas de 4 caracteres.")

    def validate_PRO_DIRECCION1(self, value):
        if len(str.strip(value)) > 4:
            if len(value)<=30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    return value
                else:
                    raise serializers.ValidationError('El DIRECCION 1 del proveedor solo permite Letras.')   
            else:
                raise serializers.ValidationError("El DIRECCION 1 del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El DIRECCION 1 del provedor debe tener mas de 4 caracteres.")

    def validate_PRO_DIRECCION2(self, value):
        if len(str.strip(value)) > 4:
            if len(value)<=30:
                if validarCaracteresAlfabeticoConEspacios(value):
                    return value
                else:
                    raise serializers.ValidationError('El DIRECCION 2 del proveedor solo permite Letras.')   
            else:
                raise serializers.ValidationError("El DIRECCION 2 del proveedor no debe superar los 30 caracteres.")
        else:
            raise serializers.ValidationError("El DIRECCION 2 del provedor debe tener mas de 4 caracteres.")
    
    def validate_PRO_ESTADO(self, value):
            if type(value) == bool:
                return value
            else:
                raise serializers.ValidationError("El estado del PROVEEDOR solo puede ser Verdadero o Falso")

    def create(self, data):
        pro_ruc = str(data['PRO_RUC']).upper()
        pro_nom = str(data['PRO_NOMBRE']).upper()
        pro_email=str(data['PRO_EMAIL']).upper()
        pro_tel1=str(data['PRO_TELEFONO1']).upper()
        pro_tel2=str(data['PRO_TELEFONO2']).upper()
        pro_dir1=str(data['PRO_DIRECCION1']).upper()
        pro_dir2=str(data['PRO_DIRECCION2']).upper()
        proveedor_nuevo = PROVEEDORES(PRO_RUC=pro_ruc,PRO_NOMBRE=pro_nom,PRO_EMAIL=pro_email,PRO_TELEFONO1=pro_tel1,PRO_TELEFONO2=pro_tel2,PRO_DIRECCION1=pro_dir1,PRO_DIRECCION2=pro_dir2,PRO_ESTADO=True)
        proveedor_nuevo.save()