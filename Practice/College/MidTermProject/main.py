from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import requests

import tweepy
import pandas as pd

consumer_key = "****" #Your API/Consumer key
consumer_secret = "***" #Your API/Consumer Secret Key
access_token = "*****"    #Your Access token key
access_token_secret = "*****" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')

    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))



# Define your Twitter API endpoint URL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# Set your Twitter API parameters (such as screen_name, count, etc.)
params = {
    "screen_name": "twitter_username",
    "count": 10  # Number of tweets to retrieve
}

# Set your Twitter API credentials
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Replace with your Twitter API access token
}

try:
    # Make the GET request to the Twitter API
    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Process and print the response data
        for tweet in data:
            print(tweet['text'])
    else:
        print("Error: Unable to fetch data from the Twitter API.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Load your preprocessed data and labels
# X = # Your preprocessed text data
# y = # Your sentiment labels

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Vectorize the text data using TF-IDF
# vectorizer = TfidfVectorizer()
# X_train = vectorizer.fit_transform(X_train)
# X_test = vectorizer.transform(X_test)

# # Initialize and train the SVM classifier
# svm_classifier = SVC(kernel='linear')
# svm_classifier.fit(X_train, y_train)

# # Predict sentiment labels on the test set
# y_pred = svm_classifier.predict(X_test)

# # Evaluate the model
# print(classification_report(y_test, y_pred))
