venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apartar enter sem digita nada: ")
vendas = []
#CRIE AQUI O PROGRAMA
while venda != "":
    vendas.append(venda)
    venda = input ("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
    print("Registro Finalizado. As vendas cadastradas foram: {} ".format(vendas))