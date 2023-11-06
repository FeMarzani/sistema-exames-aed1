# Função para gerar um HTML de exemplo com valores de referência de Glicose, PH e Proteína no sangue.
def relatorio_exames(email_entrada, ph_entrada, proteina_entrada, glicose_entrada):

    # PROCESSANDO AS VARIÁVEIS PARA A ANÁLISE.

    ph_entrada = float(ph_entrada)

    if ph_entrada < 7.0:
        ph_retorno = "pH considerado acido. Isto pode indicar problemas nos rins ou no sistema urinario."
    else:
        if ph_entrada == 7.0:
            ph_retorno = "pH neutro. Ponto 'normal'."
        else:
            ph_retorno = "pH alcalino. Isso pode indicar uma dieta acida, problemas nos rins ou no sistema urinario"

    if proteina_entrada == "Ausente" or proteina_entrada == "ausente":
        proteina_retorno = "Nao detectou-se proteina na urina. Situaçao normal."
    else:
        if proteina_entrada == "Tracos" or proteina_entrada == "tracos":
            proteina_retorno = "Pequena quantidade detectada, mas ainda dentro dos limites normais."
        else:
            proteina_retorno = "Quantidade significativa detectada. Sinal de problemas renais ou outras condicoes."

    if glicose_entrada == "Ausente" or glicose_entrada == "ausente":
        glicose_retorno = "Normal. Nao detectado."
    else:
        if glicose_entrada == "Tracos" or glicose_entrada == "tracos":
            glicose_retorno = "Pequena quantidade. Considerdo anormal e sugere problemas como diabete."
        else:
            glicose_retorno = "Quantidade significativa. Sinal de diabetes descontrolado."

    # ABRINDO ARQUIVO HTML DE RELATORIO
    with open('relatorio_exames.html', 'w') as relatorio_exames:

        # Escrevendo estrutura básica do HTML
        relatorio_exames.write('<!DOCTYPE html>\n')
        relatorio_exames.write('<html lang="en">\n')
        relatorio_exames.write('<head>\n')
        relatorio_exames.write('<meta charset="UTF-8">\n')
        relatorio_exames.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        relatorio_exames.write('<title>Relatório Exames</title>')
        relatorio_exames.write('</head>\n')
        relatorio_exames.write('<body>\n')
        relatorio_exames.write('<table border="1">')
        relatorio_exames.write(f'<caption>Relatorio de Saude Urinario do {email_entrada} </caption>\n')
    
        relatorio_exames.write('<tr>')
        relatorio_exames.write(f'<td>pH do Paciente: {ph_entrada}</td>')
        relatorio_exames.write(f'<td>Valor de Referencia: 4,5 a 8,0</td>')
        relatorio_exames.write(f'<td>Analise: {ph_retorno}</td>')
        relatorio_exames.write('</tr>')

        relatorio_exames.write('<tr>')
        relatorio_exames.write(f'<td>Proteina do Paciente: {proteina_entrada}</td>')
        relatorio_exames.write(f'<td>Valor de Referencia: Ausente ou Tracos</td>')
        relatorio_exames.write(f'<td>Analise: {proteina_retorno}</td>')
        relatorio_exames.write('</tr>')

        relatorio_exames.write('<tr>')
        relatorio_exames.write(f'<td>Glicose do Paciente: {proteina_entrada}</td>')
        relatorio_exames.write(f'<td>Valor de Referencia: Ausente ou Tracos</td>')
        relatorio_exames.write(f'<td>Analise: {glicose_retorno}</td>')
        relatorio_exames.write('</tr>')

        relatorio_exames.write(f'</table>\n')
        relatorio_exames.write(f'</body>\n')
        relatorio_exames.write(f'</html>')

        relatorio_exames.close()