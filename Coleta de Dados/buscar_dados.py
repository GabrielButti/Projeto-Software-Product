import requests
import pandas as pd

# Configuração da API Open-Meteo
URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -23.5505,  # Latitude de São Paulo
    "longitude": -46.6333,  # Longitude de São Paulo
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "America/Sao_Paulo"
}

# Requisição para obter os dados
response = requests.get(URL, params=params, verify=False)  # ⚠️ Ignorando verificação SSL
data = response.json()

# Processamento dos dados
df = pd.DataFrame({
    "data": data["daily"]["time"],
    "temp_max": data["daily"]["temperature_2m_max"],
    "temp_min": data["daily"]["temperature_2m_min"],
    "precipitacao": data["daily"]["precipitation_sum"]
})

print(df.head())  # Exibe as primeiras linhas do DataFrame
