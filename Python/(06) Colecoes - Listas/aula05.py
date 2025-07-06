# Aula 04 - Funcoes (Colecoes)

lista1 = [2.0, 3.5, 4.7]
# print(lista)

lista2 = [1, 5, 9, 11, 15]
# print(lista2)

lista3 = ['Nome', 'Nome2', 'Nome']
# print(lista3)

# lista2 = lista2 + lista3
# print(lista2)

# Tamanho da lista - Funcao len
print(len(lista1))
print(len(lista2))
print(len(lista3))

# Funcoes que so poder ser utilizadas com tipos de dados numericos
print(sum(lista1))  # Soma todos os elementos da lista
x = 2.0 + 3.5 + 4.7
print(x)

print(max(lista2))  # Retorna o maior elemento da lista
print(max(lista1))  

print(min(lista2))  # Retorna o menor elemento da lista
print(min(lista1))  # Retorna o menor elemento da lista

nome = 'Curso de Python'
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7) 

lista8 = list('Curso de Python')
print(lista8)

elemento = 8
if elemento in lista7:
   print('Esse elemento esta na lista')