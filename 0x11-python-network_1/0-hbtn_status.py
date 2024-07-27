#!/usr/bin/python3
from urllib import request, error
url = "https://alx-intranet.hbtn.io/status"
try:
    with request.urlopen(url) as response:
        res = response.read()
        print(res)
except error.HTTPError as err:
    print("httpError", err)

