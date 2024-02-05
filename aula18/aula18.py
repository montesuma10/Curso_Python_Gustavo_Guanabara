teste = []
teste.append('Gustavo')    #insere gustavo em teste
teste.append(40)           #insere 40 em teste
print(teste)
print('='*40)

galera = []
galera.append(teste[:])      #insere a lista 'teste' em lista galera
print(galera)
print('='*40)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])          #troca os elementos da posição 0 1 um de teste e acescenta na lista galera
print(galera)
print('='*40)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])           #mostra ['joao', galera]
print(galera[0][0])        #mostra  joão
print(galera[2][1])        #mostra 13
print('='*40)

for p in galera:
    print(p, end='')                 #mostra todos
print('\n')
print('=' * 40)

for p in galera:
    print(p[1], end=' , ')           #mostra todos  intens 1
print('\n')
print('=' * 40)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('\n')
print('=' * 40)

dado = []                              #digita dados e adiciona em uma lista
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
print(dado)
print('\n')
print('=' * 40)

dado = []                               #digita dados criando uma lista. e marmazena a lista de dados em outra lista
povo = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    povo.append(dado[:])
    dado.clear()
print(povo)
print('\n')
print('=' * 40)

dado2 = []                               #digita dados criando uma lista. e marmazena a lista de dados-
povo2 = []                               #em outra lista e conta os maiores e menores de idade
totmaior = 0
totmenor = 0
for c in range(0, 3):
    dado2.append(str(input('Nome: ')))
    dado2.append(int(input('Idade: ')))
    povo2.append(dado2[:])
    dado2.clear()
for p in povo2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior = totmaior + 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor = totmenor + 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')


