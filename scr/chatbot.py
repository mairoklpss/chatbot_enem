import streamlit as st
import pandas as pd
import requests
import json
import ollama

# === INTERFACE ===
st.set_page_config(
    page_title='EnemPassei',
    page_icon='📚',
    layout='centered'
)

st.title("📚 EnemPassei")

# === CRIAÇÃO DA MEMÓRIA ===

# verifica se a lista já está criada. se caso já estiver, não criar novamente.
if "messages" not in st.session_state:
    st.session_state.mensagens = []  # criação da memoria temporaria do chat atual

for message in st.session_state.mensagens:
    with st.chat_message[message['role']]:
        st.markdown(message['content'])


# === CONEXÃO OLLAMA ===

resposta_ia = ollama.chat(
    model='llama3.2:3b', 
    messages=st.session_state.mensagens, 
)

#print(resposta_ia['message']['content']) 

#st.chat_input("Digite sua mensagem...")


# ==== ENTRADA DO USUÁRIO ===

if pergunta := st.chat_input('Digite sua mensagem...'):
    st.session_state.mensagens.append({'role': 'user', 'content': pergunta}) # adiciona a mensagem do usuario na lista
    
    with st.chat_message("user"):
        st.markdown(pergunta) # mostra a mensagem do usuário

    with st.chat_message("assistant"):
       # response_placeholder = st.empty() # cria espaço vazio para a resposta da ia.
       resposta_ao_usuario = resposta_ia['message']['content']
       st.markdown(resposta_ao_usuario) # mostra a mensagem do usuário


