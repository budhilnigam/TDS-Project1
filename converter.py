import json
import csv
import re

# Load JSON data from a file
with open("users.json", "r",encoding="utf-8") as f:
    data = json.load(f)

# Define the fields we want to keep and process
fields = [
    "login", "name", "company", "location", "email", 
    "hireable", "bio", "public_repos", "followers", 
    "following", "created_at"
]

# Function to clean up company names
def clean_company_name(company):
    if company:
        # Remove leading whitespace and leading @ if it exists, convert to uppercase
        return re.sub(r"^@", "", company.strip()).upper()
    return company

# Open CSV file and write the cleaned data
with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    
    for user in data:
        # Create a dictionary with the selected and processed fields
        cleaned_user = {
            "login": user.get("login"),
            "name": user.get("name"),
            "company": clean_company_name(user.get("company")),
            "location": user.get("location"),
            "email": user.get("email"),
            "hireable": user.get("hireable"),
            "bio": user.get("bio"),
            "public_repos": user.get("public_repos"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "created_at": user.get("created_at"),
        }
        writer.writerow(cleaned_user)

print("Selected data has been cleaned and written to cleaned_users.csv.")