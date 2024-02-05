#essa versão não consegue fazr maior ou menor
'''
import random
erros = 0
computador = random.randint(0, 10)
num = int(input('Qual é o seu palpite? '))

while num != computador:
    num = int(input('Qual é o seu palpite? '))
    if num > computador:
        print('È menor...')
    else:
        print('È maior...')
    erros = erros + 1

print(f'você acertou que é o número {num} com {erros+1} tentativas')
'''
from random import randint
computador = randint(0, 10)
tentativas = 0
print('Sou seu computador... e acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?\n')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente mais uma vez.')
        else:
            print('Menos...tente mais uma vez')

print(f'Acertou com {tentativas} tentativas que o número sorteado era {jogador}')



