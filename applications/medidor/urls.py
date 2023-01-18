from django.urls import path
from . import views

app_name = 'medidor_app'

urlpatterns = [
    path(
        'registrar-medidor/',
        views.RegistrarMedidor.as_view(),
        name='api-medidor-registrar'
        ),
    path(
        'registrar-medicion/',
        views.RegistrarMedicion.as_view(),
        name='api-registrar-medicion'
    ),    
    path(
        'registrar-mediciones/',
        views.RegistrarMediciones.as_view(),
        name='api-registrar-mediciones'
    ),
    path(
        'obtener-maximo-consumo/<medidor>/',
        views.ObtenerMaximoConsumo.as_view(),
        name='api-maximo-consumo'
    ),
    path(
        'obtener-minimo-consumo/<medidor>/',
        views.ObtenerMinimoConsumo.as_view(),
        name='api-minimo-consumo'
    ),
    path(
        'obtener-consumo-total/<medidor>/',
        views.ObtenerConsumoTotal.as_view(),
        name='api-consumo-total'
    ),
    path(
        'obtener-consumo-promedio/<medidor>/',
        views.ObtenerConsumoPromedio.as_view(),
        name='api-consumo-promedio'
    ),

]

