dados = open("src/csv/dados.csv")
linhas = dados.readlines()

linhas = linhas[1:]
login = 0
quantidade = 0 

while login != True:
    for linha in linhas:
        linha = linha.strip().split(';')
        quantidade += 1
        if id_entrada == linha[0]:
            if senha_entrada == linha[1]:
                print("login feito")
                login = True
                break
            else:
                print("senha invalida")
        else:
            print("id invalido")
        

dados.close()