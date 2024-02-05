maior = 0
h = 0
f = 0
while True:
    print('-' * 20)
    print('  CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior = maior + 1
    if sexo == 'M':
        h = h + 1
    if sexo == 'F' and idade < 20:
        f = f + 1
    print('-' * 20)
    op = ' '
    while op not in 'SN':
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {f} mulheres com menos de 20 anos')