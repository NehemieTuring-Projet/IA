from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Découpe les documents en petits morceaux appelés 'chunks'.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      # Taille maximale d'un chunk
        chunk_overlap=50     # Texte commun entre deux chunks
    )

    chunks = splitter.split_documents(documents)

    return chunks
