#!/usr/bin/python3
"""
    Takes in a URL
    Sends a request to the URL
    Displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
