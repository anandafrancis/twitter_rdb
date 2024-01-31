"""
filename: signature.py
description: Creating an interface between the driver code and the Twitter API
                Flexible for Redis and SQL
"""

# import libraries and packages
import csv
from twitter_objects import Tweet
from datetime import datetime

def read_tweets(api, csvfile):
    '''
    Purpose:
        Read tweets line by line to simulate a constant stream of tweets

    Parameters:
        api (object): instance of TwitterAPI object
        csvfile (str): name of the csv file storing your tweets

    Output:
        None, the number of tweets stored in the database (posted) per second
    '''


    with open(csvfile) as file:

        # initialize timer and tweet count
        start = datetime.now()
        tweet_count = 0

        # iterate over each row in the file (except header) and add the tweet
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:

            # extract Tweet attributes
            user_id = row[0]
            tweet_text = row[1]
            tweet_ts = datetime.now()
            tweet_id = None

            # create Tweet object
            tweet = Tweet(tweet_id, user_id, tweet_ts, tweet_text)

            # post Tweet (store as record in the database)
            api.postTweet(tweet)
            tweet_count += 1

        # calculate how many tweets were posted per second
        end = datetime.now()
        runtime = end - start
        tweets_posted_per_sec = tweet_count / runtime.total_seconds()

        # display results
        print(f"Tweets Posted Per Second: {tweets_posted_per_sec}")




def get_timeline(api, count, show_tl=False):
    '''
    Purpose:
        Repeatedly pick a random user and return that user's home timeline

    Parameters:
        api (object): instance of TwitterAPI object
        count (int): the number of random timelines you want to load
        show_tl (bool): if you want to show an example timeline or not

    Output:
        None, Prints the number of timelines loaded per second and
        when get_timeline parameter show_tl=True displays 1 of the timelines
    '''

    # initialize
    timeline_count = 0
    start = datetime.now()
    for i in range(count):

        # get random timeline
        timeline = api.getTimeline()
        timeline_count += 1

    # calculate how many timelines were loaded per second
    end = datetime.now()
    runtime = end - start
    timelines_per_sec = timeline_count / runtime.total_seconds()
    print(f"Timelines Per Second: {timelines_per_sec}")

    # show an example timeline
    if show_tl:
        print(f"Twitter Timeline")
        for tweet in timeline:
            print(tweet)













