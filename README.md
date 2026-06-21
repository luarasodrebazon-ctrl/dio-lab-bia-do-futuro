# 🌙 Luna — Agente de Educação Financeira

Projeto desenvolvido como parte do laboratório **Bia do Futuro** da [DIO](https://www.dio.me/), com foco em design e documentação de agentes de IA conversacional aplicados a finanças pessoais.

---

## 📌 Sobre o Projeto

**Luna** é um agente educador financeiro projetado para auxiliar analistas e clientes corporativos a entenderem conceitos de finanças e investimentos de forma personalizada, didática e segura — sem nunca recomendar produtos diretamente.

---

## 🧠 Arquitetura

```
Cliente → Interface (Streamlit) → LLM (Ollama/Local) → Base de Conhecimento → Validação → Resposta
```

| Componente | Tecnologia |
|---|---|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | [Ollama](https://ollama.com/) (local) |
| Base de Conhecimento | JSON + CSV (dados mockados) |
| Anti-alucinação | Validação por contexto injetado no prompt |

---

## 📂 Estrutura

```
dio-lab-bia-do-futuro/
├── data/
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── transacoes.csv
│   └── historico_atendimento.csv
└── docs/
    ├── 01-documentacao-agente.md
    ├── 02-base-conhecimento.md
    ├── 03-prompts.md
    ├── 04-metricas.md
    └── 05-pitch.md
```

---

## ✅ Funcionalidades

- Responde perguntas sobre conceitos financeiros (CDI, Selic, Tesouro Direto, etc.)
- Analisa gastos e padrões do cliente com base em dados reais
- Explica produtos financeiros disponíveis de acordo com o perfil do investidor
- Recusa perguntas fora do escopo e admite limitações com transparência

---

## 🛡️ Segurança

- Não acessa dados bancários sensíveis
- Não recomenda investimentos — apenas educa
- Admite desconhecimento quando não há contexto disponível
- Não insiste em metodologias rejeitadas pelo usuário

---

## 📊 Avaliação

Testes realizados com 4 cenários principais: consulta de gastos, recomendação de produtos, perguntas fora do escopo e informações inexistentes.  
**Resultado:** o agente não alucinau em nenhum dos cenários. Ponto de melhoria: variação de respostas para perguntas idênticas.

---

## 🎥 Pitch

[📹 Assistir ao pitch](https://drive.google.com/drive/u/0/folders/1qE4TfDWmLV1UwPwssWZ1FqfraA9Xxh39)

---

## 👩‍💻 Autora

**Luara Sodré Bazon** — [LinkedIn](https://www.linkedin.com/in/luarasodrebazon) · [GitHub](https://github.com/luarasodrebazon-ctrl)

> Projeto desenvolvido para o laboratório DIO — Bia do Futuro.
