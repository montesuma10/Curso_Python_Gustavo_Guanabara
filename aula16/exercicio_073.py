ltb = ('corinthians', 'palmeiras', 'santos', 'grêmio', 'cruzeiro',
       'flamengo', 'vasco', 'chapecoense', 'atletico', 'botafogo',
       'atletico-PR', 'bahia', 'sao paulo', 'fluminense', 'sport recife',
       'ec vitoria', 'coritiba', 'avaí', 'ponte preta', 'atlético-go')
print('-='*20)
print(f'Lista de times do Brasileirão: {ltb}')
print('-='*20)
print(f'Os 5 primeiros são {ltb[0:5]}')
print('-='*20)
print(f'Os quatro últimos colocados são {ltb[16:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(ltb)} ')
print('-='*20)
print(f'O chapecoense está na {ltb.index("chapecoense")+1}ª')