from pydantic import BaseModel

class RepositoryCreate(BaseModel):
    repo_url:str