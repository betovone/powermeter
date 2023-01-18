from django.db import models
from .managers import (
    MedidorManager,
)


class Medidor(models.Model):
    llave = models.CharField(
            "Llave identificadora", 
            max_length=50, 
            unique=True
        )
    nombre = models.CharField(
            "Nombre", 
            max_length=150
        )
    
    objects = MedidorManager()

    def __str__(self):
        return f'{self.llave} - {self.nombre}'


class Medicion(models.Model):
    fecha_hora = models.DateTimeField(
            "Fecha-Hora", 
            auto_now=False, 
            auto_now_add=False,
        )
    consumo = models.PositiveIntegerField("Consumo (kwh)")
    medidor = models.ForeignKey(
            Medidor, 
            on_delete=models.CASCADE,
            related_name="medicion"
        )

    class Meta:
        unique_together = ('fecha_hora', 'medidor',)

    def __str__(self):
        return f'''
            Medidor: {self.medidor}, 
            consumo: {self.consumo}, 
            fecha: {self.fecha_hora}
        '''

