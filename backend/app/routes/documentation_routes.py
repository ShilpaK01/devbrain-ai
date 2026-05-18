from fastapi import APIRouter

from app.schema.chat_schema import (
    QuestionRequest
)

from app.agents.documentation_agent import (
    documentation_agent
)


router = APIRouter()


@router.post("/documentation")
def generate_documentation(
    request: QuestionRequest
):

    answer = documentation_agent(
        request.question
    )

    return {
        "question": request.question,
        "documentation": answer
    }