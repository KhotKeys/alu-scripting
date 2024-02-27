#!/usr/bin/python3
"""Function that queries the Reddit API and \
    returns the number of subscribbers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    else:
        return response.json().get("data").get("subscribers")
