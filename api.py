import requests

def fetch_blueprint(blueprint_id):
    """Fetches a blueprint from the API given its ID.

    Args:
        blueprint_id: The ID of the blueprint to fetch.

    Returns:
        The JSON response from the API, or None if an error occurred.
    """

    base_url = "http://54.236.25.78:4000/api"
    url_path = f"/blueprints/{blueprint_id}"

    try:
        response = requests.get(base_url + url_path)
        response.raise_for_status()  # Raise an exception for error status codes
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching blueprint: {err}")
        return None
    
def create_issue(repo_owner, repo_name, title, repo_id):
    """Creates an issue on Github Repor provided in params.

    Args:
        repo_owner: The name of account where Repo exists.
        repo_name: The name of repo itself.
        title: The title of repo to be created.
        repo_id: The repo_id that will be appended to the body / description of the issue.

    Returns:
        The JSON response from the API, or None if an error occurred.
    """

    base_url = " https://api.github.com/repos"
    url_path = f"/{repo_owner}/{repo_name}/issues"
    github_token = "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"

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    payload = {
        "title": title,
        "body": f"The repoID of the GitLab Repo is {repo_id}"
    }

    try:
        response = requests.post(base_url + url_path, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for error status codes
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error creating an issue: {err}")
        return None
    
def process_blueprint(blueprint_data):
    """Processes the blueprint data to extract GitLab repos and create GitHub issues.

    Args:
        blueprint_data: The JSON data of the fetched blueprint.
    """

    all_gitlab_repos = []

    for plan in blueprint_data["plan"]:
        for plugin in plan:
            if plugin["plugin"] == "gitextractor":
                all_gitlab_repos.append(plugin["options"])

    print("---------------------------------------")
    print(f"Total Gitlab Repos Found: {len(all_gitlab_repos)}")

    for repo in all_gitlab_repos:
        print("---------------------------------------")
        print(f"Repo ID: {repo['repoId']}")
        print(f"Name: {repo['name']}")

    if all_gitlab_repos:
        print("---------------------------------------")
        print("Selecting First Repo and creating an issue.")
        print("---------------------------------------")
        create_issue("SaadRafiq4", "Lab-API-Test", all_gitlab_repos[0]["name"], all_gitlab_repos[0]["repoId"])
        print("Github Issue created successfully. Please visit https://github.com/SaadRafiq4/Lab-API-Test/issues.")

if __name__ == "__main__":
    blueprint_id = 3
    blueprint_data = fetch_blueprint(blueprint_id)

    if blueprint_data:
        process_blueprint(blueprint_data)