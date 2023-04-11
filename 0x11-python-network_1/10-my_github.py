#!/usr/bin/python3
''' Takes GitHub credentials using the github API to display id'''

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    au = (username, password)
    r = requests.get('https://api.github.com/user', auth=au)
    print(r.json().get('id'))
