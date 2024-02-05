try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except:
    print('Erro encontrado :(')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muioto obrigado!')

print('='*60)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muioto obrigado!')

print('='*60)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir número por 0.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muioto obrigado!')