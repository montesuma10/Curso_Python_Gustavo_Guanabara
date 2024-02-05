dist = float(input('Qual a distância da viagem? '))

if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print(f'a viagem de {dist}Km5 custará R$ {valor}')