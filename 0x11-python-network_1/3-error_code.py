#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

# Retrieve URL from command-line arguments
url = sys.argv[1]

try:
    # Make a request to the URL
    with urllib.request.urlopen(url) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        # Display the body of the response
        print(response_body)

except urllib.error.HTTPError as e:
    # If an HTTP error occurs, print the error code
    print("Error code:", e.code)
