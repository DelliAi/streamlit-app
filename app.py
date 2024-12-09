import streamlit as st

# CSS Customizado
st.markdown("""
    <style>
        body {
            background-color: #040404;
            color: #f9e1cd;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3 {
            color: #FFC300;
        }
        .stButton>button {
            background-color: #FFC300;
            color: #000;
            font-size: 16px;
            border-radius: 8px;
            border: none;
        }
        .sidebar .sidebar-content {
            background-color: #1a1a1a;
            color: #f9e1cd;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #1a1a1a;
            padding: 10px;
        }
        .navbar a {
            color: #FFC300;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
        }
        .navbar a:hover {
            color: #f9e1cd;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com Navegação
st.markdown("""
    <div class="navbar">
        <div><b>Amadelli</b></div>
        <div>
            <a href="#treinamentos">Treinamentos</a>
            <a href="#ia">Assistente de IA</a>
            <a href="#painel">Painel do Funcionário</a>
            <a href="#relatorios">Relatórios</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Conteúdo Principal
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema da Amadelli. Aqui você encontra cálculos, rastreabilidade e treinamentos personalizados.")

menu = st.selectbox("Selecione uma funcionalidade:", ["Cálculo de Carga", "Rastreabilidade", "Treinamentos", "Delli AI"])

if menu == "Cálculo de Carga":
    st.header("Cálculo de Carga")
    tipo_caminhao = st.selectbox("Selecione o tipo de caminhão:", ["Volks 4 portas", "Volks 5 portas", "Volks 6 portas", "Volks 7 portas"])
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=1, step=1)
    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        caixas_restantes = quantidade_caixas % 10
        st.write(f"{fiadas_altas} fiadas altas e {caixas_restantes} caixas restantes.")

elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.markdown("**Em breve: Gráficos e relatórios interativos.**")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.markdown("**Em breve: Vídeos, quizzes e relatórios personalizados!**")

elif menu == "Delli AI":
    st.header("Assistente de IA")
    pergunta = st.text_input("Faça sua pergunta:")
    if pergunta:
        st.write(f"**Resposta simulada para:** {pergunta}")
