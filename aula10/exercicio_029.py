vel = float(input('Digite a velocidade do carro: '))
mult = (vel-80) * 7

if vel >= 80:
    print(f'Voçê ultrapassou o limite permitido de 80km/h em {vel-80}Km/h, sua multa é de R$ {mult}')
print('Tenha um bom dia, dirija com segurança')
