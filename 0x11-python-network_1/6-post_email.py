#!/usr/bin/python3
import requests
import sys

# Retrieve URL and email address from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Send a POST request to the specified URL with the email as a parameter
response = requests.post(url, data={'email': email})

# Display the body of the response
print(response.text)
