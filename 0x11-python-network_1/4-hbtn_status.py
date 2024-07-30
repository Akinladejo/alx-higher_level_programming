#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


def get_alx_intranet(url='https://alx-intranet.hbtn.io/status'):
    """
    Send a GET request to the url
    and print the response
    """
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == "__main__":
    get_alx_intranet()
