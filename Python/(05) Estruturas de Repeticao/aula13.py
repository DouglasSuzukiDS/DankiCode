# Aula 13 - Numeros Primos

print(30 * '-')

numero = int(input("Insira um número para descobrir se o mesmo é primo: "))

if numero > 1:
   for x in range(2, numero):
      if(numero % x) == 0:
         print('Esse número não é primo!')
         break
      else:
         print('Esse número é primo!')
else:
   print('Esse número não é primo!, Número menor ou igual a 1!')

print(30 * '-')
