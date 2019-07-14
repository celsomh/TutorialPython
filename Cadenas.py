# Cadenas
# Imprimir un backslash, anteponer una r
print(r"C:\Users\usuario")
print("""
cadena
a triple
comiillas""")
# Concatenar
print("Cadena"+" concatenada")
print(4*"Cadena repetida 4 veces ")
print("Cadena concatenada"" sin utilizar +""(Solo para cadenas literales)")
cadena = "Hola"
print(cadena+" Mundo concatenado")
cadena = "Esto es una cadena"
print(cadena)
print(cadena[0]+cadena[2])
print(cadena[-1]+cadena[-3])
# Cadenas rebanadas
print("Subcadena [n:n] "+cadena[2:6])
print("Subcadena [:n] "+cadena[:3])
print("Subcadena [:-n] "+cadena[:-4])
print("Longitud de cadena "+str(len(cadena)))
print(cadena)
# Escapar un ' o ""
print("Una comilla simple ' escapada entre comillas dobles")
print('Comilla doble " escapada entre comillas simples')
