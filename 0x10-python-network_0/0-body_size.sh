#!/bin/bash
# Sends a GET request to the URL specified and prints the size of the response body to stdout
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
