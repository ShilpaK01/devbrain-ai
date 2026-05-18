from sqlalchemy.orm import Session

from app.models.code_chunk import CodeChunk

from app.services.github_service import (
    get_repository_files,
    get_file_content
)

from app.services.chunking_service import (
    chunk_python_code
)

from app.services.embedding_service import (
    generate_embedding
)


def ingest_repository_chunks(
    repo_url: str,
    repository_id: int,
    db: Session
):

    files = get_repository_files(repo_url)

    python_files = [
        file for file in files
        if file.endswith(".py")
    ]

    for file_path in python_files:

        content = get_file_content(
            repo_url,
            file_path
        )

        if not content:
            continue

        chunks = chunk_python_code(content)

        for chunk in chunks:

            embedding = generate_embedding(
                chunk["code"]
            )

            db_chunk = CodeChunk(

                repository_id=repository_id,

                file_path=file_path,

                function_name=chunk["name"],

                code_chunk=chunk["code"],

                embedding=embedding
            )

            db.add(db_chunk)

    db.commit()