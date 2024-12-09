import streamlit as st

# Estilo customizado com imagem de fundo
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("https://raw.githubusercontent.com/DelliAi/streamlit-app/main/DALL-E%202024-12-08%2021.27.24%20-%20A%20modern%20four-story%20building%20....jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #f9e1cd;
        font-family: 'Arial', sans-serif;
    }}
    .stApp {{
        background-color: rgba(0, 0, 0, 0.6); /* Fundo semi-transparente para legibilidade */
        padding: 20px;
        border-radius: 10px;
    }}
    h1, h2, h3 {{
        color: #FFC300;
    }}
    .stButton>button {{
        background-color: #FFC300;
        color: #000;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: #FFA500;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema da Amadelli. Aqui você encontra cálculos, rastreabilidade e treinamentos personalizados.")

# Menu lateral de navegação
menu = st.sidebar.selectbox(
    "Selecione uma funcionalidade:",
    ["Cálculo de Carga", "Rastreabilidade", "Treinamentos", "Delli AI"]
)

# Seções dinâmicas
if menu == "Cálculo de Carga":
    st.header("Cálculo de Carga")
    tipo_caminhao = st.selectbox(
        "Selecione o tipo de caminhão:",
        ["Volks 4 portas", "Volks 5 portas", "Volks 6 portas", "Volks 7 portas"]
    )
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=1, step=1)
    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        st.write(f"Resultado: {fiadas_altas} fiadas altas.")

elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.write("Em breve: Gráficos e relatórios em desenvolvimento.")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.write("Em breve: Vídeos, quizzes e relatórios personalizados!")

elif menu == "Delli AI":
    st.header("Delli AI")
    pergunta = st.text_input("Faça sua pergunta:")
    if pergunta:
        st.write(f"Resposta simulada para: {pergunta}")
