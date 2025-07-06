# Aula 02 - Mais sobre Tuplas Tuplas

x = ('item1', 'item2')
print(x)

x = ('item3', 'item4', 'verde')
print(x)

unidade_federativas = ['SP', 'DF', 'GO']

tupla = ('item1', 'item2', 'item3', 'item4')
lista = list(tupla)
print(tupla)
print(lista)

lista.append('item5')
print(lista)

tupla = tuple(lista)
print(tupla)