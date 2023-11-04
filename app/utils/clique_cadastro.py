# Função clique inicial para verificar o clique na tela inicial.
def clique_cadastro(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return "voltar"
        else:
            if x >= 92 and x <= 296 and y >= 447 and y <= 504:
                return "entrar_paciente"