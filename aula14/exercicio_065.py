resp = 'S'
quant = 0
soma = 0
media = 0
while resp in'Ss':
    num = int(input('Digite um número: '))
    quant = quant + 1
    soma = soma + num
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/quant
print(f'Você digitou {quant} números e a media foi de {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
