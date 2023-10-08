# Importando o graphics
from graphics import *

def inicial():

    # Criando a Janela para Inicialização do Sistema
    janela = GraphWin("Plataforma de Exames - Inicial", 800,600)

    # Criando um Retangulo para "Bordalizar" a tela a fim de design.
    retangulo = Rectangle(Point(30,30), Point(770,570))
    retangulo.draw(janela)

    # Modificando cor para estilização
    janela.setBackground('gray')

    # Adicionando uma imagem logo para a tela inicial
    img = Image(Point(400,200), "assets/medicina.png")
    img.draw(janela)

    # Adicionando texto abaixo da logo
    login = Text(Point(400,270), "Plataforma de Exames Médicos")
    login.setSize(15)
    login.setFace('courier')
    login.setStyle('bold')
    login.draw(janela)
    
    # Adicionando botões para Login e Criação de Conta

    # Botão de Login
    button = Rectangle(Point(350,300), Point(450,340))
    button.setFill("green")
    button.draw(janela)
    botao = Text(Point(400, 320), "Login")
    botao.setStyle('bold')
    botao.setFace('courier')
    botao.draw(janela)

    # Botão de Cadastro
    button = Rectangle(Point(350,350), Point(450,390))
    button.setFill("red")
    button.draw(janela)
    botao = Text(Point(400, 370), "Cadastro")
    botao.setStyle('bold')
    botao.setFace('courier')
    botao.draw(janela)

    janela.getMouse()
    janela.close()

inicial()