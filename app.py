import streamlit as st

# CSS Customizado
st.markdown("""
    <style>
        body {
            background-color: #040404;
            color: #f9e1cd;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3, h4, h5 {
            color: #FFC300;
        }
        .stButton>button {
            background-color: #FFC300;
            color: #000;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
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
            padding: 10px 20px;
            border-bottom: 2px solid #FFC300;
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
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .grid-item {
            background-color: #1a1a1a;
            color: #f9e1cd;
            border: 2px solid #FFC300;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
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

# Cabeçalho principal
st.title("Amadelli Dashboard")
st.markdown("### Bem-vindo ao sistema da Amadelli. Aqui você encontra cálculos, rastreabilidade e treinamentos personalizados.")

# Menu principal
menu = st.sidebar.selectbox(
    "Selecione uma funcionalidade:",
    ["Cálculo de Carga", "Rastreabilidade", "Treinamentos", "Delli AI", "Relatórios", "Painel do Funcionário"]
)

# Cálculo de Carga
if menu == "Cálculo de Carga":
    st.header("Cálculo de Carga")
    st.markdown("**Simule o carregamento ideal com base na capacidade do caminhão.**")
    tipo_caminhao = st.selectbox(
        "Selecione o tipo de caminhão:",
        ["Volks 4 portas", "Volks 5 portas", "Volks 6 portas", "Volks 7 portas"]
    )
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=1, step=1)
    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        caixas_restantes = quantidade_caixas % 10
        st.success(f"**Resultado:** {fiadas_altas} fiadas altas e {caixas_restantes} caixas restantes.")

# Rastreabilidade
elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.markdown("""
        ### Monitoramento e Melhorias
        Veja relatórios dinâmicos sobre os turnos e identifique pontos de melhoria na produção.
    """)
    turno = st.selectbox("Selecione o turno:", ["Manhã", "Tarde", "Noite"])
    st.markdown(f"**Relatório do Turno {turno}:**")
    if turno == "Manhã":
        st.write("Produção dentro dos padrões. Nenhum problema detectado.")
    elif turno == "Tarde":
        st.write("Alguns atrasos no envase detectados. Verifique a seção 3.")
    elif turno == "Noite":
        st.write("Turno com menor produtividade. Ajustes necessários.")

# Treinamentos
elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.markdown("**Explore cursos e relatórios personalizados.**")
    st.markdown("""
        <div class="grid-container">
            <div class="grid-item">✔️ Introdução à Rastreabilidade</div>
            <div class="grid-item">📊 Gerenciamento de Turnos</div>
            <div class="grid-item">🔧 Manutenção de Máquinas</div>
            <div class="grid-item">💡 Liderança para Supervisores</div>
        </div>
    """, unsafe_allow_html=True)

# Delli AI
elif menu == "Delli AI":
    st.header("Assistente de IA")
    st.markdown("**Interaja com a Delli AI para obter respostas e insights personalizados.**")
    pergunta = st.text_input("Faça sua pergunta:")
    if st.button("Perguntar"):
        st.write(f"**Resposta simulada para:** {pergunta}")

# Relatórios
elif menu == "Relatórios":
    st.header("Relatórios")
    st.markdown("### Dados de Produtividade e Metas")
    st.markdown("""
        **Gráficos Interativos:**
        - Produtividade por Turno
        - Metas Alcançadas
        - Atrasos por Semana
    """)
    st.line_chart([10, 20, 30, 40, 50])  # Simulação de dados

# Painel do Funcionário
elif menu == "Painel do Funcionário":
    st.header("Painel do Funcionário")
    st.markdown("**Acompanhe seu desempenho e metas.**")
    st.markdown("""
        ### Resumo:
        - **Nome:** João da Silva
        - **Cargo:** Operador de Máquinas
        - **Produtividade:** 85%
        - **Metas Alcançadas:** 12/15
    """)
    st.progress(85)

# Rodapé
st.markdown("---")
st.markdown("© 2024 Amadelli Alimentos. Todos os direitos reservados.")
