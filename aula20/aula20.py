
def mostralinha():
    print('-' * 60)
    print('     CURSO EM VIDEO     ')
    print('-' * 60)


mostralinha()
print('*'*70)

def mensagem(msg):
    print('-' * 60)
    print(msg)
    print('-' * 60)


mensagem('MONTESUMA')
print('*'*70)

def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
print('*'*70)

def contador(*num):
    print(num)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
print('*'*70)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
print('*'*70)


def soma(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
print('*'*70)

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] = list[pos] * 2
        pos = pos + 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
