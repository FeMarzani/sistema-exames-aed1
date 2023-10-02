# Importando o Graphics
from graphics import *

# Importando o csv de dados de login
dados = open("src/csv/dados.csv","r")
infos = dados.readlines()
dados.close()

# Criando a janela gráfica para o sistema.
janela = GraphWin("Plataforma de Exames", 700,700)

# Criando uma função para verificação de login para abrir o sistema
def login(id, senha):
    for i in range(len(infos)):
        if id in infos[i]:
            if senha in infos[i]:
                return True
            
# Função para criar perguntas e campos
def pergunta_entrada(text, y, width):
    Text(Point(250, y), text).draw(janela)
    entry = Entry(Point(350, y), width)
    entry.draw(janela)
    return entry

# Criando perguntas e os campos
id_entrada = pergunta_entrada("Id:",230,15)
senha_entrada = pergunta_entrada("Senha:",290,15)

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