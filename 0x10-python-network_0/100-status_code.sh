#!/bin/bash
# sends request to URL passed as argument and display only status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
