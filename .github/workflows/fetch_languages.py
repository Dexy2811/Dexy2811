import requests
import os

def fetch_languages():
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    repos = response.json()

    languages = set()
    for repo in repos:
        lang_response = requests.get(repo['languages_url'], headers=headers)
        repo_languages = lang_response.json()
        languages.update(repo_languages.keys())
    
    with open('languages.txt', 'w') as f:
        for lang in languages:
            f.write(f"{lang}\n")

if __name__ == "__main__":
    fetch_languages()
