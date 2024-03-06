#!/usr/bin/python3
"""
Implement the function
"""

from collections import Counter
import requests
import re


def count_words(subreddit, word_list, after=None, counter=None):
    """
    Recursively queries the Reddit API to get the titles of all
    hot posts for a given subreddit, counts occurrences of given keywords
    in titles, and prints the sorted count.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count
        after (str): The ID of the last post from the previous request.
        counter (Counter): A counter object to keep track
        of keyword occurencec.

    Returns:
        None
    """
    if counter is None:
        counter = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'Chrome/91.0.4472.124'}
    response = requests.get(url, headers=headers,
               allow_redirects=False)

    if response.status_code == 404:
        return
    elif response.status_code != 200:
        print("Error: Received status code", response.status_code)
        return

    data = response.json()
    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                # Count occurrences of the word in the title
                count = sum(1 for _ in 
                            re.finditer(r'\b' + re.escape(word) + r'\b', title))
                counter[word] += count

        # Check if there are more pages to fetch
        if 'after' in data['data']:
            count_words(subreddit, word_list, data['data']['after'], counter)
        else:
            # Print results in descending order by count, then alphabetically
            for word, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
                if count > 0:
                    print(f"{word}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>"
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
