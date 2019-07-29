f = open('archivodetrabajo', 'w')
print(f)
# Crear un archivo binario. Se trabaja en bytes
b = open('archivobinario', 'wb')
# Se aconseja el uso de with para manejar objetos archivo
with open('archivodetrabajo', 'w') as f:
    f.write('Linea de texto escrito con el método write\nNueva linea para continuar escribiendo\nTercera linea de texto')

print(f.closed)

# Metodos de los objetos archivo
with open('archivodetrabajo') as f:
    print('Primeras 20 letras del archivo:\n', f.read(20))
    print('Las 5 letras que le prosiguen:\n', f.read(5))
    print('Lo que resta de la primera linea del archivo:\n', f.readline())
# iterar sobre un archivo
print('Texto del archivo obtenido a través de iteraciones')
with open('archivodetrabajo') as f:
    for linea in f:
        print(linea, end=' ')
    print()
with open('archivodetrabajo') as f:
    print('-'*60, '\nTexto completo')
    print(f.read())
    print('-'*60)
