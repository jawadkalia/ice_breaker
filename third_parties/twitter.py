import os
from datetime import datetime, timezone
import logging
from dotenv import load_dotenv

import tweepy


logger = logging.getLogger("twitter")
load_dotenv()
print(os.environ.get("TWITTER_API_KEY"))
api = tweepy.Client(
    bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
    consumer_key=os.environ.get("TWITTER_API_KEY"),
    consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
    access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
)



def scrape_user_tweets(username, num_tweets=5):
    """
    Scrape a Twitters user's original tweets (i.e. not retweets or replies) and returns them as a list of dictionaries.
    Each dictionay has three fields: "time_posted" (relative to now), "text" and "url".
    """
    
    # user_id = api.get_user(id=username).data.id
    user_id = api.get_me()
    tweets = api.get_users_tweets(user_id=user_id, max_results=num_tweets, exclude=['retweets', 'replies'])

    tweets_list = []
    
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["time_posted"] = datetime.now(timezone.utc) - tweet.created_at
        tweet_dict["text"] = tweet.text
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweets_list.append(tweet_dict)

    return tweets_list

if __name__ == "__main__":
    print(scrape_user_tweets("JunaidKalia"))