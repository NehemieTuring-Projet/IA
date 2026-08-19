from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.graph import create_graph


router = APIRouter()

# Création du workflow LangGraph
graph = create_graph()


class QuestionRequest(BaseModel):
    """
    Structure des données reçues par l'API.
    """

    question: str


@router.post("/chat")
def chat(request: QuestionRequest):
    """
    Endpoint permettant de poser une question à l'agent.
    """

    # État initial du workflow
    state = {
        "question": request.question,
        "context": [],
        "answer": ""
    }

    # Exécution du workflow LangGraph
    result = graph.invoke(state)

    return {
        "answer": result["answer"]
    }
