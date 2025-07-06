# Aula 10 - Recursao - Parte 01

'''def reduzirNumero(numeroInt):
   while numeroInt > 0:
      print(numeroInt)
      numeroInt -= 1

reduzirNumero(10)'''

'''
   1) Checar se o numero não é igual a 0
   2) Se ele nao for igual a 0, reduzir 1 udade
'''

def reduzirNumero(numeroInt):
   print(numeroInt)
   
   if numeroInt > 0:
      # N - 1
      reduzirNumero(numeroInt - 1)

reduzirNumero(5)