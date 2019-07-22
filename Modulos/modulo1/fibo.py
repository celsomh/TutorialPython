# Módulo de número fibonacci
def fib(n):
    '''Escribe la serie de Fibonacci hasta n'''
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    '''Devuelve la seride de Fibonacci hasta n'''
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
