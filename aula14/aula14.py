'''
for c in range (1, 10):
    print (c, end = ' ')
print ('fim')

c = 1
while c < 10:
    print(c, end = ' ')
    c = c + 1
print('fim')


n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('Fim')


r  = 'S'
while r == 'S':
     n = int(input('digite um valor:' ))
     r = str(input('Quer continuar? [S/N]')).upper()
print('fim')
'''

n = 1
par = 0
impar = 0
while n != 0:
     n = int(input('Digite um valor: '))
     if n % 2 == 0:
          par = par + 1
     else:
          impar = impar + 1
print(f'Vc digitou {par-1} numeros pare se {impar} numeros ímpares')