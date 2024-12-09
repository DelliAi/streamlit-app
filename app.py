import streamlit as st
from PIL import Image

# Carregar a imagem para o fundo
background_image = "DALL-E_2024-12-08_21.27.24.jpg"

st.markdown(
    f"""
    <style>
        /* Fundo da página */
        .stApp {{
            background: url('data:image/png;base64,{open(background_image, "rb").read().encode("base64").decode()}');
            background-size: cover;
            background-attachment: fixed;
        }}

        /* Estilizar os títulos */
        h1, h2, h3 {{
            color: #FFC300;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        }}

        /* Estilizar a barra lateral */
        .css-1d391kg { /* Sidebar */
            background-color: rgba(20,20,20,0.9);
            border: 2px solid #FFC300;
            border-radius: 8px;
        }}

        /* Botões */
        .stButton>button {{
            background-color: #FFC300;
            color: #000;
            border: none;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #FF5733;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema interativo da Amadelli. Aqui você encontra **soluções modernas** e **futurísticas**.")

# Menu lateral
menu = st.sidebar.selectbox(
    "Escolha uma funcionalidade:",
    ["Visão Geral", "Relatórios", "Treinamentos", "IA Assistente", "Configurações"]
)

# Conteúdo Dinâmico
if menu == "Visão Geral":
    st.header("Visão Geral")
    st.markdown("#### Aqui você encontra **gráficos e análises em tempo real** sobre as operações.")

elif menu == "Relatórios":
    st.header("Relatórios")
    st.markdown("#### Acesse relatórios detalhados e dinâmicos.")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.markdown("#### Explore módulos de treinamento interativos.")

elif menu == "IA Assistente":
    st.header("IA Assistente")
    st.markdown("#### Converse com nossa **IA avançada** para suporte.")

elif menu == "Configurações":
    st.header("Configurações")
    st.markdown("#### Personalize sua experiência.")
