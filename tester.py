"""
filename: driver.py
description: Testing the implementation of my TwitterAPI
"""

# import libraries and packages
from twitter_api_mysql import TwitterAPI
from signature import read_tweets, get_timeline

def main(user, password, database):
    '''
    Purpose:
        Implement Twitter API (MySQL Version) where users
        simulate a constant stream of tweets and display
        timelines for each user

    Parameters:
        user (str): your username for your MySQL Database
        password (str): your password for your MySQL database
        database (str): the name of your MySQL database (has Follows and Tweet tables)

    Output:
        None, Prints the number of timelines loaded per second and
        the number of tweets stored in the database (posted) per second.
        When get_timeline parameter show_tl=True displays 1 of the timelines
    '''

    # authenticate
    api = TwitterAPI(user, password, database)

    # post tweets and record runtime
    file = "./hw1_data/tweets_sample.csv"
    read_tweets(api, file)

    # get timelines and record runtime
    get_timeline(api, 10, show_tl=True)

    # close database connection
    api.dbu.close()


if __name__ == '__main__':
    # change with your info
    select_user = "root"
    select_password = "Moonlight123!"
    select_database = "data_eng"

    # call the main function
    main(select_user, select_password, select_database)