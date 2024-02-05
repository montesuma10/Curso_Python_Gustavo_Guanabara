dias = int(input('Digite quantos dias voçê ficou com o carro: '))
quilometros = float(input('Digite quantos quilometros voçê percorreu: '))

total = (dias*60) + (quilometros*0.15)

print(f'O total a pagar pelos {dias} dias e pelos {quilometros}Km percorrido é de R$:{total} ')