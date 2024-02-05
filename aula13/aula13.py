for i in range (0, 6): #conta crescente
    print(i)
print('FIM')
#=================================================================
for i in range (6, 0, -1): #conta descrecente
    print(i)
print('FIM')
#==================================================================
for i in range (0, 6, 2): #conta pulando de 2 em 2
    print(i)
print('FIM')
#===================================================================
i = int(input('Digite um número: ')) #conta até o número digitado
for i in range(0, i+1):
    print(i)
print("FIM")
#====================================================================
j = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for i in range(j, f+1, p): #conta do inicio digitado até o final digitado usando o passo digitado.
    print(i)
print('FIM')
#=====================================================================
for c in range(0, 3):
    n = int(input('Digite um número: ')) #pede para digitar 3x
print('FIM')
#=====================================================================
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: ')) #pede para digitar 4X e soma os valores digitados
    s = s + n
print(f'O somatório de todos os valores digitados foi:{s}\nFIM')


