# Função clique inicial para verificar o clique na tela inicial.
def clique_paciente_logado(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return "voltar"
        else:
            if x >= 93 and x <= 296 and y >= 242 and y <= 299:
                print("CONSULTAR EXAME")
                return "consultar_exames" # Gerar um relatório HTML contendo todos os exames dessa sessão de usuário.
            else:
                if x >= 93 and x <= 296 and y >= 338 and y <= 397:
                    print("CADASTRAR EXAME")
                    return "cadastrar_exames"