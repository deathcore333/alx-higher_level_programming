#!/usr/bin/python3
''' Takes in URL sends request and displays response body '''

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
