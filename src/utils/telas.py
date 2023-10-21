from graphics import *
from login_cadastro import login
from janela import desenhar_janela
from apagar_objetos import apagar_objetos

log = login()
print(log)

janela = desenhar_janela()
janela.getMouse()