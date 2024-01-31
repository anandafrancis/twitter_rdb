"""
filename: twitter_api_mysql.py

description: An API that allows users to simulate posting tweets
            and viewing timelines using relational databases (MySQL)
            to resemble the app Twitter
"""

from dbutils import DBUtils
from twitter_objects import Tweet
from datetime import datetime

class TwitterAPI:

    def __init__(self, user, password, database, host="localhost"):
        '''
        Purpose:
            Initialize TwitterAPI object instance

        Parameters:
            user (str): your username for your MySQL Database
            password (str): your password for your MySQL database
            database (str): the name of your MySQL database (has Follows and Tweet tables)
            host (str): the port name where your database is locally ran

        Output:
            None
        '''

        # initialize database connection
        self.dbu = DBUtils(user, password, database, host)

    def createTweet(self, record):
        '''
        Purpose:
            Create a Tweet object using a row of a csv file

        Parameters:
            record (object): row of a csv file

        Output:
            Tweet object of the converted csv file
        '''

        # extract Tweet attributes
        self.user_id = record[0]
        self.tweet_text = record[1]
        self.tweet_ts = datetime.now()
        self.tweet_id = None

        # create Tweet object
        tweet = Tweet(self.tweet_id, self.user_id, self.tweet_ts, self.tweet_text)
        return tweet

    def postTweet(self, tweet):
        '''
        Purpose:
            Stores new tweet as an instance in the database

        Parameters:
            tweet (object): instance of Tweet object

        Output:
            None, inserts Tweet object as a row in the Tweet SQL table
        '''

        # create SQL script
        sql = 'INSERT INTO TWEET2 (tweet_id, user_id, tweet_ts, tweet_text) VALUES (%s, %s, %s, %s)'
        val = (tweet.tweet_id, tweet.user_id, tweet.tweet_ts, tweet.tweet_text)

        # insert Tweet object as a record in TWEET Table
        self.dbu.insert_one(sql, val)

    def getTimeline(self):
        '''
        Purpose:
            Randomly select a user and display their timeline
            of the 10 most recent tweets of the users they follow

        Parameters:
            None

        Output:
            list of Tweet objects, representing the random user's timeline
        '''

        # select a random user --> get a list of who they follow --> find the 10 most recent tweets
        sql = f"SELECT * FROM TWEET " \
              f"WHERE user_id IN (SELECT follows_id FROM FOLLOWS " \
              f"WHERE user_id = (SELECT user_id FROM TWEET " \
              f"ORDER BY RAND() LIMIT 1)) " \
              f"ORDER BY tweet_ts DESC " \
              f"LIMIT 10;"

        # citation for select random user_id: https://www.javatpoint.com/sql-select-random

        # convert pandas dataframe to list of Tweet objects
        recent_tweets = self.dbu.execute(sql)
        timeline = [Tweet(row['tweet_id'], row['user_id'], row['tweet_ts'],
                          row['tweet_text']) for index, row in recent_tweets.iterrows()]


        return timeline


