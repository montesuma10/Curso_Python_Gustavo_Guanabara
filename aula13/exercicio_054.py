from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
        print(f'Essa pessoa tem {idade} anos de idade, portanto é MAIOR')
    else:
        totmenor = totmenor + 1
        print(f'Essa pessoa tem {idade} anos de idade, portanto é MENOR')
print('=*'*40)
print(f'Ao todo temos {totmaior} pessoas maior e {totmenor} pessoas menor')