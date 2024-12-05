import streamlit as st

# Configurações do título e descrição
st.set_page_config(
    page_title="Amadelli Dashboard",
    page_icon="🍦",
    layout="wide"
)

# Cabeçalho
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema da Amadelli. Aqui você encontra cálculos, rastreabilidade e treinamentos personalizados.")

# Menu de navegação lateral
menu = st.sidebar.selectbox(
    "Selecione uma funcionalidade:",
    ["Cálculo de Carga", "Rastreabilidade", "Treinamentos", "Delli AI"]
)

if menu == "Cálculo de Carga":
    st.header("Cálculo de Carga")
    tipo_caminhao = st.selectbox(
        "Selecione o tipo de caminhão:",
        ["Volks 4 portas", "Volks 5 portas", "Volks 6 portas", "Volks 7 portas"]
    )
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=1, step=1)

    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        fiadas_baixas = quantidade_caixas % 10
        st.write(f"{fiadas_altas} fiadas altas e {fiadas_baixas} caixas restantes.")

elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.write("Gráficos e relatórios em desenvolvimento.")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.write("Em breve: Vídeos, quizzes e relatórios personalizados!")

elif menu == "Delli AI":
    st.header("Delli AI")
    st.write("Interaja com a inteligência artificial personalizada da Amadelli.")
    pergunta = st.text_input("Faça sua pergunta:")
    if st.button("Perguntar"):
        st.write(f"Resposta simulada para: {pergunta}")
