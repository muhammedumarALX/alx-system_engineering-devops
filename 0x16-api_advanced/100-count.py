#!/usr/bin/python3
"""
Count occurrences of given keywords in titles of
eot articles from a subreddit.
Args:
    subreddit (str): The name of the subreddit to query.
    word_list (list): A list of keywords to count
    occurrences of.
    word_counts (dict, optional): A dictionary to
    store keyword counts. Default is None.
    after (str, optional): A Reddit API parameter
    for pagination. Default is None.

Returns:
    None
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    params = {"after": after}

    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")

        for item in data.get("children"):
            title = item.get("data").get("title")
            lowercase_title = title.lower()
            for word in word_list:
                if word in word_counts:
                    word_counts[word] += lowercase_title.count(word.lower())
                else:
                    word_counts[word] = lowercase_title.count(word.lower())

        if after:
            return count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_counts = sorted(word_counts.items(),
                                   key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print("{}: {}".format(word.lower(), count))
    else:
        return
