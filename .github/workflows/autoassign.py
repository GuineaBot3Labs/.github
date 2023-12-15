import requests
import random
import os

def get_org_members(org_name, token):
    url = f"https://api.github.com/orgs/{org_name}/members"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [member['login'] for member in response.json()]
    else:
        print(f"Failed to fetch organization members: {response.status_code}, {response.text}")
        return []

def assign_issue(issue_number, assignee, repo_name, token):
    url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}/assignees"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {'assignees': [assignee]}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code not in [200, 201]:
        print(f"Failed to assign issue: {response.status_code}, {response.text}")

def main():
    token = os.getenv('GITHUB_TOKEN')
    org_name = os.getenv('ORG_NAME')
    repo_name = os.getenv('REPO_NAME')
    issue_number = os.getenv('ISSUE_NUMBER')

    members = get_org_members(org_name, token)
    if not members:
        print("No members found in the organization.")
        return

    assignee = random.choice(members)
    assign_issue(issue_number, assignee, repo_name, token)
    print(f"Issue {issue_number} has been assigned to {assignee}")

if __name__ == "__main__":
    main()
