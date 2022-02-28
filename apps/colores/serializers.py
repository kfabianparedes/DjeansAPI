from rest_framework import serializers
from .models import COLOR

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = COLOR
        fields = ['COL_ID','COL_DESCRIPCION','COL_ESTADO']
    
    COL_ID=serializers.ReadOnlyField()
    COL_DESCRIPCION=serializers.CharField()
    COL_ESTADO=serializers.BooleanField()

    def create(self,validate_data):
        instance=COLOR()
        instance.COL_DESCRIPCION=validate_data.get('COL_DESCRIPCION')
        instance.COL_ESTADO=validate_data.get('COL_ESTADO')
        instance.save()
        return instance

    def update(self,instance,validated_data):
        instance.COL_DESCRIPCION=validated_data.get('COL_DESCRIPCION', instance.COL_DESCRIPCION)
        instance.COL_ESTADO=validated_data.get('COL_ESTADO', instance.COL_ESTADO)
        instance.save()
        return instance

    def validate_COL_DESCRIPCION(self, attrs):
        if (len(str.strip(attrs))==0):
            raise serializers.ValidationError("EL CAMPO DESCRIPCION NO DEBE ESTAR VACIO !!")
        elif (len(str.strip(attrs))>0 and len(str.strip(attrs))<10):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO SUPERA LOS 10 CARACTERES")
        elif (len(str.strip(attrs))>50):
            raise serializers.ValidationError("EL CAMPO NOMBRE NO DEBE SUPERAR LOS 10 CARACTERES")
        return attrs