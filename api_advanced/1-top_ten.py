#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
 returns the number of subscribers for a given subreddit.
 """
 import requests

def top_ten(subreddit):
    # URL for Reddit API endpoint to get hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set custom User-Agent header to avoid "403 Forbidden" error
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # Make GET request to Reddit API
    response = requests.get(url, headers=headers)

    # Check if response is successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Check if subreddit exists
        if 'error' in data:
            print("None")
            return

        # Extract titles of the first 10 hot posts
        posts = data['data']['children']
        print(f"Top 10 hot posts in r/{subreddit}:\n")
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("Failed to retrieve data from Reddit API")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
