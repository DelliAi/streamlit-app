import streamlit as st

# Estilo customizado com HTML e CSS
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
</style>
""", unsafe_allow_html=True)

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
    st.header ("Cálculo de Carga")

