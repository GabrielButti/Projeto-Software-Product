import pyodbc

# Parâmetros de conexão com o SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Projeto Software Product;'
    'Trusted_Connection=yes;'
)

# Criar um cursor
cursor = conn.cursor()

# Testar a conexão
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print("Banco conectado:", row[0])

# Fechar a conexão
cursor.close()
conn.close()
