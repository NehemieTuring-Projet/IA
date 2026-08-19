# Permet de charger des fichiers PDF
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Charge un fichier PDF et retourne une liste de documents LangChain.
    Chaque page du PDF devient un Document.
    """

    loader = PyPDFLoader(file_path)

    # Extraction du contenu du PDF
    documents = loader.load()

    return documents
