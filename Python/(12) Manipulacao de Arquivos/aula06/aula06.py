# Aula 06 - Arquivos de Texto Simples - Leitura

arquivo = open('receita.txt', 'r')

# print(arquivo.closed) # Verifica se o arquivo está fechado

# print(arquivo.read()) # Lê todo o conteúdo do arquivo

with open('receita.txt', 'r') as arq: # Aqui já abre e fecha o arquivo após fazer a leitura
   conteudo = arq.read()  # Lê todo o conteúdo do arquivo
   print(conteudo)  # Exibe o conteúdo lido