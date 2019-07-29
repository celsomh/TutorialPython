import math
import string
cadena = 'Esto es una cadena'
print('cadena sin formatear:\t', cadena)
cadena.format()
print('cadena formateada:\t', cadena)

value = 123120
# Dos funciones para convertir valores a cadena
# 1
repr(value)
# 2
str(value)

s = 'Hola Mundo.'
print(s)
str(s)
print(s)
repr(s)
print(s)
print(str(1/7))
x = 10*3.25
y = 200*200
s = 'El valor de x es '+repr(x)+', y es '+repr(y)+'...'
print(s)
hola = 'hola mundo\n'
holas = repr(hola)
print(holas)
print(repr((x, y, ('carne', 'huevos'))))
print('tabla 1')
# Dos maneras de escrbir una tabla de cuadros y cubos
# 1
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print('tabla 2')
# 2
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

cadena_numerica = '112'
# Rellenar una cadena numerica con ceros
# Nota: zfill cuenta los simbolos (+ . -)
print('\n'+cadena_numerica.zfill(5))
cadena_numerica = '3.14'
print(cadena_numerica.zfill(7))
cadena_numerica = '3.14159265359'
print(cadena_numerica.zfill(14))
# Uso básico str.format()
print('Somos los {} quienes decimos "{}!"'.format('caballeros', 'nop'))
print('{0} y {1}'.format('carne', 'huevos'))
print('{1} y {0}'.format('carne', 'huevos'))
print('Esta {comida} es {adjetivo}'.format(
    comida='carne', adjetivo='espantosa'))
print('La historia de {0}, {1}, y {otro}'.format(
    'Bill', 'Manfred', otro='Georg'))
contents = 'anguilas'
print('Mi aerodeslizador esta lleno de {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))
print('El valor de PI es aproximadamente {0:.3f}.'.format(math.pi))
tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
    print('{0:10}==>{1:10d}'.format(nombre, telefono))

print('Jack:{0[Jack]:d}; Sjoerd:{0[Sjoerd]:d}; Dcab{0[Dcab]:d}'.format(tabla))
print('Jack:{Jack:d}; Sjoerd:{Sjoerd:d};Dcab {Dcab:d}'.format(**tabla))
numero_decimal = 123.123123
numero_entero = 123123
print('Numero decimal entero {}. Ahora con dos decimales {:.2f}'.format(
    numero_decimal, numero_decimal))
nombre = 'Juan'
print('Un nombre común: {}. Sus dos letras iniciales: {:.2}'.format(nombre, nombre))
# El operador % puede usarse también para el formateo de cadenas
print(math.pi)
print('El valor de PI es aproximadamente %5.3f.' % math.pi)
