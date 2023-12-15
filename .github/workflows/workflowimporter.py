import requests
import os

def get_repos(token, org):
    url = f"https://api.github.com/orgs/{org}/repos"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

def check_workflow_exists(repo, token):
    url = repo["contents_url"].replace("{+path}", ".github/workflows/autoassign.yml")
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def add_workflow(repo, token, workflow_content):
    url = repo["contents_url"].replace("{+path}", ".github/workflows/autoassign.yml")
    headers = {"Authorization": f"token {token}", "Content-Type": "application/json"}
    data = {
        "message": "Add auto-assign workflow",
        "content": workflow_content  # Base64 encoded content of the workflow file
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 201

def main():
    token = os.getenv("GITHUB_TOKEN")
    org = os.getenv("GITHUB_ORG")
    workflow_content = ""  # TODO: Add your Base64 encoded workflow file content here

    repos = get_repos(token, org)
    for repo in repos:
        if not check_workflow_exists(repo, token):
            add_workflow(repo, token, workflow_content)

if __name__ == "__main__":
    main()
