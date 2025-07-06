# Aula 09 - Projeto Mini Game (adivinhar numero) - Parte 02

palpite = 5
numero = 9

while bool(palpite) is True:
   print('Qual o numero correto?')

   palpite = int(input('Digite um numero: '))

   if palpite == numero:
      print('Parabens voce acertou')
      break
   else:
      print('Voce errou')
else:
   print('Erro na aplicacao')