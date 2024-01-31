"""
filename: twitter_objects.py
description: Define a Tweet object to use for TwitterAPI
"""

class Tweet:

    def __init__(self, tweet_id, user_id, tweet_ts, tweet_text):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.tweet_ts = tweet_ts
        self.tweet_text = tweet_text

    def __str__(self):
        '''
        Purpose:
            Create a string representation of each tweet to display in getTimeline

        Parameters:
            None

        Output:
            Simulates a string representation of a tweet that mimics Twitter's UI
        '''

        return f"@user_{self.user_id} tweets at {self.tweet_ts}: {self.tweet_text}"


