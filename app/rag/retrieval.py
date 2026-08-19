def retrieve_documents(vector_store, question: str, k: int = 3):
    """
    Recherche les k documents/chunks les plus pertinents
    par rapport à la question.
    """

    documents = vector_store.similarity_search(
        question,
        k=k
    )

    return documents
