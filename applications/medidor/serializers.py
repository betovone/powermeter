from rest_framework import serializers

from .models import Medidor


class MedicionCompletoSerializer(serializers.Serializer):
    fecha_hora = serializers.DateTimeField()
    consumo = serializers.IntegerField(min_value=0)
    medidor = serializers.CharField()

    def validate_medidor(self, value):
        if not Medidor.objects.filter(llave=value):
            raise serializers.ValidationError('Ingrese un medidor correcto')
        return value



class MedidorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Medidor
        fields = (
            'llave',
            'nombre',
        )

class MedicionSerializer(serializers.Serializer):
    fecha_hora = serializers.DateTimeField()
    consumo = serializers.IntegerField(min_value=0)


class MedicionesSerializer(serializers.Serializer):
    medidor = serializers.CharField()
    mediciones = MedicionSerializer(many=True)

    def validate_medidor(self, value):
        if not Medidor.objects.filter(llave=value):
            raise serializers.ValidationError('Ingrese un medidor correcto')
        return value


class MedidorConsumoSerializer(serializers.Serializer):
    medidor = serializers.CharField()
    consumo = serializers.FloatField(min_value=0)
    mensaje = serializers.CharField()




