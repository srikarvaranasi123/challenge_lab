from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import pandas as pd
import pickle
from dateutil import parser
import datetime


def get_hour(time):
    hour = parser.parse(time).hour #strptime("%H")
    return hour


if __name__ == '__main__':

    # Read the data
    tweets_data = pd.read_csv("../Data/twitter_data.csv")
    # Processing the data to get features
    tweets_data['hour'] = tweets_data['time'].apply(get_hour)

    # Columns to select
    tweets_data_sub = tweets_data.loc[:, 'text']


    train_X, test_X, train_Y, test_Y = train_test_split(tweets_data_sub.values,tweets_data['favorited'].values, random_state = 42, test_size = 0.30)


    # Create a count vectorizer
    vectorizer = CountVectorizer(
        analyzer='word',
        lowercase=True,
        stop_words = 'english'
    )

    # Train the model
    features = vectorizer.fit_transform(train_X)
    features_nd = features.toarray()

    model = SVR(kernel='rbf')
    model.fit(features_nd, train_Y)

    # Test with test data
    # features_test = vectorizer.transform(test_X)
    # features_test_nd = features_test.toarray()
    #
    # predictions = model.predict(features_test_nd)
    # print(accuracy_score(test_Y, predictions))

    #adsf
    text = "this is bad"
    features_test = vectorizer.transform([text])
    features_test_nd = features_test.toarray()
    predictions = model.predict(features_test_nd)
    print(predictions)

    # Save the model
    pickle.dump(model, open("twitter_model.pkl", 'wb'))
    pickle.dump(vectorizer, open("vectorizer.pkl", 'wb'))




# Read the data

# Make test train set

# Get accuracy

# Save the model