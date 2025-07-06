# Aula 02 - Import

from random import randint

palpite = 0
numero = randint(1, 10)

while True:
   print('Qual o numero correto?')

   palpite = int(input('Digite um numero: '))

   if palpite == numero:
      print('Parabens voce acertou')
      break
   else:
      print('Voce errou')
else:
   print('Erro na aplicacao')