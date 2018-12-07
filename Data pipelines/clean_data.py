import json
import pandas as pd


def format_and_save(users, name_of_file):
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
    # Load the json
    with open("berkeley_shops.json" , 'w') as outfile:
        users = json.loads(outfile)
    # Store as csv
    format_and_save(users, 'berkeley_shops')