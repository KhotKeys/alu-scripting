#!usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # URL for Reddit API endpoint to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

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
            return 0

        # Extract number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        print("Failed to retrieve data from Reddit API")
        return 0

# Example usage
subscribers = number_of_subscribers("python")
print(f"The number of subscribers in r/python is: {subscribers}")
