# Aula 10 - Do While

palpite = 0
numero = 9

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