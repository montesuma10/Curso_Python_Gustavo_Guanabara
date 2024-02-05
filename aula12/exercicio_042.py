print('*='*30)
print('Analisador de Triângulo')
print('*='*30)
a = float(input('Primeiro segmento: '))
b = float(input('Sgundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM FORMAR triâgulo! ', end='')
    if a == b == c:
        print('O triângulo é EQUILÁTERO')
    elif a == b != c or a == c != b or b == c != a:
        print('O triângulo é ISÓSCELES')
    else:
        print('O triângulo é ESCALENO')
else:
    print('\033[31mOs segmentos NÃO PODEM FORMAR triângulo!')