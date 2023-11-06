# Função clique exames para verificar o clique na de cadastro de exames.
def clique_paciente_exames(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return "voltar"
        else:
            if x >= 540 and x <= 704 and y >= 541 and y <= 600:
                return "enviar_exame"