from fastapi import FastAPI

from app.api.routes import router


# Création de l'application FastAPI
app = FastAPI(
    title="RAG AI Agent",
    description="Agent IA utilisant RAG, LangGraph, Qdrant et Gemini",
    version="1.0.0"
)


# Ajout des routes
app.include_router(router)


@app.get("/")
def root():
    """
    Vérifie que l'API fonctionne.
    """

    return {
        "message": "RAG AI Agent is running"
    }
