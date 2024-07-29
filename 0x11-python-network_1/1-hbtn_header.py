#!/usr/bin/python3
import sys
from urllib import request

def main():
    url = sys.argv[1]  # Get the URL from the command-line arguments

    # Send a request to the URL and get the response
    with request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.headers

        # Get the value of the X-Request-Id header
        x_request_id = headers.get('X-Request-Id')

        # Print the value of the X-Request-Id header
        print(x_request_id)

if __name__ == "__main__":
    main()

