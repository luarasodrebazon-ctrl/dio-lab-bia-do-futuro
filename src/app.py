import json
import pandas as pd
import requests 
import streamlit as st

# =========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM PROMPT ===========
SYSTEM_PROMPT = """Você é a Luna, uma educadora financeira amigável e didática.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais.
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
- Evite jargões técnicos, ou explique-os quando usar.
- Destingua bem as diferenter transações em suas categorias, como alimentação, transporte, moradia, lazer, etc. para manter a clareza do cliente sobre seus gastos.
- Sempre coloque a fonte das informações que fornecer sobre atendimentos anteriores e transações recentes, para que o cliente saiba de onde vem cada dado.
"""

# =========== CHAMAR OLLAMA ===========
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    try:
        # Enviamos a requisição normalmente para o Ollama
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        
        # Se a requisição falhar ou o Ollama der erro interno (como o erro 500 do acento)
        if r.status_code != 200:
            return f"Erro no servidor Ollama (Status {r.status_code}): Certifique-se de recriar o modelo na pasta sem acentos usando o terminal."
            
        resposta_json = r.json()
        return resposta_json['response']
        
    except Exception as e:
        # Evita que a tela do Streamlit fique vermelha com o KeyError
        return f"Não foi possível obter resposta do Ollama. Detalhes: {str(e)}"

# =========== INTERFACE ===========
st.title("🎓 Luna, Sua Educadora Financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))