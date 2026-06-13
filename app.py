import streamlit as st
from pathlib import Path

from src.embeddings import get_embeddings
from src.reducer import (
    apply_pca,
    apply_tsne,
    apply_umap
)

from src.visualizer import create_plot
from src.similarity import similarity_table
from src.nearest_neighbour import nearest_neighbors
from src.analogy import solve_analogy

st.title(
    "Embedding Space Visualizer"
)

sample_file = Path(
    "data/sample_words.txt"
)

if sample_file.exists():
    default_words = sample_file.read_text(
        encoding="utf-8"
    )
else:
    default_words = ""

text = st.text_area(
    "Enter words",
    default_words,
    height=400
)

method = st.selectbox(
    "Reduction Method",
    ["PCA", "t-SNE", "UMAP"]
)

words = list(dict.fromkeys(
    [
        w.strip()
        for w in text.split("\n")
        if w.strip()
    ]
))

neighbor_word = st.text_input(
    "Find Similar Words",
    "king"
)

st.subheader("Word Analogy")

col1, col2, col3 = st.columns(3)

with col1:
    word_a = st.text_input(
        "Word A",
        "king"
    )

with col2:
    word_b = st.text_input(
        "Word B",
        "man"
    )

with col3:
    word_c = st.text_input(
        "Word C",
        "woman"
    )

if st.button("Visualize"):

    embeddings = get_embeddings(words)

    if method == "PCA":
        coords = apply_pca(embeddings)

    elif method == "t-SNE":
        coords = apply_tsne(embeddings)

    else:
        coords = apply_umap(embeddings)

    fig = create_plot(coords, words)

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.subheader("Cosine Similarity Matrix")

    sim_df = similarity_table(
        words,
        embeddings
    )

    st.dataframe(sim_df)

    st.subheader("Nearest Neighbors")

    neighbors = nearest_neighbors(
        neighbor_word,
        words,
        embeddings
    )

    for word, score in neighbors:
        st.write(
            f"{word} ({score:.3f})"
        )
    
    st.subheader("Analogy Result")

    result = solve_analogy(
        word_a,
        word_b,
        word_c,
        words,
        embeddings
    )

    if result:

        predicted_word, score = result

        st.success(
            f"{word_a} - {word_b} + {word_c} = "
            f"{predicted_word}"
        )

        st.write(
            f"Similarity: {score:.3f}"
        )