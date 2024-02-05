print('-' * 30)
print('  LOJA SUPER BARATÃO')
print('-' * 30)
total = 0
maismil = 0
quant = 0
precobarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço R$: '))
    quant = quant + 1
    total = total + preco
    if preco > 1000:
        maismil = maismil + 1
    if quant == 1 or preco < menor:
        menor = preco
        precobarato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('Conta Finalizada:')
print(f'O total da compra foi R$ {total}')
print(f'Temos {maismil} produtos custando mais de R$ 1000.00')
print(f'Entre os {quant} produtos comprados, o de menor valor é {precobarato}, que custa R$ {menor}')