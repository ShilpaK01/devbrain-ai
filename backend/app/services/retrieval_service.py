from sqlalchemy.orm import Session
from sqlalchemy import text

from app.services.embedding_service import (
    generate_embedding
)


def search_similar_chunks(
    query: str,
    db: Session,
    limit: int = 5
):

    query_embedding = generate_embedding(query)

    sql = text("""
        SELECT
            file_path,
            function_name,
            code_chunk,
            embedding <=> CAST(:embedding AS vector) AS distance
        FROM code_chunks
        ORDER BY distance
        LIMIT :limit
    """)

    results = db.execute(
        sql,
        {
            "embedding": str(query_embedding),
            "limit": limit
        }
    )

    return results.fetchall()