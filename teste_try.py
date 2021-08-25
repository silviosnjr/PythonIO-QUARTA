try :
    with open("dados/contato.csv", encoding="Latin_1") as arquivo :
        for linha in arquivo:
            print(linha)
        #arquivo.write("5, Fulano, fulano@fulano.com.br\n")
        #arquivo.flush()
except FileNotFoundError :
    print("Arquivo não encontrado")
    print("Verifique com o administrador do sistema o nome correto do arquivo")