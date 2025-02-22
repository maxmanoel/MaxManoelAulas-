def get_data():
    nome_usuario = input("Escreva seu nome: ")
    idade_usuario = int(input("Qual a sua idade? "))
    tupla_data = (nome_usuario, idade_usuario)
    return tupla_data

def mensagemgem(nome_usuario, idade_usuario):
    if idade_usuario <= 10:
        print("oi ", nome_usuario)
    else:
            print("ola", nome_usuario)
def main()
    nome_usuario,idade_usuario = get_data()
    mensagemgem(nome_usuario, idade_usuario)
main()