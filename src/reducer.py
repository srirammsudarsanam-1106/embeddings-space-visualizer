from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

def apply_pca(embeddings):

    reducer = PCA(n_components=2)

    return reducer.fit_transform(
        embeddings
    )

def apply_tsne(embeddings):

    n_samples = len(embeddings)

    perplexity = max(
        2,
        min(30, n_samples // 3)
    )

    reducer = TSNE(
        n_components=2,
        perplexity=perplexity,
        random_state=42
    )

    return reducer.fit_transform(
        embeddings
    )

def apply_umap(embeddings):

    reducer = umap.UMAP(
        n_components=2,
        random_state=42
    )

    return reducer.fit_transform(
        embeddings
    )