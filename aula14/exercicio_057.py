'''
while True:
    sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print(f'sexo {sexo} computado')
        break
    else:
        print('Erro, tente novamente')
'''
sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

