#!/usr/bin/python3
"""Returns a list of all topics for all hot articles
    for a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    data = requests.get(url, headers=header, params=params,
                        allow_redirects=False)

    if data.status_code == 200:
        response = data.json().get("data")
        after = response.get("after")

        for item in response.get("children"):
            hot_list.append(item.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    return None
