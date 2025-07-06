# Aula 07 - Arquivos de Texto Simples - Escrita

# arquivo = open('receita.txt', 'r')

# print(arquivo.closed) # Verifica se o arquivo está fechado

# print(arquivo.read()) # Lê todo o conteúdo do arquivo

with open('receita.txt', 'a') as arquivo: # Aqui já abre e fecha o arquivo após fazer a leitura
   # conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
   # print(conteudo)  # Exibe o conteúdo lido
   arquivo.write('Imaginar')