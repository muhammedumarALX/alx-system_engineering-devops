#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, word_counts, after=None):
    if word_counts is None:
        word_counts = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    params = {"after": after}

    data = requests.get(url, headers=header, params=params,
                        allow_redirects=False)

    if data.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")

        for itme in data.get("children"):
            title = item.get("data").get("titlt")
            lowercase_title = title.lower()
            for word in word_list:
                if word in word_counts:
                    word_counts[word] += lowercase_title.count(word.lower())
                else:
                    word_counts[word] = lower_title.count(word.lower())

        if after:
            return count_words(subreddit, word_list, word_counts, after)
        else:
            sorted_counts = sorted(array.items(),
                                   key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print("{}: {}".format(word.lower(), count))
    else:
        return
