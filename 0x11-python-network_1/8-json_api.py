#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import requests
import sys

def main():
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {"q" : q}
    res = requests.post(url, data=data)
    try:
        json_res = res.json()
        if json_res:
            print("[{}] {}".format(json_res["id"], json_res["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
