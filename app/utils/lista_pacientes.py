def lista_pacientes():

    # O parâmetro email_sessao será utilizado para verificar
    # qual o usuário da sessão e buscar os seus respectivos dados.

    # Abrindo o arquivo csv.
    login_paciente = open('csv/login_paciente.csv')

        
    # Pegando as linhas do csv.
    linhas = login_paciente.readlines()

    login_paciente.close()

    with open('paciente_lista.html', 'w') as paciente_lista:

        # Escrevendo estrutura básica do HTML
        paciente_lista.write('<!DOCTYPE html>\n')
        paciente_lista.write('<html lang="en">\n')
        paciente_lista.write('<head>\n')
        paciente_lista.write('<meta charset="UTF-8">\n')
        paciente_lista.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        paciente_lista.write('<title>Lista de Pacientes</title>')
        paciente_lista.write('</head>\n')
        paciente_lista.write('<body>\n')
        paciente_lista.write('<table border="1">')
        paciente_lista.write('<tr>')

        for linha in linhas:
            if linha == linhas[0]: #CABEÇALHO
                linha = linha.strip().split(';')
                print(f'LINHA CABEÇALHO {linha}')

                # ADICIONANDO O CABEÇALHO A PARTIR DE UMA CONDICIONAL DE FOR.
                for num in linha:
                    print(num)
                    paciente_lista.write(f'<th>{num}</th>')

                paciente_lista.write(f'</tr>\n')
            else:
                linha = linha.strip().split(';')
                paciente_lista.write('<tr>')

                # ADICIONANDO AS LINHAS A PARTIR DE UMA CONDICIONAL DE FOR.
                for n in linha:
                    paciente_lista.write(f'<td>{n}</td>')

                paciente_lista.write(f'<tr>\n')

        paciente_lista.write(f'</table>\n')
        paciente_lista.write(f'</body>\n')
        paciente_lista.write(f'</html>')

        paciente_lista.close()
