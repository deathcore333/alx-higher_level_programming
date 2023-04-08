#!/usr/bin/python3
''' script that takes in URL and email and sends a Post
    request to the passed URL with email as par
'''

from sys import argv
import urllib.request
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
