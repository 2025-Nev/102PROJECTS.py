import tweepy
import time
import random
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# Authentication keys for Twitter API
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Define the content of your tweets
tweets = ['This is tweet 1', 'This is tweet 2', 'This is tweet 3']

# Define a function to post a tweet
def post_tweet():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tweet = random.choice(tweets) + ' ' + now
    api.update_status(tweet)

# Set up a scheduler to post a tweet every 30 minutes
scheduler = BlockingScheduler()
scheduler.add_job(post_tweet, 'interval', minutes=30)

# Start the scheduler
scheduler.start()
