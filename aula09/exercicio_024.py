def analisando_cidade_natal(cid):
    print(cid[:5].upper()=='SANTO')


cid = str(input('Em qual cidade voçê nasceu? ')).upper()
analisando_cidade_natal(cid)