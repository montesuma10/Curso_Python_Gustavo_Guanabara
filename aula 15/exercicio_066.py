
cont  = 0
s = 0
while True:
    n = int(input('Digite um valor[999 para parar]: '))
    if n == 999:
        break
    cont = cont + 1
    s = s + n
print(f'você digitou {cont} números cujo a soma deles é {s}')