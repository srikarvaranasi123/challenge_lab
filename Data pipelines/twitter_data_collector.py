## This file is for collecting data and storing into database

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, Stream
import pandas as pd
import csv
from dateutil import parser

# Authentication

consumer_key = '5sRbHeNBaJG9pwsOwN5yLJmqt'
consumer_secret = 'uQMQIWWojWX4ujpcQXYntf4COYWkQSO7FR3ctnIaEOee3l2TcK'
access_token = '3595597154-O7Yn4Tx3j6wffXe3STrbVPDb6VS5qRQq0VAQQiV'
access_secret = 'hZkgDwEzLMqAf0lfgxxmwQN1bzeWlrnqO5nL0kqWBTBa8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# Streaming the twitter data

class MyListener(StreamListener):
    """
    Class to help in steaming of tweets
    """
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True




def get_all_tweets(screen_name, auth):

    # authorize twitter
    api = tweepy.API(auth)

    total_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    total_tweets.extend(new_tweets)

    # Saving the id of the oldest tweet
    oldest = total_tweets[-1].id - 1

    # Get all tweets
    while len(new_tweets) > 0:

        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # Add the tweets
        total_tweets.extend(new_tweets)
        oldest = total_tweets[-1].id - 1

    # Converting to correct format t
    outtweets = [[tweet.id_str, tweet.created_at.date(),tweet.created_at.time() ,tweet.text.encode("utf-8"), tweet.retweet_count,
                  tweet.favorite_count, tweet.favorited, tweet.retweeted] for tweet in total_tweets]


    # Write to csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "date", "time", "text", 'retweet_count', 'favorite_count','favorited','retweeted'])
        writer.writerows(outtweets)



    return


if __name__ == '__main__':

    # Getting the data of berkeley users
    berkeley_users= ['ninaeyu',
    'DylanFroscot',
    'Mc11wain',
    'chanel Shum',
    'healyeatsreal',
    'wheredeyatzo']

    berkeley_shops = ['huckbikes', 'angelinasmn', 'GatherBerkeley']

    for name in berkeley_users:
        get_all_tweets(name, auth)

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['#berkeley'])
