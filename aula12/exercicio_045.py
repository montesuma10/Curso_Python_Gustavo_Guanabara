from  random import  randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções:\n'
      '[1] PEDRA\n'
      '[2] PAPEL\n'
      '[3] TESOURA')
jogador = int(input('Qual é a jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=*'*15)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('=*'*15)
if computador == 0:
      if jogador == 0:
            print('EMPATE')
      elif jogador == 1:
            print('JOGADOR VENCE')
      elif jogador == 2:
            print('COMPUTADOR VENCE')
      else:
            print('JOGADA INVÁLIDA!')
elif computador == 1:
      if jogador == 0:
            print('COMPUTADOR VENCE')
      elif jogador == 1:
            print('EMPATE')
      elif jogador == 2:
            print('JOGADOR VENCE')
      else:
            print('JOGADA INVÁLIDA!')
elif computador == 2:
      if jogador == 0:
            print('JOGADOR VENCE')
      elif jogador == 1:
            print('COMPUTADOR VENCE')
      elif jogador == 2:
            print('EMPATE')
      else:
            print('JOGADA INVÁLIDA!')

