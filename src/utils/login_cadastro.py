from graphics import *
from inicial import *
from apagar_objetos import apagar_objetos

clique = inicial()
print(clique)

def login():

    # Criando lista para conseguir apagar objetos da tela posteriormente.
    desenhados = []

    # Importando arquivo csv
    dados = open("src/csv/dados.csv")
    
    # Lendo as linhas desse arquivo
    linhas = dados.readlines()

    # Retirando o cabeçalho
    linhas = linhas[1:]

    # Desenhando a janela com base na função 
    janela = desenhar_janela()

    # Criando um Retangulo para "Bordalizar" a tela a fim de design.
    retangulo = Rectangle(Point(30,30), Point(770,570))
    retangulo.draw(janela)
    desenhados.append(retangulo)


    # Adicionando uma imagem logo para a tela inicial
    img = Image(Point(400,200), "assets/medicina.png")
    img.draw(janela)
    desenhados.append(img)

    if clique == "login":
        # Adicionando texto abaixo da logo
        login = Text(Point(400,270), "Faça o Login")
        login.setSize(15)
        login.setFace('courier')
        login.setStyle('bold')
        login.draw(janela)
        desenhados.append(login)

        # Adicionando Texto de ID
        texto = Text(Point(330,310), "Digite seu ID: ")
        texto.draw(janela)
        desenhados.append(texto)

        # Abrindo entrada de ID
        id = Entry(Point(430,310), 10)
        id.draw(janela)
        desenhados.append(id)

        # Adicionando Texto de Senha
        texto2 = Text(Point(320, 340), "Digite sua senha: ")
        texto2.draw(janela)
        desenhados.append(texto2)

        # Abrindo entrada de Senha
        senha = Entry(Point(430,340), 10)
        senha.draw(janela)
        desenhados.append(senha)

        # Botão de Enviar os dados
        button1 = Rectangle(Point(350,370), Point(450,410))
        button1.setFill("green")
        button1.draw(janela)
        desenhados.append(button1)
        texto3 = Text(Point(400, 390), "Login")
        texto3.draw(janela)
        desenhados.append(texto3)

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
                                apagar_objetos(desenhados)
                                return True

                id_entrada = str(id.getText())
                senha_entrada = str(senha.getText())

                login_entrada = login(id_entrada, senha_entrada)
                if login_entrada != True:
                    login_entrada = False

                coordenada = 0
                x = 0
                y = 0

                while login_entrada != True:
                    texto4 = Text(Point(400, 423), "Login inválido. Insira seus dados novamente.")
                    texto4.undraw()
                    texto4.setStyle('bold')
                    texto4.draw(janela)
                    desenhados.append(texto4)
                    id_entrada = str(id.getText())
                    senha_entrada = str(senha.getText())
                    login_entrada = login(id_entrada,senha_entrada)
                    coordenada = janela.getMouse()
                    x = coordenada.getX()
                    y = coordenada.getY()

                apagar_objetos(desenhados)
                dados.close()
                log = "usuario"
                return log
            else:
                print(janela.getMouse())

    else:
        if clique == "medico":
            # Adicionando texto abaixo da logo
            login = Text(Point(400,270), "Olá Doutor(a)!. Realize seu Login")
            login.setSize(15)
            login.setFace('courier')
            login.setStyle('bold')
            login.draw(janela)
            desenhados.append(login)

            # Adicionando Texto de ID
            texto = Text(Point(330,310), "Digite seu ID: ")
            texto.draw(janela)
            desenhados.append(texto)

            # Abrindo entrada de ID
            id = Entry(Point(430,310), 10)
            id.draw(janela)
            desenhados.append(id)

            # Adicionando Texto de Senha
            texto2 = Text(Point(320, 340), "Digite sua senha: ")
            texto2.draw(janela)
            desenhados.append(texto2)

            # Abrindo entrada de Senha
            senha = Entry(Point(430,340), 10)
            senha.draw(janela)
            desenhados.append(senha)

            # Botão de Enviar os dados
            button1 = Rectangle(Point(325,370), Point(475,410))
            button1.setFill("Aqua")
            button1.draw(janela)
            desenhados.append(button1)
            texto3 = Text(Point(400, 390), "Login como Médico")
            texto3.draw(janela)
            desenhados.append(texto3)

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
                                    apagar_objetos(desenhados)
                                    return True

                    id_entrada = str(id.getText())
                    senha_entrada = str(senha.getText())

                    login_entrada = login(id_entrada, senha_entrada)
                    if login_entrada != True:
                        login_entrada = False

                    coordenada = 0
                    x = 0
                    y = 0

                    while login_entrada != True:
                        texto4 = Text(Point(400, 423), "Dados inválidos. Insira seus dados novamente.")
                        texto4.undraw()
                        texto4.setStyle('bold')
                        texto4.draw(janela)
                        desenhados.append(texto4)
                        id_entrada = str(id.getText())
                        senha_entrada = str(senha.getText())
                        login_entrada = login(id_entrada,senha_entrada)
                        coordenada = janela.getMouse()
                        x = coordenada.getX()
                        y = coordenada.getY()

                    apagar_objetos(desenhados)
                    log = "medico"
                    dados.close()
                    return log
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
                desenhados.append(login)

            dados = open("src/csv/dados.csv", "a+")

            # Adicionando Texto de ID
            texto = Text(Point(310,310), "Cadastre seu ID: ")
            texto.draw(janela)
            desenhados.append(texto)

            # Abrindo entrada de ID
            id = Entry(Point(430,310), 10)
            id.draw(janela)
            desenhados.append(id)

            # Adicionando Texto de Senha
            texto1 = Text(Point(310, 340), "Cadastre sua senha: ")
            texto1.draw(janela)
            desenhados.append(texto1)

            # Abrindo entrada de Senha
            senha = Entry(Point(430,340), 10)
            senha.draw(janela)
            desenhados.append(senha)

            # Botão de Enviar os dados
            button = Rectangle(Point(350,370), Point(450,410))
            button.setFill("green")
            button.draw(janela)
            desenhados.append(button)
            texto2 = Text(Point(400, 390), "Cadastro")
            texto2.draw(janela)
            desenhados.append(texto2)

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
                        texto3 = Text(Point(400, 423), "Cadastro realizado")
                        texto4 = Text(Point(400, 443), "Em alguns segundos o login será feito automaticamente")
                        desenhados.append(texto3)
                        desenhados.append(texto4)
                        texto.draw(janela)
                        texto2.draw(janela)


                    apagar_objetos(desenhados)
                    log = "usuario"
                    dados.close()
                    return log
                else:
                    print(janela.getMouse())

login()