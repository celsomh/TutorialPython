import json
x = [1, 'simple', 'lista']
print(json.dumps(x))
f = open('archivocondatosjson', 'w')
# Serializar objeto y escribirlo en archivo de texto
json.dump(x, f)
f.close()
f = open('archivocondatosjson', 'r+')
print('texto:', f.read())
