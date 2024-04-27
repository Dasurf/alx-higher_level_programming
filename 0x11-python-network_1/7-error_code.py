#!/usr/bin/python3
import requests
import sys

# Retrieve URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the HTTP status code is greater than or equal to 400
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    # Display the body of the response
    print(response.text)
