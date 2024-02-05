peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = (peso/(altura*altura))
print(f'seu IMC é {imc:.1f}, ', end='')
if imc < 18.5:
    print('você está \033[31mABAIXO\033[m do peso')
elif 18.5 < imc < 25:
    print('você está com o peso \033[32mIDEAL\033[m')
elif 25 < imc < 30:
    print('você está com \033[33mSOBREPESO\033[m do peso')
elif 30 < imc < 40:
    print('você está com \033[35mOBESIDADE!!!\033[m')
elif imc > 40:
    print('você está com \033[4;31mOBESIDADE MORBIDA\033[m')
