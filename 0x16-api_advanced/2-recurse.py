#!/usr/bin/python3
"""
Implement the function
"""
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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'custom user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            # Check if there are more pages to fetch
            if 'after' in data['data']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
    return None


if __name__ == "__main__":
    # Example of a subreddit
    subreddit = "Technology"
    hot_posts = recurse(subreddit)
    if hot_posts:
        for title in hot_posts:
            print(title)
    else:
        print("Failed to fetch posts or subreddit is invalid.")
