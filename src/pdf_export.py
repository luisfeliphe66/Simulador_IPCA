from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from datetime import datetime
import streamlit as st

def gerar_pdf(total, prestacao, juros):
    pdf_file_path = "financiamento.pdf"
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Criar uma lista de elementos para o PDF
    elements = []

    # Cabeçalho do relatório
    header = Paragraph("Relatório de Financiamento", styles['Title'])
    elements.append(header)
    elements.append(Spacer(1, 12))

    # Informações de contato
    contact_info = Paragraph("ELAC Instituição Financeira", styles['Normal'])
    elements.append(contact_info)
    elements.append(Paragraph("Telefone: (00) 3313-44733", styles['Normal']))
    elements.append(Paragraph("Email: contato@elacfinanceira.com", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Data do relatório
    data_atual = datetime.now().strftime("%d/%m/%Y")
    date_paragraph = Paragraph(f"Data: {data_atual}", styles['Normal'])
    elements.append(date_paragraph)
    elements.append(Spacer(1, 12))

    # Subtítulo
    subtitle = Paragraph("Detalhes do Financiamento", styles['Heading2'])
    elements.append(subtitle)
    elements.append(Spacer(1, 12))

    # Tabela com os resultados
    data = [
        ["Descrição", "Valor"],
        ["Total do financiamento", f"R$ {total:.2f}"],
        ["Valor da parcela", f"R$ {prestacao:.2f}"],
        ["Total de juros", f"R$ {juros:.2f}"]
    ]
    
    # Criar a tabela
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Rodapé
    footer = Paragraph("Obrigado por escolher ELAC Instituição Financeira!", styles['Normal'])
    elements.append(footer)
    elements.append(Spacer(1, 12))

    # Salvar o PDF
    doc.build(elements)

    # Permitir download do PDF
    with open(pdf_file_path, "rb") as pdf_file:
        st.success("PDF gerado. Você pode baixá-lo abaixo.")
        st.download_button(
            label="Baixar relatório PDF",
            data=pdf_file,
            file_name=pdf_file_path,
            mime="application/pdf"
        )
