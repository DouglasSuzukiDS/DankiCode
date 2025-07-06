# Aula 07 - Adicionando elementos

lista = ['carro', 'barco', 'aviao']
print(lista)

'''for x in range(len(lista)):
   print(x, lista[x])'''

'''texto = 'meunome@gmail.com'
lista2 = list(texto)
print(lista2)

texto = texto.split('@')
print(texto)'''

'''lista.insert(0, 'bicleta')
print(lista)'''

# lista.append(['bicicleta', 'navio'])
lista.extend(['bicicleta', 'navio'])

lista.append('moto')
print(lista)
for x in range(len(lista)):
   print(x, lista[x])