# Função clique inicial para verificar o clique na tela inicial.
def clique_login(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return "voltar"
        else:
            if x >= 93 and x <= 296 and y >= 327 and y <= 383:
                print("ENTRAR COMO PACIENTE")
                return "entrar_paciente"
            else:
                if x >= 93 and x <= 296 and y >= 424 and y <= 503:
                    print("ENTRAR COMO MÉDICO")
                    return "entrar_medico"
