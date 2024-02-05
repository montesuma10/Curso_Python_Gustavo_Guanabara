soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(f'Você informou {cont} pares e a soma deles é {soma}')