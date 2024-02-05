from math import factorial
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = factorial(n)
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c = c - 1
print(f, end='')