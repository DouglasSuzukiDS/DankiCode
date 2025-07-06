# Aula 05 - Projeto gerador de senhas

chave = input('Digite a base da sua senha: ')

senha = ''

for letra in chave:
   if letra in 'Aa':
      senha += '1'
   elif letra in 'Bb':
      senha += '@'
   elif letra in 'Cc':
      senha += '2'
   elif letra in 'Dd':
      senha += '3'
   elif letra in 'Ee':
      senha += '4'
   elif letra in 'Ff':
      senha += '5'
   elif letra in 'Rr':
      senha += '#'
   elif letra in 'Ss':
      senha += '%'
   elif letra in 'Mm':
      senha += '$'
   else:
      senha += letra

print(f'Sua senha é: {senha}')