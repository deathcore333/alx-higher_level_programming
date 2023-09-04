#!/usr/bin/python3
"""
    Takes 2 arguments:
        repository name
        owner name

"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    if r.status_code == 200:
        for i in r.json()[:10]:
            print("{}: {}".format(
                                  i.get("sha"),
                                  i.get("commit").get("author").get("name")))
    else:
        print("Error code: {}".format(r.status_code))
