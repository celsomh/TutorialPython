from math import pi
from collections import deque
lista = []
# Formas para agregar ítems
# Forma 1
lista.append(1)
# Forma 2
lista[len(lista):] = [2]
print(lista)
posicion = len(lista)
lista.insert(posicion, 3)
print(lista)
# Ítem, no posición
item = 2
lista.remove(item)
print(lista)
lista.append(4)
print(lista)
print(lista.pop())
print(lista)
print(lista.pop(0))
print(lista)
lista.append(2)
lista.append(1)
print(lista)
lista.clear()
print(lista)
lista.extend([1, 2, 3, 4, 4, 4, 5])
print(lista)
index = lista.index(2)
print(index)
numero = 4
print('el numero', numero, 'aparece', lista.count(numero), 'veces en la lista')
lista.extend([5, 2, 51, 12, 52, 5, 4])
print('Desordenado:\t', lista)
lista.sort()
print('Ordenado():\t', lista)
lista.reverse()
print('Lista en reversa:', lista)
lista2 = lista.copy()
print('Lista string')
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
print(frutas)
palabra = 'manzana'
print(palabra, 'aparece', frutas.count(palabra), 'veces')
palabra = 'mandarina'
print(palabra, 'aparece', lista.count(palabra), 'veces')
palabra = 'banana'
print('índice', palabra, ':', frutas.index(palabra))
print('índice (>4)', palabra, ':', frutas.index(palabra, 4))
frutas.reverse()
print('frutas en reversa', frutas)
frutas.append('uva')
print('Desordenado:\t', frutas)
frutas.sort()
print('Ordenado:\t', frutas)
print('pop:', frutas.pop())
print(frutas)
# Lista como pila
print('Pila')
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
# Colas
print('Colas')
queue = deque(['Eric', 'Jhon', 'Michael'])
queue.append('Terry')
queue.append('Graham')
print(queue)
print('popleft:', queue.popleft())
print(queue)
print('popleft:', queue.popleft())
print(queue)
# Compresión de listas
print('Lista cuadrados')
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print(cuadrados)
cuadrados = list(map(lambda x: x**2, range(10)))
# Un equivalente a lo anterior
cuadrados = [x**2 for x in range(10)]
listaCompresion = [(x, y)for x in [1, 2, 3, 4] for y in [3, 1, 4] if x != y]
print('listaCompresion:', listaCompresion)
# Un equivalente a lo anterior
combs = []
for x in[1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print('combs:', combs)
vec = [-4, -2, 0, 2, 4]
print('lista:', vec)
print('lista duplicada:', [x*2 for x in vec])
print('lista filtrada(solo +):', [x for x in vec if x >= 0])
print('valor absoluto:', [abs(x) for x in vec])
frutafresca = {'  banana', '  mora de Logan', 'maracuya  '}
print('frutafresca:', frutafresca)
print('frutafresca sin espacios', [arma.strip() for arma in frutafresca])
print('tupla(numero,cuadrado)', [(x, x**2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('vec:', vec)
print('lista compresion vec:', [num for elem in vec for num in elem])
print('pi redondeado', [str(round(pi, i)) for i in range(1, 6)])
# Listas por comprensión anidadas
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 10, 11, 12]]
print('matriz:', matriz)
print('matriz transpuesta:', [[fila[i] for fila in matriz] for i in range(4)])
# Un equivalente a lo anterior pero utilizando funcion predef.
print('matriz transpuesta (zip())', list(zip(*matriz)))
# La instrucción
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print('del a[0]')
print(a)
print('del a[2:4]')
del a[2:4]
print(a)
print('del a[:]')
del a[:]
print(a)
print('del (una variable)')
a = 'una variable'
print(a)
del a
print('Arroja un error, no existe la varible (funciona!)')