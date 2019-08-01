import sys
while True:
    try:
        x = int(input('Por favor ingrese un número: '))
        break
    except ValueError:
        print('Oops! No era válido. Intente nuevamente...')
try:
    print('Bloque try con múltiples excepciones')
except(RuntimeError, TypeError, NameError):
    pass


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')
try:
    f = open('miarchivo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Error OS: {}'.format(err))
except ValueError:
    print('No puede convertir el dato a un entero')
except:
    # Ultimo except, se puede usar como comodín.
    print('Error inesperado:', sys.exc_info()[0])
    raise
# Bloque opcional else
# Sucede cuando hubo una excepción no tratada
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('no pude abrir', arg)
    else:
        print(arg, 'tiene', len(f.readlines()), 'lineas')
        f.close()
try:
    raise Exception('carne', 'huevos')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
'''
El siguiente código lanza el siguiente error:
TypeError:cannot unpack non-iterable Exception object
De momento no interesa resolverlo.

    x, y = inst
    print('x=', x)
    print('y=', y)
'''


def esto_falla():
    x = 1/0


try:
    esto_falla()
except ZeroDivisionError as err:
    print('Manejando error en tiempo de ejecución:', err)
# Forzar que ocurra una excepción
#raise NameError('Hola')

# Una forma de determinar cuando ocurrió una excepción mas no manejarlo
try:
    raise NameError('Hola')
except NameError:
    print('Voló una excepción')
    raise
