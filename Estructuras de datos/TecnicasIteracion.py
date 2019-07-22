# Iterar sobre un diccionario
import math
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
print(caballeros)
for k, v in caballeros.items():
    print('k:', k, '\tv:', v)
# iterar con enumeración
a = ['ta', 'te', 'ti']
print(a)
for i, v in enumerate(a):
    print('i:', i, '\tv:', v)
# iterar sobre dos o mas secuencias al mmismo tiempo
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print('¿Cuál es tu {0}? {1}.'.format(p, r))
# Iterar en orden inverso
for i in reversed(range(1, 10, 2)):
    print(i)
# iterar sobre una secuencia ordenada
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
print('canasta:', canasta)
for f in sorted(set(canasta)):
    print(f)
datos = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print('datos:', datos)
datos_filtrados = []
for valor in datos:
    if not math.isnan(valor):
        datos_filtrados.append(valor)
print('datos filtrados:', datos_filtrados)
