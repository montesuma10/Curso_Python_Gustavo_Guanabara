
def contador(i, f, p):
    from time import sleep
    if p < 0:
        p = p * (-1)
    if p == 0:
        p = 1
    print('=' * 60)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(1)
            cont = cont + p
        print('FIM!')
        sleep(0.5)

    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(1)
            cont = cont - p
        print('FIM!')
        sleep(1)
        print('=' * 60)
        print('Agora é a sua vez de personalizar a contagem!')


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Início: '))
f = int(input('fim: '))
p = int(input('Passo: '))
contador(i, f, p)