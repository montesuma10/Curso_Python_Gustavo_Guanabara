def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;21mERRO: \"{entrada}\" Preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
