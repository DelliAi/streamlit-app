import streamlit as st

# CSS Customizado para um layout mais moderno
st.markdown("""
    <style>
        /* Corpo geral */
        body {
            background-color: #121212;
            color: #f9e1cd;
            font-family: 'Roboto', sans-serif;
        }

        /* Cabeçalho principal */
        .main-header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(90deg, #FFC300, #FFD966);
            color: #121212;
            font-size: 28px;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Navbar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #1e1e1e;
            padding: 15px 30px;
            border-bottom: 3px solid #FFC300;
            margin-bottom: 20px;
        }

        .navbar a {
            color: #FFC300;
            text-decoration: none;
            font-weight: bold;
            margin: 0 15px;
            transition: color 0.3s ease;
        }

        .navbar a:hover {
            color: #FFD966;
        }

        /* Cartões de funcionalidades */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }

        .grid-item {
            background-color: #1e1e1e;
            color: #f9e1cd;
            border: 2px solid #FFC300;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .grid-item:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
        }

        /* Botões */
        .stButton>button {
            background: linear-gradient(90deg, #FFC300, #FFD966);
            color: #121212;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            transition: background 0.3s ease, transform 0.3s ease;
        }

        .stButton>button:hover {
            background: #FFD966;
            transform: scale(1.05);
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #1e1e1e;
            color: #FFC300;
            border-top: 2px solid #FFC300;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
    <div class="navbar">
        <div><b>Amadelli Dashboard</b></div>
        <div>
            <a href="#treinamentos">Treinamentos</a>
            <a href="#ia">Assistente de IA</a>
            <a href="#painel">Painel do Funcionário</a>
            <a href="#relatorios">Relatórios</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Cabeçalho principal
st.markdown('<div class="main-header">Bem-vindo ao Sistema da Amadelli!</div>', unsafe_allow_html=True)

# Layout com seções interativas em cartões
st.markdown("""
    <div class="grid-container">
        <div class="grid-item">
            <h3>Cálculo de Carga</h3>
            <p>Simule o carregamento ideal com base no tipo de caminhão.</p>
        </div>
        <div class="grid-item">
            <h3>Rastreabilidade</h3>
            <p>Monitore turnos e melhore os processos de produção.</p>
        </div>
        <div class="grid-item">
            <h3>Treinamentos</h3>
            <p>Acesse cursos personalizados para sua área de atuação.</p>
        </div>
        <div class="grid-item">
            <h3>Relatórios</h3>
            <p>Visualize a produtividade e alcance de metas.</p>
        </div>
        <div class="grid-item">
            <h3>Delli AI</h3>
            <p>Obtenha respostas rápidas e soluções com a inteligência artificial personalizada.</p>
        </div>
        <div class="grid-item">
            <h3>Painel do Funcionário</h3>
            <p>Acompanhe seu progresso e metas alcançadas.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Funcionalidades interativas dinâmicas
menu = st.sidebar.selectbox(
    "Selecione uma funcionalidade:",
    ["Cálculo de Carga", "Rastreabilidade", "Treinamentos", "Delli AI", "Relatórios", "Painel do Funcionário"]
)

# Conteúdo dinâmico baseado no menu selecionado
if menu == "Cálculo de Carga":
    st.header("Cálculo de Carga")
    tipo_caminhao = st.selectbox(
        "Selecione o tipo de caminhão:",
        ["Volks 4 portas", "Volks 5 portas", "Volks 6 portas", "Volks 7 portas"]
    )
    quantidade_caixas = st.number_input("Quantidade de caixas:", min_value=1, step=1)
    if st.button("Calcular"):
        fiadas_altas = quantidade_caixas // 10
        caixas_restantes = quantidade_caixas % 10
        st.success(f"{fiadas_altas} fiadas altas e {caixas_restantes} caixas restantes.")

elif menu == "Rastreabilidade":
    st.header("Rastreabilidade")
    st.write("Aqui você monitora os processos de produção e identifica melhorias.")

elif menu == "Treinamentos":
    st.header("Treinamentos")
    st.write("Explore nossos treinamentos e cursos personalizados.")

elif menu == "Delli AI":
    st.header("Delli AI")
    st.text_input("Pergunte algo à Delli AI:")

elif menu == "Relatórios":
    st.header("Relatórios")
    st.line_chart([10, 20, 30, 40, 50])

elif menu == "Painel do Funcionário":
    st.header("Painel do Funcionário")
    st.progress(70)

# Footer
st.markdown('<div class="footer">© 2024 Amadelli Alimentos. Todos os direitos reservados.</div>', unsafe_allow_html=True)
