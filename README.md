# 🚀 Embedding Space Visualizer

An interactive Streamlit application for exploring word embeddings in a high-dimensional semantic space. This project demonstrates how modern embedding models represent words as vectors and how dimensionality reduction techniques can be used to visualize semantic relationships between words.

The application allows users to generate embeddings, visualize them in 2D, analyze semantic similarity, discover nearest neighbors, and solve word analogies using vector arithmetic.

---

## ✨ Features

* 🤖 Generate embeddings using a pre-trained Sentence Transformer model
* 📊 Visualize embeddings in 2D space using PCA, t-SNE, or UMAP
* 📈 Compute cosine similarity between words
* 🔍 Find nearest neighbors in embedding space
* 🧠 Solve word analogies using vector arithmetic
* 🎈 Interactive web interface built with Streamlit

---

## 📸 Demo Features

### 📊 Embedding Visualization

Convert words into dense vector representations using the `all-MiniLM-L6-v2` embedding model and project them into two dimensions for visualization.

Supported dimensionality reduction techniques:

* PCA (Principal Component Analysis)
* t-SNE (t-Distributed Stochastic Neighbor Embedding)
* UMAP (Uniform Manifold Approximation and Projection)

### 📈 Cosine Similarity Matrix

View pairwise semantic similarity scores between all entered words.

Example:

```text
king ↔ queen     → High Similarity
king ↔ doctor    → Medium Similarity
king ↔ banana    → Low Similarity
```

### 🔍 Nearest Neighbor Search

Find the most semantically similar words to a selected query word.

Example:

```text
Query: king

queen (0.89)
prince (0.84)
royal (0.81)
```

### 🧠 Word Analogy Solver

Perform vector arithmetic on embeddings:

```text
king - man + woman = queen
```

The application computes:

```text
embedding(king)
- embedding(man)
+ embedding(woman)
```

and returns the closest matching word in the embedding space.

---

## 📂 Project Structure

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

## 🛠️ Technologies Used

### 🤖 Machine Learning & NLP

* Sentence Transformers
* all-MiniLM-L6-v2
* Scikit-Learn

### 📊 Visualization

* Plotly
* Streamlit

### 📦 Data Processing

* NumPy
* Pandas

### 🌐 Dimensionality Reduction

* PCA
* t-SNE
* UMAP

---

## ⚙️ Installation

### 📥 Clone Repository

```bash
git clone https://github.com/your-username/embedding-space-visualizer.git

cd embedding-space-visualizer
```

### 📚 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📝 Example Input

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
apple
banana
dog
cat
lion
tiger
```

---

## 🔬 How It Works

### 1️⃣ Generate Embeddings

The application loads a pre-trained transformer model:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

Each word is transformed into a dense numerical vector that captures semantic meaning.

### 2️⃣ Reduce Dimensions

Since embeddings exist in hundreds of dimensions, they are projected into a 2D space using:

* PCA
* t-SNE
* UMAP

### 3️⃣ Visualize Semantic Relationships

The reduced vectors are displayed in an interactive Plotly scatter plot.

Words with similar meanings tend to appear closer together, while unrelated words appear farther apart.

**PCA:**

<img width="975" height="497" alt="image" src="https://github.com/user-attachments/assets/f5bb90e8-80a4-4f55-a204-fab2d112d6b3" />

**t-SNE:**

<img width="975" height="518" alt="image" src="https://github.com/user-attachments/assets/5eacd3f0-65d1-4f55-8dc6-3d24df2c7d57" />

**UMAP:**

<img width="975" height="547" alt="image" src="https://github.com/user-attachments/assets/0f6ba81f-0c98-4f59-8782-c7c4b71a9291" />


### 4️⃣ Analyze Similarity

The application calculates cosine similarity scores to:

* Build a similarity matrix
* Find nearest neighbors
* Solve analogy tasks

---

## 🎓 Educational Value

This project is an excellent learning resource for understanding:

* Embeddings and vector representations
* Semantic similarity
* Transformer-based language models
* Vector arithmetic
* Cosine similarity
* Dimensionality reduction techniques
* Interactive machine learning applications
* Natural Language Processing (NLP)

---

## 💡 Sample Analogy Tasks

```text
king - man + woman = queen

paris - france + italy = rome

doctor - hospital + school = teacher

engineer - machine + medicine = doctor
```

---

## 🏢 Real-World Applications

Embedding-based systems are widely used in modern AI applications:

* 🔎 Semantic Search Engines
* 🎯 Recommendation Systems
* 🤖 Chatbots & Virtual Assistants
* 📚 Document Retrieval
* 💬 Customer Feedback Analysis
* 🧠 Knowledge Management Systems
* 📄 Information Retrieval Pipelines
* 🚀 Large Language Models (LLMs)

---

## 🎯 Learning Outcomes

By building and exploring this project, you will gain practical experience with:

* ✅ Embedding Generation
* ✅ Semantic Similarity Analysis
* ✅ Vector Arithmetic
* ✅ Dimensionality Reduction
* ✅ NLP Fundamentals
* ✅ Transformer Models
* ✅ Streamlit Development
* ✅ Interactive Data Visualization

---

## 🚧 Future Improvements

Potential enhancements for future versions:

* 📄 Sentence and paragraph embeddings
* 🌍 Support for multilingual embeddings
* 🎲 3D embedding visualization
* 🎯 Clustering algorithms (K-Means, DBSCAN)
* ⚡ FAISS-powered nearest neighbor search
* 📤 Export visualizations as images
* 🔄 Compare multiple embedding models
* ☁️ Cloud deployment support
* 📊 Interactive filtering and clustering controls

---

## 📜 License

Feel free to use, modify, and distribute it for educational and professional purposes.

---

## 👨‍💻 Author

**Sriram M S**

Built as part of an AI/LLM portfolio project to demonstrate practical understanding of embeddings, vector spaces, semantic similarity, dimensionality reduction, and modern NLP workflows.
