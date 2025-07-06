# Aula 06 - Exercício - Trocanco variaveis

x = input('Insira o valor de x: ')
y = input('Insira o valor de y: ')

# Criaremos uma variável temporaria
temp = x
x = y
y = temp

print(f'O valor de x depois da troca é: {x}')
print(f'O valor de y depois da troca é: {y}')