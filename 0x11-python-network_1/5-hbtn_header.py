#!/usr//bin/python3
"""a script that takes in a URL, sends a request to the URL"""

import requests
import sys
def main():
    if len(sys.argv) != 2:
        print("Value Error")
        sys.exit(1)
    try:
        url = sys.argv[1]
        res = requests.get(url)
        headers = res.headers
        print(headers.get('X-Request-Id'))
    except Exception as e:
        print("Exception: {}".format(e.code))

if __name__ == "__main__":
    main()
