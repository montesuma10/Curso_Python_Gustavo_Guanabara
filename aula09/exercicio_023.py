def analisando_numero(num):
    print(f'Analisando o número: {num}')
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'milhar: {c}')
    print(f'Milhar: {m}')



num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num //100 % 10
m = num // 1000 % 10

analisando_numero(num)