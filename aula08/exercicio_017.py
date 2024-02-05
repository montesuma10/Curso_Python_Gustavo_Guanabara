from math import hypot
cat1 = float(input('Digite o primeiro cateto: '))
cat2 = float(input('Digite o segundo cateto: '))

hip = hypot(cat1, cat2)

print(f'A hipotenusa de um triangulo que tem os catetos {cat1} e {cat2} é {hip:.2f}')