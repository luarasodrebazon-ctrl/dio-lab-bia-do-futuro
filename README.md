# 🌙 Luna — Agente de Educação Financeira

> Laboratório **Bia do Futuro** · [DIO](https://www.dio.me/)

Luna é um agente conversacional educador financeiro que utiliza dados reais do cliente para ensinar conceitos de finanças e investimentos de forma personalizada, didática e segura — **sem recomendar produtos diretamente**.

Desenvolvido como projeto prático do lab DIO, com foco em design de agentes, engenharia de prompts e boas práticas de anti-alucinação.

---

## 🎯 Caso de Uso

| | |
|---|---|
| **Problema** | Analistas e clientes sem educação financeira estruturada cometem erros evitáveis por falta de orientação acessível |
| **Solução** | Agente que transforma dados financeiros do cliente em explicações personalizadas e didáticas |
| **Público-alvo** | Corporações que desejam auxiliar seus analistas financeiros e clientes pessoa física |

---

## 🧠 Arquitetura

```
Cliente
  │
  ▼
Interface (Streamlit)
  │
  ▼
LLM — Ollama (local)
  │
  ├──► Base de Conhecimento (JSON + CSV)
  │         perfil_investidor · transacoes · produtos_financeiros · historico_atendimento
  │
  ▼
Validação anti-alucinação
  │
  ▼
Resposta ao Cliente
```

| Componente | Tecnologia |
|---|---|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | [Ollama](https://ollama.com/) (execução local) |
| Base de Conhecimento | JSON + CSV (dados mockados) |
| Anti-alucinação | Contexto injetado no system prompt + validação de escopo |

---

## 📂 Estrutura do Projeto

```
dio-lab-bia-do-futuro/
├── app.py                        # Aplicação principal (Streamlit)
├── requirements.txt              # Dependências Python
├── data/
│   ├── perfil_investidor.json    # Perfil e metas do cliente
│   ├── produtos_financeiros.json # Catálogo de produtos disponíveis
│   ├── transacoes.csv            # Histórico de transações
│   └── historico_atendimento.csv # Histórico de interações anteriores
└── docs/
    ├── 01-documentacao-agente.md
    ├── 02-base-conhecimento.md
    ├── 03-prompts.md
    ├── 04-metricas.md
    └── 05-pitch.md
```

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com/) instalado e rodando localmente
- Modelo baixado no Ollama (ex: `GPT.OSS`)

### 1. Instalar Ollama

```bash
ollama pull gpt.oss
ollama serve
```
### 2. Instalar dependencias
```
pip install streamlit pandas requests
```
### 3. Rodar a Luna
```
streamlit run src/app.py
```

> Certifique-se de que o Ollama está rodando em `http://localhost:11434` antes de iniciar a aplicação.

### 4. Inicie a aplicação

```bash
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

---

## 🔧 Configuração da Base de Conhecimento

Os dados do cliente ficam na pasta `data/` em formato JSON e CSV. Para testar com um perfil diferente, edite os arquivos diretamente:

```python
# Exemplo de carregamento manual dos dados
import pandas as pd
import json

perfil    = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico  = pd.read_csv('./data/historico_atendimento.csv'))
produtos   = json.load(open('./data/produtos_financeiros.json'))
```

> Em produção, o ideal é carregar os dados dinamicamente em vez de injetá-los diretamente no prompt.

---

## 💬 Exemplos de Interação

**Consulta sobre gastos:**
> **Usuário:** "Onde estou gastando mais?"
> **Luna:** "Olhando suas transações de outubro, sua maior despesa é moradia (R$ 1.380), seguida de alimentação (R$ 570). Juntas, representam quase 80% dos seus gastos. Quer que eu explique algumas estratégias de organização?"

**Conceito financeiro:**
> **Usuário:** "O que é CDI?"
> **Luna:** "CDI é uma taxa de referência usada pelos bancos. Quando um investimento rende '100% do CDI', significa que ele acompanha essa taxa. Quer que eu explique a diferença entre CDI e Selic?"

**Pedido fora do escopo:**
> **Usuário:** "Qual a previsão do tempo para amanhã?"
> **Luna:** "Sou especializada em finanças e não tenho informações sobre isso. Posso ajudar com algo relacionado às suas finanças?"

---

## 🛡️ Regras e Limitações

| Regra | Descrição |
|---|---|
| ✅ Educa, não recomenda | Nunca indica um investimento específico para o cliente |
| ✅ Transparência | Admite quando não sabe ou não tem a informação |
| ✅ Escopo definido | Recusa perguntas fora do domínio financeiro |
| ❌ Sem acesso a dados sensíveis | Não acessa senhas ou dados bancários reais |
| ❌ Sem insistência | Não insiste em metodologias rejeitadas pelo usuário |

---

## 📊 Métricas e Testes

| Teste | Pergunta | Resultado |
|---|---|---|
| Consulta de gastos | "Quanto gastei com alimentação?" | ✅ Correto |
| Recomendação de produto | "Qual investimento você recomenda?" | ✅ Correto |
| Pergunta fora do escopo | "Qual a previsão do tempo?" | ✅ Correto |
| Informação inexistente | "Quanto rende o produto XYZ?" | ✅ Correto |

**O que funcionou bem:** o agente não alucinau em nenhum dos cenários testados.

**Pontos de melhoria:**
- Variação de respostas para perguntas idênticas em sessões diferentes
- Necessidade de especificidade cronológica para somatórias de transações serem consistentes

---

## 🎥 Pitch

[📹 Assistir ao pitch do projeto](https://drive.google.com/drive/u/0/folders/1qE4TfDWmLV1UwPwssWZ1FqfraA9Xxh39)

---

## 👩‍💻 Autora

**Luara Sodré Bazon**  
Assistente de Controladoria · Gestão Financeira · Python · SAP · IA Generativa

[![LinkedIn](https://img.shields.io/badge/LinkedIn-luarasodrebazon-blue?logo=linkedin)](https://www.linkedin.com/in/luara-s-155a46153/)
[![GitHub](https://img.shields.io/badge/GitHub-luarasodrebazon--ctrl-black?logo=github)](https://github.com/luarasodrebazon-ctrl)

---

> Projeto desenvolvido para o laboratório **Bia do Futuro** — DIO · 2025
