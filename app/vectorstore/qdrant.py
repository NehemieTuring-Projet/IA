from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore


# Connexion à Qdrant
client = QdrantClient(
    url="http://localhost:6333"
)


def create_vector_store(chunks, embeddings):
    """
    Transforme les chunks en vecteurs et les stocke dans Qdrant.
    """

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name="documents"
    )

    return vector_store


def get_vector_store(embeddings):
    """
    Récupère une collection Qdrant existante.
    """

    return QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name="documents",
        url="http://localhost:6333"
    )
