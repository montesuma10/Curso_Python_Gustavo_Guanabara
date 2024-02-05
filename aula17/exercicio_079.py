numeros =[]
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = ' '
    while op not in 'SN':
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
numeros.sort()
print(f'Você digitou os valores: {numeros}')