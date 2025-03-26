import streamlit as st
import nltk
import pandas as pd
import logging
import base64
from function import obter_valor_criticidade,obter_valor_equipe,obter_valor_dinamismo,obter_valor_cultura, obter_valor_tamanho
import google.generativeai as genai
nltk.download('punkt') 
import re

st.set_page_config(
    page_title="st.title",
    page_icon="Logo.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## Streamly Streamlit Assistant
            ### Powered using GPT-4o-mini

            **GitHub**: https://github.com/AdieLaine/

            The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
            generate code snippets for Streamlit widgets,
            and answer questions about Streamlit's latest features, issues, and more.
            Streamly has been trained on the latest Streamlit updates and documentation.
        """
    }
)

# Try configuring Google GenerativeAI
PI_KEY = "********************************"
genai.configure(api_key="******************************")
# Create a GenerativeAI model (replace 'gemini-1.5-pro-latest' if desired)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Streamlit Title
def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None


def main():
    tab1, tab2, tab3 = st.tabs(["Home","Criar plano de gerenciamento", "Galeria"])

    with tab1:
        st.subheader("""O que é o MICA?""")



    with tab2:
        img_path = "Logo.png"
        img_base64 = img_to_base64(img_path)
        if img_base64:
            st.sidebar.markdown(
                f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
                unsafe_allow_html=True,
            )

        st.sidebar.markdown("---")

        #st.image("logo.jpeg", width=1000)

        
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
                    criticidade, "Cultura organizacional: ", cultura, "Dinamismo: ", dinamismo)


        with st.container():
                time = st.number_input(
                "Em quantos meses o seu projeto deve ser finalizado?", value=None, placeholder="Type a number...")
                st.write(time, "Meses" )

        valor_criticidade = obter_valor_criticidade(criticidade)
        valor_equipe = obter_valor_equipe(equipe)
        valor_dinamismo = obter_valor_dinamismo(dinamismo)
        valor_cultura = obter_valor_cultura(cultura)
        valor_tamanho = obter_valor_tamanho(tamanho)
        valor_time = f' {time} meses'

        prompt = (f'Me forneça um plano de gerenciamento para um projeto com as etapas: iniciação, planejamento, execução, monitoramento, encerramento, as etapas devem estar divididas em {valor_time}. O modelo deve combinar os melhores elementos de:{valor_criticidade}, {valor_equipe, valor_tamanho}, {valor_cultura}, {valor_dinamismo}. A resposta deve conter somente 3 tópicos: 1.Premissa, explicando a resposta fornecida; 2.Modelo de Gerenciamento; 3.Ferramentas e tecnologias.')

        if st.button("ENVIAR"):
            response = model.generate_content(prompt, stream=True)
            generated_text = ""
            for chunk in response:
                generated_text += chunk.text
            st.write("**Resposta:**")
            st.markdown(generated_text)
            st.session_state.resultado_gerado = generated_text

        # Salvar as informações em um card expansível
        titulo = st.text_input("Titulo")
        if st.button ("Salvar"):
            if "informacoes_salvas" not in st.session_state:
                st.session_state.informacoes_salvas = []
            st.session_state.informacoes_salvas.append({"titulo": titulo, "conteudo": st.session_state.resultado_gerado})
   
    
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
                                        

            else:
                st.info("Nenhuma informação foi salva.")


if __name__ == "__main__":
    main()
