import requests
import mysql.connector
import json

# Função para extrair dados da API do Banco Central
def extrair_dados():
    serie = "ExpectativasMercadoInflacao24Meses"
    url = f"https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/{serie}?$skip=0&$orderby=Data%20desc&$format=json"
    response = requests.get(url)
    data = response.json()
    return data

# Função para carregar os dados no banco de dados MySQL
def carregar_dados(data):
    try:
        # Conectar ao MySQL
        conn = mysql.connector.connect(
            # host="mysql",
            host="simuladoripca-mysql",
            user="root",
            password="password",
            database="bacen_db"
        )
        cursor = conn.cursor()
        print("Conexão ao MySQL estabelecida com sucesso.")

        # SQL para inserir dados
        sql = """
        INSERT INTO indicador_economico (indicador, data, suavizada, media, mediana, desvio_padrao, minimo, maximo, numero_respondentes, base_calculo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Verificar o tipo de dados
        items = data.get("value")  # Acessar a lista dentro do dicionário
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    print(f"Processando item: {item}")
                    valores = (
                        item.get("Indicador"),
                        item.get("Data"),
                        item.get("Suavizada"),
                        item.get("Media"),
                        item.get("Mediana"),
                        item.get("DesvioPadrao"),
                        item.get("Minimo"),
                        item.get("Maximo"),
                        item.get("numeroRespondentes"),
                        item.get("baseCalculo")
                    )
                    cursor.execute(sql, valores)

        # Confirmar a transação
        conn.commit()
        print("Transação confirmada.")

        # Fechar a conexão
        cursor.close()
        conn.close()
        print("Conexão ao MySQL fechada.")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

if __name__ == "__main__":
    dados = extrair_dados()
    print(dados)  # Para ver como os dados estão formatados
    carregar_dados(dados)
    print("Dados inseridos com sucesso!")
