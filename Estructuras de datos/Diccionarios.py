tel = {'jack': 4098, 'sape': 4139}
print('tel:', tel)
tel['guido'] = 4127
print('tel:', tel)
print('tel[jack]:', tel['jack'])
print('del tel[\'sape\']:')
del tel['sape']
print(tel)
tel['irv'] = 4127
print("tel['irv']=4127")
print(tel)
print('keys:', list(tel.keys()))
print('keys sorted:', sorted(tel.keys()))
word = 'guido'
se_encuentra = word in tel
print(word, 'se encuentra en', tel, ':', se_encuentra)
word = 'jack'
se_encuentra = word not in tel
print(word, 'no se encuentra en', tel, ':', se_encuentra)
# Crear un diccionario con el constructor dict()
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('diccionario con dict():', d)
d = {x: x**2 for x in(2, 4, 6)}
print('diccionario por comprensión:', d)
d = dict(sape=4139, guido=4127, jack=4098)
print('otro diccionario:', d)