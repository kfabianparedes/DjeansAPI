from rest_framework import serializers
from .models import TALLA

class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TALLA
        fields = ['TAL_ID','TAL_DESCRIPCION','TAL_ESTADO']
    
    TAL_ID=serializers.ReadOnlyField()
    TAL_DESCRIPCION=serializers.CharField()
    TAL_ESTADO=serializers.BooleanField()

    def create(self,validate_data):
        instance=TALLA()
        instance.TAL_DESCRIPCION=validate_data.get('TAL_DESCRIPCION')
        instance.TAL_ESTADO=validate_data.get('TAL_ESTADO')
        instance.save()
        return instance

    def update(self,instance,validated_data):
        instance.TAL_DESCRIPCION=validated_data.get('TAL_DESCRIPCION', instance.TAL_DESCRIPCION)
        instance.TAL_ESTADO=validated_data.get('TAL_ESTADO', instance.TAL_ESTADO)
        instance.save()
        return instance

    def validate_TAL_DESCRIPCION(self, attrs):
        if (len(str.strip(attrs))==0):
            raise serializers.ValidationError("EL CAMPO DESCRIPCION NO DEBE ESTAR VACIO !!")
        elif (len(str.strip(attrs))>0 and len(str.strip(attrs))<10):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO SUPERA LOS 10 CARACTERES")
        elif (len(str.strip(attrs))>50):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO DEBE SUPERAR LOS 10 CARACTERES")
        return attrs