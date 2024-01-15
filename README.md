# Custom API to GitHub Issue Automation

## Features

- Fetches a blueprint from a Custom Swagger API endpoint.
- Extracts all GitLab repositories information from the blueprint.
- Creates GitHub issues for the first GitLab repository.

## Prerequisites

- Python 3.x
- requests library (pip install requests)
- A GitHub personal access token with repo scope (A temporary one has been included in the code)

## Usage

- Clone or download this repository.
- Install the required library: pip install requests
- Although the best approach would be to create a .env file in the root directory and add the GITHUB_TOKEN, for ease, this can be omitted as a temporary fine-scoped Personal Access Token has been included in the code.
- Run the script: **python api.py**

## Variables

You can modify the following variables in the api.py file:

- blueprint_id: The ID of the blueprint to fetch from GitLab (line 90).
- repo_owner: The owner of the GitHub repository where issues will be created (line 86).
- repo_name: The name of the GitHub repository where issues will be created (line 86).

## Additional Notes

- I would implement environment variables or a configuration file to store sensitive information like API tokens.
- Currently, logging is done in-place, without any integration for better debugging and monitoring.
- Write unit tests to ensure code quality and functionality.
- Enhance the script to allow for more flexible configuration options.
