#!/usr/bin/python3

"""a Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("sys error")
    sys.exit(1)
    
  url = sys.argv[1]
  
  try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
      res = response.info()
      x_res = res.get("X-Request-Id")
      print(x_res)
  except Exception as e:
    print("Error", e)
      
