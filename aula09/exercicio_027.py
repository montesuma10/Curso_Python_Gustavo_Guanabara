def nome_completo(nome):
    print('Muito prazer em te conhecer!')
    print(f'Seu primeiro nome é: {dividido[0]}')
    print(f'Seu último nome é: {dividido[len(dividido)-1]}')

nome = str(input('Qual o seu nome? ')).strip()
dividido = nome.split()
nome_completo(nome)