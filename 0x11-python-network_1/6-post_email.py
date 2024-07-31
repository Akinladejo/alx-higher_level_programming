#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import sys
import requests

def main():
    try:
        url = sys.argv[1]
        email = sys.argv[2]

        req = requests.post(url, data={"email" : email})
        print(req.text)
    except Exception as e:
        print("Error code : {}".format(e.code))

if __name__ == "__main__":
    main()
