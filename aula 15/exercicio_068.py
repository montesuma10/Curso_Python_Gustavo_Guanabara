print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
v = 0
while True:
    import random
    computador = random.randint(0, 10)
    n = int(input('Diga um valor: '))
    e = str(input('Par ou Ìmpar?[P/I]: ')).upper().strip()[0]
    total = computador + n
    if e == 'P':
        if total % 2 == 0:
            print(f'você jogou {n} e o computador {computador}. Total de {total} DEU PAR')
            print('Você VENCEU!')
            v = v + 1
        else:
            print(f'você jogou {n} e o computador {computador}. Total de {total} DEU ÌMPAR')
            print('Você PERDEU!')
            break
    elif e == 'I':
        if total % 2 == 1:
            print(f'você jogou {n} e o computador {computador}. Total de {total} DEU ÌMPAR')
            print('Você VENCEU!')
            v = v + 1
        else:
            print(f'você jogou {n} e o computador {computador}. Total de {total} DEU PAR')
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER Você venceu {v} vezes')