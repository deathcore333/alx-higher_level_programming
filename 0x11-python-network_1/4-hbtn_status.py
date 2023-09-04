#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
    using package 'requests'

    Body response:$
    - type: <class 'str'>$
    - content: OK$
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(r.text), r.text))
