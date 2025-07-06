# Aula 08 - Remover e Ordenar

lista = ['carro', 'barco', 'aviao']
# print(lista)

# lista.pop()
# lista.remove('barco') # Informar o elemento a ser removido
# lista.pop(0) #Informar o indice do elemento a ser removido

# del lista # Deleta a lista inteira
# del lista[0] # Deleta o primeiro elemento da lista

'''for x in range(len(lista)):
   print(x, lista[x])'''

carrinho_de_compras = ['pao', 'carne', 'verduras', 'alface']
# carrinho_de_compras.clear() # Limpa o array
carrinho_de_compras.sort() # Ordena o array

print(carrinho_de_compras)

for x in range(len(carrinho_de_compras)):
   print(x, carrinho_de_compras[x])

lista2 = [1, 50, 23, 67, 100]
print(lista2)

lista2.sort() # Ordena o array
print(lista2)

lista2.sort(reverse=True) # Ordena o array em ordem decrescente
print(lista2)

lista3 = ['Ana', 'Pedro', 'Marta', 'Clarice', 'beatriz', 'ana clara']
print(lista3)

lista3.sort() # Ordena o array
print(lista3)

lista3.sort(key = str.lower) # Ordena o array
print(lista3)