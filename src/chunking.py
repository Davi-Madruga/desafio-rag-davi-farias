TAMANHO_CHUNK = 500
OVERLAP = 5

def criar_chunks(documento):

    texto = documento["texto"]
    chunks = []
    inicio = 0
    passo = TAMANHO_CHUNK - OVERLAP

    while inicio < len(texto):
        fim = inicio + TAMANHO_CHUNK

        texto_chunk = texto[inicio:fim]

        chunks.append({
            "chunk_id" : f"CHUNK-{len(chunks) + 1:02d}",  
            "texto" : texto_chunk,
            "arquivo" : documento["arquivo"],
            "caminho" : documento["caminho"]
        }
            
        )

        inicio += passo

    return chunks
