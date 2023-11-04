# Função para apagar_objetos, com o parametro de uma lista de desenhados.
# Esta lista de desenhados vai conter o nome dos objetos desenhados a priori, a partir de um .append com seus nomes.
# Ao chamar a função será utilizado um for que irá percorrer essa lista e apagar os objetos. 

def apagar_objetos(desenhados):
    for objeto in desenhados:
        objeto.undraw()