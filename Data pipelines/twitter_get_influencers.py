import tweepy
from tweepy import OAuthHandler
import pandas as pd
from dateutil import parser
import json

# Authentication

consumer_key = '5sRbHeNBaJG9pwsOwN5yLJmqt'
consumer_secret = 'uQMQIWWojWX4ujpcQXYntf4COYWkQSO7FR3ctnIaEOee3l2TcK'
access_token = '3595597154-O7Yn4Tx3j6wffXe3STrbVPDb6VS5qRQq0VAQQiV'
access_secret = 'hZkgDwEzLMqAf0lfgxxmwQN1bzeWlrnqO5nL0kqWBTBa8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
def get_users(q, pages = 20):
    """
    Get the shops or influencers with the search k
    :param q: Search query
    :param pages: Number of pages to look for
    :return: Dictionary with user details
    """
    total_users = []
    for page in range(pages):
        users = api.search_users(q, 20, page)
        total_users = total_users + [x._json for x in users]

    return total_users

def create_csv(users, name_of_file):
    """
    Formatting the data
    :param users: users dictionary
    :param name_of_file: Name of the file
    :return: Saves the data
    """
    with open(name_of_file + '.json', 'w') as outfile:
        json.dump(users, outfile)
    id_str = []
    name = []
    screen_name = []
    description = []
    followers_count = []
    friends_count = []
    favourites_count = []
    verified = []
    location = []
    url = []
    created_at = []
    statuses_count = []

    for user in users:

        id_str.append(user['id_str'] or "")
        name.append(user['name'] or "")
        screen_name.append(user['screen_name'] or "")
        description.append(user['description'] or "")
        followers_count.append(user['followers_count'] or "")
        friends_count.append(user['friends_count'] or "")
        favourites_count.append(user['favourites_count'] or "")
        verified.append(user['verified'] or "")
        location.append(user['location'] or "")
        url.append(user['url'] or None)
        created_at.append(user['created_at'] or "")
        statuses_count.append(user['statuses_count'] or "")


    df = pd.DataFrame({ 'id_str' : id_str,
    'name' : name,
    'screen_name' : screen_name,
    'description' : description,
    'followers_count' :  followers_count,
    'friends_count' : friends_count,
    'favourites_count' : favourites_count,
    'verified' : verified,
    'location' : location,
    'url' : url,
    'created_at' : created_at,
   'statuses_count' : statuses_count
    })

    df.to_csv(name_of_file + '.csv')

if __name__ == '__main__':
    users_t = get_users('foodie berkeley', 20)
    create_csv(users_t, 'berkeley_food')


