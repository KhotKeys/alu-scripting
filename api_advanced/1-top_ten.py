#!/usr/bin/python3
"""This function retrieves the top ten posts of a given subreddit"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    feedback = requests.get(url, headers=headers)

    if feedback.status_code != 200:
        print(None)
    else:
        data = feedback.json().get("data").get("children")
        for post in data:
            print(post.get("data").get("title"))
