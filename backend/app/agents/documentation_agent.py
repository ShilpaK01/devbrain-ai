from app.services.retrieval_service import (
    search_similar_chunks
)

from app.services.ai_service import (
    generate_ai_response
)

from app.db.database import SessionLocal


def documentation_agent(query: str):

    db = SessionLocal()

    try:

        chunks = search_similar_chunks(
            query,
            db
        )

        enhanced_prompt = f"""
        You are a senior software architect.

        Analyze the repository codebase carefully.

        Explain the following clearly:
        {query}

        Focus on:
        - architecture
        - workflow
        - important functions
        - technical explanation
        """

        answer = generate_ai_response(
            enhanced_prompt,
            chunks
        )

        return answer

    finally:
        db.close()