# DevBrain AI

AI-powered repository analysis system built using FastAPI, LangGraph, Gemini, pgvector, and semantic code retrieval.

## Features

- Repository ingestion from GitHub
- Semantic code search using embeddings
- pgvector vector database integration
- AI-powered documentation agent
- LangGraph workflow orchestration
- FastAPI backend APIs
- Gemini 2.5 Flash integration

## Tech Stack

- FastAPI
- PostgreSQL
- pgvector
- Sentence Transformers
- Gemini API
- LangGraph
- SQLAlchemy
- Docker

## API Endpoints

### Ingest Repository

POST `/ingest`

```json
{
  "repo_url": "https://github.com/pallets/flask"
}
```

### Ask Questions

POST `/ask`

```json
{
  "question": "How routing works?"
}
```

### Documentation Agent

POST `/documentation`

```json
{
  "question": "Explain routing architecture"
}
```

## Architecture

1. Repository ingestion
2. Code chunking
3. Embedding generation
4. Vector storage using pgvector
5. Semantic retrieval
6. AI response generation using Gemini
7. LangGraph orchestration

## Run Locally

```bash
uvicorn app.main:app --reload
```

## Future Improvements

- Multi-agent architecture
- Background ingestion
- Streaming responses
- Frontend UI
- Dockerized backend deployment