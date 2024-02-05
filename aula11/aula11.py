#\033[mstyl; (texto)cor texto, (back)cor fundom
#\033[0;33;44m         exemplo
#0 - sem nada                            codigos para estilo
#1 - bold(negrito)                       codigos para estilo
#4 - sunderlie(sublinhado)               codigos para estilo
#7 - negative(inverte as configurações)  codigos para estilo

#30 - texto - branco -       back - 40   codigos para cores
#31 - texto - vermelho -     back - 41   codigos para cores
#32 - texto - verde -        back - 42   codigos para cores
#33 - texto - amarelo -      back - 43   codigos para cores
#34 - texto - azul -         back - 44   codigos para cores
#35 - texto - lilás -        back - 45   codigos para cores
#36 - texto - azul piscina - back - 46   codigos para cores
#37 - texto - cinza -        back - 47   codigos para cores
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;m'}
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')