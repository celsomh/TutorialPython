import time


def fib(n):
    '''Escribe la serie de Fibonacci hasta n'''  # esto es un docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(100)
f = fib
print(f(100))


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib2(200))
# Argumentos con valores por omisión
# Los argumentos con asignación pueden omitirse al momento de hacer la llamada, o entregarle valores


def pedir_confirmación(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'N', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos-1
        if reintentos < 0:
            raise ValueError('Respuesta inválida')
        print(recordatorio)


pedir_confirmación('¿Realmente quieres salir?', 2)
i = 5


def f(arg=i):
    print(arg)


i = 6
f()

print('f(a,L[])', '\n', '-'*40)


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

print('f(a,L=None)')


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
# También se le puede pasar valores de la forma key=value


def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print('-- Este loro no va a', accion, end=' ')
    print('si le aplicás', tension, 'voltios.')
    print('-- Gran plumaje tiene el', tipo)
    print('-- Está', estado, '!')


print('Loro 1')
loro(1000)
print("Loro 2")
loro(tension=200)
print("Loro 3")
loro(tension=300000, accion='VOOOOM')
print("Loro 4")
loro(accion='VOOOOOOM', tension=4000000)

print('-'*40, '\n', 'venta de queso')


def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print('-- ¿Tiene', tipo, '?')
    print('-- Lo siento, nos quedamos sin', tipo)
    for arg in argumentos:
        print(arg)
    print("-"*40)
    for c in palabrasclaves:
        print(c, ':', palabrasclaves[c])


ventadequeso('Limburger', 'Es muy liquido, sr.', 'Realmente es muy muy liquido, sr.',
             cliente='Juan Garau', vendedor='Miguel Paez', puesto='Venta de Queso Argentino')
# Documentacion
print('Documentación', '\n', '-'*40)


def mi_funcion():
    '''No hace mas que documentar la función.

No, de verdad. No hace nada.
    '''
    pass


print(mi_funcion.__doc__)
# Anotación de funciones


def f(jamon: str, huevos: str = 'huevos') -> str:
    print('Anotaciones:', f.__annotations__)
    print('Argumentos:', jamon, huevos)
    return jamon+'y'+huevos


print(f('carnes'))
