from prophets import Abraham
import sys, logging
from pprint import pprint
from datetime import datetime, timedelta

if __name__ == "__main__":
    print(f"Abraham Version: {open('version').read().strip()}")

    args = [sys.argv[1:]] if sys.argv[1:] else ["tesla"]  # default args

    # """
    darthvader = Abraham(
        news_source="newsapi",
        newsapi_key=open("keys/newsapi-public").read().strip(),
        # bearer_token=open("keys/twitter-bearer-token").read().strip(),
    )  # splitting means that it recursively splits a large text into sentences and analyzes each individually

    scores = darthvader.twitter_summary(
        *args,  # size=200
    )  # latest date to get news from
    print("\nTwitter\n--")
    pprint(scores)

    scores = darthvader.news_summary(*args)  # latest date to get news from
    print("News\n--")
    pprint(scores)