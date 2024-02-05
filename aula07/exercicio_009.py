num = int(input('Digite um número: '))
print(f'A tabuada de {num}!')

for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
    i=i+1

