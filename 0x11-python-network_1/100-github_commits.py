#!/usr/bin/python3
"""
100-github_commits.py
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/'
    repo = sys.argv[1]
    owner = sys.argv[2]
    link = url + owner + '/' + repo + '/commits'
    r = requests.get(link)
    json = r.json()
    json = json[:10]
    for i in json:
        print('{}: {}'.format(i.get("sha"), i.get("commit")
                              .get("author").get("name")))
