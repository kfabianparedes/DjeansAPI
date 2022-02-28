from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['CAT_ID','CAT_DESCRIPCION','CAT_ESTADO']
    
    CAT_ID=serializers.ReadOnlyField()
    CAT_DESCRIPCION=serializers.CharField()
    CAT_ESTADO=serializers.BooleanField()

    def create(self,validate_data):
        instance=Categoria()
        instance.CAT_DESCRIPCION=validate_data.get('CAT_DESCRIPCION')
        instance.CAT_ESTADO=validate_data.get('CAT_ESTADO')
        instance.save()
        return instance

    def update(self,instance,validated_data):
        instance.CAT_DESCRIPCION=validated_data.get('CAT_DESCRIPCION', instance.CAT_DESCRIPCION)
        instance.CAT_ESTADO=validated_data.get('CAT_ESTADO', instance.CAT_ESTADO)
        instance.save()
        return instance

    def validate_CAT_DESCRIPCION(self, attrs):
        if (len(str.strip(attrs))==0):
            raise serializers.ValidationError("EL CAMPO DESCRIPCION NO DEBE ESTAR VACIO !!")
        elif (len(str.strip(attrs))>0 and len(str.strip(attrs))<10):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO SUPERA LOS 10 CARACTERES")
        elif (len(str.strip(attrs))>50):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO DEBE SUPERAR LOS 10 CARACTERES")
        return attrs
