#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL """
import sys
from urllib import parse, request, error
def main():
    url = sys.argv[1]
    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
