import streamlit as st
import pandas as pd
import json
import ollama

# ================= CARREGAR OS DADOS =================

perfil_aluno = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/perfil_aluno.json'))
curso_viasapiens = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/curso_viasapiens.json'))
curso_ifce = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/curso_ifce.json'))
dicas_estudo = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/dicas_estudo.json'))
boas_praticas = json.load(open('/home/mairol/Documentos/VSCODE/chatbot_python/data/boas_praticas_estudo.json'))

# ================= MONTAR O CONTEXTO DO USUÁRIO =================

contexto = f"""
Aluna {perfil_aluno['nome']}.

DADOS DA ALUNA:
- Horas disponíveis: {perfil_aluno['horas_estudo_dia']}h por dia
- Dias disponíveis: {', '.join(perfil_aluno['dias_da_semana_disponiveis'])}
- Curso desejado: {', '.join(perfil_aluno['cursos_desejados'])}

SOBRE CURSOS DESEJADOS:

1. {curso_ifce['curso']} - {curso_ifce['instituicao']}
   - Turno: {curso_ifce['turno']} | Duração: {curso_ifce['duracao_anos']} anos | Vagas: {curso_ifce['vagas_semestre']} por semestre
   - PESOS SISU: Matemática={curso_ifce['pesos_sisu']['Matematica']}, Natureza={curso_ifce['pesos_sisu']['Ciencias da Natureza']}, demais áreas peso={curso_ifce['pesos_sisu']['Linguagens e Codigos']}
   - Nota de corte ampla: {curso_ifce['notas_corte_referencia_2025_1']['ampla_concorrencia']}
   - Estratégia: Foque em MATEMÁTICA (peso 3) e NATUREZA (peso 2)

2. {curso_viasapiens['curso']} - {curso_viasapiens['instituicao']}
   - Modalidade: {curso_viasapiens['modalidade']} | Duração: {curso_viasapiens['duracao_anos']} anos
   - Ingresso: {', '.join(curso_viasapiens['ingresso'])}
   - PESOS: Média simples do ENEM (sem pesos específicos)
   - Estratégia: Foque em todas as áreas igualmente

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

DICAS DE ESTUDO (use quando apropriado):
- Organização: {dicas_estudo[0]['dica']}
- Foco: {dicas_estudo[1]['dica']}
- Motivação: {dicas_estudo[2]['dica']}
- Rotina: {dicas_estudo[3]['dica']}
- Revisão: {dicas_estudo[4]['dica']}
- Procrastinação: {dicas_estudo[5]['dica']}
- Descanso: {dicas_estudo[6]['dica']}

GUIA METODOLÓGICO:

COMO MONTAR CRONOGRAMA:
1. Avalie a semana: {boas_praticas['guia_metodologico_enem']['como_montar_o_cronograma']['passo_1_avalie_sua_semana']}
2. Distribua prioridades: {boas_praticas['guia_metodologico_enem']['como_montar_o_cronograma']['passo_2_distribua_prioridades']}
3. Alterne áreas: {boas_praticas['guia_metodologico_enem']['como_montar_o_cronograma']['passo_3_alterne_areas']}
4. Reserve revisão: {boas_praticas['guia_metodologico_enem']['como_montar_o_cronograma']['passo_4_reserve_dias_de_revisao']}

TÉCNICAS DE ESTUDO:
- Estudo teórico (Humanas/Biologia): {boas_praticas['guia_metodologico_enem']['tecnicas_de_estudo_recomendadas']['estudo_teorico']}
- Estudo prático (Exatas): {boas_praticas['guia_metodologico_enem']['tecnicas_de_estudo_recomendadas']['estudo_pratico_exatas']}
- Revisão ativa: {boas_praticas['guia_metodologico_enem']['tecnicas_de_estudo_recomendadas']['revisao_ativa']}
- Correção de erros: {boas_praticas['guia_metodologico_enem']['tecnicas_de_estudo_recomendadas']['correcao_de_erros']}
- Simulado estratégico: {boas_praticas['guia_metodologico_enem']['tecnicas_de_estudo_recomendadas']['simulado_estrategico']}

REDAÇÃO:
- Frequência: {boas_praticas['guia_metodologico_enem']['estrategia_para_redacao']['frequencia']}
- Como melhorar repertório: {boas_praticas['guia_metodologico_enem']['estrategia_para_redacao']['como_melhorar_repertorio']}
- Competência 2 (Repertório): {boas_praticas['guia_metodologico_enem']['estrategia_para_redacao']['competencias_criticas']['competencia_2_repertorio']}
- Competência 5 (Proposta): {boas_praticas['guia_metodologico_enem']['estrategia_para_redacao']['competencias_criticas']['competencia_5_proposta']}

SAÚDE E MOTIVAÇÃO:
- Sono: {boas_praticas['guia_metodologico_enem']['saude_e_motivacao']['sono']}
- Pausas: {boas_praticas['guia_metodologico_enem']['saude_e_motivacao']['pausas']}
- Dias ruins: {boas_praticas['guia_metodologico_enem']['saude_e_motivacao']['dias_ruins']}
- Atividade física: {boas_praticas['guia_metodologico_enem']['saude_e_motivacao']['atividade_fisica']}

ERROS COMUNS A EVITAR:
{chr(10).join(['- ' + erro for erro in boas_praticas['guia_metodologico_enem']['erros_comuns_a_evitar']])}

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
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []  # criação da memoria temporaria do chat atual

for message in st.session_state.mensagens:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


def perguntar(mensagem):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DA ALUNA:
    {contexto}

    PERGUNTA: {mensagem}
    """

    # ================= CONEXÃO OLLAMA ====================
    resposta_ia = ollama.generate(
            model='llama3.2:3b', 
            prompt=prompt 
        )
    
    st.session_state.mensagens.append({'role': 'assistant', 'content': resposta_ia['response']}) # adiciona a mensagem do usuario na lista
    return resposta_ia['response'] # armazena a resposta da ia.

# ================= ENTRADA DO USUÁRIO =================

if pergunta := st.chat_input('Digite sua mensagem...'):
    st.session_state.mensagens.append({'role': 'user', 'content': pergunta}) 

    # BLOCO DE MENSAGEM DO USUÁRIO
    st.chat_message("user").write(pergunta) # mostra a mensagem do usuário
    
    # BLOCO DE MENSAGEM DA IA
    with st.chat_message('assistant'):
        st.write(perguntar(pergunta))
       
        
        




