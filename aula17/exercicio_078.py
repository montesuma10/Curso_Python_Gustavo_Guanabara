
n = []
maior = 0
menor = 0
for cont in range(0, 5):
    n.append(int(input(f'Digite um valor na posição {cont}: ')))
print(f'você digitou os valores: {n}')
print(f'O maior valor digitado foi {max(n)} na posições ', end='')
maior = max(n)
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(n)} na posições: ', end='')
menor = min(n)
for i, v in enumerate(n):
    if v == menor:
        print(f'{i}...', end='')

'''                  #segunda resoluçã
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
'''