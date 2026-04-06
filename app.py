import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DE INTERFACE SÉRIA ---
st.set_page_config(page_title="Veritas AI - Analista Forense", page_icon="⚖️")

# Estilo para parecer um app profissional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTextArea textarea { background-color: #1a1c24; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Veritas AI")
st.caption("Sistema de Análise Comportamental, Hipnose e Mentalismo Técnico")

# --- BARRA LATERAL PARA A CHAVE ---
with st.sidebar:
    st.header("Configurações")
    api_key = st.text_input("Insira sua API Key do Google:", type="password")
    st.info("Obtenha sua chave em: aistudio.google.com")
    st.divider()
    st.markdown("### Referências Ativas:")
    st.write("- Paul Ekman (FACS)\n- Joe Navarro (FBI)\n- Milton Erickson\n- Dave Elman\n- Daniel Kahneman")

# --- MOTOR DE INTELIGÊNCIA ---
if api_key:
    genai.configure(api_key=api_key)
    # Configuração do "Cérebro" com as regras que você exigiu
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="""
        Você é o Veritas AI. Você NÃO usa achismos. 
        Sua base de conhecimento é estritamente técnica, baseada em:
        1. Análise Comportamental: Paul Ekman (Microexpressões), Joe Navarro (Comportamentos apaziguadores), Aldert Vrij (Carga Cognitiva).
        2. Hipnose Clínica: Protocolos de Milton Erickson (indireta) e Dave Elman (direta).
        3. Mentalismo: Psicologia aplicada, Efeito Forer, e Vieses Cognitivos (Kahneman).
        
        REGRAS DE RESPOSTA:
        - Sempre cite o autor ou a teoria científica.
        - Use formato de 'Laudo Técnico'.
        - Se o usuário descrever algo sem base científica (ex: PNL de olhar para os lados), corrija educadamente citando estudos recentes.
        - Mantenha um tom sério, direto e profissional.
        """
    )

# --- INTERFACE DE ENTRADA ---
cenario = st.text_area("Descreva o cenário, gesto ou sintoma observado:", height=200, placeholder="Ex: O interlocutor travou a mandíbula e cruzou os braços ao ser questionado sobre valores...")

col1, col2 = st.columns(2)
with col1:
    tipo_analise = st.selectbox("Foco da Análise:", ["Comportamento", "Hipnose Clínica", "Mentalismo/Influência"])

if st.button("GERAR ANÁLISE TÉCNICA"):
    if not api_key:
        st.error("ERRO: Insira a API Key na barra lateral para prosseguir.")
    elif not cenario:
        st.warning("Por favor, descreva uma situação para análise.")
    else:
        with st.spinner("Processando evidências baseadas na literatura..."):
            try:
                prompt = f"Analise o seguinte cenário sob a ótica de {tipo_analise}: {cenario}"
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.subheader("📋 Relatório Pericial")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Erro na conexão: {e}")

st.markdown("---")
st.caption("Veritas AI v1.0 - Uso estritamente informativo e acadêmico.")

