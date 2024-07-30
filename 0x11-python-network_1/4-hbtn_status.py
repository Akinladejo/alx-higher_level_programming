#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
def main():
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(res.text)))
    print("\t - content: {}".format(res.text))

if __name__ == "__main__":
    main()
