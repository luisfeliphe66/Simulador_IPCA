import streamlit as st
import pandas as pd
from pdf_export import gerar_pdf  # Importa a função de geração de PDF

# Carregar dados do CSV
data = pd.read_csv('data/base.csv')

# Função para calcular o financiamento
def calcular_financiamento(taxa_juros, meses, valor_financiado):
    valor_total = valor_financiado * (1 + taxa_juros) ** meses
    prestacao = valor_total / meses
    juros_total = valor_total - valor_financiado
    return valor_total, prestacao, juros_total

# Título da página
st.title("Financiamento com Prestações Fixas")

# Inicializar variáveis de estado
if 'resultado' not in st.session_state:
    st.session_state.resultado = None
if 'total' not in st.session_state:
    st.session_state.total = None
if 'prestacao' not in st.session_state:
    st.session_state.prestacao = None
if 'juros' not in st.session_state:
    st.session_state.juros = None

# Campos de entrada
meses = st.number_input("Número de meses:", min_value=1, max_value=120)
taxa_juros = st.number_input("Taxa de juros mensal (%):", min_value=0.0, max_value=100.0) / 100
valor_financiado = st.number_input("Valor financiado (sem entrada):", min_value=0.0)

# Layout para os botões
col1, col2, col3 = st.columns(3)  # Cria três colunas


# Botão calcular
with col1:
    if st.button("Calcular"):
        total, prestacao, juros = calcular_financiamento(taxa_juros, meses, valor_financiado)
        st.session_state.resultado = f"Total do financiamento Valor: {total:.2f} , parcelas de : {prestacao:.2f} reais, sendo R$: {juros:.2f} de juros."
        
        # Armazenar valores no estado da sessão
        st.session_state.total = total
        st.session_state.prestacao = prestacao
        st.session_state.juros = juros
        
        st.success(st.session_state.resultado)

# Botão limpar
with col2:
    if st.button("Limpar"):
        # Resetar os valores no estado da sessão
        st.session_state.resultado = None
        st.session_state.total = None
        st.session_state.prestacao = None
        st.session_state.juros = None
        
        # Limpar campos de entrada
        st.session_state.meses = 1
        st.session_state.taxa_juros = 0.0
        st.session_state.valor_financiado = 0.0

# Botão imprimir
with col3:
    if st.button("Imprimir"):
        if st.session_state.resultado:
            gerar_pdf(st.session_state.total, st.session_state.prestacao, st.session_state.juros)
        else:
            st.warning("Por favor, calcule o financiamento antes de imprimir.")
