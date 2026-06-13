from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def similarity_table(words, embeddings):

    sim_matrix = cosine_similarity(embeddings)

    df = pd.DataFrame(
        sim_matrix,
        index=words,
        columns=words
    )

    return df