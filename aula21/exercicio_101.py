def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade <= 17:
        return f'Com {idade} anos: VOTO É OPCIONAL'
    elif 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO É OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO É OPCIONAL'

nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))

