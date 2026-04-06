import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Veritas AI", page_icon="⚖️")

st.title("🛡️ Veritas AI")

# Barra lateral para a chave
with st.sidebar:
    api_key = st.text_input("Insira sua API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # TENTATIVA 1: Usando o nome direto sem o "models/"
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        cenario = st.text_area("O que você observou?")

        if st.button("ANALISAR"):
            if cenario:
                response = model.generate_content(f"Analise como um perito: {cenario}")
                st.divider()
                st.write(response.text)
            else:
                st.warning("Digite algo para analisar.")
    except Exception as e:
        st.error(f"Erro de configuração: {e}")
else:
    st.info("Aguardando a sua API Key na barra lateral...")
