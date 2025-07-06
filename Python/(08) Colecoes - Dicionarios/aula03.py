# Aula 03 - Conhecendo a Funcao fromkeys

# Listas: Colecao ordenada, mutavel e que permite valoes duplicados
# Tuplas: Colecao ordenada, imutavel e que permite valores duplicados
# Dicionarios: Colecao nao ordenada, mutavel e que nao permite valores duplicados

dados = {'nome': 'Nick', 'ano': 2005, 'valor_logico': True}
# print(dados)

dados['idade'] = '20'
# print(dados)

dados.update({'estado': 'São Paulo'})
# print(dados)

# A função popitem elimina o ultimo item apenas da versão 3.7 pra cima
# Nas versoes (abaico 3.7) essa funcao elimina um item aleatorio
dados.popitem()  # Remove o ultimo item
# print(dados)

dados.pop('ano')  # Remove o item com a chave 'ano'
# print(dados)

# del dados['ano']
# print(dados)

# dados.clear()  # Limpa todos os itens do dicionario
# print(dados)

'''for x in dados:
   print(dados[x])'''

'''# for x in dados.keys():
for x in dados.values():
   print(x)'''

'''for x,y in dados.items():
   print(x, y)'''

'''dicio = dados.copy()  # Cria uma copia do dicionario
print(dicio)

dicio2 = dict(dados)  # Cria uma copia do dicionario
print(dicio2)

dados['idade'] = 25
print(dados)
print(dicio) 
print(dicio2)  '''

tupla = ('item1', 'item2', 'item3')
tupla2 = ('item1', 'item2', 'item3')
x = 0
# dicio = dict.fromkeys(tupla)  # Cria um dicionario com chaves 
# print(dicio)

# dicio = dict.fromkeys(tupla, 0)  # Cria um dicionario com chaves e o valor 0
# print(dicio)

# dicio = dict.fromkeys(tupla, tupla2)  # Cria um dicionario com chave e valor
# print(dicio)

dicio = {
   "dicio1": {
      "nome": "Nick",
      "idade": 20,
   },
   "dicio2": {
      "nome": "Shanks",
      "idade": 38,
      "dicio3": {
         "nome": "BigMom",
         "idade": 5,
      }
   },
}

print(dicio)