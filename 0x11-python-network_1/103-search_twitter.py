#!/usr/bin/python3
"""
103-search_twitter.py
"""
import requests
import sys
import base64


def authenticate(key, secret):
    """authenticates user"""
    """step 1"""
    API_key = key
    API_secret = secret
    url = 'https://api.twitter.com/oauth2/token'
    bearer_token_credentials = API_key + ':' + API_secret
    base64_bearer = base64.b64encode(bearer_token_credentials.encode('ascii'))
    """step 2"""
    bearer_decoded = base64_bearer.decode()
    header = {'Authorization': 'Basic ' + bearer_decoded,
              'Content-Type':
              'application/x-www-form-urlencoded;charset=UTF-8'}
    data = {'grant_type': 'client_credentials'}
    r = requests.post(url, headers=header, data=data)
    json = r.json()
    token = json.get("access_token")
    return (token)


if __name__ == "__main__":
    API_key = sys.argv[1]
    API_secret = sys.argv[2]
    auth_tok = authenticate(API_key, API_secret)

    url = 'https://api.twitter.com/1.1/search/tweets.json'
    header = {'Authorization': 'Bearer ' + auth_tok}
    search_string = sys.argv[3]
    search_for = '23' + search_string[1:]
    request_link = url + '?q=%' + search_for
    r = requests.get(request_link, headers=header)
    json = r.json()
    status_list = json.get("statuses")[:5]
    for i in status_list:
        print("[{}] {} by {}".format(i.get("id"),
                                     i.get("text"),
                                     i.get("user").get("name")))
