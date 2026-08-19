# Extracteur d'offres d'emploi Python

## Description du projet
Dans ce projet, nous créons un scraper web en Python qui récupère les offres d'emploi du [**Fake Python Jobs**](https://realpython.github.io/fake-jobs/). Ce scraper extrait des informations telles que l'intitulé du poste, le nom de l'entreprise, le lieu et un lien vers la description complète du poste.

Ce site, conçu spécifiquement pour l'apprentissage, est idéal pour les débutants. Il permet de se concentrer sur la compréhension de la structure HTML, la sélection des éléments et le traitement des données sans se soucier des protections anti-extraction complexes ni des restrictions légales.

## Exigences du projet
- Récupérer les données depuis [https://realpython.github.io/fake-jobs/](https://realpython.github.io/fake-jobs/)
- Extraire les champs suivants pour chaque offre d'emploi :
  - Titre de l'emploi
  - Nom de l'entreprise
  - Emplacement
  - URL de la page de détails de l'emploi
- Enregistrer les résultats dans un fichier CSV
- Utiliser un code Python propre et lisible
- Gérer les cas limites simples (par exemple, les champs manquants)

## Technologies utilisées
- **Python**
- **Requests** – pour récupérer la page web
- **Beautiful Soup (bs4)** – pour analyser et naviguer dans le HTML
- **Module CSV** – pour enregistrer les offres d'emploi

## Architecture de la solution
Le projet se compose d'un script principal (`scrapper.py`) qui gère de bout en bout la récupération de la page, l'analyse du code HTML et la sauvegarde des données structurées dans un fichier CSV (`jobs.csv`).

## Description du code
Le script `scrapper.py` s'articule autour de deux fonctions principales :
- `scrape_jobs()`: Effectue une requête HTTP GET vers l'URL cible, analyse le contenu HTML à l'aide de BeautifulSoup, et parcourt les éléments pour extraire le titre, l'entreprise, la localisation et le lien de chaque offre. Elle gère les attributs manquants et retourne une liste de dictionnaires.
- `save_to_csv(jobs, filename="jobs.csv")`: Prend la liste de dictionnaires extraite et l'enregistre de manière structurée dans un fichier CSV en utilisant le module standard `csv` de Python.

## Comment lancer le code 

1. **Créer l'environnement virtuel** :
   ```bash
   python3 -m venv venv
   ```

2. **Activer l'environnement virtuel** :
   ```bash
   source venv/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install requests beautifulsoup4
   ```

4. **Lancer le scraper** :
   *(Note : Une connexion internet est requise pour récupérer la page web).*
   ```bash
   python scrapper.py
   ```

---

## Ce que l'on apprend à travers ce projet
Après avoir réalisé ce projet, vous saurez inspecter le code HTML d'une page web, identifier des modèles réutilisables et extraire des données structurées à l'aide de Python. Vous vous familiariserez avec l'utilisation de bibliothèques tierces, l'organisation des données extraites et leur exportation pour une analyse ultérieure. Ce projet vous prépare également à aborder des tâches d'extraction de données plus avancées, telles que la pagination, le filtrage et l'analyse de sites web réels.
