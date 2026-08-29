import json
import numpy as np

from embeddings import gerar_embedding

def carregar_indice(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def similaridade_cosseno(vetor_a, vetor_b):
    produto_escalar = np.dot(vetor_a, vetor_b)

    norma_a = np.linalg.norm(vetor_a)
    norma_b = np.linalg.norm(vetor_b)

    return produto_escalar / (norma_a * norma_b)

def buscar(pergunta, indice, top_k=3):
    query_embedding = gerar_embedding(pergunta)

    resultados = []

    for chunk in indice:
        embedding_chunk = np.array(chunk["embedding"])

        score = similaridade_cosseno(
            query_embedding,
            embedding_chunk
        )

        resultados.append({
            "chunk": chunk,
            "score": score
        })

    resultados.sort(
        key=lambda resultado: resultado["score"],
        reverse=True
    )

    return resultados[:top_k]
