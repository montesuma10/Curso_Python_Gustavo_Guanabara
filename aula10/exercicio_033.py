a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('terceiro Valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print(f'O menor valor digitado é: {menor}')
maior = a
if b > a  and b > c:
    maior = b
if c > b and c > a:
    maior = c
print(f'o maior valor digitado é: {maior}')