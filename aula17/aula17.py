num = [2, 5, 9, 1]
print(num)                   #printa a lista
print('='*30)

num[2] = 3                   #substitui na posição 2 pelo número 3
print(num)
print('='*30)

num.append(7)                #acrescenta o 7 no final
print(num)
print('='*30)

num.sort()                   #coloca em oredem crescente
print(num)
print('='*30)

num.sort(reverse=True)       #coloca em ordem decrescente
print(num)
print('='*30)

print(len(num))              #mostra a quantidade de elemntos há na lista
print('='*30)

num.insert(2, 0)             #insere na posição 2 o elemento 0
print(num)
print('='*30)

num.pop()                    #elimina o último valor
print(num)
print('='*30)

num.pop(2)                   #elimina o elemento na posição 2
print(num)
print('='*30)

num.insert(2, 2)             #insere 2 na posição 2
print(num)
print('='*30)

num.remove(2)                #remove o primeiro 2
print(num)
print('='*30)

if 4 in num:                  #remove o número 4 se ele estiver
    num.remove(4)
else:
    print('Não achei o 4')
print('='*30)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
print('\n','='*30)

for c, v in enumerate(valores):                     #diz a posição e o valor corespondente
    print(f'Na posição {c} encontrei o valor {v}!')
print('='*30)

valores = list()
for cont in range(0, 5):                            #digita uma lista
    valores.append(int(input('Digite um valor: ')))
print(valores)
print('='*30)

a = [2, 3, 4, 7]
b = a                                         #ligação, tudo que faz em uma acontece na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'lista B: {b}')
print('='*30)
a = [2, 3, 4, 7]
b = a[:]                                        #copia de todos os itens não há uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'lista B: {b}')
