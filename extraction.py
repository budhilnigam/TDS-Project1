import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}","Accept": "application/vnd.github+json"}
# Replace with your JSON data containing users
with open("tokyo.json", "r") as f:
    user_data = json.load(f)

# GitHub API base URL
base_url = "https://api.github.com/users/"

# Function to get user data
def fetch_user_data(username):
    user_url = f"{base_url}{username}"
    response = requests.get(user_url,headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch user data for {username}")
        return None

# Function to get repository data for a user
def fetch_repositories(username, max_repos=500):
    repos_url = f"{base_url}{username}/repos?sort=pushed&per_page=100"
    repos = []
    page = 1

    while len(repos) < max_repos:
        response = requests.get(f"{repos_url}&page={page}",headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch repos for {username} on page {page}")
            break

        page_data = response.json()
        if not page_data:
            break

        for repo in page_data:
            if len(repos) >= max_repos:
                break

            repo_data = {
                "login": username,
                "full_name": repo["full_name"],
                "created_at": repo["created_at"],
                "stargazers_count": repo["stargazers_count"],
                "watchers_count": repo["watchers_count"],
                "language": repo["language"],
                "has_projects": repo["has_projects"],
                "has_wiki": repo["has_wiki"],
                "license_name": repo["license"]["name"] if repo["license"] else None
            }
            repos.append(repo_data)

        page += 1
        time.sleep(1)  # To respect GitHub's rate limits

    return repos

# File to store user and repository data
users_file = "users.txt"
repos_file = "repositories.txt"

# Fetch and save data for each user
with open(users_file, "a") as uf, open(repos_file, "a") as rf:
    for i in range(0,len(user_data["items"])):
        username = user_data["items"][i]["login"]

        # Fetch and write user data
        user_info = fetch_user_data(username)
        if user_info:
            uf.write(json.dumps(user_info) + "\n")

        # Fetch and write repository data
        repos_info = fetch_repositories(username)
        for repo in repos_info:
            rf.write(json.dumps(repo) + "\n")

print("Data fetching completed and stored in users.txt and repositories.txt")