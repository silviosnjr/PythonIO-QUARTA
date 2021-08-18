arquivo = open("dados/contatos.csv", encoding="latin_1", mode="a+")

arquivo.write("1, Bento José, bento@bento.com.br\n")
arquivo.write("2, Inácio Francisco, inacio@inacio.com.br\n")

arquivo.flush()
arquivo.seek(0)

for linha in arquivo:
    print(linha, end="")