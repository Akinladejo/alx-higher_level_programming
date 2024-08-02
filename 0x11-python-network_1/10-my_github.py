#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)"""
import sys
import requests

def main():
    username = sys.argv[1]
    password  = sys.argv[2]
    url = "https://api.github.com/user"

    res = requests.get(url, auth=(username, password))
    try:
        res_json = res.json()
        id_num = res_json.get('id')
        print(id_num)
    except ValueError:
        print("None")
