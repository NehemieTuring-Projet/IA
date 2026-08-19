from langchain_google_genai import ChatGoogleGenerativeAI

from app.ingestion.embeddings import get_embeddings
from app.vectorstore.qdrant import get_vector_store
from app.rag.retrieval import retrieve_documents


# Modèle Gemini utilisé pour générer les réponses
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


# Embeddings
embeddings = get_embeddings()

# Connexion à Qdrant
vector_store = get_vector_store(embeddings)


def retrieve_node(state):
    """
    Node 1 :
    Recherche les documents pertinents dans Qdrant.
    """

    question = state["question"]

    documents = retrieve_documents(
        vector_store,
        question
    )

    return {
        "context": documents
    }


def generate_node(state):
    """
    Node 2 :
    Utilise Gemini pour générer une réponse
    à partir de la question et du contexte.
    """

    question = state["question"]
    documents = state["context"]

    # On transforme les documents en texte
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
Tu es un assistant utilisant un système RAG.

Réponds à la question uniquement à partir
du contexte fourni.

CONTEXTE :
{context}

QUESTION :
{question}

Si l'information n'est pas présente dans le contexte,
indique que tu ne disposes pas de cette information.
"""

    # Appel à Gemini
    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }
