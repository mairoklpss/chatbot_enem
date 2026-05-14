# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no **Tutor ENEM**? |
|---------|---------|-----------------------------------|
| `perfil_aluno.json` | JSON | Adaptar planos e conselhos ao perfil da aluna (dificuldades, prioridades, disponibilidade) |
| `curso_ifce.json` | JSON | Informar pesos do SISU e notas de corte para Ciência da Computação no IFCE Tianguá |
| `curso_viasapiens.json` | JSON | Informar detalhes do curso de ADS na Via Sapiens (ingresso, duração, modalidade) |
| `boas_praticas_estudo.json` | JSON | Fornecer metodologias de estudo, técnicas e estratégias para o ENEM |
| `dicas_estudo.json` | JSON | Banco de dicas rápidas para organização, foco, motivação e revisão |

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON são carregados no início da sessão do Streamlit e injetados no contexto do prompt para que o agente conheça a aluna e possa personalizar as respostas.

```python
import json
import pandas as pd

perfil = json.load(open('./data/perfil_aluno.json'))
curso_ifce = json.load(open('./data/curso_ifce.json'))
curso_viasapiens = json.load(open('./data/curso_viasapiens.json'))
boas_praticas = json.load(open('./data/boas_praticas_estudo.json'))
dicas = json.load(open('./data/dicas_estudo.json'))
``` 

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Apenas será passado o conteúdo dos arquivos após o título de cada um  deles, para que o agente tenha o máximo de detalhes possíveis

*Exemplo:*
``` 
DADOS DA ALUNA E PERFIL (data/perfil_aluno.json):
{
  "nome": "Maira",
  "ocupacao": "estudante de Ensino Médio",
  "cursos_desejados": ["Análise e Desenvolvimento de Sistemas", "Ciência da Computação"],
  "dias_da_semana_disponiveis": ["segunda", "terça", "sexta", "sábado", "domingo"],
  "horas_estudo_dia": 2,
  "niveis_dificuldade": {
    "Muito Ruim (5x)": {
      "disciplinas": ["Filosofia", "Sociologia", "Repertório (Redação)"]
    },
    "Ruim (4x)": {
      "disciplinas": ["História", "Geografia", "Física", "Estatística e Probabilidade", "Estrutura e Argumentação (Redação)"]
    }
  }
}

DADOS DO CURSO IFCE (data/curso_ifce.json):
{
  "curso": "Ciência da Computação",
  "instituicao": "IFCE - Campus Tianguá",
  "turno": "Noturno",
  "pesos_sisu": {
    "Matematica": 3.0,
    "Ciencias da Natureza": 2.0,
    "Linguagens e Codigos": 1.0,
    "Ciencias Humanas": 1.0,
    "Redacao": 1.0
  }
}

DADOS DO CURSO VIA SAPIENS (data/curso_viasapiens.json):
{
  "curso": "Análise e Desenvolvimento de Sistemas",
  "instituicao": "Faculdade ViaSapiens",
  "modalidade": "Educação a Distância (EAD)",
  "duracao_anos": 3,
  "ingresso": ["Vestibular FVS", "Nota do ENEM", "Transferência"]
}

GUIA METODOLÓGICO DE ESTUDOS (data/boas_praticas_estudo.json):
{
  "como_montar_o_cronograma": {
    "passo_1_avalie_sua_semana": "Liste quantas horas líquidas você tem por dia...",
    "passo_2_distribua_prioridades": "Use seus níveis de dificuldade para decidir o que estudar cada dia..."
  },
  "tecnicas_de_estudo_recomendadas": {
    "estudo_teorico": "Vídeo-aula curta + Mapa Mental + 10 questões",
    "estudo_pratico_exatas": "Menos teoria, mais exercício"
  },
  "estrategia_para_redacao": {
    "frequencia": "1 redação completa por semana",
    "competencias_criticas": {...}
  }
}

DICAS DE ESTUDO (data/dicas_estudo.json):
[
  {"categoria": "organizacao", "dica": "Liste as 3 matérias mais importantes do dia e comece pela mais difícil"},
  {"categoria": "foco", "dica": "Que tal estudar 50 minutos e descansar 10?"},
  {"categoria": "motivacao", "dica": "Um passo por vez. Hoje você estuda 1 horinha, amanhã mais um pouco."}
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Aqui está um exemplo de como os dados serão entregues ao agente, contendo apenas as informações relevantes.

```
PERFIL DA MAIRA:
- Disponibilidade: 2h por dia (seg, ter, sex, sáb, dom)
- Prioridades: Filosofia, Sociologia, Redação, História, Geografia, Física, Química, Matemática
- Ataque Prioritário (5x): Filosofia, Sociologia, Repertório Redação
- Ataque Secundário (4x): História, Geografia, Física, Estatística, Estrutura Redação

CURSO IFCE:
- Matemática tem PESO 3 (prioridade máxima)
- Natureza tem PESO 2
- Nota de corte ampla: 678.76

GUIA DE ESTUDOS:
- Monte o cronograma baseado nos seus dias disponíveis
- Priorize níveis 5 e 4 nos seus melhores horários
- Não estude mesma área em dias seguidos
- 1 redação completa por semana

DICA DO DIA:
"Liste as 3 matérias mais importantes do dia e comece pela mais difícil"
...
