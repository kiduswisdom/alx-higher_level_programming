#!/usr/bin/python3
"""
10-my_github.py
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(user_name, passwd))
    json = r.json()
    print('{}'.format(json.get("id")))
