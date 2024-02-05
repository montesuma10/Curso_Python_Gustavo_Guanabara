'''
print('---AVALIANDO O SEU CARRO---')
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('---FIM---')

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('---FIM---')
'''
nome = str(input('Qual é o seu nome? ')).upper().strip()
if nome == 'GUSTAVO':
    print('Que nome lindo voçê tem!')
print(f'bom dia, {nome}!')
