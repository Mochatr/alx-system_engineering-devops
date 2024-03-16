#!/usr/bin/python3
""" Implement the function """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get the titles of all
    hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): A list to store the titles of the hot posts
        after (str): The ID of the last post from the previous request

    Returns:
        list: A list of titles of all hot posts for the subreddit.
        Returns None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 100, 'after':after}
    headers = {'User-Agent': 'custom user-agent'}

    response = requests.get(url,
                            parameters=parameters,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get('data').get('data', {})
    for post in data.get('children', []):
        hot_list.append(post.get('data').get('title'))

    if data.get('after'):
        return recurse(subreddit, hot_list, data.get('after'))
    else:
        return hot_list
