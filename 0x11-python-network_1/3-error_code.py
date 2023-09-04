#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
    manage urllib.error.HTTPError
        exceptions and print:
            Error code: followed by the HTTP status code
"""

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
