#!/usr/bin/python3
"""Implement the function"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API to get the titles of the first 10 hot posts
    for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        children = response.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    else:
        print('None')
