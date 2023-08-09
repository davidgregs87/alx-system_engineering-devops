#!/usr/bin/python3
""" This script has  recursive function that queries the
    Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function should
    return None.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User-Agent'}

    if hot_list is None:
        hot_list = []

    # Construct the URL for the subreddit's hot posts API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the list of posts
        posts = data['data']['children']

        # Add titles to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there's more data to fetch
        after = data['data']['after']
        if after:
            # Recurse with the new 'after' parameter
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # If the response is not successful, return None
        return None
