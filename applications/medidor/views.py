from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.views import APIView
from .serializers import (
    MedidorSerializer,
    MedicionesSerializer,
    MedidorConsumoSerializer,
    MedicionCompletoSerializer,
)
from .models import Medidor, Medicion


class ObtenerConsumoTotal(APIView):
    """
        Obtener el consumo total de un Medidor

        Ejemplo Uso: 
        http://127.0.0.1:8000/obtener-consumo-total/aaa01/
    
    """

    def get(self, request, medidor):
        
        if Medidor.objects.filter(llave=medidor):
            consumo = Medidor.objects.obtener_consumo_total(medidor)
            llave_medidor = medidor
            mensaje = 'OK'
        else:
            consumo = -1
            llave_medidor = medidor 
            mensaje = "Medidor no registrado"

        queryset = {
                'consumo': consumo,
                'medidor': llave_medidor,
                'mensaje': mensaje
        }

        serializer = MedidorConsumoSerializer(queryset)
        return Response(serializer.data)


class ObtenerMinimoConsumo(APIView):
    """
        Obtener el consumo minimo de un Medidor

        Ejemplo Uso: 
        http://127.0.0.1:8000/obtener-minimo-consumo/aaa01/
    
    """

    def get(self, request, medidor):
        
        if Medidor.objects.filter(llave=medidor):
            consumo = Medidor.objects.obtener_minimo_consumo(medidor)
            llave_medidor = medidor
            mensaje = 'OK'
        else:
            consumo = -1
            llave_medidor = medidor 
            mensaje = "Medidor no registrado"

        queryset = {
                'consumo': consumo,
                'medidor': llave_medidor,
                'mensaje': mensaje
        }

        serializer = MedidorConsumoSerializer(queryset)
        return Response(serializer.data)


class ObtenerMaximoConsumo(APIView):
    """
        Obtener el consumo maximo de un Medidor

        Ejemplo Uso: 
        http://127.0.0.1:8000/obtener-maximo-consumo/aaa01/
    
    """

    def get(self, request, medidor):
        
        if Medidor.objects.filter(llave=medidor):
            consumo = Medidor.objects.obtener_maximo_consumo(medidor)
            llave_medidor = medidor
            mensaje = 'OK'
        else:
            consumo = -1
            llave_medidor = medidor 
            mensaje = "Medidor no registrado"

        queryset = {
                'consumo': consumo,
                'medidor': llave_medidor,
                'mensaje': mensaje
        }

        serializer = MedidorConsumoSerializer(queryset)
        return Response(serializer.data)


class ObtenerConsumoPromedio(APIView):
    """
        Obtener el consumo promedio de un Medidor

        Ejemplo Uso: 
        http://127.0.0.1:8000/obtener-consumo-promedio/aaa01/
    
    """

    def get(self, request, medidor):
        
        if Medidor.objects.filter(llave=medidor):
            consumo = Medidor.objects.obtener_consumo_promedio(medidor)
            llave_medidor = medidor
            mensaje = 'OK'
        else:
            consumo = -1
            llave_medidor = medidor 
            mensaje = "Medidor no registrado"

        queryset = {
                'consumo': consumo,
                'medidor': llave_medidor,
                'mensaje': mensaje
        }

        serializer = MedidorConsumoSerializer(queryset)
        return Response(serializer.data)


class RegistrarMedidor(CreateAPIView):
    """
        Registrar un nuevo Medidor
    
        PROBAR CON POSTMAN

        Ejemplo:
        ******** BODY -> RAW -> JSON *********
        {
            "llave": "aaa01",
            "nombre": "Primer medidor"
        }
        
    """

    serializer_class = MedidorSerializer


class RegistrarMedicion(CreateAPIView):
    """
    Registrar una sola medicion para un medidor
    
    PROBAR CON POSTMAN

    Ejemplo:
    ******** BODY -> RAW -> JSON *********

    {
        "medidor": "aaa01",
        "fecha_hora": "2023-01-17 18:00",
        "consumo": "80"
    }

    """
    
    serializer_class = MedicionCompletoSerializer

    def create(self, request, *args, **kwargs):
            datos_desserializados = MedicionCompletoSerializer(data=request.data)
            datos_desserializados.is_valid(raise_exception=True)
            
            llave_medidor = datos_desserializados.validated_data['medidor']
            fecha_hora = datos_desserializados.validated_data['fecha_hora']
            consumo = datos_desserializados.validated_data['consumo']

            medidor = Medidor.objects.get(llave=llave_medidor)
        
            medicion, created = Medicion.objects.get_or_create(
                    fecha_hora = fecha_hora,
                    medidor = medidor,
                    defaults = {
                        'consumo': consumo
                    }        
                )
            
            if created:
                mensaje = 'Mediciones registradas correctamente'
            else:
                 medicion.consumo = consumo
                 medicion.save()
                 mensaje = 'Medición actualizada correctamente'

            return Response(
                {
                    'Mensaje': mensaje
                }
            )


class RegistrarMediciones(CreateAPIView):
    """
    Registrar una o mas mediciones para un medidor
    
    PROBAR CON POSTMAN

    Ejemplo:
    ******** BODY -> RAW -> JSON *********

    {
        "medidor": "aaa01",
        "mediciones": [
            {
                "fecha_hora": "2023-01-17 18:00",
                "consumo": "80"
            },
            {
                "fecha_hora": "2023-01-17 19:00",
                "consumo": "75"
            }
        ]
    }


    """
    
    serializer_class = MedicionesSerializer

    def create(self, request, *args, **kwargs):
            datos_desserializados = MedicionesSerializer(data=request.data)
            datos_desserializados.is_valid(raise_exception=True)
            
            llave_medidor = datos_desserializados.validated_data['medidor']
            lista_mediciones = datos_desserializados.validated_data['mediciones']

            medidor = Medidor.objects.get(llave=llave_medidor)
        
            for medicion in lista_mediciones:
                med, created = Medicion.objects.get_or_create(
                    fecha_hora = medicion['fecha_hora'],
                    medidor = medidor,
                    defaults = {
                        'consumo': medicion['consumo']
                    }        
                )
            
                if not created:
                    med.consumo = medicion['consumo']
                    med.save()
                
            return Response(
                {
                    'Mensaje': 'Mediciones registradas correctamente'
                }
            )

