from rest_framework import serializers

from apps.marcas.models import MARCAS


class marcaSerializers(serializers.ModelSerializer):
    class Meta:
        model=MARCAS
        fields=['MAR_ID','MAR_DESCRIPCION','MAR_ESTADO']

    MAR_ID=serializers.ReadOnlyField()
    MAR_DESCRIPCION=serializers.CharField()
    MAR_ESTADO=serializers.BooleanField()
    
    # METODO DE CREACION SUCURSAL
    def create(self,validate_data):
        instance=MARCAS()
        instance.MAR_DESCRIPCION=validate_data.get('MAR_DESCRIPCION')
        instance.MAR_ESTADO=validate_data.get('MAR_ESTADO')
        instance.save()
        return instance
        
    # METODO DE EDICION SUCURSAL
    def update(self, instance, validated_data):
        instance.MAR_DESCRIPCION=validated_data.get('MAR_DESCRIPCION',instance.MAR_DESCRIPCION)
        instance.MAR_ESTADO=validated_data.get('MAR_ESTADO',instance.MAR_ESTADO)
        instance.save()
        return instance