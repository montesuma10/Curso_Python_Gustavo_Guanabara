numeros = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    op = ' '
    while op not in 'SN':
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'A lista completa é {numeros}')
print('Os números pares são:', end=' ')
for n in numeros:
    if n % 2 == 0:
        par.append(n)
print(par, end=' ')
print('\nOs números impares são:', end=' ')
for n in numeros:
    if n % 2 != 0:
        impar.append(n)
print(impar, end= ' ')


