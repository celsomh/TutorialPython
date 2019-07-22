canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print('canasta:', canasta)
se_encuentra = 'naranja' in canasta
print('naranja en canasta:', se_encuentra)
se_encuentra = 'yerba' in canasta
print('yerba in canasta:', se_encuentra)
a = set('abracadabra')
b = set('alacazam')
print('a:', a)
print('b:', b)
print('a-b:', a-b)
print('a|b:', a | b)
print('a&c:', a & b)
print('a^b:', a ^ b)
# Comprensión de conjuntos
a = {x for x in 'abracadabra' if x not in 'abc'}
print('lista compresion:', a)
