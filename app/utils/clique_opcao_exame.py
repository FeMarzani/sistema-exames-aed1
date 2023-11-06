# Função clique exames para verificar o clique na parte de opção do exame após inserção de informações.
def clique_opcao_exames(janela):

    while True:
        coordenada = janela.getMouse()
        y = int(coordenada.getY())
        x = int(coordenada.getX())

        print(coordenada)

        # Verificando onde foi o clique do usuário. Se foi na área de voltar, ele retornará para a primeira página.
        if x >= 719 and x <= 800 and y >= 542 and y <= 600:
            return "voltar"
        else:
            # Se clicar aqui, ele retornara uma variável para entrar na sessão de geração de relatório, posteriormente à inserção de dados do exame.
            if x >= 93 and x <= 296 and y >= 243 and y <= 298:
                return "gerar_relatorio"
            else:
                if x >= 93 and x <= 296 and y >= 338 and y <= 396:
                    return "editar_exame" # Volta para a tela anterior para reenviar o exame e ler tudo de novo.