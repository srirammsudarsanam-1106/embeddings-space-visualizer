import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def nearest_neighbors(
    query_word,
    words,
    embeddings,
    k=3
):

    if query_word not in words:
        return []

    query_idx = words.index(query_word)

    similarities = cosine_similarity(
        [embeddings[query_idx]],
        embeddings
    )[0]

    sorted_indices = np.argsort(
        similarities
    )[::-1]

    neighbors = []

    for idx in sorted_indices:

        if idx != query_idx:

            neighbors.append(
                (
                    words[idx],
                    similarities[idx]
                )
            )

        if len(neighbors) == k:
            break

    return neighbors