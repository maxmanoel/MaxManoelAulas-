nome = ["max", "gustavo", "marcos", "vitor"]
telefone = ["991757458", "9196758", "578891"]
bairro = ["boa vista", "comasa", "aventureriro"]


nome_usuario = input("Inserir o seu nome: ")


if nome_usuario in nome:
    i = nome.index(nome_usuario)  
    telefone_usuario = telefone[i]  
    bairro_usuario = bairro[i]  
    print("Nome: {}  Telefone: {}  Bairro: {}".format(nome_usuario, telefone_usuario, bairro_usuario))
else:
    print("{} nome não encontrado.".format(nome_usuario))



