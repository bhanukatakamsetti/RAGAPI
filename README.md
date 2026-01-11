# RAGAPI

A lightweight **Retrieval-Augmented Generation (RAG)** API built with FastAPI, ChromaDB, and Ollama. This API allows you to build a knowledge base and query it using local LLMs.

## 🚀 Features

- **Add Documents**: Store text documents in a vector database (ChromaDB)
- **Query Knowledge Base**: Ask questions and get AI-generated answers based on your stored documents
- **Local LLM Support**: Uses Ollama for text generation (default: TinyLlama)
- **Persistent Storage**: Documents are stored persistently using ChromaDB
- **Fast & Lightweight**: Built with FastAPI for high performance

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+**
- **Ollama** - [Install Ollama](https://ollama.ai/)
  ```bash
  # Pull the default model
  ollama pull tinyllama
  ```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhanukatakamsetti/RAGAPI.git
   cd RAGAPI
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn chromadb ollama
   ```

## 🚦 Usage

### Start the API Server

```bash
uvicorn app:app --reload
```

Or using Python module:
```bash
python -m uvicorn app:app --reload
```

The API will be available at: `http://localhost:8000`

### Environment Variables

You can customize the LLM model by setting the `MODEL_NAME` environment variable:

```bash
# PowerShell
$env:MODEL_NAME = "llama2"

# Bash/Linux/Mac
export MODEL_NAME="llama2"
```

Default model: `tinyllama`

## 📡 API Endpoints

### 1. Health Check
**GET** `/health`

Check if the API is running.

**Response:**
```json
{
  "status": "ok"
}
```

### 2. Add Document
**POST** `/add?text=<your_text>`

Add a document to the knowledge base.

**Parameters:**
- `text` (string): The document text to store

**Example:**
```bash
curl -X POST "http://localhost:8000/add?text=FastAPI is a modern web framework for building APIs with Python"
```

**Response:**
```json
{
  "status": "success",
  "message": "data is added to knowledge base",
  "id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### 3. Query Knowledge Base
**POST** `/query?q=<your_question>`

Ask a question and get an AI-generated answer based on stored documents.

**Parameters:**
- `q` (string): Your question

**Example:**
```bash
curl -X POST "http://localhost:8000/query?q=What is FastAPI?"
```

**Response:**
```json
{
  "answer": "FastAPI is a modern web framework for building APIs with Python..."
}
```

## 🧪 Example Workflow

```bash
# 1. Add some documents to the knowledge base
curl -X POST "http://localhost:8000/add?text=Python is a high-level programming language"
curl -X POST "http://localhost:8000/add?text=FastAPI is built on top of Starlette and Pydantic"

# 2. Query the knowledge base
curl -X POST "http://localhost:8000/query?q=What is Python?"
```

## 📁 Project Structure

```
RAGAPI/
├── app.py              # Main FastAPI application
├── embed.py            # Embedding utilities
├── chromadb/           # Persistent vector database storage
├── venv/               # Virtual environment (not tracked)
├── __pycache__/        # Python cache (not tracked)
└── README.md           # This file
```

## 🔧 How It Works

1. **Document Storage**: When you add text via `/add`, it's stored in ChromaDB as embeddings
2. **Semantic Search**: When you query via `/query`, ChromaDB finds the most relevant document
3. **Answer Generation**: The relevant context is passed to Ollama LLM which generates an answer

## 📝 Logging

The API logs important events with timestamps:
- Model initialization
- Query requests
- Document additions

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Bhanu Katakamsetti**
- GitHub: [@bhanukatakamsetti](https://github.com/bhanukatakamsetti)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [Ollama](https://ollama.ai/) - Local LLM runtime
