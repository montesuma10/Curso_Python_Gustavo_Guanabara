aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A Média do(a) {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
print('='*60)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')