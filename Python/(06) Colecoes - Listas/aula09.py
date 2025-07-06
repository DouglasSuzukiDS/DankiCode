# Aula 09 - Copiando Listas

lista = ['a', 'b', 'c']
lista2 = [1, 4, 6]

'''lista = lista + lista2
print(lista)'''

'''lista.extend(lista2)
print(lista)'''

'''for x in lista2:
   lista.append(x)'''

# print(lista)

# lista3 = lista # Aqui a lista3 é uma referência para a lista original, não uma cópia.
lista3 = lista.copy()  # Aqui a lista3 é uma cópia da lista original.
print(lista3)

lista3.append('d')

print(lista)
print(lista3)