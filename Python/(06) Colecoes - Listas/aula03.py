# Aula 03 - Slicing

lista = ['chicago', 'queens', 'salvador', 'pernambuco']
# print(lista)

lista2 = [2, 3, 7, 8, 10]
# print(lista2)

lista3 = [2.0, 3.5, 6.3]
# print(lista3)

lista4 = [True, False]
# print(lista4)

lista5 = [True, 'chicago', 2.5, False, 4, 8]
# print(lista5)

print(type(lista2))

print(lista5[1])

print(lista5[-6])

print(lista5[::])
print(30 * '-')

print(lista5[1:]) # Retona do index que destacamos até o fim da lista
print(lista5[2:]) # Retona do index que destacamos até o fim da lista
print(lista5[:3]) # Retorna do começo da lista até o index - 1
print(lista5[:4]) # Retorna do começo da lista até o index - 1
print(lista5[1:4])