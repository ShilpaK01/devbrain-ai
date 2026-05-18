from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.models import repository
from app.models import code_chunk
from app.routes.chat_routes import router as chat_router
from app.routes.repository_routes import router as repository_router
from app.routes.documentation_routes import (
    router as documentation_router
)

app = FastAPI()
app.include_router(chat_router)
app.include_router(repository_router)
app.include_router(documentation_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {"message":"DevBrain AI Backend Running"}