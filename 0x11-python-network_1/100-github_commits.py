#!/usr/bin/python3
''' takes two arguments and prints the user's last ten commits '''

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
