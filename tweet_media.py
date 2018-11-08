#!/usr/bin/env python
import os
import sys
import tweepy

status = sys.argv[1]
media = sys.argv[2]

CONSUMER_KEY=os.environ['CONSUMER_KEY']
CONSUMER_SECRET_KEY=os.environ['CONSUMER_SECRET_KEY']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
ACCESS_SECRET=os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
resp = api.update_with_media(media, status=status) 
print(resp)
