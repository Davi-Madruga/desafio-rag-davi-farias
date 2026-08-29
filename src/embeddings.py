from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def gerar_embedding(texto):
    embedding = modelo.encode(texto)

    return embedding

def adicionar_embeddings(chunks):
    for chunk in chunks:
        chunk["embedding"] = gerar_embedding(chunk["texto"]).tolist()
        
    return chunks