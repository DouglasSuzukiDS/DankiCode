# Aula 03 - Loops

tupla = ('item1')
tupla2 = ('a', 'b')

tupla = 'item1', 'item2', 'item3'

for x in tupla:
   print(x)   

for  x in range(len(tupla)):
   print(x)

lista = ['item1', 'item2', 'item3', 'item4', 'item5']
print(lista)

(x, *y, z) = lista # O * é usado para capturar o restante dos itens da lista

print(f'X: {x}')
print(f'Y: {y}')
print(f'Z: {z}') 