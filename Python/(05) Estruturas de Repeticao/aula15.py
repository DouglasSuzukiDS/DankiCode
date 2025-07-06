# Aula 15 - Exercicio 03

'''
20 termos - significa que você deve fazer a soma dos 20 primeiros termos


exemplo: se o termo 1° é igual a 5 e a regra de soma é termo anterior + 2.


1° termo: 5


2° termo: 5 + 2 = 7


3° termo: 7 + 2 = 9


4° termo: 9 + 2 = 11


até o último termo solicitado.
'''

count = 1

num = int(input('Digite o primeiro termo: '))

while count <= 20:
   print(num)
   num += 2
   count += 1