# Importando o Graphics
from utils.graphics import *

# Importando o csv de dados de login
dados = open("src/csv/dados.csv","r+")
linhas = dados.readlines()

cabecalho = linhas[0]
linhas = linhas[1:]

# Criando a janela gráfica para o sistema.
janela = GraphWin("Plataforma de Exames - Login", 700,700)

titulo_login = Text(Point(350, 180), "Tela de Login")
titulo_login.setSize(20)
titulo_login.draw(janela)

# Criando variáveis iniciais para condicional
senha_resultado = ""

# Criando uma função para verificação de login para abrir o sistema
def login(id, senha):
    for linha in linhas:
        id_verdadeiro, senha_verdadeiro = linha.strip().split(',')
        if id == id_verdadeiro:
            if senha == senha_verdadeiro:
                return True
                break
            else:
                senha_resultado = "Senha Errada"
                return False
        else:
            return False
            
# Função para criar perguntas e campos
def pergunta_login(text, y, width):
    Text(Point(250, y), text).draw(janela)
    entry = Entry(Point(350, y), width)
    entry.draw(janela)
    return entry

# Criando perguntas e os campos
id_entrada = pergunta_login("Id:",230,15)
senha_entrada = pergunta_login("Senha:",290,15)

# Botão de Login
button = Rectangle(Point(300,350), Point(400,380))
button.setFill("gray")
button.draw(janela)
Text(Point(350, 365), "Login").draw(janela)

# Botão de Cadastro
button = Rectangle(Point(300,410), Point(400,440))
button.setFill("green")
button.draw(janela)
Text(Point(350, 425), "Cadastro").draw(janela)

janela.getMouse()

# Pegando os valores de input do usuário
id = str(id_entrada.getText())
senha = str(senha_entrada.getText())
login_entrada = login(id,senha)

while login_entrada != True:
    if senha_resultado == "Senha Errada":
        Text(Point(300, 400), "Senha Errada").draw(janela)
        senha = str(senha_entrada.getText())
        login_entrada = login(id,senha)
    else:
        Text(Point(300, 400), "Login inválido. Insira seus dados novamente e clique em cadastrar.").draw(janela)
        id = str(id_entrada.getText())
        senha = str(senha_entrada.getText())
        login_entrada = login(id,senha)


janela.close()
print("LOGIN FEITO")

# Criando uma janela de visualização do paciente para registro de informações de exame de sangue.
janela = GraphWin("Plataforma de Exames - Paciente", 700,700)

def pergunta_paciente(text, y, width):
    Text(Point(250, y), text).draw(janela)
    entry = Entry(Point(350, y), width)
    entry.draw(janela)
    return entry

# Criação das perguntas
nome_paciente = pergunta_paciente("Nome:",200,15)
idade_paciente = pergunta_paciente("Idade:",230,5)
hemoglobina_paciente = pergunta_paciente("Hemoglobina (g/dL):",260,5)
glicose_paciente = pergunta_paciente("Glicose (mg/dL):",290,5)
colesterol_total = pergunta_paciente("Colesterol (mg/dL):",320,5)

# Botão de Enviar os dados
button = Rectangle(Point(250,350), Point(350,380))
button.setFill("green")
button.draw(janela)
Text(Point(300, 365), "Enviar").draw(janela)

nome = nome_paciente.getText()
idade = idade_paciente.getText()
hemoglobina = hemoglobina_paciente.getText()
glicose = glicose_paciente.getText()
colesterol = colesterol_total.getText()

# Importando o csv de dados de paciente para registro
paciente = open("csv/paciente.csv","w")
paciente_string = nome + "," + idade + "," + hemoglobina + "," + glicose + "," + colesterol
print(paciente_string)
paciente.write(paciente_string)
paciente.close()

janela.getMouse()
janela.close()