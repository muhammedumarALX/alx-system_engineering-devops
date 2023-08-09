#!/usr/bin/python3
"""Queries the `REDDIT API` and
    returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that returns number of suscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']["subscribers"]
        return subscribers
    return 0
