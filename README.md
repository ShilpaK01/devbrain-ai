# 🚀 DevBrain AI

**DevBrain AI** is a production-ready AI-powered repository analysis platform that enables developers to understand and explore GitHub repositories through natural language. Using **Retrieval-Augmented Generation (RAG)**, semantic code search, and **LangGraph** orchestration, the system retrieves relevant code from a repository and generates context-aware responses using **Google Gemini 2.5 Flash**.

The project is designed to help developers quickly understand unfamiliar codebases, generate architecture-aware documentation, and answer technical questions without manually navigating thousands of lines of code.

---

## ✨ Features

- 📂 Analyze public GitHub repositories
- 🔍 Semantic code search using vector embeddings
- 🤖 Conversational repository Q&A powered by Gemini 2.5 Flash
- 📖 AI-generated repository documentation
- 🔄 LangGraph workflow orchestration
- ⚡ FastAPI REST APIs
- 🗄️ PostgreSQL + pgvector for vector storage
- 🐳 Dockerized backend for easy deployment

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | REST API framework |
| LangGraph | Workflow orchestration |
| Google Gemini 2.5 Flash | Large Language Model |
| Sentence Transformers | Embedding generation |
| PostgreSQL | Database |
| pgvector | Vector similarity search |
| SQLAlchemy | ORM |
| Docker | Containerization |

---

# System Architecture

```
                GitHub Repository
                        │
                        ▼
              Repository Ingestion
                        │
                        ▼
               AST Code Chunking
                        │
                        ▼
          Sentence Transformer Embeddings
                        │
                        ▼
             PostgreSQL + pgvector
                        │
                        ▼
               Semantic Retrieval
                        │
                        ▼
               LangGraph Workflow
                        │
                        ▼
            Gemini 2.5 Flash LLM
                        │
                        ▼
              AI Generated Response
```

---

# How It Works

### 1. Repository Ingestion

The user provides a public GitHub repository URL.

Example:

```json
{
    "repo_url":"https://github.com/pallets/flask"
}
```

The application clones the repository and extracts source files for analysis.

---

### 2. Code Chunking

The repository is divided into meaningful chunks using AST-based parsing to preserve the logical structure of the codebase.

---

### 3. Embedding Generation

Each code chunk is converted into semantic embeddings using Sentence Transformers.

---

### 4. Vector Storage

Generated embeddings are stored in PostgreSQL using the pgvector extension for efficient similarity search.

---

### 5. Semantic Retrieval

When a user asks a question, the application retrieves the most relevant code chunks from the vector database.

---

### 6. AI Response Generation

The retrieved context is passed to Gemini 2.5 Flash through a LangGraph workflow, which generates accurate and context-aware responses.

---

# API Endpoints

## Repository Ingestion

**POST** `/ingest`

Request

```json
{
    "repo_url":"https://github.com/pallets/flask"
}
```

---

## Ask Questions

**POST** `/ask`

Request

```json
{
    "question":"How does routing work?"
}
```

---

## Documentation Generator

**POST** `/documentation`

Request

```json
{
    "question":"Explain the repository architecture."
}
```

---

# Project Structure

```
DevBrain-AI/

│
├── app/
│   ├── api/
│   ├── database/
│   ├── graph/
│   ├── models/
│   ├── services/
│   ├── embeddings/
│   └── main.py
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .env.example
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/devbrain-ai.git

cd devbrain-ai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql://username:password@localhost/devbrain

GEMINI_API_KEY=your_api_key
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# Technical Highlights

- Built an end-to-end Retrieval-Augmented Generation (RAG) pipeline for repository analysis.
- Implemented semantic code retrieval using Sentence Transformers and pgvector.
- Designed modular LangGraph workflows for retrieval and response generation.
- Integrated Google Gemini 2.5 Flash for context-aware code explanations.
- Developed RESTful APIs using FastAPI.
- Containerized the backend using Docker for deployment.
- Structured the application using a modular and scalable architecture.

---

# Future Improvements

- Multi-agent repository analysis
- Streaming responses
- Background repository indexing
- Authentication and user management
- Repository visualization dashboard
- Support for private GitHub repositories
- Frontend interface using React or Next.js
- Evaluation pipeline for response quality

---

# Screenshots

> Add screenshots here.

- Repository Ingestion
- Swagger API
- Ask Question
- Documentation Generation

---

# Demo

> Add a GIF or short screen recording demonstrating:

- Repository ingestion
- Asking repository questions
- Generated responses
- Documentation generation

---

# License

This project is licensed under the MIT License.

---

# Author

**Shilpa K**

AI Engineer | Generative AI | FastAPI | LangGraph | RAG | Multi-Agent Systems

GitHub: https://github.com/yourusername

Portfolio: https://sanguleakb.github.io
