# Aula 02 - Retorno

'''lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
var1 = print('RBMK Reactor')
print(lista)
print(f'O Retorno da funcao pop é: {retorno}')
print(f'O Retorno da funcao print é: {var1}')'''

def ola_mundo():
   # print('Olá, Mundo!')
   return 'Olá, Mundo!'

retorno = ola_mundo()
# print(retorno)
# print(ola_mundo())

def par_impar():
   numero = 41

   if numero % 2 == 0:
      return 'Numero Par'
   
   return 'Numero Ímpar'

print(par_impar())

x = 0

if x == 0:
   print(0)

print('Ola')