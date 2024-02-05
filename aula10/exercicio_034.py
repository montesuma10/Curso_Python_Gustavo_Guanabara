sal = float (input('Digite o valor do seu salário: '))

if sal >= 1250:
    sal = (sal + (sal*10/100))
else:
    sal = (sal + (sal*15/100))

print(f' Seu novo salário será de R$ {sal}')