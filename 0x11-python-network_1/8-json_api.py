#!/usr/bin/python3
import requests
import sys

# Define the URL
url = 'http://0.0.0.0:5000/dasurf'

# Define the letter parameter
if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

# Send a POST request with the letter parameter
response = requests.post(url, data={'q': q})

# Check if the response body is properly JSON formatted and not empty
try:
    data = response.json()
    if data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
