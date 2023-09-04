#!/usr/bin/python3
""""
    Takes in a URL and an email address
    Sends a POST request to the passed URL with the email as a parameter
    Displays the body of the response.
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
