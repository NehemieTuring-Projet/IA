# 🤖 Assistant IA - Gemini API

Un chatbot en ligne de commande qui utilise l'API Google Gemini pour répondre à vos questions.

## 📋 Prérequis

- **Python 3.10+**
- Un compte Google et une **clé API Gemini** (gratuite)

## 🚀 Installation

### 1. Installer les dépendances

```bash
pip install google-genai python-dotenv
```

| Package         | Rôle                                                                 |
|-----------------|----------------------------------------------------------------------|
| `google-genai`  | Permet à Python de communiquer avec l'API Google Gemini              |
| `python-dotenv` | Charge la clé API depuis un fichier `.env` (sécurité)                |

### 2. Obtenir une clé API

1. Rendez-vous sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Connectez-vous avec votre compte Google
3. Cliquez sur **"Create API Key"**
4. Copiez la clé générée

### 3. Configurer la clé API

Créez un fichier `.env` à la racine du projet :

```
GEMINI_API_KEY=votre-clé-ici
```

> ⚠️ **Ne partagez jamais votre clé API** et ne la commitez pas sur Git.

## ▶️ Lancer le programme

```bash
python3 main.py
```

Le programme vous demandera de saisir une question, puis affichera la réponse générée par Gemini.

### Exemple

```
$ python3 main.py
Entrer votre question: Qui est le président du Cameroun ?
Le président actuel du Cameroun est Paul Biya. Il est à la tête de l'État depuis le 6 novembre 1982.
```

## 📁 Structure du projet

```
OPENAI/
├── main.py     # Script principal
├── .env        # Clé API (non versionné)
├── Note.txt    # Notes explicatives
└── README.md   # Ce fichier
```

## 🔧 Détails techniques

- **Modèle utilisé** : `gemini-3.5-flash`
- **SDK** : `google-genai`
- Le code OpenAI original est conservé en commentaire dans `main.py` pour référence
