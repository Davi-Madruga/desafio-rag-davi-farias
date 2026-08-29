from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def gerar_embedding(texto):
    embedding = modelo.encode(texto)

    return embedding
