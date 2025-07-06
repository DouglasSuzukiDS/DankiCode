# Aula 03 - Jogo Pedra, Papel ou Tesoura - Parte 01

from random import choice

jogador_vitorias = 0
maquina_vitorias = 0

def opcao_jogador():
   esc_jogador = input('Escolha Pedra, Papel ou Tesoura')
   esc_jogador = esc_jogador.lower()

   if esc_jogador == 'pedra':
      return esc_jogador
   elif esc_jogador == 'papel':
      return esc_jogador
   elif esc_jogador == 'tesoura':
      return esc_jogador
   else:
      print('Opção inválida. Tente novamente.')
      opcao_jogador()

def opcao_maquina():
   esc_maquina = choice(['pedra', 'papel', 'tesoura'])

   return esc_maquina

while True:
   esc_jogador = opcao_jogador()
   esc_maquina = opcao_maquina()

   esc_jogador = input('Você quer jogar novamento? ')
   if esc_jogador in ['SIM', 'sim', 's', 'S']:
      pass
   elif esc_jogador in ['NAO', 'nao', 'n', 'N']:
      break
   else:
      break