
print('Gerador de P.A.')
print('=*' * 10)
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo = termo + raz
        cont = cont + 1
    print('PAUSA')
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f'Progressão finalizada com {total} termos mostrados')
