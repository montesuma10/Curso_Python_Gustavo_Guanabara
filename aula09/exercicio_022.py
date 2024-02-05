def analisando_nome(nome):
    print('Analisando o seu nome...')
    print(f'Seu nome em maiusculo é {nome.upper()}')
    print(f'seu nome em minúsculo é {nome.lower()}')
    print(f'Seu nome tem ao todo {qtd_letras} caracteres')
    print(f'Seu primeiro nome é {dividido[0]}')
    print(f'Seu primeiro nome tem {len(dividido[0])} letras')


nome = str(input('Digite seu nome completo: ')).strip()
qtd_letras = int(len(nome) - nome.count(" "))
dividido = nome.split()
analisando_nome(nome)