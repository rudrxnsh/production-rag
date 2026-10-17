
# Production RAG — Enterprise Knowledge Assistant

A production-oriented Retrieval-Augmented Generation (RAG) system designed to answer questions from enterprise documents using evidence-backed retrieval and source citations.

## Project Status

**Status:** Foundation setup

This project is under active development. Planned features are not considered complete until implemented and tested.

## Objectives

- Ingest PDF and DOCX documents.
- Extract and chunk text while preserving source metadata.
- Store document embeddings in PostgreSQL with pgvector.
- Combine semantic and keyword retrieval.
- Improve retrieval using Reciprocal Rank Fusion (RRF) and reranking.
- Generate answers grounded in retrieved context.
- Return citations with source document and page information.
- Expose the system through a FastAPI backend.
- Evaluate retrieval quality and answer grounding.
- Package the application for reproducible deployment.

## Planned Technology Stack

- Python
- FastAPI and Pydantic
- PostgreSQL and pgvector
- LangChain and LangGraph
- PyMuPDF and python-docx
- Pytest and Ruff
- Docker Compose

The final stack may evolve as implementation and evaluation reveal what is necessary.

## Architecture

Planned pipeline:

1. Document ingestion and validation
2. Text extraction and chunking
3. Embedding generation and indexing
4. Hybrid retrieval and reranking
5. Context construction and answer generation
6. Citation generation and evaluation
7. API delivery and deployment

## Project Structure

```text
production-rag/
├── src/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── generation/
│   ├── ingestion/
│   ├── retrieval/
│   └── workflows/
├── tests/
├── docs/
├── evals/
├── scripts/
├── alembic/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Prerequisites

- Python 3.12 or newer
- Git
- A virtual environment

Database and model-provider setup will be documented as those components are implemented.

## Development Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the project and development dependencies.
4. Run the configured linting and test commands.

Detailed commands will be added as the foundation is verified.

## Evaluation

The project will use reproducible evaluation datasets and report relevant metrics such as Recall@K, Mean Reciprocal Rank (MRR), answer relevance, and groundedness where appropriate.

No performance claims are made until they are measured and documented.

## Security

- Do not commit API keys, passwords, or private documents.
- Keep secrets in local environment configuration or a secret manager.
- Validate uploaded files and enforce resource limits.
- Restrict access to documents and their retrieved content.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
