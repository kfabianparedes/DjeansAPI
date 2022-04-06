
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from apps.sucursales.models import SUCURSALES

class sucursalSerializers(serializers.ModelSerializer):
    class Meta:
        model=SUCURSALES
        fields=['SUC_ID','SUC_NOMBRE','SUC_DIRECCION','SUC_ESTADO']

    SUC_ID=serializers.ReadOnlyField()
    SUC_NOMBRE=serializers.CharField()
    SUC_DIRECCION=serializers.CharField()
    SUC_ESTADO=serializers.BooleanField()
    
    # METODO DE CREACION SUCURSAL
    def create(self,validate_data):
        instance=SUCURSALES()
        instance.SUC_NOMBRE=validate_data.get('SUC_NOMBRE')
        instance.SUC_DIRECCION=validate_data.get('SUC_DIRECCION')
        instance.SUC_ESTADO=validate_data.get('SUC_ESTADO')
        instance.save()
        return instance
        
    # METODO DE EDICION SUCURSAL
    def update(self, instance, validated_data):
        instance.SUC_NOMBRE=validated_data.get('SUC_NOMBRE',instance.SUC_NOMBRE)
        instance.SUC_DIRECCION=validated_data.get('SUC_DIRECCION',instance.SUC_DIRECCION)
        instance.SUC_ESTADO=validated_data.get('SUC_ESTADO',instance.SUC_ESTADO)
        instance.save()
        return instance
        
    def validate_SUC_NOMBRE(self, attrs):
        # if (attrs['SUC_NOMBRE']):
        # if (str.strip(attrs).isalpha()):
            if (len(str.strip(attrs))==0):
                raise serializers.ValidationError("EL CAMPO NOMBRE NO DEBE ESTAR VACIO !!!")
            elif (len(str.strip(attrs))>0 and len(str.strip(attrs))<30):
                raise serializers.ValidationError("EL CAMPO NOMBRE NO SUPERAR LOS 30 CARACTERES")
            return attrs
        # else:
        #     raise serializers.ValidationError("EL CAMPO NOMBRE SOLO DEBE CONTENER LETRAS")
        
    def validate_SUC_DIRECCION(self, attrs):
        if (len(str.strip(attrs))>0 and len(str.strip(attrs))<30):
            raise serializers.ValidationError("EL CAMPO direccion NO SUPERA LOS 30 CARACTERES")
        return super().validate(attrs)