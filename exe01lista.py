lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3= [11,12,13,14,15]
todas_listas = [lista1,lista2,lista3]
print(todas_listas)

produtos= ["tv", "celular", "teclado" , "tlabet"]
print(produtos[1])

produtos= ["tv", "celular", "teclado" , "tlabet"]
vendas = [100 , 1500, 350, 270, 900]
print("As vendas de {} foram de {}" .format(produtos[1], vendas[1]))


produtos= ["tv", "celular", "teclado" , "tlabet"]
i = produtos.index("mouse")
print("O valor de 1 é " ,+ str(i))
print("O produto da posição i é " + str(produtos[i]))

produtos= ["tv", "celular", "teclado" , "tlabet" , "mouse", "geladeira", "forno"]
estoque = [100,150,100,120,70,180,80]

produto = input("Iserir o nome do produto e letra minuscula: ")
if produto in produtos:
    i - produto.index(produto)
    qnt_estoque = estoque [i]
    print(" Temos {} unidades de {} no estoque" .format (qnt_estoque,produto))
else:
    print( " {} nao existe no estoque " .format (produto))

