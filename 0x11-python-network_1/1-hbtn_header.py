#!/usr/bin/python3
''' takes the url sends a request to the URL
and displays value of the X-request-Id

Usage: ./1-hbtn_header.py <URL>
'''
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
