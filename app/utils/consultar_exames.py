def consultar_exames(email_sessao):

    # O parâmetro email_sessao será utilizado para verificar
    # qual o usuário da sessão e buscar os seus respectivos dados.

    # Abrindo o arquivo csv.
    paciente_exames = open('csv/paciente_exames.csv')

        
    # Pegando as linhas do csv.
    linhas = paciente_exames.readlines()

    paciente_exames.close()

    with open('consultar_exames.html', 'w') as consultar_exames:

        # Escrevendo estrutura básica do HTML
        consultar_exames.write('<!DOCTYPE html>\n')
        consultar_exames.write('<html lang="en">\n')
        consultar_exames.write('<head>\n')
        consultar_exames.write('<meta charset="UTF-8">\n')
        consultar_exames.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        consultar_exames.write('<title>Consultar Exames</title>')
        consultar_exames.write('</head>\n')
        consultar_exames.write('<body>\n')
        consultar_exames.write('<table border="1">')
        consultar_exames.write('<tr>')

        for linha in linhas:
            if linha == linhas[0]: #CABEÇALHO
                linha = linha.strip().split(';')
                print(f'LINHA CABEÇALHO {linha}')

                # ADICIONANDO O CABEÇALHO A PARTIR DE UMA CONDICIONAL DE FOR.
                for num in linha:
                    print(num)
                    consultar_exames.write(f'<th>{num}</th>')

                consultar_exames.write(f'</tr>\n')
            else:
                linha = linha.strip().split(';')
                if email_sessao == linha[0]:
                    print("É IGUAL")

                    consultar_exames.write('<tr>')

                    # ADICIONANDO AS LINHAS A PARTIR DE UMA CONDICIONAL DE FOR.
                    for n in linha:
                        consultar_exames.write(f'<td>{n}</td>')

                    consultar_exames.write(f'<tr>\n')
                else:
                    pass

        consultar_exames.write(f'</table>\n')
        consultar_exames.write(f'</body>\n')
        consultar_exames.write(f'</html>')

        consultar_exames.close()
