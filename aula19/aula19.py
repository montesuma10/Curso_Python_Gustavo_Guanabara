
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
'''
print(pessoas)                   #printa dados do dicionario
print(pessoas['nome'])           #printa o nome gustavo
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #printa nome e idade
print(pessoas.keys()) #printa as chaves
print(pessoas.values()) #printa os valores
print(pessoas.items()) #printa os keys e valores
print('='*60)

for k in pessoas.keys():
    print(k)
print('='*60)

for k in pessoas.values():
    print(k)
print('='*60)

for k in pessoas.items():
    print(k)
print('='*60)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*60)

del pessoas['sexo']                 #apaga o sexo
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*60)

pessoas['nome'] = 'leandro'            #substitui gustavo por leandro
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*60)

pessoas['peso'] = 98.5                #adiciona elemento peso
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('='*60)

brasil = []                                         #lista sigla declarada
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}   #dicionarrio estado1
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}        #dicionario estado2
brasil.append(estado1)                              #adicionando estado1
brasil.append(estado2)                              #adicionando estado2
print(estado1)                                      #printa dicionario 1
print(estado2)                                      #printa dicionario 2
print(brasil)                                       #printa dicionario 1 e 2
print(brasil[0])                                    #printa primeiro dicionario
print(brasil[1])                                    #printa segundo dicionario
print(brasil[1]['sigla'])                           #sigla do estado 2(SP)
print('='*60)
'''
estado = dict()                                       #fatiamento com copia
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}/', end='')
    print()
