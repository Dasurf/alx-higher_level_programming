#!/bin/bash
# takes in a URL, sends a request to the URL, displays size of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
