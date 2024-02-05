valor_casa = float(input('Qual o valor da casa? R$: '))
sal = float(input('Qual o valor do seu salário? R$: '))
anos = int(input('Em quantos anos deseja financiar? R$: '))
meses =  anos*12
valor_mes = valor_casa/meses
limite_de_fin = sal*0.3

if valor_mes <= limite_de_fin:
    print(f'Para pagar uma casa de R${valor_casa} em {anos} anos o valor da prestação será de R$ {valor_mes}')
    print('\033[32mPARABÉNS, FINANCIAMENTO APROVADO!!!\033[m')
else:
    print(f'Para pagar uma casa de R${valor_casa} em {anos} anos o valor da prestação será de R$ {valor_mes}')
    print('\033[31mINFELIZMENTE O EMPRESTIMO FOI NEGADO!!!\033[m')
    print(f'O valor máximo da prestação não pode ultrapassar R${limite_de_fin}')