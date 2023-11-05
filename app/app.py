import time

from utils.graphics                 import *
from utils.desenhar_janela          import *
from utils.apagar_objetos           import apagar_objetos
from utils.coordenada_inicial       import *
from utils.clique_login             import *
from utils.clique_cadastro          import clique_cadastro
from utils.clique_paciente_logado   import clique_paciente_logado
from utils.clique_doutor_logado     import clique_doutor_logado

def aplicacao():

    desenhados = []

    # Importando imagem da tela inicial do nosso sistema.
    inicial = Image(Point(400,300), "assets/tela_inicial.png")
    desenhados.append(inicial)
   
    # Desenhando a janela com base na função e utilizando a imagem de tela inicial para usar de base.
    janela = desenhar_janela()
    inicial.draw(janela)

    status = ""
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

            # Desenhando os campos de entrada de dados para o login.

            # EMAIL
            email = Entry(Point(203, 165), 30)
            email.draw(janela)
            desenhados.append(email)

            # SENHA
            senha = Entry(Point(203, 277), 30)
            senha.draw(janela)
            desenhados.append(senha)

            # Verificando clique para saber se o usuário clicou no login, login como médico ou voltar.
            clique_log = clique_login(janela)
            if clique_log == "voltar":
                apagar_objetos(desenhados)

                desenhados.append(inicial)
                inicial.draw(janela)

                clique = clique_inicial(janela)
            else:
                if clique_log == "entrar_paciente":
                    
                    status = "espera"
                    while status == "espera" and clique != "voltar":

                        # ABRINDO CSV DOS DADOS PARA VERIFICAÇÃO
                        login_paciente = open("csv/login_paciente.csv")

                        # Lendo as linhas desse arquivo
                        linhas = login_paciente.readlines()
                        print(linhas)

                        # Pegando email e senha
                        email_entrada = str(email.getText())
                        senha_entrada = str(senha.getText())

                        # Criando uma condicional verificadora.
                        for linha in linhas:
                            linha = linha.strip().split(';')
                            print(linha, linha[1], linha)
                            if email_entrada == linha[1] and senha_entrada == linha[2]:
                                print("SIM")
                                status = "paciente_logado"
                                break
                            else:
                                print("NÃO")
                        
                        if status == "paciente_logado":
                            print("LOGIN REALIZADO")
                            login_paciente.close()
                            status = "paciente_logado"
                        else:
                            print("NÃO REALIZADO O LOGIN, ACESSO INVÁLIDO")
                            clique = clique_login(janela)
                else:
                    if clique_log == "entrar_medico":
                        
                        status = "espera"
                        while status == "espera" and clique != "voltar":

                            # Abrindo CSV dos dados de médicos para a verificação.
                            login_medico = open("csv/login_medico.csv")

                            # Lendo as linhas desse CSV
                            linhas = login_medico.readlines()
                            print(linhas)

                            # Pegando email e senha.
                            email_entrada = str(email.getText())
                            senha_entrada = str(senha.getText())

                            # Colocando condicional verificadora.
                            for linha in linhas:
                                linha = linha.strip().split(';')
                                print(linha, linha[1], linha[2])
                                if email_entrada == linha[1] and senha_entrada == linha[2]:
                                    print("HÁ UM DOUTOR COM ESSES DADOS. LOGIN REALIZADO.")
                                    status = "doutor_logado"
                                    break
                                else:
                                    print("NÃO")

                            if status == "doutor_logado":
                                print("LOGIN COMO DOUTOR REALIZADO.")
                                login_medico.close()
                                status = "doutor_logado"
                            else:
                                print("NÃO REALIZADO O LOGIN. ACESSO PARA DOUTOR INVÁLIDO")
                                clique = clique_login(janela)




        else:
            if clique == "cadastro":

                # Apagando objetos da tela.
                apagar_objetos(desenhados)

                # Desenhando o design da tela de login
                cadastro = Image(Point(400,300), "assets/cadastro.png")
                cadastro.draw(janela)
                desenhados.append(cadastro)

                # Abrindo campo de entrada de dados de cadastro.
                ## NOME
                nome = Entry(Point(203,165), 30)
                nome.draw(janela)
                desenhados.append(nome)

                ## EMAIL
                email = Entry(Point(203,285), 30)
                email.draw(janela)
                desenhados.append(email)

                ## SENHA
                senha = Entry(Point(203, 405), 30)
                senha.draw(janela)
                desenhados.append(senha)

                # Verificando clique para saber se o usuário clicou no login, login como médico ou voltar.
                clique = clique_cadastro(janela)
                if clique == "voltar":
                    apagar_objetos(desenhados)

                    desenhados.append(inicial)
                    inicial.draw(janela)

                    clique = clique_inicial(janela)
                else:
                    if clique == "login_cadastro":
                        print("CADASTRO FEITO, LOGIN AUTOMÁTICO REALIZADO.")

                        # ABRINDO CSV DE CADASTRO DOS DADOS PARA INSERIR O PACIENTE NOVO
                        login_paciente = open("csv/login_paciente.csv", "a+")

                        # Pegando as entradas do usuário (nome, email e senha)
                        nome_entrada = str(nome.getText())
                        email_entrada = str(email.getText())
                        senha_entrada = str(senha.getText())

                        # Abrindo uma string de cadastro para ser a mensagem que será escrita no csv.
                        string_cadastro = nome_entrada + ";" + email_entrada + ";" + senha_entrada + "\n"

                        # Escrevendo o novo cadastro no CSV.
                        login_paciente.write(string_cadastro)

                        # Mostrando mensagem ao usuário.
                        texto1 = Text(Point(192, 540), "Cadastro realizado")
                        texto2 = Text(Point(192, 555), "O login será feito automaticamente")
                        texto1.draw(janela)
                        texto2.draw(janela)
                        desenhados.append(texto1)
                        desenhados.append(texto2)

                        # Abrindo um timer para mostrar uma mensagem para o usuário. O login será feito automaticamente.
                        inicio = time.time()

                        # Aguardando a duração especificada.
                        while time.time() - inicio < 3:
                            pass

                        status = "paciente_logado"
        

        if status == "paciente_logado":

                apagar_objetos(desenhados)

                # Desenhando o design da tela de bem vindo paciente
                bem_vindo = Image(Point(400,300), "assets/bem_vindo_paciente.png")
                bem_vindo.draw(janela)
                desenhados.append(bem_vindo)

                clique = clique_paciente_logado(janela)
                if clique == "voltar":
                    apagar_objetos(desenhados)

                    desenhados.append(inicial)
                    inicial.draw(janela)

                    clique = clique_inicial
        else:
            if status == "doutor_logado":

                apagar_objetos(desenhados)

                # Desenhando o design da tela de bem vindo doutor
                bem_vindo_doutor = Image(Point(400,300), "assets/bem_vindo_paciente.png")
                bem_vindo_doutor.draw(janela)
                desenhados.append(bem_vindo_doutor)

                clique = clique_doutor_logado(janela)
                if clique == "voltar":
                    apagar_objetos(desenhados)

                    desenhados.append(inicial)
                    inicial.draw(janela)

                    clique = clique_inicial
                # COLOCAR AQUI A FUNÇÃO DE CLIQUE PARA O DOUTOR. E CÓDIGO RESTANTE PARA ELE







aplicacao()
