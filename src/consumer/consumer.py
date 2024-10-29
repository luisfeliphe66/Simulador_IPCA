import requests
import mariadb
import json
from datetime import datetime

# Função para extrair dados da API do Banco Central
def extrair_dados():
    serie = "25352"
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados?formato=json"
    response = requests.get(url)
    data = response.json()


    # Exibe o conteúdo original de 'data' para ajudar na depuração
    print(f"Conteúdo de data (inicial): {data}")

    return data

# Função para carregar os dados no banco de dados MySQL
def carregar_dados(data):
    try:
        # Conectar ao MySQL
        conn = mariadb.connect(
            host="mariadb",
            port=3306,
            user="root",
            password="admin",
            database="bc_data"
        )

        cursor = conn.cursor()
        print("Conexão ao mariadb estabelecida com sucesso.")

        # # SQL para inserir dados
        sql = """
        INSERT INTO taxa_juros (data, valor)
        VALUES (%s, %s)
        """

        valores = [(converter_data(item["data"]), item["valor"]) for item in data]

        cursor.executemany(sql, valores)

        # Confirmar a transação
        conn.commit()
        print("Transação confirmada.")

        # Fechar a conexão
        cursor.close()
        conn.close()
        print("Conexão ao MySQL fechada.")

    except mariadb.Error as err:
        print(f"Erro: {err}")

def converter_data(data_str):
    """Converte a data do formato DD/MM/AAAA para AAAA-MM-DD."""
    return datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")

if __name__ == "__main__":
    dados = extrair_dados()
    print(dados)  # Para ver como os dados estão formatados
    carregar_dados(dados)
    print("Dados inseridos com sucesso!")
