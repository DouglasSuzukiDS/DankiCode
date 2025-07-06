# Aula 01 - Dicionarios

# Listas: Colecao ordenada, mutavel e que permite valoes duplicados
# Tuplas: Colecao ordenada, imutavel e que permite valores duplicados
# Dicionarios: Colecao nao ordenada, mutavel e que nao permite valores duplicados

dicionario = {'nome': 'Nick', 'idade': 20, 'nacionalidade': 'russo', 'idade': 22}
print(dicionario)

print(dicionario['nome']) # Acessar o valor

print(dicionario.get('idade')) # Acessar o valor com o metodo get

print(len(dicionario))

print(dicionario.keys()) # Acessar as chaves do dicionario

print(dicionario.values()) # Acessar os valores do dicionario

print(dicionario.items()) # Acessar os itens do dicionario