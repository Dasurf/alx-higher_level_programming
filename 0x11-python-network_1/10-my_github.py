#!/usr/bin/python3
import requests
import sys

# GitHub username and password (personal access token)
username = sys.argv[1]
password = sys.argv[2]

# Define the GitHub API endpoint
url = 'https://api.github.com/dasurf'

# Set up Basic Authentication with the provided credentials
auth = (username, password)

# Send a GET request to the GitHub API
response = requests.get(url, auth=auth)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON and display the user id
    user_data = response.json()
    print(user_data['id'])
else:
    # If the request was not successful, print None
    print(None)
