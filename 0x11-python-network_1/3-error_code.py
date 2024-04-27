#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
