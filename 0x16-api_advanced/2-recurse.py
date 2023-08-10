#!/usr/bin/python3
"""Returns a list of all topics for all hot articles
    for a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    params = {}
    if after:
        params["after"] = after

    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for item in children:
                    title = item.get("data").get("title")
                    hot_list.append(title)
                after = data.get("after")
                if after:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None
