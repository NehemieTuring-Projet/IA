# 🤖 RAG AI Agent

Agent intelligent de question-réponse basé sur vos propres documents, utilisant l'architecture **RAG** (Retrieval-Augmented Generation) avec **LangGraph**, **Qdrant**, et **Gemini**.

---

## 📋 Table des matières

- [Problématique](#-problématique)
- [Solution proposée](#-solution-proposée)
- [Architecture de la solution](#-architecture-de-la-solution)
- [Structure du projet](#-structure-du-projet)
- [Technologies utilisées](#-technologies-utilisées)
- [Prérequis](#-prérequis)
- [Installation et lancement](#-installation-et-lancement)
- [Utilisation de l'API](#-utilisation-de-lapi)
- [Ce que le projet apporte](#-ce-que-le-projet-apporte)

---

## ❓ Problématique

Les modèles de langage (LLM) comme Gemini sont puissants, mais ils présentent une limitation majeure : **ils ne connaissent pas vos documents privés**. Si vous leur posez une question sur le contenu d'un cours, d'un rapport interne ou d'un document personnel, ils ne pourront pas y répondre correctement. Ils risquent même d'**halluciner**, c'est-à-dire inventer une réponse qui semble plausible mais qui est fausse.

**Comment permettre à un LLM de répondre de manière fiable à des questions portant sur des documents spécifiques qu'il n'a jamais vus ?**

---

## 💡 Solution proposée

Ce projet implémente un **agent RAG** (Retrieval-Augmented Generation) qui résout ce problème en 3 étapes :

1. **Ingestion** : Les documents PDF sont chargés, découpés en petits morceaux (chunks) et transformés en vecteurs numériques (embeddings) stockés dans une base de données vectorielle.
2. **Recherche** (Retrieval) : Lorsqu'une question est posée, le système recherche les morceaux de documents les plus pertinents par rapport à la question.
3. **Génération** : Les morceaux pertinents sont envoyés comme contexte au LLM (Gemini), qui génère une réponse **uniquement basée sur les documents fournis**, éliminant ainsi les hallucinations.

Le tout est orchestré par **LangGraph** qui gère le workflow sous forme de graphe, et exposé via une **API REST** avec **FastAPI**.

---

## 🏗 Architecture de la solution

```
                    DOCUMENTS
                 PDF / TXT / DOCX
                       │
                       ▼
                ┌─────────────┐
                │  LangChain  │
                │ Load + Chunk│
                └──────┬──────┘
                       │
                       ▼
              Sentence Transformers
                   Embeddings
                       │
                       ▼
                 ┌──────────┐
                 │  Qdrant  │
                 └────┬─────┘
                      │
                      │ recherche
                      ▼
Question ──────► LangGraph
                      │
                      ▼
              Contexte pertinent
                      │
                      ▼
                 Gemini API
                      │
                      ▼
                   Réponse
                      │
                      ▼
                  FastAPI
```

### Flux détaillé

| Étape | Composant | Rôle |
|-------|-----------|------|
| 1 | **LangChain (PyPDFLoader)** | Charge les fichiers PDF et extrait le texte page par page |
| 2 | **LangChain (RecursiveCharacterTextSplitter)** | Découpe le texte en chunks de 500 caractères avec un chevauchement de 50 |
| 3 | **Sentence Transformers** | Transforme chaque chunk en vecteur numérique (embedding) via le modèle `all-MiniLM-L6-v2` (local, gratuit) |
| 4 | **Qdrant** | Stocke les vecteurs et permet la recherche par similarité |
| 5 | **LangGraph** | Orchestre le workflow : recherche → génération |
| 6 | **Gemini API** | Génère une réponse contextuelle à partir des chunks pertinents |
| 7 | **FastAPI** | Expose l'agent via une API REST |

---

## 📁 Structure du projet

```
rag-agent/
│
├── documents/              # Dossier contenant vos fichiers PDF
│   ├── cours_ia.pdf
│   └── cours_python.pdf
│
├── app/
│   ├── main.py             # Point d'entrée FastAPI
│   │
│   ├── ingestion/          # Chargement et préparation des documents
│   │   ├── loader.py       # Chargement des PDF (PyPDFLoader)
│   │   ├── chunker.py      # Découpage en chunks
│   │   └── embeddings.py   # Modèle d'embeddings (HuggingFace)
│   │
│   ├── vectorstore/        # Base de données vectorielle
│   │   └── qdrant.py       # Connexion et opérations Qdrant
│   │
│   ├── rag/                # Logique de recherche
│   │   └── retrieval.py    # Recherche par similarité
│   │
│   ├── agent/              # Agent LangGraph
│   │   ├── graph.py        # Définition du workflow (graphe)
│   │   ├── nodes.py        # Étapes du workflow (retrieve + generate)
│   │   └── state.py        # Structure de l'état partagé
│   │
│   └── api/                # Couche API
│       └── routes.py       # Endpoints REST
│
├── ingest.py               # Script d'ingestion des documents
├── .env                    # Clé API Google (GOOGLE_API_KEY)
├── requirements.txt        # Dépendances Python
└── README.md
```

---

## 🛠 Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **Python 3.10+** | Langage principal |
| **LangChain** | Chargement de documents, découpage en chunks, interface LLM |
| **LangGraph** | Orchestration du workflow sous forme de graphe |
| **Qdrant** | Base de données vectorielle (via Docker) |
| **Sentence Transformers** | Génération d'embeddings locaux (`all-MiniLM-L6-v2`) |
| **Gemini (Google)** | LLM pour la génération de réponses |
| **FastAPI** | Framework pour l'API REST |
| **Uvicorn** | Serveur ASGI pour exécuter FastAPI |

---

## 📦 Prérequis

- **Python 3.10** ou supérieur
- **Docker** (pour exécuter Qdrant)
- **Une clé API Google** (pour Gemini) → [Obtenir une clé](https://aistudio.google.com/apikey)

---

## 🚀 Installation et lancement

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd rag-agent
```

### 2. Installer les dépendances Python

```bash
pip install langchain langchain-community langchain-text-splitters langchain-qdrant langchain-huggingface sentence-transformers qdrant-client langgraph langchain-google-genai fastapi uvicorn pypdf python-dotenv
```

### 3. Configurer la clé API

Créez un fichier `.env` à la racine du projet et ajoutez votre clé API Google :

```env
GOOGLE_API_KEY=votre_cle_api_google_ici
```

### 4. Ajouter vos documents

Placez vos fichiers PDF dans le dossier `documents/`.

### 5. Lancer la base de données Qdrant (Docker)

```bash
docker run -p 6333:6333 qdrant/qdrant
```

> ⚠️ Laissez ce terminal ouvert, Qdrant doit rester actif.

### 6. Ingérer les documents dans Qdrant

Dans un nouveau terminal, exécutez le script d'ingestion qui va charger vos PDF, les découper, créer les embeddings et les stocker dans Qdrant :

```bash
python3 ingest.py
```

> Cette étape n'est à faire qu'**une seule fois** (ou à chaque fois que vous ajoutez de nouveaux documents).

### 7. Lancer le serveur FastAPI

```bash
uvicorn app.main:app --reload --env-file .env
```

Le serveur démarre sur [http://localhost:8000](http://localhost:8000).

---

## 💬 Utilisation de l'API

### Documentation interactive (Swagger UI)

Ouvrez votre navigateur sur [http://localhost:8000/docs](http://localhost:8000/docs) pour accéder à l'interface interactive. Cliquez sur **POST /chat** → **Try it out** pour tester.

### Via curl (terminal)

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "Qu est-ce que le machine learning ?"}'
```

### Via Postman

- **Méthode** : POST
- **URL** : `http://localhost:8000/chat`
- **Body** (JSON) :

```json
{
  "question": "Qu'est-ce que le machine learning ?"
}
```

### Exemple de réponse

```json
{
  "answer": "D'après les documents fournis, le machine learning est une branche de l'intelligence artificielle qui permet aux machines d'apprendre à partir de données..."
}
```

---

## ✨ Ce que le projet apporte

| Avantage | Description |
|----------|-------------|
| **Réponses fiables** | L'agent répond uniquement à partir de vos documents, pas d'hallucinations |
| **Données privées** | Vos documents restent locaux, jamais envoyés à un service tiers pour l'indexation |
| **Embeddings gratuits** | Le modèle Sentence Transformers fonctionne localement, sans coût |
| **Extensible** | Ajoutez facilement de nouveaux documents en relançant `ingest.py` |
| **API prête à l'emploi** | L'API REST peut être intégrée dans n'importe quelle application (web, mobile, chatbot) |
| **Architecture modulaire** | Chaque composant (ingestion, vectorstore, RAG, agent, API) est indépendant et réutilisable |
| **Workflow orchestré** | LangGraph permet d'ajouter facilement de nouvelles étapes au pipeline (validation, reformulation, etc.) |

---

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives et personnelles.
