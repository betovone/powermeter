import json
from os import setsid
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

no_repetidos = list(set(repetidos))
print(f'1- Lista de valores no repetidos: {no_repetidos}')

valores_en_comun = list(set(repetidos).intersection(set(r)))
print(f'2- Valores en común entre la lista \'r\' y la lista \'repetidos\': {valores_en_comun} ')

diccionario_d_str = json.loads(d_str)
print(f'3- Diccionario de d_str: {diccionario_d_str}, tipo de dato: {type(diccionario_d_str)}')

