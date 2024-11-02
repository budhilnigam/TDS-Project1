import json
import csv

# Load JSON data from a file
with open("repositories.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define the fields we want to keep and process
fields = [
    "login", "full_name", "created_at", "stargazers_count", 
    "watchers_count", "language", "has_projects", "has_wiki", 
    "license_name"
]

# Open CSV file and write the cleaned data with UTF-8 encoding
with open("repositories.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    
    for repo in data:
        # Create a dictionary with the selected and processed fields
        cleaned_repo = {
            "login": repo["login"],
            "full_name": repo.get("full_name"),
            "created_at": repo.get("created_at"),
            "stargazers_count": repo.get("stargazers_count"),
            "watchers_count": repo.get("watchers_count"),
            "language": repo.get("language"),
            "has_projects": repo.get("has_projects"),
            "has_wiki": repo.get("has_wiki"),
            "license_name": repo["license_name"]
        }
        writer.writerow(cleaned_repo)

print("Selected data has been cleaned and written to repositories.csv.")