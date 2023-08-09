#!/usr/bin/python3
"""A modeule about Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """A module that fetches the number of subscribers in a subreddit"""

    # Take the second argument as it's value
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Add a new User-Agent to allow access
    new_agent = {'User-Agent': 'MyApp'}

    # Pass the new agent(header parameter) in the get method
    response = requests.get(url, headers=new_agent)
    if response.status_code == 200:
        data = response.json()
        data = data['data']['subscribers']
        return(data)
    else:
        return 0
