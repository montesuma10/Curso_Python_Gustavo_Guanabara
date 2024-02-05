
frase = 'Curso em Vídeo Python'
print(frase)                               #exibe a frase
print(frase[9])                            #mostra o elemento na posição 9
print(frase[9:13])                         #mostra o elemento da posição 9 até a 13
print(frase[9:21])                         #mostra o elemento da posição 9 até a 21
print(frase[9:21:2])                       #mostra o elemento da posição 9 até a 21 pulando de 2 em 2
print(frase[:5])                           #mostra do elemnto 0 até a 5
print(frase[15:])                          #mostra do elemnto 15 até a último
print(frase[9::3])                         #mostra do elemnto a partir do 9 até o último pulando de 3 em 3
print(len(frase))                          #conta a quantidade de  elementos
print(frase.count('o'))                    #conta quantas vezes aparece a letra 'o'
print(frase.count('o',0,13))               #conta quantas vezes aparece a letra 'o' da posição 0 até a 13
print(frase.find('deo'))                   #se existir a palvra, mostra em qual posição ela inicia 'deo'
print(frase.rfind('deo'))                  #se existir a palvra, mostra em qual posição ela inicia 'deo' a partir da direita
print(frase.find('android'))               #procura a palavra android, se nao achar retorna -1
print('Curso' in frase)                    #procura a palavra curso em frase
print(frase.replace('Python', 'Android'))  #substitui 'python' por 'android'
print(frase.upper())                       #Deixa tudo em maiusculo
print(frase.lower())                       #Deixa tudo em minusculo
print(frase.capitalize())                  #tudo em minusculo, menos a primeira letra da frase
print(frase.title())                       #tudo em minusculo, menos a primeira letra de cada palavra
print(frase.strip())                       #elimina os espaços em branco do inicio e começo da frase
print(frase.rstrip())                      #elimina os espaços em branco da direita
print(frase.lstrip())                      #elimina os espaços em branco da esquerda
print(frase.split())                       #Divide a estring usando os espaços+
print('-'.join(frase))                     #Junta as string colocando um '-' entre elas
