# Linea de comentario

""" Comentario 
formado por
varias lineas"""

'''Comentario de varias
lineas pero
utilizando comillas simples
Es usado de manera indistinta a la comilla doble '''

print("Esto es un texto. Primer print")

# Variables
# Variables numericas
numero1 = int(2)
numero2 = float(2.5)

print(numero1)
print(numero2)
# Para obtener el tipo de variable
print(type(numero1))
print(type(numero2))
# Variables de texto
# Puede ser escrito entre comillas simples o dobles
texto = "Esto es un texto en comillas dobles"
texto2 = 'Esto es otro texto en comilla simples'
print(texto)
print(texto2)
# Para escribir un texto de varias lineas se usa triple comillas dobles
texto3 = """Texto
de
varias
lineas"""
print(texto3)
# Convertir un entero a string
texto3 = str(54)
print(texto3)
# Para concatenar se usa +
print("Cadena "+"concatenada")
# Para concatenar variable de texto con numerica
# Se debe transformar la variable numerica a string
texto = "Esto es un texto"
numero = 15
print(texto+" "+str(numero))
# Listas
Ferrari2014 = ["Fernando alonso", "Kimi Raikkonen"]
print(Ferrari2014)
Ferrarir2013 = ['Fernando Alonso', 'Felipe Massa']
print(Ferrarir2013)
# Tambien pueden mezclarse texto y numeros
arrayTextoNumerico = ['texto', 24, 'texto2', 25]
print(arrayTextoNumerico)
# Operacion con listas
print(Ferrari2014[1])
Ferrari2014.pop(1)
print(Ferrari2014)
Ferrari2014.append("Kimi Raikkonen")
print(Ferrari2014)
del(Ferrari2014[0])
Ferrari2014.insert(0, "Fernando Alonso")
print(Ferrari2014)
Ferrari2014.extend(Ferrarir2013)
print(Ferrari2014)
Ferrari2014.remove("Fernando Alonso")
print(Ferrari2014)
# Diccionarios
diccionario = {'Piloto 1': 'Fernando Alonso',
               'Piloto 2': 'Kimi Raikkonen', 'Piloto 3': 'Felipe Masssa'}
print(diccionario)
# Operaciones con diccionarios
print(diccionario.get('Piloto 1'))
print(diccionario.pop('Piloto 1'))
print(diccionario)
diccionario.update({'Piloto 4': 'Lewis Hamilton'})
diccionario.update({'Piloto 2': 'Sebastian Vettel'})
print(diccionario)
print('Piloto 1' in diccionario)
print('Piloto 2' in diccionario)
print("Sebastian Vettel" in diccionario.values())
del diccionario['Piloto 2']
print(diccionario)
#Conjuntos (sets)
conjunto = {'Fernando Alonso', 'Kimi Raikkonen', 'Felipe Massa'}
print(conjunto)
# Condicionales
Alonso_Position = 1
if(Alonso_Position == 1):
    print("Espectacular Alonso, se ha hecho justificar a pesar del coche")
    print("Ya queda menos para ganar el mundial")
elif (Alonso_Position > 1):
    print("Gran carrera de Alonso, lástima que el coche no esté a la altura")
else:
    print("No ha podido terminar la carrera por a una avería mecánica")
Massa_Position = 2
if(Alonso_Position == 1 and Massa_Position == 2):
    print("Alonso primero, Massa segundo")
if(Alonso_Position == 1 or Massa_Position == 1):
    print("Alonso o Massa, terminó primero")
Alonso_Position = 2
if(not Alonso_Position == 1):
    print("Alonso no logró ganar")
# Bucles while y for
print("Bucle while")
vuelta = 1
while vuelta < 10:
    print("Vuelta "+str(vuelta))
    vuelta = vuelta+1
print("Bucle for")
for vuelta in range(1, 10):
    print("Vuelta "+str(vuelta))
coches = ("Ferrari", "Tesla", "BMW", "Audi")
for coche in coches:
    print(coche)
for i, coche in enumerate(coches):
    print(str(i)+" - "+coche)
<<<<<<< HEAD
=======
#Modulos
>>>>>>> 4a041abb97d987f52e3262cb0dc875cfc808d9be
