import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import altair as alt
from PIL import Image
from st_aggrid import AgGrid
import base64

# Configuração do Banco de Dados
def create_database():
    conn = sqlite3.connect("amadelli.db")
    cursor = conn.cursor()
    
    # Tabela para relatórios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        data TEXT NOT NULL
    )
    """)
    
    # Tabela para imagens
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("amadelli.db")
    cursor = conn.cursor()
    
    # Inserindo dados de exemplo
    cursor.execute("INSERT INTO reports (title, data) VALUES ('Relatório de Vendas', 'Vendas aumentaram 20% este mês.')")
    cursor.execute("INSERT INTO images (name, path) VALUES ('Fachada', './DALL-E_2024-12-08_21.27.24.webp')")
    
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect("amadelli.db")
    df_reports = pd.read_sql_query("SELECT * FROM reports", conn)
    df_images = pd.read_sql_query("SELECT * FROM images", conn)
    conn.close()
    return df_reports, df_images

# Criar banco e inserir dados iniciais
create_database()
insert_data()
df_reports, df_images = load_data()

# Configuração do fundo
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

set_background("./DALL-E_2024-12-08_21.27.24.webp")
