import json

from src.busca import buscar, carregar_indice
from ollama import chat


MODELO = "qwen3:4b"
CAMINHO_INDICE = "data/indice.json"
TOP_K = 3


def criar_contexto(resultados):
    contexto = ""

    for resultado in resultados:
        chunk = resultado["chunk"]

        contexto += f"""
Chunk ID: {chunk["id"]}
Caminho: {chunk["caminho"]}
Score: {resultado["score"]:.4f}

{chunk["texto"]}

{"-" * 70}
"""

    return contexto


def gerar_resposta(pergunta, contexto):
    prompt = f"""
Você é um assistente que responde perguntas exclusivamente com base no contexto fornecido.

Regras:
- Use somente informações presentes no contexto.
- Não use conhecimento externo nem invente informações.
- Se o contexto for suficiente, responda normalmente.
- Se for insuficiente, não tente responder. Diga que não compreende o assunto da pergunta,
  informe explicitamente o assunto principal abordado pelo documento e diga que pode
  responder perguntas relacionadas a esse assunto.

Retorne SOMENTE um JSON válido, sem Markdown ou qualquer texto fora dele.

Formato obrigatório:
{{
    "contexto_suficiente": true ou false,
    "resposta": "sua resposta aqui"
}}

"contexto_suficiente" deve ser um booleano (true/false), nunca uma string.
A chave "resposta" deve sempre existir.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

    resposta = chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    conteudo = resposta["message"]["content"]

    resultado = json.loads(conteudo)

    return resultado["resposta"], resultado["contexto_suficiente"]


def executar_rag(pergunta):
    indice = carregar_indice(CAMINHO_INDICE)

    resultados = buscar(
        pergunta,
        indice,
        top_k=TOP_K
    )

    contexto = criar_contexto(resultados)

    resposta = gerar_resposta(
        pergunta,
        contexto
    )

    return resultados, resposta
