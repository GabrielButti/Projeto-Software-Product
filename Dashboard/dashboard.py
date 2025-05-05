import streamlit as st
import pyodbc
import pandas as pd
import plotly.express as px

# Conexão com o SQL Server
conexao = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=SPON080100101\\PROJETO;'
    'DATABASE=Clima_Tempo;'
    'Trusted_Connection=yes;'
)

# Carregando os dados
df = pd.read_sql("SELECT * FROM Clima", conexao)

st.title("Dashboard Climático 🌤️")

# Gráfico de temperatura ao longo do tempo
st.subheader("Temperatura ao longo do tempo")
fig_temp = px.line(df, x="DataHora", y="Temperatura", color="Cidade", markers=True)
st.plotly_chart(fig_temp)

# Distribuição das condições do clima
st.subheader("Frequência das Condições Climáticas")
condicoes = df["Condicao"].value_counts().reset_index()
condicoes.columns = ["Condicao", "Frequencia"]
fig_cond = px.bar(condicoes, x="Condicao", y="Frequencia", color="Condicao")
st.plotly_chart(fig_cond)

# Temperatura média por cidade
st.subheader("Temperatura média por cidade")
medias = df.groupby("Cidade")["Temperatura"].mean().reset_index()
fig_media = px.bar(medias, x="Cidade", y="Temperatura", color="Cidade")
st.plotly_chart(fig_media)

# Umidade média por cidade
st.subheader("Umidade média por cidade")
umidade = df.groupby("Cidade")["Umidade"].mean().reset_index()
fig_umidade = px.bar(umidade, x="Cidade", y="Umidade", color="Cidade")
st.plotly_chart(fig_umidade)

# Máxima e mínima temperatura por cidade
st.subheader("Temperaturas máximas e mínimas por cidade")
temp_extremos = df.groupby("Cidade").agg(Maxima=("Temperatura", "max"), Minima=("Temperatura", "min")).reset_index()
fig_extremos = px.bar(temp_extremos, x="Cidade", y=["Maxima", "Minima"], barmode="group")
st.plotly_chart(fig_extremos)

# Histograma de temperaturas
st.subheader("Distribuição das temperaturas")
fig_hist = px.histogram(df, x="Temperatura", nbins=20, color="Cidade")
st.plotly_chart(fig_hist)
