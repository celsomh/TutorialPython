# Las comparaciones pueden encadenarse
n1, n2, n3 = 5, 8, 8
if(n1 < n2 == n3):
    print('Se cumple la condición')
b1 = True
b2 = True
b3 = False
if(b1 and b2 and b3):
    print('Todos son verdaderos')
# Negar el resultado de una comparación
dia_lluvioso = False
dia_soleado = False
if(not(dia_lluvioso) and dia_soleado):
    print('Se puede salir de casa')
cadena1 = 'Esto es una cadena'
cadena2 = 'es una'
if(cadena2 in cadena1):
    print('cadena1 contiene a cadena2')

if(cadena1 is cadena2):
    print('cadena1 es = a cadena2')
else:
    print('cadena1 es != a cadena2')
c1, c2, c3 = '', 'Trondheim', 'Paso Hammmer'
non_nulo = c1 or c2 or c3
print('non_nulo:', non_nulo)
c1 = 'Trondheimasda'
non_nulo = c1 and c2 and c3
print('non_nulo:', non_nulo)
