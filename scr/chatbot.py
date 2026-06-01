import streamlit as st
import pandas as pd
import json
import ollama

# ================= CARREGAR OS DADOS =================

perfil_aluno = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/perfil_aluno.json'))
curso_viasapiens = json.load(open('./data/curso_viasapiens.json'))
curso_ifce = json.load(open('./data/curso.json'))
dicas_estudo = json.load(open('./data/dicas_estudo.json'))
boas_praticas = json.load(open('./data/boas_praticas_estudo.json'))

# ================= MONTAR O CONTEXTO DO USUÁRIO =================

contexto = f"""
Aluna {perfil_aluno['nome']}.

DADOS DA ALUNA:
- Horas disponíveis: {perfil_aluno['horas_estudo_dia']}h por dia
- Dias disponíveis: {', '.join(perfil_aluno['dias_da_semana_disponiveis'])}
- Curso desejado: {', '.join(perfil_aluno['cursos_desejados'])}

PRIORIDADES DE ESTUDO:
1. ATAQUE PRIORITÁRIO (5x): Filosofia, Sociologia, Repertório da Redação
2. ATAQUE SECUNDÁRIO (4x): História, Geografia, Física, Estatística
3. CONSOLIDAÇÃO (3x): Gramática, Biologia, Proposta de Intervenção
4. MANUTENÇÃO (2x): Literatura, Álgebra, Geometria, Química
5. REVISÃO (1x): Inglês, Matemática Básica
"""

# ================= SYSTEM PROMPT =================

SYSTEM_PROMPT = f"""
Você é o EnemPassei, um tutor educacional especialista em ENEM 2026.
Sua personalidade é motivadora, paciente, didática e encorajadora.
Você ensina com calma, adapta a explicação ao nível da aluna e NUNCA julga erros — você aprende com eles junto com a aluna.
Seu objetivo é EDUCAR e ORGANIZAR, não pressionar.
Você ajuda a criar planos de estudo personalizados, explica conceitos de forma simples e oferece dicas de gestão de tempo e motivação.

REGRAS:
- Não invente o que não sabe
- Não ignore cansaço da aluna
- Baseie respostas no perfil da aluna
- Seja direta (sem textão)

COMPORTAMENTO:
- Cronograma: use os dias e horas disponíveis
- Aluna perdida: comece pelo nível 5 e 4
- Aluna cansada: sugira descanso
- Não corrige questões

LIMITAÇÕES:
- Não corrige questões
- Não substitui professor
- Não guarda dados sensíveis

EXEMPLO:
Aluna: "Me ajuda com cronograma?"
Resposta: "Claro! Você tem X horas por dia em [dias]. Que tal focar em Filosofia e Sociologia primeiro (suas prioridades)?"
"""

# ================= INTERFACE =================
st.set_page_config(
    page_title='EnemPassei',
    page_icon='📚',
    layout='centered'
)

st.title("📚 EnemPassei")

# ================= CRIAÇÃO DA MEMÓRIA =================

# verifica se a lista já está criada. se caso já estiver, não criar novamente.
if "messages" not in st.session_state:
    st.session_state.mensagens = []  # criação da memoria temporaria do chat atual

for message in st.session_state.mensagens:
    with st.chat_message[message['role']]:
        st.markdown(message['content'])


# ================= ENTRADA DO USUÁRIO =================

if pergunta := st.chat_input('Digite sua mensagem...'):
    st.session_state.mensagens.append({'role': 'user', 'content': pergunta}) # adiciona a mensagem do usuario na lista
    
    # BLOCO DE MENSAGEM DO USUÁRIO
    with st.chat_message("user"):
        st.markdown(pergunta) # mostra a mensagem do usuário

    # BLOCO DE MENSAGEM DA IA
    with st.chat_message("assistant"):
       prompt = f"""
        {SYSTEM_PROMPT}

        CONTEXTO DO CLIENTE:
        {contexto}

        Pergunta: {pergunta}"""

       # ================= CONEXÃO OLLAMA ====================
       resposta_ia = ollama.chat(
            model='llama3.2:3b', 
            messages=prompt, 
        )
       #response_placeholder = st.empty() # cria espaço vazio para a resposta da ia.
       resposta_ao_usuario = resposta_ia['message']['content'] # armazena a resposta da ia.
       st.markdown(resposta_ao_usuario) # mostra a mensagem da ia.

    st.session_state.mensagens.append({'role': 'assistent', 'content': resposta_ao_usuario}) # adiciona a mensagem do usuario na lista


