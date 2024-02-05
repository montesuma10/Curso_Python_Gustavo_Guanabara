num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print(f'O primeiro valor({num1}) é maior que o segundo valor({num2})')
elif num2 > num1:
    print(f'O segundo valor({num2}) é maior que o primeiro valor({num1})')
else:
    print(f'Não existe valor maior. O primeiro valor({num1}) é igual ao segundo valor({num2})')
