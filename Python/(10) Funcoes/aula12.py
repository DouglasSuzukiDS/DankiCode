'''01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.

a) Uma função que receba X e Y como entrada e retorne o maior deles;

b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;'''

def bigger(x, y):
    if x > y:
        return print(f'O maior número é: {x}')
    else:
        return print(f'O maior número é: {y}')

def average(x, y):
    return print(f'A média aritmética entre {x} e {y} é: {(x + y) / 2}')

def showResults(x, y):
   bigger(x, y)
   average(x, y)

# 02 - Escreva uma função de potenciação, em que os dados de entrada são: base e expoente (inteiros).
def exponentiation(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / (base ** abs(exponent)) # ABS => mantem o valor positivo do expoente
    else:
        return base ** exponent

#03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora padrão do windows 10
def calculator():
      print('Selecione a operação:')
      print('1. Adição')
      print('2. Subtração')
      print('3. Multiplicação')
      print('4. Divisão')
   
      choice = input('Digite o número da operação (1/2/3/4): ')
   
      if choice in ['1', '2', '3', '4']:
         num1 = float(input('Digite o primeiro número: '))
         num2 = float(input('Digite o segundo número: '))
   
         if choice == '1':
               return print(f'Resultado: {num1 + num2}')
         elif choice == '2':
               return print(f'Resultado: {num1 - num2}')
         elif choice == '3':
               return print(f'Resultado: {num1 * num2}')
         elif choice == '4':
               if num2 != 0:
                  return print(f'Resultado: {num1 / num2}')
               else:
                  return print('Erro: Divisão por zero!')
      else:
         return print('Opção inválida!')
      
showResults(10, 20)
print(exponentiation(2, 3))
calculator()