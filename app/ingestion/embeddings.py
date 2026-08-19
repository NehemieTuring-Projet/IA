from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    """
    Charge le modèle d'embeddings.
    
    Le modèle fonctionne localement :
    aucune API payante n'est nécessaire.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings
