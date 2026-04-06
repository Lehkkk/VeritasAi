import streamlit as st
import google.generativeai as genai

st.title("🛡️ Veritas AI")

# Campo da Chave na lateral
with st.sidebar:
    chave = st.text_input("Cole sua API Key aqui:", type="password")

if chave:
    try:
        genai.configure(api_key=chave)
        # Usando o nome mais simples possível do modelo
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        texto = st.text_area("Descreva o comportamento:")
        
        if st.button("ANALISAR"):
            if texto:
                # Aqui o código tenta gerar a resposta
                response = model.generate_content(f"Analise tecnicamente: {texto}")
                st.markdown("### 📋 Relatório")
                st.write(response.text)
            else:
                st.warning("Escreva algo antes.")
    except Exception as e:
        # Se der erro, ele vai mostrar EXATAMENTE o que é
        st.error(f"Atenção: {e}")
else:
    st.info("Insira a chave na esquerda para começar.")
