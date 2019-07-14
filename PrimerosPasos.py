a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
print("Imprimir una valor entero pasado como argumento aparte: ", 12312)
#Para evitar el salto de linea
a, b = 0, 1
while b < 10:
    print(b,end=',')
    a, b = b, a+b
