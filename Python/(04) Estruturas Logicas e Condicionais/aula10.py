# Aula 10 - Exercicios 01

# 01) Área de um retângulo
'''
print('Cálculo da área de um retangulo')

altura_retangulo = float(input('Informe a altura do retângulo: '))
base_retangulo = float(input('Informe a base do retângulo: '))

area_retangulo =  base_retangulo * altura_retangulo
print(f'A área do retângulo é: {area_retangulo} da unidade de medida')
'''

# 02_ Area de um quadrado
'''
print('Cálculo da área de um retangulo')

altura_quadrado = float(input('Informe a altura do quadrado: '))
base_quadrado = float(input('Informe a base do quadrado: '))

area_quadrado = base_retangulo * altura_retangulo
print(f'A área do quadrado é: {area_quadrado} da unidade de medida')
'''

# 03) Se o produto que quer avaliar custa (??) reais qual será o valor do mesmo com desconto de (??)% ? 
'''
print('Cálculo do valor do produto com desconto')

valor_produto = float(input('Informe o valor do produto: '))
desconto = float(input('Informe o desconto em porcentagem: '))
valor_final = valor_produto - (valor_produto * (desconto / 100))
print(f'O valor do produto com desconto é: R${valor_final}')
'''

# 04) Área de um círculo
'''
print('Cálculo da área de um círculo')

raio = int(input('Informe o raio do círculo: '))
area_circulo = 3.14 * (raio ** 2)
print(f'A área do círculo é: {area_circulo} da unidade de medida')
'''

# 05) Conversão de reais para dolar
'''
print('Cálculo da conversão de reais para dolares')
valor_reais = float(input('Informe o valor em reais: '))
valor_dolar = float(input('Informe o valor do dólar: '))
valor_final = valor_reais / valor_dolar
print(f'O valor em dólares é: ${valor_final}')
'''

# 06) Conversão do dolar para reais
print('Cálculo da conversão de dolares para reais')
valor_dolar = float(input('Informe o valor do dólar: '))
valor_reais = float(input('Informe o valor em reais: '))
valor_final = valor_dolar / valor_reais
print(f'O valor em dólares é: ${valor_final}')