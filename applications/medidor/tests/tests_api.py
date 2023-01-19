from rest_framework.test import APITestCase
from rest_framework import status
from applications.medidor.models import (
        Medidor,
        Medicion,
)


class RestAPITests(APITestCase):

    def setUp(self):

        medidor1 = Medidor.objects.create(
            llave='cre01',
            nombre='Medidor creado desde setUp'
        )
        medidor2 = Medidor.objects.create(
            llave='cre02',
            nombre='Medidor creado desde setUp'
        )
        Medicion.objects.create(
            medidor = medidor2,
            fecha_hora = "2023-01-19 18:00",
            consumo = "180" 
        )
        Medicion.objects.create(
            medidor = medidor2,
            fecha_hora = "2023-01-19 19:00",
            consumo = "120" 
        )


        self.medidor1_data = dict(
            llave="www01",
            nombre="Medidor maipu"
        )
        self.medidor2_data = dict(
            llave="www02",
            nombre="Medidor godoy cruz"
        )
        self.medicion_maipu = dict(
            fecha_hora="2023-01-18 17:00",
            consumo="100",
            medidor="cre01"
        )
        self.mediciones_maipu = {
            "medidor": "cre01",
            "mediciones": [
                {
                    "fecha_hora": "2023-01-18 18:00",
                    "consumo": "110"
                },
                {
                    "fecha_hora": "2023-01-18 19:00",
                    "consumo": "150"
                }
            ]   
        }
        

    def test_registrar_medidor(self):
        response = self.client.post(
            '/registrar-medidor/',
            self.medidor1_data,
            format='json'
        )
        #print(response)
        # devuelve 201 porque se crea con CREATEAPIVIEW sin
        # usar el metodo create a mano por lo que esa vista
        # devulve 201 cdo crea un objeto
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

    def test_registrar_medicion(self):
        response = self.client.post(
            '/registrar-medicion/',
            self.medicion_maipu,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_registrar_mediciones(self):
        response = self.client.post(
            '/registrar-mediciones/',
            self.mediciones_maipu,
            format='json'
        )
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_consumo_maximo(self):
        response = self.client.get(
            '/obtener-maximo-consumo/cre02/',
        )
        #print(response.data)
        self.assertEqual(response.data['consumo'], 180.0) 

    def test_consumo_minimo(self):
        response = self.client.get(
            '/obtener-minimo-consumo/cre02/',
        )
        #print(response.data)
        self.assertEqual(response.data['consumo'], 120.0) 

    def test_consumo_total(self):
        response = self.client.get(
            '/obtener-consumo-total/cre02/',
        )
        #print(response.data)
        self.assertEqual(response.data['consumo'], 300.0) 

    def test_consumo_promedio(self):
        response = self.client.get(
            '/obtener-consumo-promedio/cre02/',
        )
        #print(response.data)
        self.assertEqual(response.data['consumo'], 150.0) 

