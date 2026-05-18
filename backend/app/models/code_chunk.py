from sqlalchemy import Column, Integer, String, Text, ForeignKey
from pgvector.sqlalchemy import Vector

from app.db.base import Base


class CodeChunk(Base):

    __tablename__ = "code_chunks"

    id = Column(Integer, primary_key=True, index=True)

    repository_id = Column(
        Integer,
        ForeignKey("repositories.id")
    )

    file_path = Column(String)

    function_name = Column(String)

    code_chunk = Column(Text)

    embedding = Column(Vector(384))