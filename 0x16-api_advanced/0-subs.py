#!/usr/bin/python3
"""
Implement the function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers
    for a given subreddit

    Args:
        subreddit(str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        Return 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Chrome/91.0.4472.124'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
