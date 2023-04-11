#!/usr/bin/python3
''' script that takes URL, Sends request and displays value of request id '''

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
