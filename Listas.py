cuadrados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cuadrados)
print("Rebanada "+str(cuadrados[1:4]))
print("Rebanada "+str(cuadrados[:6]))
print("Rebanada "+str(cuadrados[3:]))
cuadradosNegativos = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
print(cuadradosNegativos)
print("Concatenación "+str(cuadrados)+str(cuadradosNegativos))
cuadrados[0] = -1
print(cuadrados)
cuadrados.append(10)
cuadrados.append(11)
print(cuadrados)
letras = ['a', "b", "c", 'd', "e", 'f', 'g']
print(letras)
letras[2:5] = ['C', 'D', 'E']
print(letras)
letras[2:5] = []
print(letras)
letras[:] = []
print("Lista vacía "+str(letras))
letras = ['a', "b", "c", 'd', "e", 'f', 'g']
print("Longitud lista "+str(len(letras)))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("Cadenas dentro de otra "+str(x))
print(x[0][2])
