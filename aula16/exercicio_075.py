num = (int(input('Digite um nùmero: ')),
           int(input('Digite outro nùmero: ')),
               int(input('Digite mais um nùmero: ')),
                   int(input('Digite o último nùmero: ')))
print('=*'*30)
print(f'você diditou os valores: {num}')
print('=*'*30)
if 9 in num:
    print(f'O número 9 aparece {num.count(9)} ')
else:
    print('Nenhum número 9 foi digitado')
if 3 in num:
    print(f'O valor 3 foi digitado primeiro na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os números pares são:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')

