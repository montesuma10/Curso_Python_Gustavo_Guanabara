#diferença entre print e rturn
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 1)
somar(2, 2)
somar(6)
print('='*60)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1=somar(3, 2, 1)
r2=somar(2, 2)
r3=somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')
print('='*60)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print('='*60)
'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('È par!')
else:
    print('È ímpar!')


