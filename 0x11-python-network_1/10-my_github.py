#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    try:
        json_obj = response.json()
        id_num = json_obj.get('id')
        print(id_num)
    except ValueError:
        print("None")
