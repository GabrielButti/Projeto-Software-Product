import pandas as pd
import pyodbc

# Conexão com o banco
dados_conexao = (
    'DRIVER={SQL Server};'
    'SERVER=SPON080100101\\PROJETO;'
    'DATABASE=Clima_Tempo;'
    'Trusted_Connection=yes;'
)
conexao = pyodbc.connect(dados_conexao)

# Lendo a tabela
df = pd.read_sql("SELECT * FROM Clima", conexao)

# Ajuste de tipos
df['DataHora'] = pd.to_datetime(df['DataHora'])
df['Data'] = df['DataHora'].dt.date

# Temperatura média
media_temp = df['Temperatura'].mean()
print(f"Temperatura média geral: {media_temp:.2f} °C")

# Dias com temperatura acima de 30°C
dias_quentes = df[df['Temperatura'] > 30]['Data'].unique()
print("\nDias com temperatura acima de 30°C:")
for dia in dias_quentes:
    print(f" - {dia}")

# Umidade média por dia
umidade_dia = df.groupby('Data')['Umidade'].mean()
print("\nUmidade média por dia:")
print(umidade_dia)

# Velocidade do vento máxima por dia
vento_maximo = df.groupby('Data')['VelocidadeVento'].max()
print("\nVelocidade máxima do vento por dia:")
print(vento_maximo)

# Frequência de condições climáticas
frequencia_condicoes = df['Condicao'].value_counts()
print("\nCondições climáticas registradas:")
print(frequencia_condicoes)
