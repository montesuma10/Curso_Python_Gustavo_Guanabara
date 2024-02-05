from time import sleep
print('Gerador de P.A.')
print('=*' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo = termo + raz
    cont = cont + 1
    sleep(1)
print('FIM')
sleep(1)