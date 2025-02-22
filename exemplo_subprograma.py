def get_nome():
    nome_usuario = input("Entre com seu nome: ")
    return nome_usuario

def print_mensagem(nome_usuario):
        print("Olá Jovem Padawan", nome_usuario)

def main():
            nome_usuario = get_nome()
            print_mensagem(nome_usuario)
main()

