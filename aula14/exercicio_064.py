num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número [999 para parar]: '))
print(f'você digitou {cont} números e a soma deles é {soma}')

