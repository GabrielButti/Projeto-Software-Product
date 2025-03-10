
# Projeto de Coleta e Análise de Dados Climáticos

Este projeto tem como objetivo coletar dados climáticos utilizando a **API Open-Meteo**, armazená-los em um banco de dados SQL Server, e realizar a análise desses dados para gerar insights climáticos. O foco principal é monitorar as condições climáticas ao longo do tempo, como a temperatura máxima, mínima e a precipitação diária.

## Funcionalidades

- **Coleta de dados climáticos**: Utiliza a API Open-Meteo para coletar dados climáticos de uma localidade específica.
- **Armazenamento em banco de dados**: Os dados coletados são armazenados em um banco de dados SQL Server para análise posterior.
- **Análise dos dados**: Realização de análise básica sobre as condições climáticas, como temperaturas e precipitação.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para coleta e análise dos dados.
- **API Open-Meteo**: Fonte de dados climáticos gratuitos.
- **SQL Server**: Banco de dados utilizado para armazenar os dados coletados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **PyODBC**: Biblioteca para conectar o Python ao SQL Server.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

2. Instale as dependências:
   Se estiver usando o `pip`, execute o seguinte comando no terminal:
   ```bash
   pip install -r requirements.txt
   ```

   Caso você queira instalar as dependências manualmente, execute:
   ```bash
   pip install pandas pyodbc requests
   ```

3. Certifique-se de ter o **SQL Server** instalado e em execução. Caso não tenha, você pode [baixar o SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads).

4. Instale o **ODBC Driver 17 for SQL Server**. Você pode [baixá-lo aqui](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

## Configuração do Banco de Dados

1. No SQL Server, crie um banco de dados para armazenar os dados climáticos. Você pode fazer isso no **SQL Server Management Studio (SSMS)** ou via script SQL:

   ```sql
   CREATE DATABASE clima_db;
   ```

2. Crie a tabela **clima** no banco de dados:

   ```sql
   CREATE TABLE clima (
       id INT PRIMARY KEY IDENTITY,
       data DATE,
       temp_max FLOAT,
       temp_min FLOAT,
       precipitacao FLOAT
   );
   ```

3. Altere o arquivo de conexão no código Python para refletir as credenciais do seu banco de dados:

   ```python
   conn = pyodbc.connect(
       'DRIVER={ODBC Driver 17 for SQL Server};'
       'SERVER=localhost;'  # ou o IP/nome do servidor
       'DATABASE=clima_db;'  # Nome do banco de dados
       'UID=seu_usuario;'  # Nome do usuário
       'PWD=sua_senha'  # Senha do usuário
   )
   ```

## Como Usar

1. **Coletar dados climáticos**:
   Execute o script de coleta de dados. Ele irá buscar os dados da API Open-Meteo, como temperatura máxima, mínima e precipitação para o dia e armazená-los no banco de dados:

   ```bash
   python buscar_dados.py
   ```

2. **Armazenar dados no banco de dados**:
   O script irá automaticamente conectar ao banco de dados SQL Server e inserir os dados coletados na tabela `clima`.

3. **Verificar os dados**:
   Após executar a coleta, você pode consultar os dados diretamente no SQL Server usando o SQL Server Management Studio (SSMS) ou outro cliente SQL. Aqui está um exemplo de consulta para verificar os dados inseridos:

   ```sql
   SELECT * FROM clima;
   ```

## Estrutura do Projeto

```
/Projeto
│
├── buscar_dados.py           # Script de coleta de dados da API Open-Meteo
├── salvar_postgres.py        # Script para salvar os dados no banco de dados SQL Server
├── requirements.txt          # Arquivo com as dependências do projeto
└── README.md                 # Este arquivo
```

## Contribuições

Sinta-se à vontade para contribuir para o projeto. Se encontrar algum problema ou tiver sugestões de melhorias, fique à vontade para abrir um **issue** ou **pull request**.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
