from typing import TypedDict


class AgentState(TypedDict):
    """
    État qui circule entre les différentes étapes
    du workflow LangGraph.
    """

    question: str

    # Documents récupérés dans Qdrant
    context: list

    # Réponse générée par Gemini
    answer: str
