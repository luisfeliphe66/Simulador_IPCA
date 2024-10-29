import pymysql
import pandas as pd

# Configurações de conexão com o MariaDB
host = "mariadb"
user = "root"
password = "admin"
database = "bc_data"
port = 3306

# Consulta SQL desejada
query = "SELECT * FROM taxa_juros;"

try:
    # Conexão com o MariaDB
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    # Carregar dados da consulta em um DataFrame do Pandas
    df = pd.read_sql(query, connection)

    # Exportar o DataFrame para um arquivo CSV
    df.to_csv("resultado_consulta.csv", index=False)
    print("Consulta executada e exportada para resultado_consulta.csv com sucesso.")

except Exception as e:
    print("Erro ao conectar e consultar o banco de dados:", e)

finally:
    # Fechar a conexão
    if connection:
        connection.close()