from graphics import *
from inicial import *

clique = inicial()
print(clique)

def login():

    # Importando arquivo csv
    dados = open("src/csv/dados.csv", "a+")
    
    # Lendo as linhas desse arquivo
    linhas = dados.readlines()

    # Retirando o cabeçalho
    linhas = linhas[1:]

    # Abrindo uma janela nova com os mesmos parâmetros
    janela = GraphWin("Plataforma de Exames - Inicial", 800,600)

    # Criando um Retangulo para "Bordalizar" a tela a fim de design.
    retangulo = Rectangle(Point(30,30), Point(770,570))
    retangulo.draw(janela)


    # Adicionando uma imagem logo para a tela inicial
    img = Image(Point(400,200), "assets/medicina.png")
    img.draw(janela)

    if clique == "login":
        # Adicionando texto abaixo da logo
        login = Text(Point(400,270), "Faça o Login")
        login.setSize(15)
        login.setFace('courier')
        login.setStyle('bold')
        login.draw(janela)

        # Adicionando Texto de ID
        texto = Text(Point(330,310), "Digite seu ID: ")
        texto.draw(janela)

        # Abrindo entrada de ID
        id = Entry(Point(430,310), 10)
        id.draw(janela)

        # Adicionando Texto de Senha
        texto = Text(Point(320, 340), "Digite sua senha: ")
        texto.draw(janela)

        # Abrindo entrada de Senha
        senha = Entry(Point(430,340), 10)
        senha.draw(janela)

        # Botão de Enviar os dados
        button = Rectangle(Point(350,370), Point(450,410))
        button.setFill("green")
        button.draw(janela)
        Text(Point(400, 390), "Login").draw(janela)

        while True:

            coordenada = janela.getMouse()
            x = coordenada.getX()
            y = coordenada.getY()
            print(coordenada)

            if x >= 350 and x <= 450 and y >= 370 and y <= 410:
                # Buscando os valores de entrada do usuário

                def login(id_entrada,senha_entrada):
                    
                    # Condicional de verificação de login.
                    for linha in linhas:
                        linha = linha.strip().split(';')
                        if id_entrada == linha[0]:
                            if senha_entrada == linha[1]:
                                print("login feito")
                                return True
                            else:
                                return False
                        else:
                            return False

                id_entrada = str(id.getText())
                senha_entrada = str(senha.getText())

                login_entrada = login(id_entrada, senha_entrada)

                coordenada = 0
                x = 0
                y = 0

                while login_entrada != True:
                    texto = Text(Point(400, 423), "Login inválido. Insira seus dados novamente.")
                    texto.undraw()
                    texto.setStyle('bold')
                    texto.draw(janela)
                    id_entrada = str(id.getText())
                    senha_entrada = str(senha.getText())
                    login_entrada = login(id_entrada,senha_entrada)
                    coordenada = janela.getMouse()
                    x = coordenada.getX()
                    y = coordenada.getY()

                texto.undraw()
                janela.close()
                dados.close()
            else:
                print(janela.getMouse())

    else:
        if clique == "cadastro":
            # Adicionando texto abaixo da logo
            login = Text(Point(400,270), "Cadastre-se")
            login.setSize(15)
            login.setFace('courier')
            login.setStyle('bold')
            login.draw(janela)

        # Adicionando Texto de ID
        texto = Text(Point(310,310), "Cadastre seu ID: ")
        texto.draw(janela)

        # Abrindo entrada de ID
        id = Entry(Point(430,310), 10)
        id.draw(janela)

        # Adicionando Texto de Senha
        texto = Text(Point(310, 340), "Cadastre sua senha: ")
        texto.draw(janela)

        # Abrindo entrada de Senha
        senha = Entry(Point(430,340), 10)
        senha.draw(janela)

        # Botão de Enviar os dados
        button = Rectangle(Point(350,370), Point(450,410))
        button.setFill("green")
        button.draw(janela)
        Text(Point(400, 390), "Cadastro").draw(janela)

        while True:

            coordenada = janela.getMouse()
            x = coordenada.getX()
            y = coordenada.getY()
            print(coordenada)

            if x >= 350 and x <= 450 and y >= 370 and y <= 410:
                # Buscando os valores de entrada do usuário e cadastrando

                id_entrada = str(id.getText())
                senha_entrada = str(senha.getText())

                minhastring = id_entrada + ';' + senha_entrada + '\n'
                dados.write(minhastring)

                for timer in range(100):
                    texto = Text(Point(400, 423), "Cadastro realizado")
                    texto2 = Text(Point(400, 443), "Em alguns segundos o login será feito automaticamente")
                    texto.draw(janela)
                    texto2.draw(janela)

                janela.close()
                dados.close()
            else:
                print(janela.getMouse())

login()