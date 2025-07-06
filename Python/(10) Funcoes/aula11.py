# Aula 11 - Recursao - Parte 02

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

# reduzirNumero(5)

# Fatorial sem recursao
def fatorialS(numero): 
   fatorial = 1

   if numero == 0:
      return 1
   else:
      for x in range(1, numero + 1):
         fatorial *= x
      
      return fatorial
   
# print(fatorialS(5))

# Fatorial com recursao
def fatorialR(numero):
   if numero == 0:
      return 1
   else:
      return numero * fatorialR(numero - 1)

print(fatorialR(5))