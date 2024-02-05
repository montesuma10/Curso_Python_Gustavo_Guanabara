def analisando_frase(frase):
    print('A frase tem:', frase.count('A'),'letra "A"')
    print('A primeira letra "A" se encontra na posição:', frase.find('A')+1)
    print('A última letra "A" se encontra na posição:',frase.rfind('A')+1)



frase = str(input('Digite a frase: ')).upper().strip()
analisando_frase(frase)