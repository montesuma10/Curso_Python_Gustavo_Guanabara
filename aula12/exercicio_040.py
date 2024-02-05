nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media > 7:
    print(f'Sua média foi {media:.1f}, \033[32mPARABÉNS APROVADO!!!\033[m')
elif media > 5 and media < 6.9:
    print(f'Sua média foi {media:.1f}, \033[33mATENÇÃO RECUPERAÇÃO!!!\033[m')
else:
    print(f'Sua média foi {media:.1f}, \033[31mINFELIZMENTE REPROVADO!!!\033[m')