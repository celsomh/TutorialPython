class Error(Exception):
    '''Clase base para excepciones en el módulo'''
    pass


class EntradaError(Error):
    '''Excepcion lanzada por errores en las entradas

    Atributos:
        expresión -- expresion de entrada en la que ocurre el error
        mensaje -- explicación del error
    '''

    def __init__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje


class TransicionError(Error):
    '''Lanzada cuando una operación intenta una transicion de estado no permitida.

    Atributos:
    previo -- estado al principio de la transicion
    siguiente -- nuevo estado intentado
    mensaje -- explicación de porqué la transicion no está permitida
    '''

    def __init__(self, previo, siguiente, mensaje):
        self.precvio = previo
        self.siguiente = siguiente
        self.mensaje = mensaje


'''
Codigo comentado con el fin de evitar la excepción y continuar 
try:
    raise KeyboardInterrupt
finally:
    print('Chau, mundo!')
'''


def dividir(x, y):
    try:
        result = x/y

    except ZeroDivisionError:
        print('¡división por cero!')
    else:
        print('el resultado es:', result)
    finally:
        print('ejecutando la cláusula finally')


dividir(1, 0)
