# Função clique inicial para verificar o clique na tela inicial.
def clique_inicial(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        # Verificando onde foi o clique do usuário. Se foi na área do login, ele retornará login.
        if x >= 93 and x <= 243 and y >= 241 and y <= 300:
            return "login"
        else:
            # Se for cadastro, ele retorna cadastro.
            if x >= 93 and x <= 243 and y >= 338 and y <= 396:
                return "cadastro"