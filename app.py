import streamlit as st

# Estilo customizado com HTML e CSS
st.markdown(f"""
    <style>
        body {{
            background-image: url("https://raw.githubusercontent.com/seu-repositorio/sua-imagem/main/image.jpg");
            background-size: cover;
            color: #f9e1cd;
            font-family: 'Arial', sans-serif;
        }}
        .main-content {{
            background-color: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }}
        h1, h2, h3 {{
            color: #FFC300;
        }}
        .sidebar .sidebar-content {{
            background-color: #1a1a1a;
            color: #f9e1cd;
        }}
        .stButton>button {{
            background-color: #FFC300;
            color: #000;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: #f9e1cd;
            color: #000;
        }}
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema da Amadelli. Aqui você encontra cálculos, rastreabilidade e treinamentos personalizados.")

# Layout principal com a imagem de fundo
st.markdown('<div class="main-content">', unsafe_allow_html=True)

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
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=0, step=1)

    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        caixas_restantes = quantidade_caixas % 10
        st.write(f"### {fiadas_altas} fiadas altas e {caixas_restantes} caixas restantes.")

elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.write("Gráficos e relatórios em desenvolvimento!")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.write("Em breve: Vídeos, quizzes e relatórios personalizados!")

elif menu == "Delli AI":
    st.header("Delli AI")
    pergunta = st.text_input("Faça sua pergunta:")
    if st.button("Perguntar"):
        st.write(f"Resposta simulada para: {pergunta}")

st.markdown('</div>', unsafe_allow_html=True)
