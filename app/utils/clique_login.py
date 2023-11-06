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
            # Se clicar aqui, ele retornara uma variável para entrar na sessão de login como paciente.
            if x >= 93 and x <= 296 and y >= 327 and y <= 383:
                return "entrar_paciente"
            else:
                # Se clicar aqui, ele retornara uma variável para entrar na sessão de login como médico.
                if x >= 93 and x <= 296 and y >= 424 and y <= 503:
                    return "entrar_medico"
