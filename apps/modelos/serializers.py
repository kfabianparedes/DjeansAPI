from rest_framework import serializers
from .models import MODELO

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELO
        fields = ['MOD_ID','MOD_DESCRIPCION','MOD_ESTADO']
    
    MOD_ID=serializers.ReadOnlyField()
    MOD_DESCRIPCION=serializers.CharField()
    MOD_ESTADO=serializers.BooleanField()

    def create(self,validate_data):
        instance=MODELO()
        instance.MOD_DESCRIPCION=validate_data.get('MOD_DESCRIPCION')
        instance.MOD_ESTADO=validate_data.get('MOD_ESTADO')
        instance.save()
        return instance

    def update(self,instance,validated_data):
        instance.MOD_DESCRIPCION=validated_data.get('MOD_DESCRIPCION', instance.MOD_DESCRIPCION)
        instance.MOD_ESTADO=validated_data.get('MOD_ESTADO', instance.MOD_ESTADO)
        instance.save()
        return instance

    def validate_MOD_DESCRIPCION(self, attrs):
        if (len(str.strip(attrs))==0):
            raise serializers.ValidationError("EL CAMPO DESCRIPCION NO DEBE ESTAR VACIO !!")
        elif (len(str.strip(attrs))>0 and len(str.strip(attrs))<10):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO SUPERA LOS 10 CARACTERES")
        elif (len(str.strip(attrs))>50):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO DEBE SUPERAR LOS 10 CARACTERES")
        return attrs