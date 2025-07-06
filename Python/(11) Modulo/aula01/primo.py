# Aula 01 - Modulo

def primo(numero):
   if numero > 1:
      for x in range(2, numero):
         if(numero % x) == 0:
            return 'Esse número não é primo!'
         else:
            return 'Esse número é primo!'
   else:
      return 'Esse número não é primo!, Número menor ou igual a 1!'
