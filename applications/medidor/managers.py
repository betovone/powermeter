from django.db import models
from django.db.models import Max, Min, Sum, Avg

class MedidorManager(models.Manager):

    def obtener_maximo_consumo(self, llave):
        return self.filter(llave=llave).aggregate(
            max=Max('medicion__consumo')
        )['max']

    def obtener_minimo_consumo(self, llave):
        return self.filter(llave=llave).aggregate(
            min=Min('medicion__consumo')
        )['min']

    def obtener_consumo_total(self, llave):
        return self.filter(llave=llave).aggregate(
            consumo_total=Sum('medicion__consumo')
        )['consumo_total']
    
    def obtener_consumo_promedio(self, llave):
        return self.filter(llave=llave).aggregate(
            consumo_promedio=Avg('medicion__consumo')
        )['consumo_promedio']

