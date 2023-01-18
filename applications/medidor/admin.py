from django.contrib import admin
from .models import Medidor, Medicion

class MedidorAdmin(admin.ModelAdmin):
    list_display = ('llave', 'nombre',)

class MedicionAdmin(admin.ModelAdmin):
    list_display = ('medidor', 'fecha_hora', 'consumo', )

admin.site.register(Medidor, MedidorAdmin)
admin.site.register(Medicion, MedicionAdmin)


