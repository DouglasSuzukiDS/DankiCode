# Aula 07 - Verificando sinal numerico

numero = int(input("Digite um número: "))

if numero > 0:
   print(f'O número {numero} é positivo.')
elif numero == 0:
   print(f'O número {numero} é neutro.')
else:
   print(f'O número {numero} é negativo.')