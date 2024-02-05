dic = {}
list = []
cont = 0
somaid = 0
while True:
    dic.clear()
    dic['Nome'] = str(input('Nome: '))
    cont = cont + 1
    os = ' '
    os = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while os not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        os = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if os == 'MF':
        break
    dic['Sexo'] = os
    dic['Idade'] = int(input('Idade: '))
    somaid = somaid + dic['Idade']
    list.append(dic.copy())
    op = ' '
    op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        print('ERRO! Responda apenas S ou N')
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break


print('='*60)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
media = somaid/cont
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for d in list:
    if d['Sexo'] == 'F':
        print(f'{d["Nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for d in list:
    if d['Idade'] >= media:
        print('     ', end='')
        for k, v in d.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')


