lanche = 'Hamburguer', 'suco', 'Pizza', 'Pudim'
for comida in lanche:                                     #printa todos elementos
    print(f'Eu vou comer {comida}')
print('='*40)
for cont in range (0, len(lanche)):                       #printa a numeração dos elementos
    print(cont)
print('='*40)
for cont in range (0, len(lanche)):                       #printa todos elementos
    print(f'Eu vou comer {lanche[cont]}')
print('='*40)
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  #printa todos elementos com sua respectiva posição
print('='*40)
for pos, comida in enumerate (lanche):                       #printa todos elementos com sua respectiva posição
    print(f'Eu vou comer {comida} na posição {pos}')
print('='*40)
print(sorted(lanche))                                        #mostra lanche em ordem alfabética
print('='*40)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[-1])
print(lanche[-2])
print(lanche[-3])
print(lanche[-4])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print('='*40)
a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a           #ATENÇÃO!!! a+ b é diferente de b + a
print(a)            #printa a
print(b)            #print b
print(c)            #print c
print(len(c))       #printa numero de elementos de c
print(c.count(5))   #conta quantas vezes aparece 5 em c
print(c.index(8))   #printa a posição que está o número 8
print(c.index(5))   #printa a posição que está o numero 5
print(c.index(5, 1))#printa a posição que está o numero 5 a partir da posição 1
print('='*40)
pessoa = 'Gustavo', 39, 'M', 99.88
#del(pessoa) deleta a tubla toda
print(pessoa)