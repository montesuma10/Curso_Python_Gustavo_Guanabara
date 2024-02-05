jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('='*60)
print(jogador)
print('='*60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='*60)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas ')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
