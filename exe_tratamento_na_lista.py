produtos =  ["tv", "celular", "teclado" , "tlabet" , "mouse", "geladeira", "forno"]
item_usuario = input("Qual itens voce deseja remover: ")
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print("O produto {} não existe na lista".format(item_usuario))
