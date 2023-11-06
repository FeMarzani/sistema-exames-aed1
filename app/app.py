import time

from utils.graphics                 import *
from utils.desenhar_janela          import *
from utils.apagar_objetos           import apagar_objetos
from utils.coordenada_inicial       import *
from utils.clique_login             import *
from utils.clique_cadastro          import clique_cadastro
from utils.clique_paciente_logado   import clique_paciente_logado
from utils.clique_doutor_logado     import clique_doutor_logado
from utils.consultar_exames         import consultar_exames
from utils.clique_paciente_exames   import clique_paciente_exames
from utils.clique_opcao_exame       import clique_opcao_exames
from utils.relatorio                import relatorio_exames

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

                    clique = clique_inicial(janela)
                else:
                    if clique == "cadastrar_exames":
                        sessao = ""
                        while sessao != "exit":
                            apagar_objetos(desenhados)

                            cadastrar_exame = Image(Point(400,300), "assets/cadastrar_exame.png")
                            cadastrar_exame.draw(janela)
                            desenhados.append(cadastrar_exame)

                            # CRIANDO CAMPOS PARA A ENTRADA DE INFORMAÇÕES DOS EXAMES.

                            # VOLUME
                            volume = Entry(Point(165, 240), 15)
                            volume.draw(janela)
                            desenhados.append(volume)

                            # COR
                            cor = Entry(Point(165, 311), 15)
                            cor.draw(janela)
                            desenhados.append(cor)

                            # ASPECTO
                            aspecto = Entry(Point(165, 387), 15)
                            aspecto.draw(janela)
                            desenhados.append(aspecto)

                            # pH
                            ph = Entry(Point(165, 460), 15)
                            ph.draw(janela)
                            desenhados.append(ph)

                            # DENSIDADE
                            densidade = Entry(Point(165, 533), 15)
                            densidade.draw(janela)
                            desenhados.append(densidade)

                            # PROTEÍNA
                            proteina = Entry(Point(420,238), 15)
                            proteina.draw(janela)
                            desenhados.append(proteina)

                            # GLICOSE
                            glicose = Entry(Point(420,316), 15)
                            glicose.draw(janela)
                            desenhados.append(glicose)

                            # LEUCÓCITOS
                            leucocitos = Entry(Point(435,386), 15)
                            leucocitos.draw(janela)
                            desenhados.append(leucocitos)

                            # CORPOS CETÔNICOS
                            corpos = Entry(Point(465,462), 10)
                            corpos.draw(janela)
                            desenhados.append(corpos)

                            # HEMOGLOBINA
                            hemoglobina = Entry(Point(440,536), 10)
                            hemoglobina.draw(janela)
                            desenhados.append(hemoglobina)

                            # BILIRRUBINA
                            bilirrubina = Entry(Point(715,240), 10)
                            bilirrubina.draw(janela)
                            desenhados.append(bilirrubina)

                            # UROBILINOGÊNIO
                            urobilinogenio = Entry(Point(715,315), 10)
                            urobilinogenio.draw(janela)
                            desenhados.append(urobilinogenio)

                            # NITRITO
                            nitrito = Entry(Point(715,390), 10)
                            nitrito.draw(janela)
                            desenhados.append(nitrito)

                            # DATA DO EXAME
                            data = Entry(Point(715,462), 7)
                            data.draw(janela)
                            desenhados.append(data)

                            clique = clique_paciente_exames(janela)
                            
                            if clique == "voltar":
                                apagar_objetos(desenhados)
                                sessao = "exit"

                                desenhados.append(inicial)
                                inicial.draw(janela)

                                clique = clique_inicial(janela)
                            else:
                                if clique == "enviar_exame":

                                    # Pegando os textos das entradas de dados para variáveis de sessão.
                                    volume_entrada = str(volume.getText())
                                    print(volume_entrada)
                                    cor_entrada = str(cor.getText())
                                    aspecto_entrada = str(aspecto.getText())
                                    ph_entrada = str(ph.getText())
                                    densidade_entrada = str(densidade.getText())
                                    proteina_entrada = str(proteina.getText())
                                    glicose_entrada = str(glicose.getText())
                                    leucocitos_entrada = str(leucocitos.getText())
                                    corpos_entrada = str(corpos.getText())
                                    hemoglobina_entrada = str(hemoglobina.getText())
                                    bilirrubina_entrada = str(bilirrubina.getText())
                                    urobilinogenio_entrada = str(urobilinogenio.getText())
                                    nitrito_entrada = str(nitrito.getText())
                                    data_entrada = str(data.getText())

                                    apagar_objetos(desenhados)

                                    opcao_exame = Image(Point(400,300), "assets/opcao_exame.png")
                                    opcao_exame.draw(janela)
                                    desenhados.append(opcao_exame)

                                    # Adicionando função para verificar clique na tela de opção exame.
                                    clique = clique_opcao_exames(janela)

                                    if clique == "voltar":
                                        apagar_objetos(desenhados)
                                        sessao = "exit"

                                        desenhados.append(inicial)
                                        inicial.draw(janela)

                                        clique = clique_inicial(janela)
                                    else:
                                        if clique == "editar_exame":
                                            apagar_objetos(desenhados)
                                        else:
                                            if clique == "gerar_relatorio":

                                                # Abrindo CSV para salvar o exame.
                                                paciente_exames = open("csv/paciente_exames.csv", "a+")

                                                # Abrindo uma string de cadastro para ser a mensagem que será salva no CSV de exames
                                                # E que também será utilizada ao realizar o relatório.

                                                string_exame = email_entrada + ';' + volume_entrada + ';' + cor_entrada + ';' + aspecto_entrada + ';' + ph_entrada + ';' + densidade_entrada + ';' + proteina_entrada + ';' + glicose_entrada + ';' + leucocitos_entrada + ';' + corpos_entrada + ';' + hemoglobina_entrada + ';' + bilirrubina_entrada + ';' + urobilinogenio_entrada + ';' + nitrito_entrada + ';' + data_entrada + "\n"

                                                # Escrevendo o exame no CSV.
                                                paciente_exames.write(string_exame)
                                                paciente_exames.close()
                                                print("SALVO NO CSV")

                                                # Gerando HTML
                                                relatorio_exames(email_entrada, ph_entrada, proteina_entrada, glicose_entrada)

                                                # Fechando sessão para sair do while.
                                                sessao = "exit"
                                                janela.close()

                                                # Código para gerar o relatório HTML.

                    else:
                        if clique == "consultar_exames":

                            email_sessao = email_entrada
                            consultar_exames(email_sessao)
                            print("Arquivo de Consulta de Exames Gerado com Sucesso. Sistema retornando a tela inicial!")

                            apagar_objetos(desenhados)

                            desenhados.append(inicial)
                            inicial.draw(janela)
                            clique = clique_inicial(janela)
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
