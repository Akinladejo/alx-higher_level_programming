#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import sys
from urllib import request

if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print("USAGE <URL>")
        sys.exit(1)
    
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            res = response.headers
            x_res = res.get('X-Request-Id')
            print(x_res)

    except Exception as e:
        print("error", e)
