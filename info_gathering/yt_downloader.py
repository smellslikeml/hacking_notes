#!/usr/bin/env python
import os
import sys
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlencode
from pytube import YouTube

qstring = sys.argv[1] # write like urls
out_dir = sys.argv[2]
base = "https://www.youtube.com/results?" #search_query="
s = {"search_query": qstring}
s = urlencode(s)

r = requests.get(base + s)
page = r.text
soup=bs(page,'html.parser')

vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
count=0
os.chdir(out_dir)
for item in videolist:
    # increment counter:
    count+=1
    try:
        yt = YouTube(item)
        # grab the video:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    except:
        pass
