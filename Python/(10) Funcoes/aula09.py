# Aula 09 - Kwargs

# Argumento Arbitrario **Kwargs - Keyword Arguments
# Essa função recebe argumentos que serao atribuidos em um dicionario

def imprimir_nomes(**nomes):
   print(f'{nomes['nome']} {nomes["sobrenome"]}')

imprimir_nomes(nome='Nick', sobrenome='Diatlov')