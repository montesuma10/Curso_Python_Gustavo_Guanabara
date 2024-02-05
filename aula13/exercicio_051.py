print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

p = int(input('Primeiro termo: '))
r =int(input('Razão: '))
f = p + (10*r)
for c in range(p, f, r):
    print(c, end=' --> ')
print('ACABOU')
