#!/usr/bin/env python
'''
Uses Tweepy to print recent 100 tweets
to STDOUT from target twitter handle.
[Usage]
    python target_tweets.py <twitter_handle>
'''
import os
import sys
import tweepy

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret_key = os.environ['CONSUMER_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

target_twitter = sys.argv[1]
new_tweets = api.user_timeline(screen_name=target_twitter, count=100)
print([new_tweets[idx].text for idx in range(len(new_tweets))])
