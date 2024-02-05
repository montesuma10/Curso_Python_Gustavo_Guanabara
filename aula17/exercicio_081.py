numeros = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(numeros)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista!')