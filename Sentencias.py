x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print("Negativo cambiado a cero")
elif x == 0:
    print("Cero")
elif x == 1:
    print('Simple')
else:
    print('Mas')
# Parte 2
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
    print(p, len(p))
for p in palabras[:]:
    if len(p) > 6:
        palabras.insert(0, p)
    print(type(p))
    print("p: ", p)
# La función
print('for in range(5)')
for i in range(5):
    print(i)
print('for in range (5,10)')
for i in range(5, 10):
    print(i)
print('for in range(2,10,3)')
for i in range(2, 10, 3):
    print(i)
print('for in range(-10,-100,30)')
for i in range(-10, -100, -30):
    print(i)
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print(i, a[i])
print(range(10))
print(list(range(5)))
# Parte 3
print("Parte 3")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
    else:
        print(n, " es un numero primo")
for num in range(2, 10):
    if num % 2 == 0:
        print('Encontré un número par', num)
        continue
    print('Encontré un número', num)
# Parte 4
# pass no hace nada, pero tien algunas aplicaciones 
while (True):
    pass #Espera una interrupción de teclado
