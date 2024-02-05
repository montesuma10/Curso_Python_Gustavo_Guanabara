from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = (n1+n2)
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opção == 2:
        mult = (n1 * n2)
        print(f'A multiplicação de {n1} x {n2} = {mult}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Inform os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    print('=*' * 30)
    sleep(2)
print('Fim do programa! Volte sempre!')


