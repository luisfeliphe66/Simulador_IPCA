# # !pip install requests
# import requests
# import json

# # Busca a serie
# serie = "ExpectativasMercadoInflacao24Meses"
# url = f"https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/{serie}?$top=10000&$skip=0&$orderby=Data%20desc&$format=json"

# response = requests.get(url)
# data = response.json()

# # Transforme os dados conforme necessário
# # processed_data = process_data(data)
# processed_data = data

# # Função para enviar dados ao OpenMetadata
# def send_to_openmetadata(data):
#     url = "http://localhost:8585/api/v1/metadata"
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     return response.status_code

# status = send_to_openmetadata(processed_data)
# print(f"Status da Ingestão: {status}")


import requests
import psycopg2
import json

# Função para extrair dados da API do Banco Central
def extrair_dados():
    serie = "ExpectativasMercadoInflacao24Meses"
    url = f"https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/{serie}?$skip=0&$orderby=Data%20desc&$format=json"
    # url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
    response = requests.get(url)
    data = response.json()
    return data

# Função para inserir os dados no banco de dados MySQL
def carregar_dados(data):
    # Conectar ao MySQL
    try:
        conn = psycopg2.connect(
            host="localhost",
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
        print(f"Tipo de 'data': {type(data)}")
        items = data.get("value")  # Acessar a lista dentro do dicionário
        if isinstance(items, list):
            for item in items:
                print(f"Tipo de 'item': {type(item)}")
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
                    print("Primeiro item inserido com sucesso.")
                    break  # Sair do loop após o primeiro item


        # Confirmar a transação
        conn.commit()
        print("Transação confirmada.")

        # Fechar a conexão
        cursor.close()
        conn.close()
        print("Conexão ao Postgres fechada.")

    except psycopg2.Error as err:
        print(f"Erro: {err}")

if __name__ == "__main__":
    dados = extrair_dados()
    print(dados)  # Para ver como os dados estão formatados
    carregar_dados(dados)
    print("Dados inseridos com sucesso!")
