import fibo
import sys
a = [1, 2, 3, 4, 5]
print('dir():', dir())
print('dir(fibo):', dir(fibo))
print('name:', fibo.__name__)
print('package:', fibo.__package__)
print('loader:', fibo.__loader__)
print('file:', fibo.__file__)
print('cached', fibo.__cached__)
print('builtins', fibo.__builtins__)
print('dir(sys):', dir(sys))
