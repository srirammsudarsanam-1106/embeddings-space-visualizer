import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def solve_analogy(
    word_a,
    word_b,
    word_c,
    words,
    embeddings
):

    try:

        idx_a = words.index(word_a)
        idx_b = words.index(word_b)
        idx_c = words.index(word_c)

    except ValueError:
        return None

    analogy_vector = (
        embeddings[idx_a]
        - embeddings[idx_b]
        + embeddings[idx_c]
    )

    similarities = cosine_similarity(
        [analogy_vector],
        embeddings
    )[0]

    excluded = {
        idx_a,
        idx_b,
        idx_c
    }

    ranked = np.argsort(
        similarities
    )[::-1]

    for idx in ranked:

        if idx not in excluded:

            return (
                words[idx],
                similarities[idx]
            )

    return None