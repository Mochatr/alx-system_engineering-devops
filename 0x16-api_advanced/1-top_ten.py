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
        data = response.json()
        if 'data' in data and 'children' data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    # Example of a subreddit
    subreddit = "Gaming"
    top_ten(subreddit)
