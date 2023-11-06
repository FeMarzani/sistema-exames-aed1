<div align="center">
  <img src="app/assets/logo_readme.png" alt="Logo UOL" width="300px" height="240px">
</div>

<div align="center">
  <h1> Sistema de informação para gerenciamento de exames médicos utilizando a Graphics (AED1)</h1>
</div>

<div align="center">
  <p>Equipe por trás do sistema</p>
</div>

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://www.linkedin.com/in/emylly-guimaraes/">
          <img src="https://avatars.githubusercontent.com/u/107193565?v=4" width="100px;" alt="Foto da Emylly Guimarães"/><br>
          <sub><b>Emylly Guimarães</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/felipemarzani/">
          <img src="https://avatars.githubusercontent.com/u/107329291?v=4" width="100px;" alt="Foto do Felipe Marzani da Silva"/><br>
          <sub><b>Felipe Marzani</b></sub>
        </a>
      </td>
    </tr>
  </table>
</div>

### 1. Propósito
Nesse sistema, uma pessoa pode informar dados de exames médicos, sendo, atualmente, dados de exame de urina.
- O médico pode visualizar o exame de qualquer paciente;
- O paciente pode editar os dados de seus exames;
- Cada exame possui uma data, um nome e um valor;
- O sistema gera um relatório HTML com todos os exames de um dado paciente;
- Tanto médico quanto paciente devem ter login/senha registrados em um arquivo CSV;
- Os dados de exame devem ser armazenados em um arquivo CSV.
- O sistema gera um relatório de análise com informações de pH, Glicose e Proteína na urina.


### 2. Como executar

1. Clone este repositório ou baixe o arquivo zip.

    ```bash
    git clone https://github.com/FeMarzani/sistema-exames-aed1
    ```

2. Abra o terminal fora ou dentro do VSCode, entre na pasta app.
    ```bash
    cd app
    ```

3. Execute o arquivo app.py. É possível executar executando da seguinte forma:
    ```bash
    python3 app.py
    ```

### 3. Estrutura de Pastas
- **app**
  - **assets**
    - `...`
  - **csv**
    - `login_medico`
    - `login_paciente`
    - `paciente_exames`
  - **utils**
    - `apagar_objetos`
    - `clique_cadastro`
    - `clique_doutor_logado`
    - `clique_login`
    - `clique_opcao_exame`
    - `clique_paciente_exame`
    - `clique_paciente_logado`
    - `consultar_exames`
    - `coordenada_inicial`
    - `desenhar_janela`
    - `gerar_lista_click`
    - `graphics`
    - `lista_pacientes`
    - `pegar_coordenada`
    - `relatorio`
  - `app`
    