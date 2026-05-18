from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.repository import Repository
from app.schema.repository_schema import RepositoryCreate
from app.services.github_service import get_repo_details
from app.services.ingestion_service import (
    ingest_repository_chunks
)

router = APIRouter()

@router.post("/ingest")

def ingest_repository(
    repo: RepositoryCreate, 
    db: Session = Depends(get_db)
):
    github_data = get_repo_details(repo.repo_url)

    if not github_data:
        return {"error": "Failed to fetch repository details from GitHub."}
    
    new_repo = Repository(
        repo_name=github_data["repo_name"],
        repo_url=github_data["repo_url"],
        branch=github_data["default_branch"],
        status="ingested"
    )

    db.add(new_repo)
    db.commit()
    db.refresh(new_repo)

    ingest_repository_chunks(
    repo.repo_url,
    new_repo.id,
    db
)

    return {
        "message": "Repository ingested successfully",
        "repository_id": new_repo.id
    }