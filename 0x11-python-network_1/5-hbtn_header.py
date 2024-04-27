#!/usr/bin/python3
import requests
import sys

# Retrieve URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Retrieve the value of the X-Request-Id header from the response
x_request_id = response.headers.get('X-Request-Id')

# Display the value of the X-Request-Id header
print(x_request_id)
