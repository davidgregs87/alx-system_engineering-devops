#!/usr/bin/python3
"""A module about Reddit API"""

import requests


def top_ten(subreddit):
    """A function that prints out the 10 hot post from Reddit
    API with any valid subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set new user agent
    new_agent = {'User-Agent': 'MyApp1'}
    count = 0
    req_output = 10
    res = requests.get(url, headers=new_agent)
    if res.status_code == 200:
        data = res.json()
        datas = data['data']['children']
        for data in datas:
            print(data['data']['title'])
            count += 1
            if count == req_output:
                break
    else:
        print(None)
