import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Veritas AI - Analista Forense", page_icon="⚖️")

st.title("🛡️ Veritas AI")
st.caption("Sistema de Análise Comportamental e Hipnose Técnica")

with st.sidebar:
    st.header("Configurações")
    api_key = st.text_input("Insira sua API Key:", type="password")
    st.info("Obtenha sua chave em: aistudio.google.com")

if api_key:
    genai.configure(api_key=api_key)
    # AQUI ESTÁ A CORREÇÃO: Adicionamos 'models/' antes do nome
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        system_instruction="Analise como um perito forense baseado em Paul Ekman e Joe Navarro."
    )

cenario = st.text_area("O que você observou?")

if st.button("ANALISAR"):
    if not api_key:
        st.error("Coloque a chave na barra lateral!")
    else:
        try:
            response = model.generate_content(cenario)
            st.divider()
            st.subheader("📋 Relatório")
            st.write(response.text)
        except Exception as e:
            st.error(f"Erro: {e}")
