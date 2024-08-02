#!/usr/bin/python3
"""list all previous 10 commits"""

import sys
import requests

def main():
  url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
  response = requests.get(url)
  commit = res.json()
  try:
    for i in range(10):
      print("{}, {}".format(commit[i].get("sha"),
                            commit[i].get("commit").get("author").get("name")))
  except IndexError:
    pass

if __name__ == "__main__:
main()
