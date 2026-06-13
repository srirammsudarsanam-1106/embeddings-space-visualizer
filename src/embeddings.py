from sentence_transformers import SentenceTransformer

def get_embeddings(words):
    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )
    embeddings = model.encode(words)
    return embeddings