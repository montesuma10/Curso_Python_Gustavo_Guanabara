time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    totp= int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, totp):
        partidas.append(int(input(f'      Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    op = ' '
    op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        print('ERRO! Responda apenas S ou N')
        op = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('='*60)
print(time)
print('='*60)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*60)

while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('='*60)
print('<< VOLTE SEMPRE >>')





