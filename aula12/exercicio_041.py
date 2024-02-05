from datetime import date

ano_nasc = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é MIRIM')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é JUNIOR')
elif 19 < idade <= 25:
    print(f'Você tem {idade} anos, sua categoria é SÊNIOR')
else:
    print(f'Você tem {idade} anos, sua categoria é MASTER')
