from fastapi import APIRouter

from app.schema.chat_schema import (
    QuestionRequest
)

from app.graph.rag_graph import (
    rag_graph
)


router = APIRouter()


@router.post("/ask")
def ask_question(request: QuestionRequest):

    result = rag_graph.invoke({
        "question": request.question
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }