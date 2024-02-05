loja = str('lojas guanabara').upper()
print(f'{loja:=^40}')
valor = float(input('Preço da compras: R$ '))
print('FORMA DE PAGAMENTO\n'
      '[1] à vista dinheiro/cheue\n'
      '[2] à vista no cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão')
op = int(input('Qual a opção? '))
if op == 1:
    valor_a_pagar = valor - (valor*0.1)
    print(f'Sua compra terá um desconto de 10%!\nSua compra de R${valor} vai custar R${valor_a_pagar} no final.')
elif op == 2:
    valor_a_pagar = valor - (valor*0.05)
    print(f'Sua compra terá um desconto de 5%!\nSua compra de R${valor} vai custar R${valor_a_pagar} no final.')
elif op == 3:
    valor_a_pagar = valor
    parcela = valor/2
    print(f'Sua compra será parcelada em 2X de R${parcela}\nSua compra de R${valor} vai custar R${valor_a_pagar}.')
elif op == 4:
    num_parcelas = int(input('Digite o número de parcelas:'))
    valor_a_pagar = valor + (valor*0.20)
    parcela = valor_a_pagar/num_parcelas
    print(f'Sua compra será parcelada em {num_parcelas}X de R${parcela:.2f} com acrescimo de 20% de juros!\nSua compra de R${valor} vai custar R${valor_a_pagar} no final.')
else:
    print('Comando inválido, tente novamente!')



