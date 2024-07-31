#!/usr/bin/python3
"""Python script that takes in a URL"""

import requests
import sys

def main():
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
        
if __name__ == '__main__':
    main()
