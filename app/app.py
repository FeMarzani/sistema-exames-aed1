
from utils.graphics             import *
from utils.desenhar_janela      import *
from utils.apagar_objetos       import apagar_objetos
from utils.coordenada_inicial   import *
from utils.clique_login         import *
from utils.clique_cadastro      import clique_cadastro

def aplicacao():

    desenhados = []

    # Importando imagem da tela inicial do nosso sistema.
    inicial = Image(Point(400,300), "assets/tela_inicial.png")
    desenhados.append(inicial)
   
    # Desenhando a janela com base na função e utilizando a imagem de tela inicial para usar de base.
    janela = desenhar_janela()
    inicial.draw(janela)

    condicional = "voltar"
    while condicional == "voltar":

        # Utilizando a função de coordenada inicial para verificar onde foi o clique do usuário na tela inicial.
        clique = clique_inicial(janela)

        if clique == "login":

            # Apagando objetos da tela anterior.
            apagar_objetos(desenhados)

            # Desenhando o design da tela de login
            login = Image(Point(400,300), "assets/login.png")
            login.draw(janela)
            desenhados.append(login)

            # Verificando clique para saber se o usuário clicou no login, login como médico ou voltar.
            clique = clique_login(janela)
            if clique == "voltar":
                apagar_objetos(desenhados)

                desenhados.append(inicial)
                inicial.draw(janela)

                clique = clique_inicial(janela)
        else:
            if clique == "cadastro":

                # Apagando objetos da tela.
                apagar_objetos(desenhados)

                # Desenhando o design da tela de login
                cadastro = Image(Point(400,300), "assets/cadastro.png")
                cadastro.draw(janela)
                desenhados.append(cadastro)

                # Verificando clique para saber se o usuário clicou no login, login como médico ou voltar.
                clique = clique_cadastro(janela)
                if clique == "voltar":
                    apagar_objetos(desenhados)

                    desenhados.append(inicial)
                    inicial.draw(janela)

                    clique = clique_inicial(janela)


aplicacao()
