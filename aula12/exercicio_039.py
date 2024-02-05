from datetime import date
ano_nasc = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade > 18:
    print(f'PASSOU DO TEMPO de voçê se alistar, está com {idade} anos, já se passaram {idade-18} anos do prazo')
    print(f'o alistamento era pra ter sido no ano de {ano_nasc+18}')
elif idade == 18:
    print(f'HORA DE SE ALISTAR, está com {idade} anos')
else:
    print(f'AINDA VAI SE ALISTAR, está com {idade} anos ainda, faltam {18-idade} anos para isso')
    print(f'o alistamento será no ano de {ano_nasc + 18}')
