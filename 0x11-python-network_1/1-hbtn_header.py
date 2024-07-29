#!/usr/bin/python3
import sys
from urllib import request

def main():
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    main()

