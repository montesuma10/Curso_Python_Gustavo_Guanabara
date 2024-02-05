
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO')

'''
while True:
    from time import sleep
    from random import choice
    print('='*30)
    print('JOGO DO SIGNIFICADO DO NOME')
    print('='*30)

    nome = str(input ('Digite seu nome: ')).upper()
    print('processando.')
    sleep(1)
    print('processando..')
    sleep(1)
    print('processando...')
    sleep(1)
    if nome == 'RICARDO':
        print('DO LATIM, QUE VEIO POR SUA VEZ DOS GERMÂNICOS, \033[33mFORTE E CORAJOSO\033[m')
    elif 'FELIPE' or 'GUSTAVO':
        lista = ['PUTA', 'RAPARIGA', 'BANDIDA', 'RAMEIRA']
        escolhido = choice(lista)
        print(f'vc é: \033[31m{escolhido}!!!\033[m')
'''

