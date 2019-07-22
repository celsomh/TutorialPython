# Tupla
t = 12345, 54321, 'hola!'
print('tupla:', t)
print('t[0]', t[0])
u = t, (1, 2, 3, 4, 5)
print('tupla anidada:', u)
v = ([1, 2, 3], [3, 2, 1])
print('tupla mutable:', v)
tupla_vacía = ()
print('tupla vacía:', tupla_vacía)
tupla_singleton = 'hola',
print('tupla única:', tupla_singleton)
# Empaquetado de tuplas
t = 12345, 54321, 'hola!'
# Desempaquetado de secuencias
x, y, z = t
print('x:', x, '\ny:', y, '\nz:', z)
