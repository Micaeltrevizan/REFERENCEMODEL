import streamlit as st
import nltk
import pandas as pd
import logging
import base64
import os  # Importe a biblioteca os
from function import obter_valor_criticidade, obter_valor_equipe, obter_valor_dinamismo, obter_valor_cultura, obter_valor_tamanho, obter_metodologia_por_fase
import google.generativeai as genai
nltk.download('punkt')
import re
from fpdf import FPDF  # Importe a biblioteca fpdf2

st.set_page_config(
    page_title="MICA - Gerador de Metodologias Híbridas",
    page_icon="Logo.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## MICA - Gerador de Metodologias Híbridas
            ### Powered by Gemini

            **GitHub**: [Seu Repositório no GitHub]

            Esta ferramenta utiliza o modelo MICA e IA Generativa para auxiliar na criação de planos de gerenciamento de projetos híbridos.
        """
    }
)

# Configure Google GenerativeAI com variável de ambiente
PI_KEY = os.environ.get("GOOGLE_GEMINI_API_KEY")
if PI_KEY:
    genai.configure(api_key=PI_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
else:
    st.error("A chave da API do Google Gemini não foi configurada como variável de ambiente ('GOOGLE_GEMINI_API_KEY').")
    st.stop()

# Streamlit Title
def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

def create_pdf(title, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    try:
        pdf.cell(200, 10, txt=title, ln=1, align="C")
        pdf.multi_cell(0, 10, txt=content)
        return pdf.output(dest="S")
    except Exception as e:
        st.error(f"Erro ao criar PDF: {e}")
        return None

def download_card_info(title, content):
    pdf_bytes = create_pdf(title, content)
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{title}.pdf">Baixar PDF</a>'
    return href

def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Criar plano de gerenciamento", "Galeria"])

    with tab1:
        st.subheader("""Cansado de escolher entre metodologias ágeis e tradicionais?""")
        st.write("""Apresentamos o MICA, a plataforma inovadora que utiliza o revolucionário modelo de referência MICA (Methodology Identification and Choice Analysis) em conjunto com a inteligência artificial generativa para criar planos de gerenciamento de projetos híbridos sob medida para as suas necessidades.""")
        st.subheader("""Como funciona?""")
        st.write("""Ao inserir as características específicas do seu projeto, nosso sistema, impulsionado por IA generativa, analisa esses fatores utilizando o modelo MICA para:""")
        st.write("""1. Identificar as metodologias ágeis e tradicionais mais adequadas para o seu contexto.""")
        st.write("""2. Sugerir uma combinação estratégica dessas metodologias para formar um modelo híbrido otimizado para as diferentes fases do seu projeto.""")
        st.image("etapas.png", width=800)  # Caminho relativo
    with tab2:
        img_path = "Logo.png"  # Caminho relativo
        img_base64 = img_to_base64(img_path)
        if img_base64:
            st.sidebar.markdown(
                f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
                unsafe_allow_html=True,
            )

        st.sidebar.markdown("---")

        st.subheader("""Preencha as informações abaixo de acordo com as necessidades do seu projeto""")

        col1, col2, col3, col4, col5 = st.columns(5)

        with st.container():
            with col1:
                criticidade = st.slider("Criticidade", 1, 3, 3)
                st.caption("Impacto que o sucesso ou fracasso do projeto terá para a organização.")
            with col2:
                equipe = st.slider("Equipe", 1, 3, 3)
                st.caption("Habilidades, conhecimentos e experiências da equipe")
            with col3:
                tamanho = st.slider("Tamanho", 1, 3, 3)
                st.caption("O tamanho se refere à magnitude ou escopo do projeto")
            with col4:
                cultura = st.slider("Cultura", 1, 3, 3)
                st.caption("Como a cultura da empresa influencia a concepção do projeto")
            with col5:
                dinamismo = st.slider("Dinamismo", 1, 3, 3)
                st.caption("Capacidade de se adaptar em resposta a mudanças.")

        st.write("Criticidade: ", criticidade, "Equipe: ", equipe, "Tamanho: ",
                 tamanho, "Cultura organizacional: ", cultura, "Dinamismo: ", dinamismo)

        with st.container():
            time = st.number_input(
                "Em quantos meses o seu projeto deve ser finalizado?", value=None, placeholder="Type a number...")
            st.write(time, "Meses")

        valor_criticidade = obter_valor_criticidade(criticidade)
        valor_equipe = obter_valor_equipe(equipe)
        valor_dinamismo = obter_valor_dinamismo(dinamismo)
        valor_cultura = obter_valor_cultura(cultura)
        valor_tamanho = obter_valor_tamanho(tamanho)
        valor_time = f' {time} meses'

        # Obter as metodologias recomendadas por fase
        metodologias_por_fase = obter_metodologia_por_fase(criticidade, equipe, dinamismo, cultura, tamanho)

        prompt = (
            f'Me forneça um plano de gerenciamento que combine os melhores elementos das metodologias indicadas em {valor_criticidade}, {valor_equipe},{valor_tamanho},{valor_cultura}, {valor_dinamismo}. As fases devem ser formadas com o match das metodologias coletadas anteriormente e {metodologias_por_fase}, utilizar uma metodologia por etapa, a execuçao e o monitoramento devem caminhar juntos), as etapas devem estar divididas em {valor_time}. A resposta deve conter somente 3 tópicos: 1.Premissa, explicando a resposta fornecida; 2.Modelo de Gerenciamento; 3.Ferramentas e tecnologias.')

        if st.button("Gerar plano de gerenciamento"):
            response = model.generate_content(prompt, stream=True)
            generated_text = ""
            for chunk in response:
                generated_text += chunk.text
            st.write("**Resposta:**")
            st.markdown(generated_text)
            st.session_state.resultado_gerado = generated_text

        # Salvar as informações em um card expansível
        titulo = st.text_input("Titulo")
        col_save, col_download = st.columns([1, 1])
        with col_save:
            if st.button("Salvar"):
                if "informacoes_salvas" not in st.session_state:
                    st.session_state.informacoes_salvas = []
                st.session_state.informacoes_salvas.append({"titulo": titulo, "conteudo": st.session_state.resultado_gerado})
        with col_download:
            if "resultado_gerado" in st.session_state and st.session_state.resultado_gerado:
                pdf_bytes = create_pdf(titulo if titulo else "Plano de Gerenciamento", st.session_state.resultado_gerado)
                st.download_button(
                    label="Baixar PDF",
                    data=pdf_bytes,
                    file_name=f"{titulo if titulo else 'plano_gerenciamento'}.pdf",
                    mime="application/pdf",
                )
            else:
                st.caption("Gere o plano de gerenciamento para habilitar o download.")

    with tab3:
        st.header("Informações Salvas")
        if "informacoes_salvas" in st.session_state:
            for card in st.session_state.informacoes_salvas:
                with st.expander(card["titulo"]):
                    st.markdown(card["conteudo"])

                    st.subheader("Progresso das Fases")

                    fases = ["Iniciação", "Planejamento", "Execução", "Monitoramento e Controle", "Encerramento"]

                    if "fases_concluidas" not in st.session_state:
                        st.session_state.fases_concluidas = {fase: False for fase in fases}

                    for fase in fases:
                        st.session_state.fases_concluidas[fase] = st.checkbox(fase, value=st.session_state.fases_concluidas[fase])

                    total_fases = len(fases)
                    fases_concluidas = sum(1 for concluida in st.session_state.fases_concluidas.values() if concluida)
                    percentual_concluido = (fases_concluidas / total_fases) * 100 if total_fases > 0 else 0

                    st.progress(percentual_concluido / 100)
                    st.write(f"{percentual_concluido:.2f}% concluído")

                    # Adicionar o botão de download para cada card salvo
                    pdf_bytes = create_pdf(card["titulo"], card["conteudo"])
                    b64 = base64.b64encode(pdf_bytes).decode()
                    href = f'<a href="data:application/pdf;base64,{b64}" download="{card["titulo"]}.pdf">Baixar PDF</a>'
                    st.markdown(href, unsafe_allow_html=True)

        else:
            st.info("Nenhuma informação foi salva.")

if __name__ == "__main__":
    main()
