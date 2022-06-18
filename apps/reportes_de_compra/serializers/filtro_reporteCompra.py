from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import Serializer

class FiltroReporteSucursal(Serializer):
    fechaIni=serializers.DateField(required=True,
                                    error_messages={
                                        "required":"Debe seleccionar la fecha Inicial",
                                        "blank": "La fecha Inicial no puede estar vacia"
                                    })
    fechaFin=serializers.DateField(required=True,
                                    error_messages={
                                        "required":"Debe seleccionar la fecha Inicial",
                                        "blank": "La fecha Final no puede estar vacia"
                                    })
    def validate_fechaIni(self,attrs):
        f_Actual=datetime.today().strftime('%Y-%m-%d')
        if attrs>= f_Actual:
            raise serializers.ValidationError("La fecha no puede ser superior a la Actual")
        else:
            if datetime.strptime(attrs,'%Y-%m-%d')==False:
                raise serializers.ValidationError("La fecha mo cumple con el formato Valido")
            else:
                return attrs

    def validate_fechaFin(self, attrs):
        try:
            f_Actual=datetime.today().strftime('%Y-%m-%d')
            datetime.strptime(attrs,'%Y-%m-%d')
            if attrs >f_Actual:
                raise serializers.ValidationError('La fecha Ingresada no puede ser superior a la Actual')
            else:
                return attrs
        except ValueError:
            raise serializers.ValidationError("El formato de la fecha es Invalida...")
    # def validate(self, attrs):
    #     if attrs['fechaIni']>attrs['fechaFin']:
    #         raise serializers.ValidationError('La fecha Inicial no puede ser superior a la fecha Final')
    #     else:
    #         return attrs