import streamlit as st
from PIL import Image
import base64
import sqlite3
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import altair as alt
import random
import time
from streamlit_folium import st_folium
import folium

# Configurações gerais e estilo do app
def set_global_styles():
    st.set_page_config(
        page_title="Amadelli Interactive Dashboard",
        page_icon="🍴",
        layout="wide",
    )
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to bottom, #333333, #1e1e1e);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #2f2f2f;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_global_styles()

# Função para carregar imagem de fundo
def set_background(image_path):
    with open(image_path, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/png;base64,{encoded_image});
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Início do app
st.title("Amadelli Interactive Dashboard")
st.markdown("### Bem-vindo ao sistema mais avançado da **Amadelli Food Service**.")

# Barra de Navegação Lateral
menu = st.sidebar.radio(
    "Menu de Navegação",
    ["Visão Geral", "Relatórios", "Treinamentos", "Delli IA", "Configurações"]
)

# Placeholder para conteúdo dinâmico
placeholder = st.empty()

# Função para animação simples no título
def animated_title():
    for _ in range(2):
        st.markdown(
            """
            <style>
            h1 {
                animation: glow 1.5s infinite;
            }
            @keyframes glow {
                0% {text-shadow: 0 0 5px #FFC300, 0 0 10px #FFC300;}
                50% {text-shadow: 0 0 20px #FF5733, 0 0 40px #FF5733;}
                100% {text-shadow: 0 0 5px #FFC300, 0 0 10px #FFC300;}
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(0.5)

# Cabeçalho principal animado
st.markdown(
    """
    <style>
    h1 {
        color: #FFC300;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        font-family: 'Verdana', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Amadelli Interactive Dashboard")
animated_title()
st.markdown("---")

# Função para aplicar temas personalizados
def apply_theme(theme_name):
    if theme_name == "Claro":
        st.markdown(
            """
            <style>
            body {
                background-color: #FFFFFF;
                color: #000000;
            }
            .stSidebar {
                background-color: #F0F0F0;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif theme_name == "Escuro":
        st.markdown(
            """
            <style>
            body {
                background-color: #1A1A1A;
                color: #FFFFFF;
            }
            .stSidebar {
                background-color: #2E2E2E;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif theme_name == "Amadelli":
        st.markdown(
            """
            <style>
            body {
                background: linear-gradient(180deg, #FFC300, #FF5733);
                color: #FFFFFF;
            }
            .stSidebar {
                background-color: #FFC300;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Adicionando escolha de tema no menu lateral
st.sidebar.header("⚙️ Personalização")
selected_theme = st.sidebar.selectbox(
    "Selecione o tema:",
    ["Claro", "Escuro", "Amadelli"],
    index=2
)
apply_theme(selected_theme)

# Novo menu interativo com ícones
menu_options = {
    "Visão Geral": "📊",
    "Relatórios": "📄",
    "Treinamentos": "📚",
    "Delli AI": "🤖",
    "Configurações": "⚙️"
}
menu = st.sidebar.radio(
    "Menu de Navegação",
    options=list(menu_options.keys()),
    format_func=lambda option: f"{menu_options[option]} {option}",
)

# Estilo moderno do menu
st.sidebar.markdown(
    """
    <style>
    .stSidebar .css-1d391kg {
        background: linear-gradient(to bottom, #FFC300, #FF5733);
        border-radius: 10px;
        color: white;
        font-weight: bold;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibição da seleção no cabeçalho
st.markdown(
    f"""
    <style>
    h2 {{
        text-align: center;
        font-family: 'Arial', sans-serif;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
        color: #FF5733;
    }}
    </style>
    <h2>{menu}</h2>
    """,
    unsafe_allow_html=True,
)

if menu == "Visão Geral":
    st.markdown("Bem-vindo à **Visão Geral**. Explore os principais indicadores e métricas da empresa.")
elif menu == "Relatórios":
    st.markdown("**Relatórios** detalhados para análise de desempenho.")
elif menu == "Treinamentos":
    st.markdown("Acesse os **Treinamentos Interativos** e acompanhe seu progresso.")
elif menu == "Delli AI":
    st.markdown("Interaja com a **Delli AI** para suporte inteligente.")
elif menu == "Configurações":
    st.markdown("Personalize suas preferências no painel de **Configurações**.")

# Dados fictícios para gráficos de relatórios
import pandas as pd
import plotly.express as px
import altair as alt

data_relatorio = pd.DataFrame({
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
    "Produção (toneladas)": [120, 150, 110, 170, 190],
    "Vendas (toneladas)": [100, 140, 105, 160, 180],
    "Erros de Produção (%)": [5, 4, 6, 3, 2],
    "Eficiência (%)": [90, 92, 88, 95, 97]
})

# Painel de Relatórios Avançados
if menu == "Relatórios":
    st.header("📊 Relatórios de Desempenho")
    
    # Seção de Filtros
    st.subheader("🔍 Filtros")
    filtro_mes = st.selectbox("Selecione o mês para análise:", data_relatorio["Mês"])
    filtro_categoria = st.multiselect(
        "Selecione as categorias para visualização:",
        ["Produção", "Vendas", "Erros de Produção", "Eficiência"]
    )
    
    # Gráfico de Produção e Vendas
    if "Produção" in filtro_categoria or "Vendas" in filtro_categoria:
        st.subheader("📈 Produção e Vendas")
        fig = px.bar(
            data_relatorio,
            x="Mês",
            y=["Produção (toneladas)", "Vendas (toneladas)"],
            barmode="group",
            title="Produção vs. Vendas",
            labels={"value": "Toneladas", "variable": "Categoria"},
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico de Erros e Eficiência
    if "Erros de Produção" in filtro_categoria or "Eficiência" in filtro_categoria:
        st.subheader("📉 Erros e Eficiência")
        fig = alt.Chart(data_relatorio).mark_line(point=True).encode(
            x="Mês",
            y=alt.Y("Erros de Produção (%)", axis=alt.Axis(title="Percentual (%)")),
            color=alt.value("red"),
        ) + alt.Chart(data_relatorio).mark_line(point=True).encode(
            x="Mês",
            y=alt.Y("Eficiência (%)", axis=alt.Axis(title="Percentual (%)")),
            color=alt.value("green"),
        )
        st.altair_chart(fig, use_container_width=True)
    
    # Tabela detalhada
    st.subheader("📋 Dados Detalhados")
    st.dataframe(data_relatorio, use_container_width=True)
    
    # Botão de download do relatório
    st.download_button(
        label="📥 Baixar Relatório em CSV",
        data=data_relatorio.to_csv(index=False).encode("utf-8"),
        file_name="relatorio_desempenho.csv",
        mime="text/csv"
    )

# Notificações em Tempo Real
import random
import time
from datetime import datetime

def gerar_notificacoes():
    notificacoes = [
        "📢 Nova meta atingida! Produção ultrapassou 200 toneladas este mês.",
        "⚠️ Aviso: Manutenção programada para 15/12 na unidade São Paulo.",
        "🎉 Parabéns! Funcionário do mês: Maria Santos.",
        "🔔 Relatório semanal disponível para download."
    ]
    return random.choice(notificacoes)

# Seção de Notificações no Menu Lateral
st.sidebar.header("🔔 Notificações em Tempo Real")
notificacoes_placeholder = st.sidebar.empty()

# Loop para exibir notificações a cada 10 segundos
if st.sidebar.button("Iniciar Notificações"):
    for _ in range(5):  # Limite para 5 notificações (ou ajuste conforme necessário)
        notificacao_atual = gerar_notificacoes()
        notificacoes_placeholder.warning(notificacao_atual)
        time.sleep(10)

# Animação de Destaques no Dashboard Principal
if menu == "Visão Geral":
    st.header("🔥 Destaques da Semana")
    st.markdown(
        """
        <style>
        .destaque {
            font-size: 20px;
            font-weight: bold;
            color: #FF5733;
            animation: piscar 1.5s infinite;
        }
        @keyframes piscar {
            0% {opacity: 1;}
            50% {opacity: 0.5;}
            100% {opacity: 1;}
        }
        </style>
        <div class="destaque">🚀 Recorde de Produção Mensal: 200 toneladas alcançadas!</div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Resumo Rápido")
    col1, col2, col3 = st.columns(3)
    col1.metric("Produção Atual", "200 toneladas", "+10%")
    col2.metric("Vendas Totais", "180 toneladas", "+8%")
    col3.metric("Eficiência", "95%", "+2%")

# Adicionando Informações Dinâmicas ao Rodapé
st.markdown("---")
st.markdown(
    f"""
    <footer style="text-align: center; padding: 10px; font-size: 14px; color: #f9e1cd;">
        Atualizado às {datetime.now().strftime("%H:%M:%S")} | © 2024 Amadelli Food Service
    </footer>
    """,
    unsafe_allow_html=True
)

# Notificações em Tempo Real
import random
import time
from datetime import datetime

def gerar_notificacoes():
    notificacoes = [
        "📢 Nova meta atingida! Produção ultrapassou 200 toneladas este mês.",
        "⚠️ Aviso: Manutenção programada para 15/12 na unidade São Paulo.",
        "🎉 Parabéns! Funcionário do mês: Maria Santos.",
        "🔔 Relatório semanal disponível para download."
    ]
    return random.choice(notificacoes)

# Seção de Notificações no Menu Lateral
st.sidebar.header("🔔 Notificações em Tempo Real")
notificacoes_placeholder = st.sidebar.empty()

# Loop para exibir notificações a cada 10 segundos
if st.sidebar.button("Iniciar Notificações"):
    for _ in range(5):  # Limite para 5 notificações (ou ajuste conforme necessário)
        notificacao_atual = gerar_notificacoes()
        notificacoes_placeholder.warning(notificacao_atual)
        time.sleep(10)

# Animação de Destaques no Dashboard Principal
if menu == "Visão Geral":
    st.header("🔥 Destaques da Semana")
    st.markdown(
        """
        <style>
        .destaque {
            font-size: 20px;
            font-weight: bold;
            color: #FF5733;
            animation: piscar 1.5s infinite;
        }
        @keyframes piscar {
            0% {opacity: 1;}
            50% {opacity: 0.5;}
            100% {opacity: 1;}
        }
        </style>
        <div class="destaque">🚀 Recorde de Produção Mensal: 200 toneladas alcançadas!</div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Resumo Rápido")
    col1, col2, col3 = st.columns(3)
    col1.metric("Produção Atual", "200 toneladas", "+10%")
    col2.metric("Vendas Totais", "180 toneladas", "+8%")
    col3.metric("Eficiência", "95%", "+2%")

# Adicionando Informações Dinâmicas ao Rodapé
st.markdown("---")
st.markdown(
    f"""
    <footer style="text-align: center; padding: 10px; font-size: 14px; color: #f9e1cd;">
        Atualizado às {datetime.now().strftime("%H:%M:%S")} | © 2024 Amadelli Food Service
    </footer>
    """,
    unsafe_allow_html=True
)

# Gráficos Interativos no Dashboard
import plotly.express as px
import pandas as pd

# Dados fictícios de desempenho mensal
data = pd.DataFrame({
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"],
    "Produção (Ton)": [120, 140, 150, 160, 170, 200],
    "Vendas (Ton)": [100, 130, 145, 155, 165, 190],
    "Eficiência (%)": [85, 87, 89, 90, 92, 95]
})

if menu == "Visão Geral":
    st.header("📊 Gráficos de Desempenho")

    # Filtro para selecionar o tipo de gráfico
    tipo_grafico = st.radio(
        "Selecione o Tipo de Gráfico:",
        ["Produção Mensal", "Vendas Mensais", "Eficiência (%)"],
        index=0
    )

    # Renderizando gráficos com base na escolha
    if tipo_grafico == "Produção Mensal":
        fig = px.bar(
            data,
            x="Mês",
            y="Produção (Ton)",
            title="Produção Mensal",
            labels={"Produção (Ton)": "Toneladas Produzidas"},
            color="Produção (Ton)",
            text="Produção (Ton)"
        )
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_grafico == "Vendas Mensais":
        fig = px.line(
            data,
            x="Mês",
            y="Vendas (Ton)",
            title="Vendas Mensais",
            labels={"Vendas (Ton)": "Toneladas Vendidas"},
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_grafico == "Eficiência (%)":
        fig = px.area(
            data,
            x="Mês",
            y="Eficiência (%)",
            title="Eficiência Mensal",
            labels={"Eficiência (%)": "Percentual de Eficiência"},
            color_discrete_sequence=["#FFC300"]
        )
        st.plotly_chart(fig, use_container_width=True)

    # Adicionando Métricas ao Lado dos Gráficos
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Produção Atual", f"{data['Produção (Ton)'].iloc[-1]} toneladas", "+10%")
    col2.metric("Vendas Totais", f"{data['Vendas (Ton)'].iloc[-1]} toneladas", "+8%")
    col3.metric("Eficiência", f"{data['Eficiência (%)'].iloc[-1]}%", "+3%")

# Gráfico de Comparação Interativa no Menu Relatórios
if menu == "Relatórios":
    st.header("📈 Comparativo de Produção e Vendas")

    # Gráfico combinado
    fig_combined = px.bar(
        data,
        x="Mês",
        y=["Produção (Ton)", "Vendas (Ton)"],
        barmode="group",
        title="Comparativo de Produção e Vendas",
        labels={"value": "Toneladas", "variable": "Categoria"}
    )
    st.plotly_chart(fig_combined, use_container_width=True)

    # Estatísticas adicionais
    st.subheader("📊 Estatísticas Gerais")
    st.markdown(f"- **Maior Produção:** {data['Produção (Ton)'].max()} toneladas em {data.loc[data['Produção (Ton)'].idxmax(), 'Mês']}.")
    st.markdown(f"- **Maior Venda:** {data['Vendas (Ton)'].max()} toneladas em {data.loc[data['Vendas (Ton)'].idxmax(), 'Mês']}.")
    st.markdown(f"- **Eficiência Máxima:** {data['Eficiência (%)'].max()}% em {data.loc[data['Eficiência (%)'].idxmax(), 'Mês']}.")

# Adicionando botão para exportação de dados
if menu == "Relatórios":
    st.markdown("---")
    st.subheader("📂 Exportar Relatórios")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Dados em CSV",
        data=csv,
        file_name="relatorio_dados.csv",
        mime="text/csv"
    )

import sqlite3

# Configuração inicial do banco de dados
def setup_database():
    conn = sqlite3.connect("amadelli_app.db")
    cursor = conn.cursor()
    
    # Tabela para usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        feedback TEXT
    )
    """)

    # Tabela para relatórios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Tabela para feedbacks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        feedback TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    conn.close()

# Inserir dados de exemplo no banco
def insert_sample_data():
    conn = sqlite3.connect("amadelli_app.db")
    cursor = conn.cursor()
    
    # Inserir dados de exemplo para relatórios
    cursor.execute("INSERT INTO reports (title, content) VALUES (?, ?)", 
                   ("Relatório de Produção", "Produção de 150 toneladas em Novembro."))
    cursor.execute("INSERT INTO reports (title, content) VALUES (?, ?)", 
                   ("Relatório de Vendas", "Vendas de 140 toneladas em Novembro."))
    
    conn.commit()
    conn.close()

# Exibir dados de relatórios no app
def display_reports_from_db():
    conn = sqlite3.connect("amadelli_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, content, created_at FROM reports")
    reports = cursor.fetchall()
    conn.close()

    st.subheader("📄 Relatórios Salvos")
    for report in reports:
        title, content, created_at = report
        st.markdown(f"### {title}")
        st.markdown(f"*Criado em:* {created_at}")
        st.write(content)
        st.markdown("---")

# Adicionar feedback ao banco de dados
def add_feedback(name, email, feedback_text):
    conn = sqlite3.connect("amadelli_app.db")
    cursor = conn.cursor()

    # Verificar se o usuário já existe
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if not user:
        # Criar um novo usuário
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
    
    user_id = user[0]
    
    # Inserir o feedback
    cursor.execute("INSERT INTO feedbacks (user_id, feedback) VALUES (?, ?)", (user_id, feedback_text))
    conn.commit()
    conn.close()
    st.success("Feedback enviado com sucesso!")

# Configuração inicial do banco de dados e dados de exemplo
setup_database()
insert_sample_data()

# Exibindo relatórios no menu "Relatórios"
if menu == "Relatórios":
    st.header("📑 Relatórios do Banco de Dados")
    display_reports_from_db()

# Formulário para enviar feedback no menu "Configurações"
if menu == "Configurações":
    st.header("📝 Envie Seu Feedback")

    with st.form("feedback_form"):
        name = st.text_input("Nome:")
        email = st.text_input("E-mail:")
        feedback_text = st.text_area("Seu Feedback:")
        submitted = st.form_submit_button("Enviar Feedback")
        
        if submitted and name and email and feedback_text:
            add_feedback(name, email, feedback_text)

import plotly.graph_objects as go
import altair as alt

# Dados simulados para gráficos
def generate_sample_data():
    data = pd.DataFrame({
        "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"],
        "Produção (ton)": [120, 130, 140, 150, 160, 170],
        "Vendas (ton)": [110, 120, 130, 140, 150, 160],
        "Desempenho (%)": [85, 87, 90, 92, 94, 96]
    })
    return data

# Exibir gráficos no menu "Visão Geral"
def display_charts(data):
    st.subheader("📊 Gráficos de Desempenho")

    col1, col2 = st.columns(2)

    # Gráfico de barras com Plotly
    with col1:
        st.markdown("### Produção Mensal")
        bar_chart = px.bar(
            data,
            x="Mês",
            y="Produção (ton)",
            title="Produção por Mês",
            color="Mês",
            text="Produção (ton)",
            labels={"Produção (ton)": "Toneladas"}
        )
        st.plotly_chart(bar_chart, use_container_width=True)

    # Gráfico de linhas com Altair
    with col2:
        st.markdown("### Desempenho e Vendas")
        line_chart = alt.Chart(data).mark_line(point=True).encode(
            x="Mês",
            y="Desempenho (%)",
            color=alt.value("#FFC300"),
            tooltip=["Mês", "Desempenho (%)"]
        ).interactive()

        sales_chart = alt.Chart(data).mark_line(point=True, color="blue").encode(
            x="Mês",
            y="Vendas (ton)",
            tooltip=["Mês", "Vendas (ton)"]
        ).interactive()

        combined_chart = alt.layer(line_chart, sales_chart).resolve_scale(
            y="independent"
        ).properties(
            title="Comparação de Desempenho e Vendas"
        )

        st.altair_chart(combined_chart, use_container_width=True)

# Adicionar painel de indicadores rápidos
def display_quick_indicators(data):
    st.markdown("### 📈 Indicadores Rápidos")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Produção Atual", value=f"{data['Produção (ton)'].iloc[-1]} ton", delta="+10 ton")
    with col2:
        st.metric(label="Vendas Atuais", value=f"{data['Vendas (ton)'].iloc[-1]} ton", delta="+10 ton")
    with col3:
        st.metric(label="Desempenho", value=f"{data['Desempenho (%)'].iloc[-1]}%", delta="+2%")

# Adicionar análises interativas no menu "Relatórios"
def interactive_analysis(data):
    st.subheader("📊 Análise Interativa de Dados")

    col1, col2 = st.columns([2, 1])

    # Selecionar métrica para análise
    with col2:
        metric = st.selectbox("Selecione uma métrica:", data.columns[1:])

    # Gráfico interativo com a métrica escolhida
    with col1:
        st.markdown(f"### Análise de {metric}")
        chart = alt.Chart(data).mark_bar().encode(
            x="Mês",
            y=metric,
            color="Mês",
            tooltip=["Mês", metric]
        ).interactive()

        st.altair_chart(chart, use_container_width=True)

# Exibição no menu "Visão Geral" e "Relatórios"
data = generate_sample_data()

if menu == "Visão Geral":
    st.header("📊 Visão Geral - Indicadores e Desempenho")
    display_quick_indicators(data)
    display_charts(data)

if menu == "Relatórios":
    st.header("📑 Relatórios Detalhados")
    interactive_analysis(data)

# Delli AI - Configuração e Destaque
import openai

# Configuração da API da OpenAI
openai.api_key = "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"

# Função para consultar a API da OpenAI
def delli_ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao processar a resposta: {e}"

# Interface da Delli AI no Streamlit
def delli_ai_interface():
    st.header("🤖 Delli AI - Sua Assistente Inteligente")

    # Fundo estilizado
    st.markdown(
        """
        <style>
        .delli-header {
            background: linear-gradient(90deg, #FFC300, #FF5733);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .delli-box {
            border: 2px solid #FFC300;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }
        </style>
        <div class="delli-header">Delli AI - O Futuro da Amadelli</div>
        """,
        unsafe_allow_html=True,
    )

    # Entrada de dados
    st.markdown("<div class='delli-box'>Digite sua pergunta abaixo:</div>", unsafe_allow_html=True)
    question = st.text_input("Pergunta para a Delli AI:")

    # Botão de envio
    if st.button("Perguntar"):
        if question:
            with st.spinner("Delli AI está pensando..."):
                prompt = f"""
                Você é Delli AI, uma assistente virtual da Amadelli. Responda à pergunta de forma clara, amigável e objetiva:
                {question}
                """
                answer = delli_ai_response(prompt)
                st.success("Resposta da Delli AI:")
                st.markdown(f"**{answer}**")
        else:
            st.error("Por favor, insira uma pergunta.")

    # Destaque visual e animação
    st.markdown(
        """
        <div style="text-align: center;">
            <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_kwi1f9iv.json" 
                background="transparent" 
                speed="1" 
                style="width: 300px; height: 300px;" 
                loop 
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Histórico de perguntas e respostas
    st.subheader("📜 Histórico de Interações")
    if "delli_history" not in st.session_state:
        st.session_state["delli_history"] = []

    if question:
        st.session_state["delli_history"].append({"Pergunta": question, "Resposta": answer})

    for interaction in st.session_state["delli_history"]:
        st.markdown(f"**Pergunta:** {interaction['Pergunta']}")
        st.markdown(f"*Resposta:* {interaction['Resposta']}")
        st.markdown("---")

# Adicionar Delli AI ao menu principal
if menu == "Delli AI":
    delli_ai_interface()

# Dashboard Avançado - Indicadores e Widgets
def dashboard_avancado():
    st.header("📊 Painel de Controle - Dashboard Interativo")
    
    # Estilo visual do painel
    st.markdown(
        """
        <style>
        .dashboard-header {
            background: linear-gradient(90deg, #FF5733, #FFC300);
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #FFC300;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        </style>
        <div class="dashboard-header">Dashboard Interativo</div>
        """,
        unsafe_allow_html=True,
    )

    # Indicadores rápidos
    st.markdown("### 🔎 Indicadores Rápidos")
    col1, col2, col3 = st.columns(3)
    col1.markdown("<div class='card'><h3>Produção</h3><p>1,200 ton</p></div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'><h3>Vendas</h3><p>950 ton</p></div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'><h3>Eficiência</h3><p>88%</p></div>", unsafe_allow_html=True)

    # Gráficos interativos
    st.markdown("---")
    st.subheader("📈 Gráficos de Desempenho")

    # Dados fictícios para gráficos
    data = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai"],
        "Produção (ton)": [120, 140, 160, 150, 180],
        "Vendas (ton)": [100, 120, 140, 130, 150],
    })

    # Gráfico de barras - Produção
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Produção Mensal**")
        fig = px.bar(data, x="Mês", y="Produção (ton)", title="Produção Mensal")
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico de linha - Vendas
    with col2:
        st.markdown("**Vendas Mensais**")
        fig = px.line(data, x="Mês", y="Vendas (ton)", markers=True, title="Vendas Mensais")
        st.plotly_chart(fig, use_container_width=True)

    # Widgets interativos
    st.markdown("---")
    st.subheader("⚙️ Configurações Interativas")

    col1, col2 = st.columns(2)
    with col1:
        filtro_mes = st.selectbox("Selecione o Mês:", data["Mês"])
        st.write(f"Você selecionou: {filtro_mes}")

    with col2:
        progresso = st.slider("Progresso Atual (%)", 0, 100, 50)
        st.progress(progresso / 100)

    # Animações e Destaques
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_kgsp5rhv.json" 
                background="transparent" 
                speed="1" 
                style="width: 300px; height: 300px;" 
                loop 
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Adicionar ao menu principal
if menu == "Visão Geral":
    dashboard_avancado()

# Interface Avançada da Delli AI
def delli_ai_interativa():
    st.header("🤖 Delli AI - Sua Assistente Inteligente")

    # Estilo personalizado para a seção
    st.markdown(
        """
        <style>
        .delli-header {
            background: linear-gradient(90deg, #FFC300, #FF5733);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
        }
        .delli-card {
            background: white;
            border: 2px solid #FFC300;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .delli-chat {
            background: #f9f9f9;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
        }
        </style>
        <div class="delli-header">Converse com a Delli AI</div>
        """,
        unsafe_allow_html=True,
    )

    # Caixa de diálogo interativa
    st.markdown("### 📝 Pergunte à Delli AI")
    with st.form(key="delli_chat_form"):
        pergunta = st.text_input("Digite sua pergunta:")
        enviar = st.form_submit_button("Enviar")

    # Configuração da API da OpenAI
    import openai
    openai.api_key = "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"

    if enviar and pergunta:
        with st.spinner("A Delli AI está processando sua pergunta..."):
            try:
                # Geração de resposta pela OpenAI
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Você é a Delli AI da Amadelli. Responda de forma clara e útil à pergunta: {pergunta}",
                    max_tokens=150,
                    temperature=0.7,
                )
                resposta = response.choices[0].text.strip()
            except Exception as e:
                resposta = f"Erro ao processar sua solicitação: {str(e)}"
        
        # Exibir resposta em um card estilizado
        st.markdown(
            f"""
            <div class="delli-card">
                <strong>Pergunta:</strong>
                <div class="delli-chat">{pergunta}</div>
                <strong>Resposta:</strong>
                <div class="delli-chat">{resposta}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Seção de feedback
    st.markdown("---")
    st.subheader("💬 Dê seu feedback sobre a Delli AI")
    feedback = st.text_area("Como podemos melhorar a Delli AI?")
    if st.button("Enviar Feedback"):
        st.success("Obrigado pelo seu feedback! Ele será analisado pela nossa equipe.")

    # Adicionando animações para a Delli AI
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <lottie-player src="https://assets10.lottiefiles.com/private_files/lf30_jil3zhtu.json" 
                background="transparent" 
                speed="1" 
                style="width: 300px; height: 300px;" 
                loop 
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Adicionar ao menu principal
if menu == "Delli AI":
    delli_ai_interativa()

# Visualizações Avançadas de Indicadores e Animações
def visualizacoes_avancadas():
    st.header("📊 Painel de Indicadores")

    # Indicadores principais com visual aprimorado
    st.markdown(
        """
        <style>
        .indicator-box {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .indicator {
            background: linear-gradient(90deg, #FFC300, #FF5733);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 25%;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            font-size: 18px;
        }
        </style>
        <div class="indicator-box">
            <div class="indicator">
                <strong>Produção Mensal</strong>
                <p>1,200 toneladas</p>
            </div>
            <div class="indicator">
                <strong>Pedidos Processados</strong>
                <p>5,400 pedidos</p>
            </div>
            <div class="indicator">
                <strong>Eficiência</strong>
                <p>94%</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Animações para engajamento
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_kDX32M.json" 
                background="transparent" 
                speed="1" 
                style="width: 300px; height: 300px;" 
                loop 
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Painel interativo com dados fictícios
    st.markdown("### 📈 Tendências")
    import altair as alt
    import pandas as pd

    # Dados fictícios
    data = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Produção (Toneladas)': [1000, 1100, 1200, 1250, 1400, 1500],
        'Pedidos Processados': [4000, 4200, 4500, 4800, 5000, 5400]
    })

    # Gráfico de barras
    bar_chart = alt.Chart(data).mark_bar().encode(
        x='Mês',
        y='Produção (Toneladas)',
        color=alt.value('#FFC300')
    ).properties(title="Produção Mensal")

    # Gráfico de linha
    line_chart = alt.Chart(data).mark_line(point=True).encode(
        x='Mês',
        y='Pedidos Processados',
        color=alt.value('#FF5733')
    ).properties(title="Pedidos Processados Mensalmente")

    col1, col2 = st.columns(2)
    with col1:
        st.altair_chart(bar_chart, use_container_width=True)
    with col2:
        st.altair_chart(line_chart, use_container_width=True)

    # Exportação de gráficos
    st.markdown("### 📥 Exportar Gráficos")
    st.download_button(
        label="Baixar Produção (CSV)",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name='producao.csv',
        mime='text/csv',
    )

    # Feedback interativo com emojis
    st.markdown("### 📢 Feedback Rápido")
    feedback_col1, feedback_col2, feedback_col3 = st.columns(3)
    with feedback_col1:
        st.button("😃 Satisfeito")
    with feedback_col2:
        st.button("😐 Indiferente")
    with feedback_col3:
        st.button("☹️ Insatisfeito")

# Adicionar ao menu principal
if menu == "Indicadores":
    visualizacoes_avancadas()

# Seção Delli AI com Visual Melhorado
def delli_ai_interface():
    st.header("🤖 Delli AI - Sua Assistente Inteligente")
    st.markdown(
        """
        <style>
        .delli-header {
            font-size: 24px;
            color: #FF5733;
            text-align: center;
            font-weight: bold;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
        }
        .chat-container {
            border: 2px solid #FFC300;
            border-radius: 15px;
            padding: 20px;
            background: rgba(255, 243, 176, 0.1);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            color: #333;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .delli-response {
            color: #FF5733;
            font-style: italic;
            margin-bottom: 20px;
        }
        </style>
        """
    )

    # Configurar API OpenAI
    import openai
    openai.api_key = "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"

    # Função para interagir com a OpenAI
    def gerar_resposta(pergunta):
        try:
            resposta = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Delli AI, uma assistente focada em suporte técnico e orientações para o sistema Amadelli. Responda de forma clara e útil: {pergunta}",
                max_tokens=150,
                temperature=0.7
            )
            return resposta.choices[0].text.strip()
        except Exception as e:
            return f"Erro ao acessar a API da OpenAI: {str(e)}"

    # Interface de Chat
    with st.container():
        st.markdown("<h2 class='delli-header'>Converse com a Delli AI</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="chat-container">
                <p style="text-align: center;">Digite sua dúvida e a Delli AI ajudará você!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Campo de entrada de pergunta
        pergunta = st.text_input("Digite sua pergunta aqui:")
        if pergunta:
            with st.spinner("Delli AI está pensando..."):
                resposta = gerar_resposta(pergunta)
                st.markdown(
                    f"""
                    <div class="chat-container">
                        <p class="user-message">Você: {pergunta}</p>
                        <p class="delli-response">Delli AI: {resposta}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Adicionar Animação à Interface
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_i8yvxdkr.json"  
                background="transparent"  
                speed="1"  
                style="width: 300px; height: 300px;"  
                loop  
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Feedback sobre a resposta
    st.markdown("### 📢 Avalie a Resposta")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("👍 Útil")
    with col2:
        st.button("👎 Não Útil")
    with col3:
        st.button("🤔 Precisa Melhorar")

# Adicionar ao menu principal
if menu == "Delli AI":
    delli_ai_interface()

# Seção de Destaques com Visual Impactante
def destaque_dashboard():
    st.markdown(
        """
        <style>
        .destaques-container {
            padding: 20px;
            background: linear-gradient(145deg, #FF5733, #FFC300);
            border-radius: 15px;
            color: white;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .destaques-header {
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .destaques-content {
            font-size: 18px;
        }
        </style>
        <div class="destaques-container">
            <h2 class="destaques-header">🎯 Destaques do Dia</h2>
            <p class="destaques-content">Acompanhe os principais indicadores e novidades!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Produção", "1.250 ton", "+15%")
    with col2:
        st.metric("Vendas", "R$ 2.1M", "+8%")
    with col3:
        st.metric("Eficiência", "94%", "+3%")

# Gráficos Dinâmicos com Interatividade
def graficos_interativos():
    st.subheader("📊 Análise de Dados Interativa")
    st.markdown(
        """
        <style>
        .graph-section {
            border: 2px solid #FFC300;
            border-radius: 10px;
            padding: 15px;
            background: rgba(255, 195, 0, 0.1);
            margin-bottom: 20px;
        }
        </style>
        """
    )

    # Dados para gráficos
    data_graficos = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Produção (Ton)": [1000, 1100, 1200, 1250, 1300, 1350],
        "Vendas (Milhões)": [1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
    })

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='graph-section'>", unsafe_allow_html=True)
        fig1 = px.bar(
            data_graficos,
            x="Mês",
            y="Produção (Ton)",
            title="Produção Mensal",
            color="Mês",
            text="Produção (Ton)"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='graph-section'>", unsafe_allow_html=True)
        fig2 = px.line(
            data_graficos,
            x="Mês",
            y="Vendas (Milhões)",
            markers=True,
            title="Vendas Mensais"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Painel com Notícias Recentes
def noticias_dashboard():
    st.subheader("📰 Últimas Notícias")
    noticias = [
        "📈 Produção do mês ultrapassa 1.250 toneladas pela primeira vez!",
        "🚀 Novo treinamento em liderança será lançado na próxima semana.",
        "🔧 Atualizações no sistema de rastreabilidade em andamento."
    ]
    st.markdown(
        """
        <style>
        .news-item {
            border-left: 4px solid #FF5733;
            padding: 10px;
            margin: 5px 0;
            background: #fdf3e3;
            border-radius: 8px;
        }
        </style>
        """
    )
    for noticia in noticias:
        st.markdown(f"<div class='news-item'>{noticia}</div>", unsafe_allow_html=True)

# Layout Principal do Dashboard
def layout_principal():
    st.title("📊 Dashboard Principal - Amadelli")
    destaque_dashboard()
    st.markdown("---")
    graficos_interativos()
    st.markdown("---")
    noticias_dashboard()

# Adicionando ao menu principal
if menu == "Visão Geral":
    layout_principal()

# Destaque Exclusivo à Delli AI
def delli_ai_interface():
    st.title("🤖 Delli AI - Sua Assistente Virtual")
    st.markdown(
        """
        <style>
        .delli-ai-container {
            border: 2px solid #FFC300;
            border-radius: 15px;
            padding: 20px;
            background: linear-gradient(145deg, #FF5733, #FFC300);
            color: white;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .delli-ai-header {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }
        .delli-ai-input {
            margin-top: 20px;
        }
        </style>
        <div class="delli-ai-container">
            <h2 class="delli-ai-header">Como posso te ajudar hoje?</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Caixa de entrada para perguntas
    pergunta = st.text_input("Pergunte algo à Delli AI:", placeholder="Digite aqui sua dúvida...")
    if st.button("Enviar"):
        if pergunta.strip():
            with st.spinner("A Delli AI está pensando..."):
                resposta = gerar_resposta_delli_ai(pergunta)
                st.success("Resposta gerada com sucesso!")
                st.markdown(f"**Delli AI:** {resposta}")
        else:
            st.error("Por favor, insira uma pergunta válida.")

# Função de Geração de Resposta para a Delli AI
def gerar_resposta_delli_ai(pergunta):
    import openai
    openai.api_key = "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"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"""
            Você é a Delli AI, uma inteligência artificial projetada para atender usuários do sistema Amadelli.
            Responda à pergunta com clareza, precisão e profissionalismo:
            
            Pergunta: {pergunta}
            """,
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

# Animação Exclusiva para a Delli AI
def animacao_delli_ai():
    st.markdown(
        """
        <div style='text-align: center;'>
            <lottie-player src="https://assets4.lottiefiles.com/packages/lf20_touohxv0.json"  
                background="transparent"  
                speed="1"  
                style="width: 300px; height: 300px;"  
                loop  
                autoplay>
            </lottie-player>
        </div>
        """,
        unsafe_allow_html=True
    )

# Página de Finalização
def finalizacao_dashboard():
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h3 style="color: #FFC300;">Obrigado por usar o Amadelli Dashboard!</h3>
            <p>Esperamos que você tenha uma experiência incrível. Para dúvidas ou sugestões, entre em contato conosco.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

# Adicionando ao Menu Principal
if menu == "Delli AI":
    delli_ai_interface()
    animacao_delli_ai()
elif menu == "Configurações":
    finalizacao_dashboard()
