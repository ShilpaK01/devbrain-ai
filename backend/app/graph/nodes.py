from app.graph.state import GraphState
from app.services.retrieval_service import search_similar_chunks
from app.services.ai_service import generate_ai_response
from app.db.database import SessionLocal

def retrieval_node(graph_state:GraphState):
    db = SessionLocal()
    
    chunks = search_similar_chunks(
        graph_state["question"],
        db
    )
    return {
        "chunks": chunks
    }

def generation_node(graph_state:GraphState):

    answer = generate_ai_response(
        graph_state["question"],
        graph_state["chunks"]
    )
    return{
        "answer":answer
    }