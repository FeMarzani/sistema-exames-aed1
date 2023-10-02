# Importando o Graphics
from graphics import *

# Importando o csv de dados de login
dados = open("src/csv/dados.csv","r")
infos = dados.readlines()
dados.close()

# Criando a janela gráfica para o sistema.
janela = GraphWin("Plataforma de Exames - Login", 700,700)

# Criando uma função para verificação de login para abrir o sistema
def login(id, senha):
    for i in range(len(infos)):
        if id in infos[i]:
            if senha in infos[i]:
                return True
            
# Função para criar perguntas e campos
def pergunta_login(text, y, width):
    Text(Point(250, y), text).draw(janela)
    entry = Entry(Point(350, y), width)
    entry.draw(janela)
    return entry

# Criando perguntas e os campos
id_entrada = pergunta_login("Id:",230,15)
senha_entrada = pergunta_login("Senha:",290,15)

# Botão de Enviar
button = Rectangle(Point(250,350), Point(350,380))
button.setFill("green")
button.draw(janela)
Text(Point(300, 365), "Enviar").draw(janela)

janela.getMouse()

# Pegando os valores de input do usuário
id = str(id_entrada.getText())
senha = str(senha_entrada.getText())
login_entrada = login(id,senha)

while login_entrada != True:
    Text(Point(300, 400), "Login inválido").draw(janela)
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
paciente = open("src/csv/paciente.csv","w")
paciente_string = nome + "," + idade + "," + hemoglobina + "," + glicose + "," + colesterol
print(paciente_string)
paciente.write(paciente_string)
paciente.close()

janela.getMouse()
janela.close()