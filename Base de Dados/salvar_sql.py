import requests
import pandas as pd
import pyodbc
import certifi

# Coordenadas de São Paulo
latitude = -23.5505
longitude = -46.6333

# URL da API Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,windspeed_10m&timezone=auto"

# Requisição
resposta = requests.get(url, verify=False)
dados = resposta.json()

# Criar DataFrame com os dados
df = pd.DataFrame({
    'DataHora': dados['hourly']['time'],
    'Temperatura': dados['hourly']['temperature_2m'],
    'Umidade': dados['hourly']['relative_humidity_2m'],
    'VelocidadeVento': dados['hourly']['windspeed_10m']
})

df['Cidade'] = 'São Paulo'
df['DataHora'] = pd.to_datetime(df['DataHora'])

# Conectar ao SQL Server
dados_conexao = (
    'DRIVER={SQL Server};'
    'SERVER=SPON080100101\\PROJETO;'
    'DATABASE=Clima_Tempo;'
    'Trusted_Connection=yes;'
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Inserir dados na tabela Clima
for _, linha in df.iterrows():
    cursor.execute('''
        INSERT INTO Clima (Cidade, DataHora, Temperatura, Umidade, VelocidadeVento)
        VALUES (?, ?, ?, ?, ?)
    ''', linha['Cidade'], linha['DataHora'], linha['Temperatura'], linha['Umidade'], linha['VelocidadeVento'])

conexao.commit()
cursor.close()
conexao.close()

print("Dados inseridos com sucesso!")
