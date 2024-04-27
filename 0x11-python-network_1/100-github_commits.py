#!/usr/bin/python3
import requests
import sys


def get_commits(repo_name, owner_name):
    # GitHub API endpoint for listing commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the list of commits from the response JSON
        commits = response.json()

        # Iterate over the first 10 commits
        for commit in commits[:10]:
            sha = commit['sha'][:7]  # Extract first 7 characters of the SHA
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits")


if __name__ == "__main__":
    # Extract repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Call the function to get and print the commits
    get_commits(repo_name, owner_name)
