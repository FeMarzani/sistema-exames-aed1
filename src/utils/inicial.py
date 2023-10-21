# Importando o graphics
from janela import desenhar_janela
from apagar_objetos import apagar_objetos
from graphics import *

def inicial():

    # Desenhando a janela com base na função 
    janela = desenhar_janela()

    desenhados = []

    # Criando um Retangulo para "Bordalizar" a tela a fim de design.
    retangulo1 = Rectangle(Point(30,30), Point(770,570))
    retangulo1.draw(janela)
    desenhados.append(retangulo1)


    # Adicionando uma imagem logo para a tela inicial
    img1 = Image(Point(400,200), "assets/medicina.png")
    img1.draw(janela)
    desenhados.append(img1)

    # Adicionando texto abaixo da logo
    login = Text(Point(400,270), "Plataforma de Exames Médicos")
    login.setSize(15)
    login.setFace('courier')
    login.setStyle('bold')
    login.draw(janela)
    desenhados.append(login)
    
    # Adicionando botões para Login e Criação de Conta

    # Botão de Login
    button1 = Rectangle(Point(350,300), Point(450,340))
    button1.setFill("green")
    button1.draw(janela)
    botao1 = Text(Point(400, 320), "Login")
    botao1.setStyle('bold')
    botao1.setFace('courier')
    botao1.draw(janela)
    desenhados.append(button1)
    desenhados.append(botao1)

    # Botão de Cadastro
    button2 = Rectangle(Point(350,350), Point(450,390))
    button2.setFill("red")
    button2.draw(janela)
    botao2 = Text(Point(400, 370), "Cadastro")
    botao2.setStyle('bold')
    botao2.setFace('courier')
    botao2.draw(janela)
    desenhados.append(button2)
    desenhados.append(botao2)

    # Botão de login como médico
    button3 = Rectangle(Point(305,400), Point(495,480))
    button3.setFill('aqua')
    button3.draw(janela)
    botao3 = Text(Point(400,440), "Login como Médico")
    botao3.setStyle('bold')
    botao3.setFace('courier')
    botao3.draw(janela)
    desenhados.append(button3)
    desenhados.append(botao3)

    # Criando uma condicional para verificar onde foi o clique do usuário.

    # Definindo variáveis para o funcionamento da condicional
    clique = None

    # Enquanto for verdadeiro, a janela manterá aberta lendo os cliques do usuário.
    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Se o usuário clicar na posição y e x de algum dos objetos a janela se fechará.
        if y >= 300 and y <= 340 and x >= 350 and x <= 450:
            clique = "login"
            apagar_objetos(desenhados)
            return clique
        else:
            if y >= 350 and y <= 390 and x >= 350 and x <= 450:
                clique = "cadastro"
                apagar_objetos(desenhados)
                return clique
            else:
                if y >= 400 and y <= 480 and x >= 305 and x <= 495:
                    clique = "medico"
                    apagar_objetos(desenhados)
                    return clique