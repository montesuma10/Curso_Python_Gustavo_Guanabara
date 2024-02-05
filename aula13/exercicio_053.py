frase = str(input('Digite a frase: '))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso = inverso + junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('a frase digitada não é um palindromo')
