num = int(input('Digite um númrto inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal')
op = int(input('Sua opção: '))
if op == 1:
    print(f'O {num} convertido para BINÀRIO é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'O {num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'O {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')