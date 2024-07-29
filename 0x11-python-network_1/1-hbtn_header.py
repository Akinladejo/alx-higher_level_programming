#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            # Retrieve and print the value of the X-Request-Id header
            response_headers = response.info()
            x_request_id = response_headers.get('X-Request-Id')
            print(x_request_id)
    except Exception as e:
        print("Error:", e)
