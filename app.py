import streamlit as st
from PIL import Image
import base64

# Carregar imagem de fundo
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
        unsafe_allow_html=True
    )

set_background("DALL-E_2024-12-08_21.27.24.jpg")

# Cabeçalho Principal
st.markdown(
    """
    <style>
    h1, h2 {
        color: #FFC300;
        font-family: 'Arial', sans-serif;
        text-align: center;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Amadelli Interactive Dashboard")
st.markdown("### Bem-vindo ao sistema mais avançado da **Amadelli Food Service**.")

# Barra de Navegação Lateral
menu = st.sidebar.radio(
    "Menu de Navegação",
    ["Visão Geral", "Relatórios", "Treinamentos", "Assistente IA", "Configurações"]
)

# Placeholder para conteúdo dinâmico
placeholder = st.empty()

# Estrutura inicial das seções
if menu == "Visão Geral":
    placeholder.header("Visão Geral")
    placeholder.markdown(
        """
        Explore os principais indicadores e análises da empresa. 
        Visualize os gráficos de desempenho e tome decisões estratégicas.
        """
    )
elif menu == "Relatórios":
    placeholder.header("Relatórios")
    placeholder.markdown("Acesse relatórios detalhados sobre produção, vendas e rastreabilidade.")

elif menu == "Treinamentos":
    placeholder.header("Treinamentos")
    placeholder.markdown("Participe de treinamentos interativos para aperfeiçoar suas habilidades.")

elif menu == "Assistente IA":
    placeholder.header("Assistente IA")
    placeholder.markdown("Converse com a IA Amadelli para suporte instantâneo.")

elif menu == "Configurações":
    placeholder.header("Configurações")
    placeholder.markdown("Personalize sua experiência com o dashboard.")

import time
import numpy as np
import pandas as pd
import plotly.express as px

# Função para animações simples no título
def animated_title():
    for _ in range(3):
        st.markdown(
            """
            <style>
            h1 {
                animation: glow 1.5s infinite;
            }
            @keyframes glow {
                0% {text-shadow: 0 0 10px #FFC300, 0 0 20px #FFC300;}
                50% {text-shadow: 0 0 20px #FF5733, 0 0 30px #FF5733;}
                100% {text-shadow: 0 0 10px #FFC300, 0 0 20px #FFC300;}
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.5)

if menu == "Visão Geral":
    placeholder.empty()
    animated_title()
    
    # Dados Dinâmicos para Gráficos
    data = pd.DataFrame({
        "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
        "Produção (ton)": [120, 130, 110, 150, 170],
        "Vendas (ton)": [100, 120, 105, 140, 160],
    })

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Produção Mensal")
        fig1 = px.bar(data, x="Mês", y="Produção (ton)", color="Mês", title="Produção por Mês")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Vendas Mensais")
        fig2 = px.line(data, x="Mês", y="Vendas (ton)", markers=True, title="Vendas por Mês")
        st.plotly_chart(fig2, use_container_width=True)

    # Indicadores Rápidos
    st.markdown("---")
    st.subheader("Indicadores Rápidos")
    col3, col4, col5 = st.columns(3)
    col3.metric("Produção Atual", "170 ton", "+20 ton")
    col4.metric("Vendas Atuais", "160 ton", "+15 ton")
    col5.metric("Eficiência", "94%", "+3%")

if menu == "Relatórios":
    placeholder.empty()
    placeholder.markdown(
        """
        <style>
        .report-section {
            border: 2px solid #FFC300;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            background: rgba(255, 195, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    placeholder.markdown("<div class='report-section'><h2>Relatório Semanal</h2><p>Veja os dados mais recentes.</p></div>", unsafe_allow_html=True)

# Aguardando mais interações
st.markdown("---")
st.info("Navegue entre as abas laterais para explorar mais funcionalidades.")

# Adicionando seções avançadas no menu
if menu == "Treinamentos":
    st.header("📚 Treinamentos Amadelli")
    
    # Simulador de Progresso
    with st.container():
        st.subheader("Acompanhe seu progresso nos treinamentos")
        progresso = st.slider("Progresso Atual (%)", min_value=0, max_value=100, step=1)
        st.progress(progresso / 100)

        if progresso == 100:
            st.success("Parabéns! Você completou todos os treinamentos.")

    st.markdown("---")

    # Catálogo de Treinamentos
    st.subheader("Catálogo de Treinamentos Disponíveis")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://via.placeholder.com/150", use_column_width=True)
        st.markdown("**Treinamento em Segurança**")
        st.button("Inscreva-se")

    with col2:
        st.image("https://via.placeholder.com/150", use_column_width=True)
        st.markdown("**Manutenção Preventiva**")
        st.button("Inscreva-se")

    with col3:
        st.image("https://via.placeholder.com/150", use_column_width=True)
        st.markdown("**Boas Práticas de Produção**")
        st.button("Inscreva-se")

if menu == "Delli AI":
    st.header("🤖 Assistente de IA - Delli AI")

    # Painel de Perguntas e Respostas
    with st.form("form_pergunta"):
        pergunta = st.text_input("Faça sua pergunta para a Delli AI")
        submit = st.form_submit_button("Enviar")

        if submit and pergunta:
            resposta = f"A Delli AI está analisando sua pergunta: '{pergunta}'"
            st.write(resposta)
    
    st.markdown("---")

    # Área de Chat com Simulação
    st.subheader("Chat Simulado com Delli AI")
    mensagens = ["Como posso melhorar minha produtividade?", "Quais são os relatórios disponíveis?"]
    mensagens_respostas = [
        "Você pode melhorar sua produtividade priorizando tarefas e revisando metas diárias.",
        "Os relatórios disponíveis incluem Relatório Semanal, Eficiência de Máquinas, e Relatório de Produção Mensal.",
    ]

    for i, (msg, resp) in enumerate(zip(mensagens, mensagens_respostas)):
        st.markdown(f"**Usuário:** {msg}")
        st.markdown(f"*Delli AI:* {resp}")
        if i < len(mensagens) - 1:
            st.markdown("---")

# Layout Interativo e Animações
def rotating_banner():
    st.markdown(
        """
        <style>
        @keyframes rotate {
            0% {transform: rotate(0deg);}
            50% {transform: rotate(180deg);}
            100% {transform: rotate(360deg);}
        }
        .rotating {
            animation: rotate 10s infinite linear;
        }
        </style>
        <div class="rotating">
            <h3 style="color:#FFC300;">Destaques da Semana: Novos Treinamentos Disponíveis!</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

rotating_banner()

st.markdown("---")
st.info("Navegue por todas as seções para explorar o app completo.")

# Seção de Relatórios Detalhados
if menu == "Relatórios":
    st.header("📊 Relatórios de Desempenho e Produção")

    # Filtro por Categoria
    st.subheader("Filtrar Relatórios")
    col1, col2 = st.columns(2)

    with col1:
        categoria = st.selectbox(
            "Selecione a Categoria:",
            ["Produção", "Manutenção", "Treinamentos", "Eficiência de Máquinas"],
        )

    with col2:
        periodo = st.date_input("Selecione o Período")

    # Exibindo Relatórios com Gráficos Interativos
    st.markdown(f"### Relatórios - {categoria} ({periodo})")
    if categoria == "Produção":
        st.bar_chart({"Dias": [1, 2, 3, 4, 5], "Produção (ton)": [10, 12, 9, 14, 11]})

    elif categoria == "Manutenção":
        st.line_chart({"Dias": [1, 2, 3, 4, 5], "Tempo (horas)": [2, 1.5, 3, 2.5, 2]})

    elif categoria == "Treinamentos":
        st.area_chart({"Dias": [1, 2, 3, 4, 5], "Participantes": [20, 25, 22, 30, 28]})

    elif categoria == "Eficiência de Máquinas":
        st.line_chart({"Dias": [1, 2, 3, 4, 5], "Eficiência (%)": [85, 90, 88, 92, 89]})

    st.markdown("---")

    # Exportação de Relatórios
    st.subheader("Exportar Relatórios")
    st.download_button(
        label="📥 Baixar Relatório em PDF",
        data="Relatório de exemplo: Desempenho da Semana",
        file_name="relatorio_desempenho.pdf",
        mime="application/pdf",
    )

# Elementos Visuais Modernos e Animações
def glowing_button(label, color="#FFC300", glow_color="#FFD700"):
    st.markdown(
        f"""
        <style>
        .glow-button {{
            background-color: {color};
            border: none;
            color: black;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            box-shadow: 0 0 20px {glow_color};
            transition: box-shadow 0.3s ease-in-out;
        }}
        .glow-button:hover {{
            box-shadow: 0 0 40px {glow_color};
        }}
        </style>
        <button class="glow-button">{label}</button>
        """,
        unsafe_allow_html=True,
    )

# Botões de Destaque na Tela Principal
if menu == "Cálculo de Carga":
    st.subheader("Destaques da Tela")
    glowing_button("🔍 Veja mais detalhes")
    glowing_button("🛠 Ajuste Configurações")

# Integrações com Dados em Tempo Real
st.sidebar.subheader("📡 Dados em Tempo Real")

# Exemplo: Indicador de Eficiência
st.sidebar.metric(label="Eficiência Atual", value="89%", delta="+2%")
st.sidebar.metric(label="Produção Hoje", value="14.2 ton", delta="-1.1 ton")

# Gráfico de Eficiência em Tempo Real
st.sidebar.line_chart({"Tempo (horas)": [1, 2, 3, 4, 5], "Eficiência (%)": [85, 86, 88, 89, 90]})

# Rodapé com Informações Dinâmicas
st.markdown(
    """
    <footer style='text-align: center; padding: 10px; font-size: 14px; color: #f9e1cd;'>
        © 2024 Amadelli Food Service. Todos os direitos reservados.
    </footer>
    """,
    unsafe_allow_html=True,
)

# Página de Treinamentos com Elementos Visuais Dinâmicos
if menu == "Treinamentos":
    st.header("🎓 Treinamentos Personalizados")

    # Animação de Destaque
    st.markdown(
        """
        <div style='text-align: center;'>
            <lottie-player src="https://assets9.lottiefiles.com/packages/lf20_touohxv0.json"  
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

    # Lista de Treinamentos Disponíveis
    st.subheader("📜 Lista de Treinamentos")
    treinamentos = [
        "Segurança na Produção",
        "Manutenção Preventiva",
        "Treinamento de Operadores",
        "Gestão de Qualidade",
    ]

    for treinamento in treinamentos:
        st.write(f"✅ {treinamento}")

    # Módulo de Inscrição
    st.subheader("📅 Inscrição em Treinamentos")
    nome_usuario = st.text_input("Seu Nome:")
    email_usuario = st.text_input("Seu Email:")
    treinamento_selecionado = st.selectbox("Selecione um Treinamento:", treinamentos)
    if st.button("Inscrever-se"):
        st.success(f"Inscrição realizada com sucesso em '{treinamento_selecionado}'!")

# Painel do Funcionário com Gráficos Interativos
if menu == "Painel do Funcionário":
    st.header("👷 Painel do Funcionário")

    # Informações Pessoais
    st.subheader("📋 Dados Pessoais")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nome Completo", value="João da Silva")
        st.text_input("Cargo", value="Operador de Máquinas")
    with col2:
        st.text_input("Turno", value="Diurno")
        st.text_input("Departamento", value="Produção")

    # Gráficos de Desempenho Individual
    st.subheader("📈 Desempenho Individual")
    desempenho_data = {
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai"],
        "Eficiência (%)": [85, 87, 90, 92, 89],
    }
    st.line_chart(desempenho_data)

    # Progresso de Treinamento
    st.subheader("📊 Progresso de Treinamento")
    st.progress(75)

# Adicionando Fundo Animado ao App
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(180deg, #040404, #1a1a1a);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Gráfico em Tempo Real
st.sidebar.subheader("📊 Produção em Tempo Real")
import random
import time

placeholder = st.sidebar.empty()

for i in range(10):
    data = {"Produção": [random.randint(10, 20) for _ in range(5)]}
    placeholder.line_chart(data)
    time.sleep(0.5)

# Animação de Carga Finalizada
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <lottie-player src="https://assets4.lottiefiles.com/packages/lf20_3jwyea7w.json"  
            background="transparent"  
            speed="1"  
            style="width: 400px; height: 400px;"  
            loop  
            autoplay>
        </lottie-player>
    </div>
    """,
    unsafe_allow_html=True,
)

# Melhorias na Página de Configurações
if menu == "Configurações":
    st.header("⚙️ Configurações do Sistema")
    
    # Opções de Tema
    st.subheader("🎨 Escolha o Tema")
    tema = st.selectbox("Selecione um Tema:", ["Claro", "Escuro", "Automático"])
    if tema == "Claro":
        st.success("Tema Claro selecionado.")
    elif tema == "Escuro":
        st.success("Tema Escuro selecionado.")
    else:
        st.success("Tema Automático selecionado com base na hora do dia.")
    
    # Preferências de Notificações
    st.subheader("🔔 Notificações")
    email_notif = st.checkbox("Receber notificações por email")
    sms_notif = st.checkbox("Receber notificações por SMS")
    push_notif = st.checkbox("Receber notificações push")
    
    if st.button("Salvar Configurações"):
        st.success("Configurações salvas com sucesso!")
    
    # Segurança e Privacidade
    st.subheader("🔒 Segurança e Privacidade")
    st.write("Atualize sua senha ou configure a autenticação de dois fatores.")
    nova_senha = st.text_input("Nova Senha", type="password")
    confirmar_senha = st.text_input("Confirmar Senha", type="password")
    if st.button("Atualizar Senha"):
        if nova_senha == confirmar_senha and nova_senha != "":
            st.success("Senha atualizada com sucesso!")
        else:
            st.error("As senhas não coincidem ou estão vazias.")
    
    # Feedback do Usuário
    st.subheader("📝 Feedback")
    feedback = st.text_area("Deixe seu feedback ou sugestão:")
    if st.button("Enviar Feedback"):
        st.success("Obrigado pelo seu feedback!")
    
# Adicionando Animações com Bibliotecas Externas
st.markdown(
    """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.4/lottie.min.js"></script>
    <div id="animation" style="width: 100%; height: 400px;"></div>
    <script>
    var animation = bodymovin.loadAnimation({
        container: document.getElementById('animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'https://assets4.lottiefiles.com/packages/lf20_u4yrau.json'
    })
    </script>
    """,
    unsafe_allow_html=True,
)

# Inserindo Mapas Interativos
st.header("🌍 Localização das Unidades Amadelli")
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[-23.5505, -46.6333], zoom_start=5)

# Marcadores das Unidades
folium.Marker([-23.5505, -46.6333], popup="Unidade São Paulo").add_to(m)
folium.Marker([-22.9068, -43.1729], popup="Unidade Rio de Janeiro").add_to(m)
folium.Marker([-19.9167, -43.9345], popup="Unidade Belo Horizonte").add_to(m)

# Exibindo o mapa no Streamlit
st_data = st_folium(m, width=700)

# Chatbot Integrado com Simulação
if menu == "Assistente IA":
    st.header("🤖 Chatbot Amadelli - Sua Assistente Virtual")
    
    if 'mensagens' not in st.session_state:
        st.session_state['mensagens'] = []
    
    with st.form("form_chat"):
        mensagem_usuario = st.text_input("Você:")
        enviar = st.form_submit_button("Enviar")
    
    if enviar and mensagem_usuario:
        st.session_state['mensagens'].append(("Você", mensagem_usuario))
        # Simulando a resposta do chatbot
        resposta_chatbot = f"Desculpe, ainda estou aprendendo. Você disse: {mensagem_usuario}"
        st.session_state['mensagens'].append(("Chatbot", resposta_chatbot))
    
    # Exibindo a conversa
    for remetente, mensagem in st.session_state['mensagens']:
        if remetente == "Você":
            st.markdown(f"**{remetente}:** {mensagem}")
        else:
            st.markdown(f"*{remetente}:* {mensagem}")
    
    # Opção de limpar a conversa
    if st.button("Limpar Conversa"):
        st.session_state['mensagens'] = []

# Integração com Redes Sociais (Links)
st.sidebar.markdown("### 🔗 Siga-nos nas Redes Sociais")
st.sidebar.markdown("[Facebook](https://www.facebook.com/amadelli)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/amadelli)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/company/amadelli)")

# Melhorias na Responsividade do App
st.markdown(
    """
    <style>
    @media only screen and (max-width: 600px) {
        .stApp {
            background-size: contain;
        }
        .sidebar-content {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Atualizações em Tempo Real com Dados Fictícios
import threading

def update_metrics():
    while True:
        with st.sidebar:
            st.metric(label="Usuários Online", value=f"{random.randint(50, 150)}")
            st.metric(label="Pedidos em Processamento", value=f"{random.randint(20, 80)}")
        time.sleep(5)

thread = threading.Thread(target=update_metrics)
thread.start()

# Dashboard de Relatórios
if menu == "Relatórios":
    st.header("📊 Relatórios Gerenciais")
    st.subheader("Resumo das Operações")
    
    # Gráficos Dinâmicos com Altair
    import altair as alt
    import pandas as pd
    import numpy as np
    
    # Dados fictícios para os relatórios
    data = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Produção (toneladas)': [50, 70, 65, 90, 100, 110],
        'Pedidos Processados': [300, 400, 450, 500, 600, 650]
    })
    
    # Gráfico de barras para produção
    bar_chart = alt.Chart(data).mark_bar().encode(
        x='Mês',
        y='Produção (toneladas)',
        color=alt.value('#FFC300')
    ).properties(title="Produção Mensal")
    
    # Gráfico de linha para pedidos processados
    line_chart = alt.Chart(data).mark_line(point=True).encode(
        x='Mês',
        y='Pedidos Processados',
        color=alt.value('#FF5733')
    ).properties(title="Pedidos Processados Mensalmente")
    
    # Exibindo os gráficos
    st.altair_chart(bar_chart, use_container_width=True)
    st.altair_chart(line_chart, use_container_width=True)
    
    # Detalhes Adicionais
    st.subheader("📄 Relatórios Específicos")
    relatorio = st.selectbox("Selecione um Relatório:", ["Relatório de Vendas", "Relatório de Produção", "Relatório de Eficiência"])
    
    if relatorio == "Relatório de Vendas":
        st.write("Relatório de vendas detalhado será exibido aqui.")
    elif relatorio == "Relatório de Produção":
        st.write("Relatório de produção detalhado será exibido aqui.")
    else:
        st.write("Relatório de eficiência detalhado será exibido aqui.")
    
    # Botão de Download
    if st.button("📥 Baixar Relatório"):
        st.success("Relatório baixado com sucesso!")
    
# Sistema de Notificações ao Vivo
st.sidebar.header("🔔 Notificações Recentes")
notificacoes = [
    "Novo pedido processado na unidade São Paulo.",
    "Treinamento concluído por 10 funcionários.",
    "Manutenção programada para 15/12 na unidade Rio de Janeiro."
]

# Loop para exibir notificações
for notificacao in notificacoes:
    st.sidebar.markdown(f"✅ {notificacao}")
    st.sidebar.markdown("---")

# Melhorias no Layout com Espaçamento e Bordas Suaves
st.markdown(
    """
    <style>
    .stApp {
        padding: 10px;
        border: 2px solid #FFC300;
        border-radius: 10px;
        background-image: url('DALL-E 2024-12-08 21.27.24 - A modern four-story building with a geometric facade featuring predominant tones of yellow, black, and light gray in large rectangular blocks, creatin.webp');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .stSidebar {
        padding: 10px;
        border: 2px solid #FF5733;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Animações Interativas com LottieFiles (Continuação)
st.subheader("🎥 Vídeo de Boas-Vindas")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Adicionando Um Carrossel de Imagens
st.subheader("📷 Galeria de Imagens")
from PIL import Image

# Galeria dinâmica
galeria = [
    ("Fábrica em São Paulo", "imagem_sao_paulo.jpg"),
    ("Unidade Rio de Janeiro", "imagem_rio.jpg"),
    ("Centro de Treinamento", "imagem_treinamento.jpg")
]

for titulo, imagem in galeria:
    st.image(imagem, caption=titulo, use_column_width=True)

# Integração com APIs Externas (Dados do Clima)
st.subheader("🌦️ Clima Atual nas Unidades")
import requests

def obter_clima(cidade):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=SEU_TOKEN_AQUI&units=metric"
    resposta = requests.get(api_url).json()
    if resposta.get("main"):
        temperatura = resposta["main"]["temp"]
        descricao = resposta["weather"][0]["description"]
        return f"{temperatura}°C, {descricao.capitalize()}"
    return "Dados não disponíveis"

# Exibindo o clima
clima_sp = obter_clima("São Paulo")
clima_rj = obter_clima("Rio de Janeiro")
clima_bh = obter_clima("Belo Horizonte")

st.write(f"São Paulo: {clima_sp}")
st.write(f"Rio de Janeiro: {clima_rj}")
st.write(f"Belo Horizonte: {clima_bh}")

# Painel de Controle para Configurações Avançadas
if menu == "Configurações":
    st.header("⚙️ Configurações do Sistema")
    
    # Temas de Interface
    st.subheader("🎨 Personalização de Tema")
    tema = st.radio(
        "Escolha um tema:",
        options=["Claro", "Escuro", "Amadelli (Padrão)"],
        index=2
    )
    
    if tema == "Claro":
        st.markdown(
            """
            <style>
            body { background-color: #FFFFFF; color: #000000; }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.success("Tema Claro Aplicado!")
    elif tema == "Escuro":
        st.markdown(
            """
            <style>
            body { background-color: #000000; color: #FFFFFF; }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.success("Tema Escuro Aplicado!")
    else:
        st.markdown(
            """
            <style>
            body { background-color: #040404; color: #FFC300; }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.success("Tema Amadelli Aplicado!")

    # Configurações de Notificações
    st.subheader("🔔 Configurações de Notificações")
    ativar_notificacoes = st.checkbox("Ativar Notificações")
    ativar_email = st.checkbox("Ativar Notificações por Email")
    ativar_sms = st.checkbox("Ativar Notificações por SMS")

    if ativar_notificacoes:
        st.write("Notificações Ativadas!")
        if ativar_email:
            st.write("✔️ Notificações por Email Ativadas.")
        if ativar_sms:
            st.write("✔️ Notificações por SMS Ativadas.")

    # Atualizações de Sistema
    st.subheader("🔄 Atualizações")
    st.write("Verificar por atualizações disponíveis:")
    if st.button("Verificar Agora"):
        st.info("Seu sistema está atualizado com a versão mais recente.")
    
# Área de Relatórios Interativos com Mapas Dinâmicos
if menu == "Relatórios":
    st.header("🌍 Relatórios Geográficos")
    
    # Criando um mapa interativo
    import folium
    from streamlit_folium import st_folium
    
    mapa = folium.Map(location=[-23.55052, -46.633308], zoom_start=5)
    folium.Marker(
        [-23.55052, -46.633308], popup="Unidade São Paulo"
    ).add_to(mapa)
    folium.Marker(
        [-22.906847, -43.172896], popup="Unidade Rio de Janeiro"
    ).add_to(mapa)
    folium.Marker(
        [-19.916681, -43.934493], popup="Unidade Belo Horizonte"
    ).add_to(mapa)
    
    st_folium(mapa, width=700, height=500)

# Gráficos Avançados com Plotly
if menu == "Treinamentos":
    st.header("📈 Análise de Treinamentos")
    
    import plotly.express as px
    
    # Dados fictícios de progresso nos treinamentos
    treinamento_data = pd.DataFrame({
        "Treinamento": ["Segurança", "Higiene", "Produção", "Liderança"],
        "Participantes": [120, 85, 100, 60],
        "Conclusão (%)": [90, 75, 80, 70]
    })
    
    # Gráfico de dispersão interativo
    fig = px.scatter(
        treinamento_data,
        x="Treinamento",
        y="Conclusão (%)",
        size="Participantes",
        color="Treinamento",
        title="Progresso nos Treinamentos",
        labels={"Treinamento": "Tipo de Treinamento", "Conclusão (%)": "Percentual de Conclusão"}
    )
    st.plotly_chart(fig)

# Área para Feedback dos Usuários
if menu == "Delli AI":
    st.header("💬 Feedback dos Usuários")
    st.text_area("Deixe seu feedback sobre a Delli AI:", placeholder="Escreva aqui...")
    if st.button("Enviar Feedback"):
        st.success("Obrigado pelo seu feedback!")

# Adicionando Indicadores de Progresso
st.sidebar.subheader("Progresso Geral")
st.sidebar.progress(75)  # Exemplo com 75% concluído

# Notificações em Tempo Real
st.sidebar.subheader("🔔 Alertas Recentes")
alertas = ["Manutenção Programada: 15/12", "Capacitação obrigatória: 20/12"]
for alerta in alertas:
    st.sidebar.warning(alerta)

# Integração com Formulários Google para Recrutamento
st.sidebar.subheader("📋 Cadastro para Treinamentos")
st.sidebar.write("[Clique aqui para se cadastrar](https://forms.gle/SEU_FORM_GOOGLE)")

# Painel Interativo de Análise de Dados
if menu == "Painel do Funcionário":
    st.header("📊 Painel do Funcionário")
    
    # Seção de Pontuação de Desempenho
    st.subheader("⭐ Desempenho")
    desempenho_data = {
        "Nome": ["João Silva", "Maria Santos", "Carlos Oliveira", "Ana Paula"],
        "Pontuação": [85, 92, 78, 88],
        "Treinamentos Concluídos": [10, 12, 8, 11],
        "Horas de Trabalho": [160, 170, 150, 165]
    }
    df_desempenho = pd.DataFrame(desempenho_data)
    st.table(df_desempenho)

    # Análise Interativa de Produtividade
    st.subheader("📈 Análise de Produtividade")
    fig = px.bar(
        df_desempenho,
        x="Nome",
        y="Pontuação",
        color="Pontuação",
        text="Treinamentos Concluídos",
        labels={"Pontuação": "Desempenho (%)"},
        title="Comparação de Desempenho"
    )
    st.plotly_chart(fig)

    # Ferramenta para Filtrar Dados
    st.subheader("🔍 Filtros Avançados")
    filtro_nome = st.selectbox("Selecione o Funcionário:", df_desempenho["Nome"])
    funcionario_selecionado = df_desempenho[df_desempenho["Nome"] == filtro_nome]
    st.write(f"Detalhes de {filtro_nome}:")
    st.write(funcionario_selecionado)

# Área de Notícias e Atualizações
st.sidebar.subheader("📰 Notícias e Atualizações")
noticias = [
    "Novo treinamento disponível: 'Gestão de Tempo'.",
    "Reconhecimento: Funcionário do Mês é Maria Santos!",
    "Atualização de sistema programada para 12/12."
]
for noticia in noticias:
    st.sidebar.info(noticia)

# Integração com Google Calendar
st.sidebar.subheader("📅 Próximos Eventos")
calendario_eventos = [
    "15/12: Treinamento de Segurança",
    "20/12: Reunião Geral",
    "05/01: Atualização de Procedimentos"
]
for evento in calendario_eventos:
    st.sidebar.write(f"📌 {evento}")

# Adicionando Animações com Lottie
st.subheader("🎥 Animações Interativas")
from streamlit_lottie import st_lottie

# Função para carregar animações Lottie
def carregar_lottie(url):
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animação de boas-vindas
animacao_bem_vindo = carregar_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json")
st_lottie(animacao_bem_vindo, height=300, key="bem_vindo")

# Integração com API de Clima
st.sidebar.subheader("🌤️ Clima Atual")
cidade = st.sidebar.text_input("Digite sua cidade:", "São Paulo")
if st.sidebar.button("Ver Clima"):
    # Substituir por integração com API real
    st.sidebar.info(f"🌡️ Clima em {cidade}: 25°C, Chuva Leve")

# Gráficos de Tendência com Altair
st.subheader("📊 Tendências")
import altair as alt

tendencia_data = pd.DataFrame({
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril"],
    "Produção": [1200, 1350, 1450, 1550],
    "Treinamentos": [200, 250, 300, 350]
})

fig_tendencia = alt.Chart(tendencia_data).mark_line(point=True).encode(
    x="Mês",
    y="Produção",
    tooltip=["Produção", "Treinamentos"]
).interactive()

st.altair_chart(fig_tendencia, use_container_width=True)

# Botão para Download de Relatórios
st.subheader("📥 Baixe Relatórios Detalhados")
if st.button("Download Relatório de Produtividade"):
    # Criando dados fictícios para o relatório
    relatorio_data = pd.DataFrame({
        "Funcionário": ["João Silva", "Maria Santos", "Carlos Oliveira", "Ana Paula"],
        "Horas Trabalhadas": [160, 170, 150, 165],
        "Produtividade (%)": [85, 92, 78, 88]
    })
    csv = relatorio_data.to_csv(index=False).encode("utf-8")
    st.download_button("Baixar CSV", data=csv, file_name="relatorio_produtividade.csv")

# Notificações Pop-up com Streamlit Toast
st.sidebar.subheader("📬 Mensagens Instantâneas")
if st.sidebar.button("Mostrar Mensagem Importante"):
    st.sidebar.toast("⚠️ Atenção: Nova política de segurança implementada!", duration=10)


# Integração com Realidade Aumentada (placeholder para futuras implementações)
st.subheader("🌀 Realidade Aumentada (Em Breve)")
st.markdown("""
    Experimente visualizar dados em 3D e interagir com painéis dinâmicos usando tecnologias de realidade aumentada.
    Esta funcionalidade estará disponível em futuras atualizações. Fique ligado!
""")

# Painel de Configurações do Usuário
if menu == "Configurações":
    st.header("⚙️ Configurações")
    st.subheader("👤 Perfil do Usuário")
    with st.form("perfil_form"):
        nome = st.text_input("Nome Completo", value="João da Silva")
        email = st.text_input("E-mail", value="joao.silva@amadelli.com")
        telefone = st.text_input("Telefone", value="(11) 98765-4321")
        salvar = st.form_submit_button("Salvar Alterações")
        if salvar:
            st.success("Informações atualizadas com sucesso!")

    st.subheader("🌐 Preferências de Interface")
    tema = st.radio(
        "Escolha o tema:",
        options=["Claro", "Escuro", "Personalizado"],
        index=1
    )
    if tema == "Personalizado":
        cor_personalizada = st.color_picker("Selecione a cor principal:", "#e0782c")
        st.write(f"Cor escolhida: {cor_personalizada}")

# Painel de Feedback
st.sidebar.subheader("📢 Envie Seu Feedback")
feedback = st.sidebar.text_area("Como podemos melhorar o sistema?")
if st.sidebar.button("Enviar Feedback"):
    st.sidebar.success("Obrigado pelo seu feedback! Ele será analisado pela nossa equipe.")

# Rodapé Moderno
st.markdown("---")
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1e1e1e;
        color: #f9e1cd;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
        © 2024 Amadelli Food Service | Todos os direitos reservados | 
        <a href="https://amadelli.com" target="_blank" style="color: #FFC300; text-decoration: none;">Visite nosso site</a>
    </div>
""", unsafe_allow_html=True)

# Adicionando Interatividade com Gráficos Dinâmicos
if menu == "Relatórios":
    st.header("📊 Relatórios Detalhados")
    relatorio_data = pd.DataFrame({
        "Mês": ["Janeiro", "Fevereiro", "Março", "Abril"],
        "Produção (Toneladas)": [1200, 1400, 1600, 1800],
        "Erros (Quantidade)": [10, 7, 5, 4],
    })

    st.subheader("📈 Produção Mensal")
    grafico_producao = alt.Chart(relatorio_data).mark_bar().encode(
        x="Mês",
        y="Produção (Toneladas)",
        color="Mês",
        tooltip=["Produção (Toneladas)", "Erros (Quantidade)"]
    )
    st.altair_chart(grafico_producao, use_container_width=True)

    st.subheader("📉 Erros Mensais")
    grafico_erros = px.line(
        relatorio_data,
        x="Mês",
        y="Erros (Quantidade)",
        markers=True,
        title="Redução de Erros ao Longo dos Meses",
        labels={"Erros (Quantidade)": "Quantidade de Erros"}
    )
    st.plotly_chart(grafico_erros)

# Finalização
st.balloons()
st.markdown("""
    🎉 Obrigado por usar o sistema Amadelli Dashboard! Aproveite as funcionalidades e melhore continuamente sua experiência.
""")



