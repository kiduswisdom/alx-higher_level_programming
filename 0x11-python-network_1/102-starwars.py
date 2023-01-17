#!/usr/bin/python3
"""
101-starwars.py
"""
import requests
import sys


def get_movies(name):
    """prints movies for a given name"""
    films = name.get("films")
    for film in films:
        r = requests.get(film)
        json = r.json()
        print("\t{}".format(json.get("title")))


def print_all(json):
    """prints names and movies"""
    for i in json.get("results"):
        print(i.get("name"))
        get_movies(i)


def pagination(json, value):
    """goes through pages"""
    next_page = json.get("next")
    while next_page:
        r = requests.get(next_page, params=value)
        json = r.json()
        print_all(json)
        next_page = json.get("next")


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    value = {'search': sys.argv[1]}
    r = requests.get(url, params=value)
    json = r.json()
    print('Number of results: {}'.format(json.get("count")))
    print_all(json)
    pagination(json, value)
