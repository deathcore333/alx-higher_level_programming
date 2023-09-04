#!/usr/bin/python3
"""
    Takes your GitHub credentials (username and password)
    Uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    au = (user, pwd)
    r = requests.get('https://api.github.com/user', auth=au)
    print(r.json().get('id'))
