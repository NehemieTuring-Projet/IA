import os
from pathlib import Path
from app.ingestion.loader import load_pdf
from app.ingestion.chunker import split_documents
from app.ingestion.embeddings import get_embeddings
from app.vectorstore.qdrant import create_vector_store


def main():
    # Chemin absolu vers le dossier documents
    docs_dir = Path(__file__).parent / "documents"

    # Charger tous les PDF du dossier
    all_documents = []

    for pdf_file in docs_dir.glob("*.pdf"):
        print(f"Chargement de : {pdf_file.name}")
        docs = load_pdf(str(pdf_file))
        all_documents.extend(docs)

    if not all_documents:
        print("Erreur : Aucun document n'a pu être chargé.")
        return

    print(f"\n{len(all_documents)} pages chargées au total.")

    print("Découpage en chunks...")
    chunks = split_documents(all_documents)
    print(f"{len(chunks)} chunks créés.")

    print("Création des embeddings et stockage dans Qdrant...")
    embeddings = get_embeddings()
    create_vector_store(chunks, embeddings)

    print("\nTerminé ! La collection 'documents' est créée dans Qdrant.")


if __name__ == "__main__":
    main()
