estoque = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100]
produtos = ["coca cola" , "pepsi" , "guarana", "skol" , "brahma", "agua" , "del vale", "red bull", "doly", "fanta", "sprite", "sukita", "pepsi"]
nivel_minimo = 100
for i,qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(produtos [i], qtde)

