# Embedding Space Visualizer

An interactive Streamlit application for exploring word embeddings in a high-dimensional semantic space. This project demonstrates how modern embedding models represent words as vectors and how dimensionality reduction techniques can be used to visualize relationships between words.

The application allows users to:

* Generate embeddings using a pre-trained Sentence Transformer model
* Visualize embeddings in 2D space using PCA, t-SNE, or UMAP
* Compute cosine similarity between words
* Find nearest neighbors in embedding space
* Solve word analogies using vector arithmetic

---

## Demo Features

### 1. Embedding Visualization

Convert words into dense vector representations using the `all-MiniLM-L6-v2` embedding model and project them into two dimensions for visualization.

Supported dimensionality reduction techniques:

* PCA (Principal Component Analysis)
* t-SNE (t-Distributed Stochastic Neighbor Embedding)
* UMAP (Uniform Manifold Approximation and Projection)

---

### 2. Cosine Similarity Matrix

View pairwise semantic similarity scores between all entered words.

Example:

| Word 1 | Word 2 | Similarity |
| ------ | ------ | ---------- |
| king   | queen  | High       |
| king   | banana | Low        |

---

### 3. Nearest Neighbor Search

Find the most semantically similar words to a selected query word based on cosine similarity.

Example:

```text
Query: king

queen (0.89)
prince (0.84)
royal (0.81)
```

---

### 4. Word Analogy Solver

Perform vector arithmetic on embeddings:

```text
king - man + woman = queen
```

The application calculates:

```text
embedding(king)
− embedding(man)
+ embedding(woman)
```

and returns the closest matching word in the embedding space.

---

## Project Structure

```text
embedding-space-visualizer/
│
├── app.py
│
├── data/
│   └── sample_words.txt
│
├── src/
│   ├── embeddings.py
│   ├── reducer.py
│   ├── visualizer.py
│   ├── similarity.py
│   ├── nearest_neighbour.py
│   └── analogy.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

### Machine Learning

* Sentence Transformers
* all-MiniLM-L6-v2
* Scikit-Learn

### Visualization

* Plotly
* Streamlit

### Data Processing

* NumPy
* Pandas

### Dimensionality Reduction

* PCA
* t-SNE
* UMAP

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/embedding-space-visualizer.git

cd embedding-space-visualizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## Example Input

```text
king
queen
man
woman
doctor
nurse
teacher
student
engineer
scientist
```

---

## How It Works

### Step 1: Generate Embeddings

The application uses a pre-trained transformer model:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

Each word is converted into a dense numerical vector that captures semantic meaning.

---

### Step 2: Reduce Dimensions

Since embeddings exist in hundreds of dimensions, the vectors are projected into 2D using one of:

* PCA
* t-SNE
* UMAP

---

### Step 3: Visualize

Plotly generates an interactive scatter plot where:

* Nearby points represent semantically similar words
* Distant points represent unrelated concepts

---

### Step 4: Semantic Analysis

The application provides:

* Similarity matrix
* Nearest-neighbor retrieval
* Word analogy reasoning

using cosine similarity.

---

## Educational Value

This project is ideal for learning:

* Embeddings and vector representations
* Semantic similarity
* Transformer-based sentence encoders
* Vector arithmetic
* Dimensionality reduction
* Interactive machine learning applications
* Natural Language Processing fundamentals

---

## Sample Analogy Tasks

```text
king - man + woman = queen

paris - france + italy = rome

doctor - hospital + school = teacher
```

---

## Future Improvements

Possible enhancements include:

* Support for sentence embeddings
* 3D visualization
* Clustering algorithms
* Interactive nearest-neighbor highlighting
* Embedding comparison across multiple models
* FAISS-based vector search
* Custom embedding uploads
* Export visualizations as images

---

## Business Applications

Embedding visualization and similarity analysis are widely used in:

* Semantic search systems
* Recommendation engines
* Chatbots and virtual assistants
* Document retrieval
* Customer feedback analysis
* Knowledge management systems
* Information retrieval pipelines
* Large Language Model (LLM) applications

---

## Learning Outcomes

By building this project, you will gain hands-on experience with:

* Embedding generation
* Vector databases concepts
* Similarity search
* Dimensionality reduction techniques
* NLP workflows
* Interactive ML application development
* Streamlit deployment

---

## License

This project is licensed under the MIT License.

---

## Author

**Sriram M S**

Built as part of an LLM, Embeddings, and Vector Space Learning portfolio to demonstrate practical understanding of semantic representations and vector-based reasoning.
