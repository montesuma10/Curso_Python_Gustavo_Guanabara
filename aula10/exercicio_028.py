while True:
    import random
    import time
    computador = random.randint(0, 5)
    num = int(input('Digite um número de 0-5: '))
    print('Processando...')
    time.sleep(3)
    if computador == num:
        print(f'Você venceu, o número era {computador}')
    else:
        print(f'Você perdeu, o número era {computador}')
    print('=*'*20)