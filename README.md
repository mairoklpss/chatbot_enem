# 🎓 EnemPassei - Chatbot de Estudos para o ENEM 2026

<div align="center">

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

</div>

## 📋 Sobre o Projeto

**EnemPassei** é um chatbot educacional desenvolvido para auxiliar estudantes na preparação para o ENEM 2026. O agente utiliza inteligência artificial local (Ollama) para oferecer:

- ✨ **Planos de estudo personalizados** baseados no perfil e disponibilidade do aluno
- 📚 **Organização de cronogramas** adaptados à rotina
- 🎯 **Priorização de conteúdos** com base nas dificuldades individuais
- 💡 **Dicas de produtividade** e técnicas de estudo comprovadas
- 📊 **Informações sobre pesos do SISU** para cursos específicos

## 🎯 Público-Alvo

Estudantes que estão se preparando para o ENEM 2026, especialmente aqueles que:
- Estudam sozinhos e precisam de orientação
- Têm dificuldade em organizar a rotina de estudos
- Buscam um acompanhamento motivador e personalizado

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| **Python** | Linguagem principal do projeto |
| **Streamlit** | Framework para interface web interativa |
| **Ollama** | Execução de modelos de IA localmente |
| **Pandas** | Manipulação e organização dos dados do perfil |

## 📁 Estrutura do Projeto
```
📁 chatbot_enem/
│
├── 📁 data/                              # Dados mockados do agente
│   ├── perfil_aluno.json                 # Perfil da aluna (dificuldades, disponibilidade)
│   ├── curso_ifce.json                   # Dados do curso IFCE (pesos, notas de corte)
│   ├── curso_viasapiens.json             # Dados do curso Via Sapiens
│   ├── boas_praticas_estudo.json         # Metodologias e técnicas de estudo
│   └── dicas_estudo.json                 # Banco de dicas de produtividade
│
├── 📁 docs/                              # Documentação do projeto
│   ├── 01-documentacao-agente.md         # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md           # Estratégia de dados e integração
│   ├── 03-prompts.md                     # Engenharia de prompts e exemplos
│   └── 04-metricas.md                    # Avaliação e métricas do agente
│
├── 📁 src/                               # Código da aplicação
│   └── app.py                            # Aplicação principal Streamlit
│
└── 📄 README.md                          # Documentação do projeto
```

## ✅ Funcionalidades Implementadas

- [x] Carregamento da base de conhecimento (JSON)
- [x] Contexto personalizado com perfil da aluna
- [x] Sistema de prompts com regras definidas
- [ ] Interface de chat com Streamlit
- [ ] Conexão com Ollama local
- [ ] Testes de qualidade e preenchimento do docs das métricas

---
<div align="center">

⭐ Desenvolvido por Maira Lopes.

*Em desenvolvimento • ENEM 2026*

</div>
