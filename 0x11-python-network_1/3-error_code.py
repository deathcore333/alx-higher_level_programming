#!/usr/bin/python3
''' takes URL sends request to URL and displays the response '''

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


