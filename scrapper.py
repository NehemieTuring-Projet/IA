import csv
import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"

# La fonction qui nous permet de scrapper les données du site
def scrape_jobs():
    # On récupère le code html de la page web dont l'URL est ci-dessus
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job in soup.select("div.card-content"):
        # Ici nous analysons Soup et nous stockons dans les variable ci-dessous les differents champs d'un emploie

        title_element = job.select_one("h2.title")
        company_element = job.select_one("h3.company")
        location_element = job.select_one("p.location")
        link_element = job.select_one("a.card-footer-item")

        title = title_element.get_text(strip=True) if title_element else ""
        company = company_element.get_text(strip=True) if company_element else ""
        location = location_element.get_text(strip=True) if location_element else ""

        if link_element and link_element.get("href"):
            job_url = link_element["href"]
        else:
            job_url = ""


        
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "url": job_url
        })
    return jobs

# La fonction qui nous permet de sauvegarder les données dans un fichier CSV
def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "company", "location", "url"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(jobs)

# La fonction principale qui permet d'executer le code
if __name__ == "__main__":
    jobs = scrape_jobs()

    save_to_csv(jobs)

    print(f"{len(jobs)} offres enregistrées dans jobs.csv")