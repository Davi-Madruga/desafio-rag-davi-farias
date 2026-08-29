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
Você é um assistente que responde perguntas com base exclusivamente
nas informações fornecidas no contexto.

Analise o contexto antes de responder.

Regras:
- Use somente as informações presentes no contexto.
- Não utilize conhecimento externo.
- Não invente informações.
- Responda de forma clara e objetiva.
- Se o contexto não possuir informações suficientes para responder
  à pergunta, considere o contexto insuficiente.
- Se o contexto for insuficiente, informe isso na resposta.

Retorne sua resposta no seguinte formato JSON:

{{
    "contexto_suficiente": true ou false,
    "resposta": "sua resposta aqui"
}}

Não escreva nada fora do JSON.

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
