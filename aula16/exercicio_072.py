numero = 'zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
         'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numero[n]}')
        break
    else:
        print('Tente novamente. Digite um número entre 0 e 20')

