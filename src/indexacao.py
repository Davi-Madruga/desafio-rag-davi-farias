import json
import os

from chunking import criar_chunks
from embeddings import adicionar_embeddings
from ingestao import ler_documentos

def salvar_indice(chunks, caminho):
    os.makedirs("data", exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(chunks, arquivo, ensure_ascii=False, indent=2)

documentos = ler_documentos()
chunks = []

for documento in documentos:
    chunks_temp = criar_chunks(documento)
    chunks.extend(chunks_temp)

for i in range(len(chunks)):
    chunks[i]["id"] = f"CHUNK-{i + 1:03d}"

chunks = adicionar_embeddings(chunks)

salvar_indice(chunks,"data/indice.json")
print("Índice criado com sucesso!")
