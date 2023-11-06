# Função clique doutor logado para verificar o clique na tela de bem vindo do doutor.
def clique_doutor_logado(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return 'voltar'
        else:
            if x >= 93 and x <= 296 and y >= 242 and y <= 323:
                return 'lista_pacientes' # Gerar um relatório HTML contendo toda a lista de pacientes (nome, email apenas)
            else:
                if x >= 93 and x <= 296 and y >= 340 and y <= 417:
                    return 'pesquisar_pacientes' # Entrada de email