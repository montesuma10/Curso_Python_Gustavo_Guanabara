from datetime import datetime
empreg = {}
empreg['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
empreg['Idade'] = datetime.now().year - nasc
empreg['Cart_de_Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if empreg['Cart_de_Trabalho'] != 0:
    empreg['Ano_de_Contratação'] = int(input('Ano de Contratação: '))
    empreg['Salário'] = float(input('Salário: R$'))
    empreg['Aposentadoria'] = empreg['Idade'] + ((empreg['Ano_de_Contratação'] + 35) - datetime.now().year)
print('=' * 60)
for k, v in empreg.items():
    print(f' - {k} é igual a {v}')
