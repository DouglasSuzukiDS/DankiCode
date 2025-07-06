# Aula 02 - Adicionar e remover elementos

# Listas: Colecao ordenada, mutavel e que permite valoes duplicados
# Tuplas: Colecao ordenada, imutavel e que permite valores duplicados
# Dicionarios: Colecao nao ordenada, mutavel e que nao permite valores duplicados
# Sets: Colecao não ordenada, imutavel e que nao permite valores duplicados
# Os sets tambem sao conhecidos como conjuntos

'''conjunto = {'item1', 'item2', 'item3', 3, True, 4.7, 'São Paulo'}
print(type(conjunto))
print(len(conjunto))'''

'''tupla = (3, 7, 9, 5)
# conjunto = set(tupla)
conjunto = set((3, 7, 9, 5))  # Convertendo uma tupla em um conjunto
print(conjunto)'''

'''conj = { 'item1', 'item2'}

for x in conj:
   print(x)'''

'''conjunto = {4, 6, 8, 9, 1}
print(11 in conjunto)  # Verifica se o valor 11 está no conjunto'''

'''set1 = {'item1', 'item2', 'item3'}
print(set1)
set1.add('item5')
print(set1)
set1.add(8)
set1.add(True)
print(set1)'''

# Adicionando elementos
'''set1 = {4, 5, 7, 8, 9, 1}
set2 = {'item3', 'item5', 'item1'}
set1.update(set2)  # Adiciona os elementos de set2 a set1
print(set1)
# set1.update([1, 4, 7, 8, 9, 3, 'item5', 'item6'])
set1.update((1, 4, 7, 8, 9, 3, 'item5', 'item6'))
print(set1)'''

# Removendo elementos
set1 = {1, 4, 7, 8, 9, 3, 'item5', 'item6'}
print(set1)

set1.pop()
print(set1)

set1.remove('item5')  # Remove o elemento 'item5'
set1.discard('item6')  # Remove o elemento 'item6'
print(set1)

set1.clear()  # Limpa todos os elementos do conjunto
print(set1)