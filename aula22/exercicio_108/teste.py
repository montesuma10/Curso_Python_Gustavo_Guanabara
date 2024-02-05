import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))} ')
print(f'A dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))} ')
print(f'Aumentando 10% o {moeda.moeda(p)} em {moeda.moeda(moeda.aumentar(p, 10))} ')
print(f'Diminuindo 10% o {moeda.moeda(p)} em {moeda.moeda(moeda.diminuir(p, 10))} ')