import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)} ')
print(f'A dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)} ')
print(f'Aumentando 10% o {moeda.moeda(p)} em {moeda.aumentar(p, 10, True)} ')
print(f'Diminuindo 13% o {moeda.moeda(p)} em {moeda.diminuir(p, 13, True)} ')