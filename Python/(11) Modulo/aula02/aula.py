# Aula 02 - Import
from random import *

# print(random.random())
print(randint(1, 5))

'''
   # Modulo - Arquivos com extens]ao .py. Ou seja, arquivos Python.
   # Pacotes = Diretórios contendo conjuto de módulos. Pastas com vários arquivos python.
'''

from pacote import principal, segundario
from pacote.sub_diretorio import outro as modulo

print(principal.soma(2, 3))
print(segundario.quadratica(5))
print(modulo.cubica(3))