#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Data needs to be bytes

with urllib.request.urlopen(url, data) as response:
    response_body = response.read().decode('utf-8')
    print(response_body)
