#!/usr/bin/python3
"""script to fetch data fro url"""

from urllib.request import Request,urlopen
from urllib.error import HTTPError, URLError
if __name__ == "__main__":
    url = Request("https://alx-intranet.hbtn.io/status")
    try:
        with urlopen(url) as response:
            res = response.read()
            print("Body response:")
            print("\t - type: {}",format(type(res)))
            print("\t - content: {}".format(res))
            print("\t utf8 content: {}".format(res.decode('utf-8')))
    except HTTPError as er:
        print("HTTPError", er)

