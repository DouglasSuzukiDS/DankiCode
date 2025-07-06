# Aula 13 - Exercicios

# 01) Verifique a idade da pessoa e informe se ela é maior de idade ou não.
'''
idade = int(input("Informe sua idade: "))

if idade < 18:
   print("Voce é menor de idade")
else:
   print("Voce é maior de idade")'''

# 02) Busque a idade do nadadr e classifique na tabela
idade = int(input("Informe a idade do nadador: "))

if int(idade) > 4 and idade < 8: 
   print("Infantil A") 
elif idade > 7 and idade < 11: 
   print("Infantil B") 
elif idade > 10 and idade < 14: 
   print("Juvenil A") 
elif idade > 13 and idade < 18: 
   print("Juvenil B") 
else: print("Voce nao pertence ao grupo de Natacao")